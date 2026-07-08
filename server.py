#!/usr/bin/env python3
"""FitScope local web server with SQLite authentication.

Run from the site directory with: python3 server.py --port 4182
"""

from __future__ import annotations

import argparse
import shutil
import hashlib
import hmac
import json
import os
import secrets
import sqlite3
import threading
import time
from http import HTTPStatus
from http.cookies import SimpleCookie
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse


ROOT = Path(__file__).resolve().parent
INSTANCE_DIR = ROOT / "instance"
DB_PATH = INSTANCE_DIR / "fitscope.db"
COOKIE_NAME = "fitscope_session"
SESSION_SECONDS = 7 * 24 * 60 * 60
MAX_BODY_BYTES = 64 * 1024
PASSWORD_N = 2**14
PASSWORD_R = 8
PASSWORD_P = 1


def connect_db() -> sqlite3.Connection:
    connection = sqlite3.connect(DB_PATH, timeout=10)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def password_hash(password: str, salt: bytes) -> bytes:
    return hashlib.scrypt(
        password.encode("utf-8"),
        salt=salt,
        n=PASSWORD_N,
        r=PASSWORD_R,
        p=PASSWORD_P,
        dklen=32,
    )


def create_user(connection: sqlite3.Connection, email: str, password: str, name: str, role: str) -> None:
    if connection.execute("SELECT 1 FROM users WHERE email = ?", (email,)).fetchone():
        return
    salt = secrets.token_bytes(16)
    connection.execute(
        """
        INSERT INTO users (email, password_salt, password_hash, display_name, role)
        VALUES (?, ?, ?, ?, ?)
        """,
        (email, salt, password_hash(password, salt), name, role),
    )


def initialize_database() -> None:
    INSTANCE_DIR.mkdir(parents=True, exist_ok=True)
    with connect_db() as connection:
        connection.executescript(
            """
            PRAGMA journal_mode = WAL;

            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE COLLATE NOCASE,
                password_salt BLOB NOT NULL,
                password_hash BLOB NOT NULL,
                display_name TEXT NOT NULL,
                role TEXT NOT NULL CHECK (role IN ('manager', 'operator')),
                active INTEGER NOT NULL DEFAULT 1,
                created_at INTEGER NOT NULL DEFAULT (unixepoch())
            );

            CREATE TABLE IF NOT EXISTS sessions (
                token_hash TEXT PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                expires_at INTEGER NOT NULL,
                created_at INTEGER NOT NULL DEFAULT (unixepoch())
            );

            CREATE TABLE IF NOT EXISTS user_preferences (
                user_id INTEGER PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
                language TEXT NOT NULL DEFAULT 'zh' CHECK (language IN ('zh', 'en')),
                default_page TEXT NOT NULL DEFAULT '',
                return_alert INTEGER NOT NULL DEFAULT 1,
                order_alert INTEGER NOT NULL DEFAULT 1,
                evidence_alert INTEGER NOT NULL DEFAULT 1,
                updated_at INTEGER NOT NULL DEFAULT (unixepoch())
            );

            CREATE TABLE IF NOT EXISTS followed_entities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                entity_type TEXT NOT NULL CHECK (entity_type IN ('category', 'group', 'sku')),
                entity_id TEXT NOT NULL,
                label TEXT NOT NULL DEFAULT '',
                context TEXT NOT NULL DEFAULT '',
                created_at INTEGER NOT NULL DEFAULT (unixepoch()),
                UNIQUE (user_id, entity_type, entity_id)
            );

            CREATE INDEX IF NOT EXISTS sessions_user_id_idx ON sessions(user_id);
            CREATE INDEX IF NOT EXISTS followed_entities_user_idx ON followed_entities(user_id, entity_type);
            """
        )
        shared_password = os.environ.get("FITSCOPE_DEMO_PASSWORD", "FitScope2026!")
        create_user(connection, "manager@fitscope.local", shared_password, "Yuyang Chen", "manager")
        create_user(connection, "operator@fitscope.local", shared_password, "Demo Operator", "operator")
        connection.execute("DELETE FROM sessions WHERE expires_at <= ?", (int(time.time()),))


def public_user(row: sqlite3.Row) -> dict[str, object]:
    return {
        "id": row["id"],
        "email": row["email"],
        "displayName": row["display_name"],
        "role": row["role"],
    }


class RateLimiter:
    def __init__(self) -> None:
        self._attempts: dict[str, list[float]] = {}
        self._lock = threading.Lock()

    def allowed(self, key: str) -> bool:
        now = time.time()
        with self._lock:
            attempts = [stamp for stamp in self._attempts.get(key, []) if now - stamp < 60]
            if len(attempts) >= 8:
                self._attempts[key] = attempts
                return False
            attempts.append(now)
            self._attempts[key] = attempts
            return True


RATE_LIMITER = RateLimiter()


class FitScopeHandler(SimpleHTTPRequestHandler):
    server_version = "FitScope/1.0"

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self) -> None:
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "same-origin")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
        if not urlparse(self.path).path.startswith("/api/"):
            self.send_header("Cache-Control", "public, max-age=60")
        super().end_headers()

    def copyfile(self, source, outputfile) -> None:
        try:
            shutil.copyfileobj(source, outputfile)
        except (BrokenPipeError, ConnectionResetError):
            return

    def send_json(self, payload: object, status: int = HTTPStatus.OK, cookie: str | None = None) -> None:
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        if cookie:
            self.send_header("Set-Cookie", cookie)
        self.end_headers()
        self.wfile.write(body)

    def redirect_to_app(self) -> None:
        self.send_response(HTTPStatus.FOUND)
        self.send_header("Location", "/commerce-os/index.html")
        self.end_headers()

    def read_json(self) -> dict[str, object] | None:
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            return None
        if length <= 0 or length > MAX_BODY_BYTES:
            return None
        try:
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            return None
        return payload if isinstance(payload, dict) else None

    def session_token(self) -> str:
        cookie = SimpleCookie()
        cookie.load(self.headers.get("Cookie", ""))
        morsel = cookie.get(COOKIE_NAME)
        return morsel.value if morsel else ""

    def authenticated_user(self) -> sqlite3.Row | None:
        token = self.session_token()
        if not token:
            return None
        token_digest = hashlib.sha256(token.encode("utf-8")).hexdigest()
        with connect_db() as connection:
            return connection.execute(
                """
                SELECT users.* FROM sessions
                JOIN users ON users.id = sessions.user_id
                WHERE sessions.token_hash = ? AND sessions.expires_at > ? AND users.active = 1
                """,
                (token_digest, int(time.time())),
            ).fetchone()

    def require_user(self) -> sqlite3.Row | None:
        user = self.authenticated_user()
        if not user:
            self.send_json({"error": "authentication_required"}, HTTPStatus.UNAUTHORIZED)
        return user

    def auth_cookie(self, token: str, max_age: int = SESSION_SECONDS) -> str:
        parts = [f"{COOKIE_NAME}={token}", "HttpOnly", "SameSite=Strict", "Path=/", f"Max-Age={max_age}"]
        if os.environ.get("FITSCOPE_SECURE_COOKIE") == "1":
            parts.append("Secure")
        return "; ".join(parts)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path.startswith("/instance/") or any(part.startswith(".") for part in Path(parsed.path).parts if part not in {"/", ""}):
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        if parsed.path in {"/", "/site", "/site/", "/commerce-os", "/commerce-os/", "/site/commerce-os", "/site/commerce-os/", "/site/commerce-os/index.html"}:
            self.redirect_to_app()
            return
        if parsed.path == "/api/health":
            self.send_json({"status": "ok"})
            return
        if parsed.path == "/api/auth/session":
            user = self.authenticated_user()
            if not user:
                self.send_json({"error": "no_session"}, HTTPStatus.UNAUTHORIZED)
                return
            self.send_json({"user": public_user(user)})
            return
        if parsed.path == "/api/me/preferences":
            user = self.require_user()
            if not user:
                return
            with connect_db() as connection:
                row = connection.execute("SELECT * FROM user_preferences WHERE user_id = ?", (user["id"],)).fetchone()
            self.send_json({"preferences": dict(row) if row else {}})
            return
        if parsed.path == "/api/me/following":
            user = self.require_user()
            if not user:
                return
            query = parse_qs(parsed.query)
            entity_type = query.get("type", [""])[0]
            search = query.get("q", [""])[0].strip().lower()
            clauses = ["user_id = ?"]
            params: list[object] = [user["id"]]
            if entity_type in {"category", "group", "sku"}:
                clauses.append("entity_type = ?")
                params.append(entity_type)
            if search:
                clauses.append("(lower(label) LIKE ? OR lower(entity_id) LIKE ? OR lower(context) LIKE ?)")
                term = f"%{search}%"
                params.extend([term, term, term])
            with connect_db() as connection:
                rows = connection.execute(
                    f"SELECT entity_type, entity_id, label, context, created_at FROM followed_entities WHERE {' AND '.join(clauses)} ORDER BY created_at DESC",
                    params,
                ).fetchall()
            self.send_json({"items": [dict(row) for row in rows]})
            return
        super().do_GET()

    def do_HEAD(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path.startswith("/instance/") or any(part.startswith(".") for part in Path(parsed.path).parts if part not in {"/", ""}):
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        if parsed.path in {"/", "/site", "/site/", "/commerce-os", "/commerce-os/", "/site/commerce-os", "/site/commerce-os/", "/site/commerce-os/index.html"}:
            self.redirect_to_app()
            return
        super().do_HEAD()

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/api/auth/login":
            payload = self.read_json()
            email = str((payload or {}).get("email", "")).strip().lower()
            password = str((payload or {}).get("password", ""))
            limiter_key = f"{self.client_address[0]}:{email}"
            if not RATE_LIMITER.allowed(limiter_key):
                self.send_json({"error": "too_many_attempts"}, HTTPStatus.TOO_MANY_REQUESTS)
                return
            with connect_db() as connection:
                user = connection.execute("SELECT * FROM users WHERE email = ? AND active = 1", (email,)).fetchone()
                valid = bool(user) and hmac.compare_digest(password_hash(password, user["password_salt"]), user["password_hash"])
                if not valid:
                    self.send_json({"error": "invalid_credentials"}, HTTPStatus.UNAUTHORIZED)
                    return
                token = secrets.token_urlsafe(32)
                token_digest = hashlib.sha256(token.encode("utf-8")).hexdigest()
                connection.execute(
                    "INSERT INTO sessions (token_hash, user_id, expires_at) VALUES (?, ?, ?)",
                    (token_digest, user["id"], int(time.time()) + SESSION_SECONDS),
                )
            self.send_json({"user": public_user(user)}, cookie=self.auth_cookie(token))
            return
        if parsed.path == "/api/auth/logout":
            token = self.session_token()
            if token:
                with connect_db() as connection:
                    connection.execute("DELETE FROM sessions WHERE token_hash = ?", (hashlib.sha256(token.encode("utf-8")).hexdigest(),))
            self.send_json({"ok": True}, cookie=self.auth_cookie("", 0))
            return
        if parsed.path == "/api/me/following":
            user = self.require_user()
            if not user:
                return
            payload = self.read_json() or {}
            entity_type = str(payload.get("entityType", ""))
            entity_id = str(payload.get("entityId", "")).strip()
            if entity_type not in {"category", "group", "sku"} or not entity_id:
                self.send_json({"error": "invalid_entity"}, HTTPStatus.BAD_REQUEST)
                return
            with connect_db() as connection:
                connection.execute(
                    """
                    INSERT INTO followed_entities (user_id, entity_type, entity_id, label, context)
                    VALUES (?, ?, ?, ?, ?)
                    ON CONFLICT(user_id, entity_type, entity_id)
                    DO UPDATE SET label = excluded.label, context = excluded.context
                    """,
                    (user["id"], entity_type, entity_id, str(payload.get("label", "")), str(payload.get("context", ""))),
                )
            self.send_json({"ok": True}, HTTPStatus.CREATED)
            return
        self.send_json({"error": "not_found"}, HTTPStatus.NOT_FOUND)

    def do_PUT(self) -> None:
        if urlparse(self.path).path != "/api/me/preferences":
            self.send_json({"error": "not_found"}, HTTPStatus.NOT_FOUND)
            return
        user = self.require_user()
        if not user:
            return
        payload = self.read_json() or {}
        language = str(payload.get("language", "zh"))
        if language not in {"zh", "en"}:
            language = "zh"
        with connect_db() as connection:
            connection.execute(
                """
                INSERT INTO user_preferences (user_id, language, default_page, return_alert, order_alert, evidence_alert, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, unixepoch())
                ON CONFLICT(user_id) DO UPDATE SET
                  language = excluded.language,
                  default_page = excluded.default_page,
                  return_alert = excluded.return_alert,
                  order_alert = excluded.order_alert,
                  evidence_alert = excluded.evidence_alert,
                  updated_at = unixepoch()
                """,
                (
                    user["id"], language, str(payload.get("defaultPage", "")),
                    int(bool(payload.get("returnAlert", True))), int(bool(payload.get("orderAlert", True))),
                    int(bool(payload.get("evidenceAlert", True))),
                ),
            )
        self.send_json({"ok": True})

    def do_DELETE(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path != "/api/me/following":
            self.send_json({"error": "not_found"}, HTTPStatus.NOT_FOUND)
            return
        user = self.require_user()
        if not user:
            return
        query = parse_qs(parsed.query)
        entity_type = query.get("entityType", [""])[0]
        entity_id = query.get("entityId", [""])[0]
        with connect_db() as connection:
            connection.execute(
                "DELETE FROM followed_entities WHERE user_id = ? AND entity_type = ? AND entity_id = ?",
                (user["id"], entity_type, entity_id),
            )
        self.send_json({"ok": True})

    def log_message(self, format_string: str, *args: object) -> None:
        print(f"[{self.log_date_time_string()}] {self.address_string()} {format_string % args}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run FitScope Commerce OS")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=4182)
    args = parser.parse_args()
    initialize_database()
    server = ThreadingHTTPServer((args.host, args.port), FitScopeHandler)
    print(f"FitScope is running at http://{args.host}:{args.port}/commerce-os/index.html")
    print("Manager: manager@fitscope.local / FitScope2026!")
    print("Operator: operator@fitscope.local / FitScope2026!")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
