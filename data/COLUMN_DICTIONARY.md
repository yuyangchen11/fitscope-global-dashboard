# Data Column Dictionary

Plain-language field explanations for every CSV committed under `data/`. Row counts exclude the header row.

## Hugging Face H&M Search / Sample Mirror

- Folder: `data/huggingface_hm_search/`
- Source: Derived from public H&M-style search/sample exports staged locally
- Dashboard role: Provides lightweight H&M-like processed metrics for fallback testing and dashboard development.
- Boundary: Not the primary audited source when Kaggle H&M files are available.

### `data/huggingface_hm_search/processed/huggingface_hm_search_articles_sample.csv`

- Layer: `processed`
- Rows: 1,000
- Columns: 25

| Column | Plain-language meaning |
|---|---|
| `article_id` | H&M 商品文章/SKU 编号。 |
| `product_code` | 商品代码。 |
| `prod_name` | 商品名称。 |
| `product_type_no` | 商品类型编号。 |
| `product_type_name` | 商品类型名称。 |
| `product_group_name` | 商品大类。 |
| `graphical_appearance_no` | 图案外观编号。 |
| `graphical_appearance_name` | 图案外观名称。 |
| `colour_group_code` | 颜色组编号。 |
| `colour_group_name` | 颜色组名称。 |
| `perceived_colour_value_id` | 感知颜色深浅编号。 |
| `perceived_colour_value_name` | 感知颜色深浅。 |
| `perceived_colour_master_id` | 主颜色编号。 |
| `perceived_colour_master_name` | 主颜色名称。 |
| `department_no` | 部门编号。 |
| `department_name` | 部门名称。 |
| `index_code` | 业务线代码。 |
| `index_name` | 业务线名称。 |
| `index_group_no` | 业务线组编号。 |
| `index_group_name` | 业务线组名称。 |
| `section_no` | 专区编号。 |
| `section_name` | 专区名称。 |
| `garment_group_no` | 服装组编号。 |
| `garment_group_name` | 服装组名称。 |
| `detail_desc` | 商品详情描述。 |

First data row sample:

```csv
article_id,product_code,prod_name,product_type_no,product_type_name,product_group_name,graphical_appearance_no,graphical_appearance_name,colour_group_code,colour_group_name,perceived_colour_value_id,perceived_colour_value_name,perceived_colour_master_id,perceived_colour_master_name,department_no,department_name,index_code,index_name,index_group_no,index_group_name,section_no,section_name,garment_group_no,garment_group_name,detail_desc
108775015,108775,Strap top,253,Vest top,Garment Upper body,1010016,Solid,9,Black,4,Dark,5,Black,1676,Jersey Basic,A,Ladieswear,1,Ladieswear,16,Womens Everyday Basics,1002,Jersey Basic,Jersey top with narrow shoulder straps.
```

### `data/huggingface_hm_search/processed/huggingface_hm_search_color_metrics.csv`

- Layer: `processed`
- Rows: 50
- Columns: 2

| Column | Plain-language meaning |
|---|---|
| `colour_group_name` | 颜色组名称。 |
| `articles` | 商品数。 |

First data row sample:

```csv
colour_group_name,articles
Black,22670
```

### `data/huggingface_hm_search/processed/huggingface_hm_search_index_group_metrics.csv`

- Layer: `processed`
- Rows: 5
- Columns: 2

| Column | Plain-language meaning |
|---|---|
| `index_group_name` | 业务线组名称。 |
| `articles` | 商品数。 |

First data row sample:

```csv
index_group_name,articles
Ladieswear,39737
```

### `data/huggingface_hm_search/processed/huggingface_hm_search_product_group_metrics.csv`

- Layer: `processed`
- Rows: 19
- Columns: 2

| Column | Plain-language meaning |
|---|---|
| `product_group_name` | 商品大类。 |
| `articles` | 商品数。 |

First data row sample:

```csv
product_group_name,articles
Garment Upper body,42741
```

### `data/huggingface_hm_search/processed/huggingface_hm_search_product_type_metrics.csv`

- Layer: `processed`
- Rows: 131
- Columns: 2

| Column | Plain-language meaning |
|---|---|
| `product_type_name` | 商品类型名称。 |
| `articles` | 商品数。 |

First data row sample:

```csv
product_type_name,articles
Trousers,11169
```

### `data/huggingface_hm_search/processed/huggingface_hm_search_sales_channel_metrics.csv`

- Layer: `processed`
- Rows: 2
- Columns: 2

| Column | Plain-language meaning |
|---|---|
| `sales_channel_id` | 销售渠道编号。 |
| `transactions` | 交易数。 |

First data row sample:

```csv
sales_channel_id,transactions
2,22379862
```

### `data/huggingface_hm_search/processed/huggingface_hm_search_top_article_transactions.csv`

- Layer: `processed`
- Rows: 1,000
- Columns: 2

| Column | Plain-language meaning |
|---|---|
| `article_id` | H&M 商品文章/SKU 编号。 |
| `transactions` | 交易数。 |

First data row sample:

```csv
article_id,transactions
706016001,50287
```

### `data/huggingface_hm_search/processed/huggingface_hm_search_transaction_daily_metrics.csv`

- Layer: `processed`
- Rows: 734
- Columns: 4

| Column | Plain-language meaning |
|---|---|
| `date` | 日期。 |
| `transactions` | 交易数。 |
| `price_sum` | 成交价格。 |
| `avg_price` | 平均价格。 |

First data row sample:

```csv
date,transactions,price_sum,avg_price
2018-09-20,48399,1415.3458,0.029243
```

### `data/huggingface_hm_search/processed/huggingface_hm_search_transactions_sample.csv`

- Layer: `processed`
- Rows: 1,000
- Columns: 5

| Column | Plain-language meaning |
|---|---|
| `t_dat` | 交易日期。 |
| `customer_id` | 顾客匿名 ID。 |
| `article_id` | H&M 商品文章/SKU 编号。 |
| `price` | 成交价格。 |
| `sales_channel_id` | 销售渠道编号。 |

First data row sample:

```csv
t_dat,customer_id,article_id,price,sales_channel_id
2018-09-20,000058a12d5b43e67d225668fa1f8d618c13dc232df0cad8ffe7ad4a1091e318,663713001,0.0508305084745762,2
```

## Kaggle Retail Fashion Boutique Data Sales Analytics 2025

- Folder: `data/kaggle_fashion_boutique/`
- Source: https://www.kaggle.com/datasets/pratyushpuri/retail-fashion-boutique-data-sales-analytics-2025
- Dashboard role: Provides category KPI proxy fields such as price, rating, return flag, return reason, markdown and stock for operating readiness.
- Boundary: Use as company-KPI proxy until replaced by first-party internal data.

### `data/kaggle_fashion_boutique/processed/kaggle_fashion_boutique_company_category_kpi.csv`

- Layer: `processed`
- Rows: 6
- Columns: 14

| Column | Plain-language meaning |
|---|---|
| `category` | 标准化业务类目。 |
| `source_category` | 标准化业务类目。 |
| `products` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `gmv` | 商品交易额。 |
| `conversion` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `returnRate` | 比例类指标，用于对比不同类目或时间段。 |
| `margin` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `inventoryTurn` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `avg_rating` | 平均评分。 |
| `avg_markdown` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `returned_items` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `top_return_reason` | 退货原因。 |
| `size_issue_returns` | 尺码。 |
| `quality_issue_returns` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |

First data row sample:

```csv
category,source_category,products,gmv,conversion,returnRate,margin,inventoryTurn,avg_rating,avg_markdown,returned_items,top_return_reason,size_issue_returns,quality_issue_returns
outerwear,Outerwear,334,48672.81,0.0494,0.1617,0.4713,3.798,2.411,10.769,54,Changed Mind,12,12
```

### `data/kaggle_fashion_boutique/processed/kaggle_fashion_boutique_daily_kpi.csv`

- Layer: `processed`
- Rows: 273
- Columns: 5

| Column | Plain-language meaning |
|---|---|
| `date` | 日期。 |
| `products` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `gmv` | 商品交易额。 |
| `return_rate` | 退货率或退货代理指标。 |
| `avg_rating` | 平均评分。 |

First data row sample:

```csv
date,products,gmv,return_rate,avg_rating
2024-08-06,1,36.8,0.0,3.9
```

### `data/kaggle_fashion_boutique/processed/kaggle_fashion_boutique_return_reason_metrics.csv`

- Layer: `processed`
- Rows: 36
- Columns: 4

| Column | Plain-language meaning |
|---|---|
| `category` | 标准化业务类目。 |
| `return_reason` | 退货原因。 |
| `count` | 数量类指标，用于统计规模。 |
| `share_in_category` | 标准化业务类目。 |

First data row sample:

```csv
category,return_reason,count,share_in_category
accessories,Color Mismatch,13,0.0323
```

### `data/kaggle_fashion_boutique/raw/kaggle_fashion_boutique_dataset.csv`

- Layer: `raw`
- Rows: 2,176
- Columns: 14

| Column | Plain-language meaning |
|---|---|
| `product_id` | 商品匿名 ID。 |
| `category` | 标准化业务类目。 |
| `brand` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `season` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `size` | 尺码。 |
| `color` | 颜色。 |
| `original_price` | 成交价格。 |
| `markdown_percentage` | 折扣/降价比例。 |
| `current_price` | 当前售价。 |
| `purchase_date` | 日期。 |
| `stock_quantity` | 库存数量。 |
| `customer_rating` | 顾客评分。 |
| `is_returned` | 是否退货。 |
| `return_reason` | 退货原因。 |

First data row sample:

```csv
product_id,category,brand,season,size,color,original_price,markdown_percentage,current_price,purchase_date,stock_quantity,customer_rating,is_returned,return_reason
FB000001,Outerwear,Zara,Spring,XL,Red,196.01,0.0,196.01,2025-07-05,37,3.0,False,
```

## Kaggle H&M Personalized Fashion Recommendations

- Folder: `data/kaggle_hm_personalized/`
- Source: https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data
- Dashboard role: Provides apparel assortment structure, product hierarchy, article-level sample records and transaction momentum proxies.
- Boundary: No order status, returns, payment, margin, product cost, or traffic events.

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_age_bucket_metrics.csv`

- Layer: `processed`
- Rows: 7
- Columns: 3

| Column | Plain-language meaning |
|---|---|
| `age_bucket` | 顾客年龄。 |
| `customers` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `share` | 比例类指标，用于对比不同类目或时间段。 |

First data row sample:

```csv
age_bucket,customers,share
20_to_29,528358,0.385106
```

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_articles_sample.csv`

- Layer: `processed`
- Rows: 1,000
- Columns: 9

| Column | Plain-language meaning |
|---|---|
| `article_id` | H&M 商品文章/SKU 编号。 |
| `prod_name` | 商品名称。 |
| `product_type_name` | 商品类型名称。 |
| `product_group_name` | 商品大类。 |
| `colour_group_name` | 颜色组名称。 |
| `index_group_name` | 业务线组名称。 |
| `section_name` | 专区名称。 |
| `garment_group_name` | 服装组名称。 |
| `detail_desc` | 商品详情描述。 |

First data row sample:

```csv
article_id,prod_name,product_type_name,product_group_name,colour_group_name,index_group_name,section_name,garment_group_name,detail_desc
0108775015,Strap top,Vest top,Garment Upper body,Black,Ladieswear,Womens Everyday Basics,Jersey Basic,Jersey top with narrow shoulder straps.
```

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_color_metrics.csv`

- Layer: `processed`
- Rows: 50
- Columns: 3

| Column | Plain-language meaning |
|---|---|
| `colour_group_name` | 颜色组名称。 |
| `articles` | 商品数。 |
| `share` | 比例类指标，用于对比不同类目或时间段。 |

First data row sample:

```csv
colour_group_name,articles,share
Black,22670,0.214796
```

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_customer_status_metrics.csv`

- Layer: `processed`
- Rows: 4
- Columns: 3

| Column | Plain-language meaning |
|---|---|
| `club_member_status` | 会员状态。 |
| `customers` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `share` | 比例类指标，用于对比不同类目或时间段。 |

First data row sample:

```csv
club_member_status,customers,share
ACTIVE,1272491,0.927485
```

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_customers_sample.csv`

- Layer: `processed`
- Rows: 1,000
- Columns: 7

| Column | Plain-language meaning |
|---|---|
| `customer_id` | 顾客匿名 ID。 |
| `FN` | 是否订阅时尚新闻。 |
| `Active` | 顾客是否活跃。 |
| `club_member_status` | 会员状态。 |
| `fashion_news_frequency` | 时尚资讯订阅频率。 |
| `age` | 顾客年龄。 |
| `postal_code` | 顾客邮编。 |

First data row sample:

```csv
customer_id,FN,Active,club_member_status,fashion_news_frequency,age,postal_code
00000dbacae5abe5e23885899a1fa44253a17956c6d1c3d25f88aa139fdfc657,,,ACTIVE,NONE,49,52043ee2162cf5aa7ee79974281641c6f11a68d276429a91f8ca0d4b6efa8100
```

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_fashion_news_metrics.csv`

- Layer: `processed`
- Rows: 5
- Columns: 3

| Column | Plain-language meaning |
|---|---|
| `fashion_news_frequency` | 时尚资讯订阅频率。 |
| `customers` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `share` | 比例类指标，用于对比不同类目或时间段。 |

First data row sample:

```csv
fashion_news_frequency,customers,share
NONE,877711,0.63974
```

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_index_group_metrics.csv`

- Layer: `processed`
- Rows: 5
- Columns: 3

| Column | Plain-language meaning |
|---|---|
| `index_group_name` | 业务线组名称。 |
| `articles` | 商品数。 |
| `share` | 比例类指标，用于对比不同类目或时间段。 |

First data row sample:

```csv
index_group_name,articles,share
Ladieswear,39737,0.376504
```

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_product_group_metrics.csv`

- Layer: `processed`
- Rows: 19
- Columns: 3

| Column | Plain-language meaning |
|---|---|
| `product_group_name` | 商品大类。 |
| `articles` | 商品数。 |
| `share` | 比例类指标，用于对比不同类目或时间段。 |

First data row sample:

```csv
product_group_name,articles,share
Garment Upper body,42741,0.404967
```

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_product_type_metrics.csv`

- Layer: `processed`
- Rows: 131
- Columns: 3

| Column | Plain-language meaning |
|---|---|
| `product_type_name` | 商品类型名称。 |
| `articles` | 商品数。 |
| `share` | 比例类指标，用于对比不同类目或时间段。 |

First data row sample:

```csv
product_type_name,articles,share
Trousers,11169,0.105825
```

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_sales_channel_metrics.csv`

- Layer: `processed`
- Rows: 2
- Columns: 3

| Column | Plain-language meaning |
|---|---|
| `sales_channel_id` | 销售渠道编号。 |
| `transactions` | 交易数。 |
| `share` | 比例类指标，用于对比不同类目或时间段。 |

First data row sample:

```csv
sales_channel_id,transactions,share
2,22379862,0.704028
```

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_section_metrics.csv`

- Layer: `processed`
- Rows: 56
- Columns: 3

| Column | Plain-language meaning |
|---|---|
| `section_name` | 专区名称。 |
| `articles` | 商品数。 |
| `share` | 比例类指标，用于对比不同类目或时间段。 |

First data row sample:

```csv
section_name,articles,share
Womens Everyday Collection,7295,0.069119
```

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_summary.csv`

- Layer: `processed`
- Rows: 5
- Columns: 2

| Column | Plain-language meaning |
|---|---|
| `metric` | 指标名称。 |
| `value` | 指标值。 |

First data row sample:

```csv
metric,value
articles,105542
```

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_top_article_transactions.csv`

- Layer: `processed`
- Rows: 200
- Columns: 7

| Column | Plain-language meaning |
|---|---|
| `article_id` | H&M 商品文章/SKU 编号。 |
| `transactions` | 交易数。 |
| `prod_name` | 商品名称。 |
| `product_group_name` | 商品大类。 |
| `product_type_name` | 商品类型名称。 |
| `index_group_name` | 业务线组名称。 |
| `colour_group_name` | 颜色组名称。 |

First data row sample:

```csv
article_id,transactions,prod_name,product_group_name,product_type_name,index_group_name,colour_group_name
0706016001,50287,Jade HW Skinny Denim TRS,Garment Lower body,Trousers,Divided,Black
```

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_transaction_articles_sample.csv`

- Layer: `processed`
- Rows: 815
- Columns: 9

| Column | Plain-language meaning |
|---|---|
| `article_id` | H&M 商品文章/SKU 编号。 |
| `prod_name` | 商品名称。 |
| `product_type_name` | 商品类型名称。 |
| `product_group_name` | 商品大类。 |
| `colour_group_name` | 颜色组名称。 |
| `index_group_name` | 业务线组名称。 |
| `section_name` | 专区名称。 |
| `garment_group_name` | 服装组名称。 |
| `detail_desc` | 商品详情描述。 |

First data row sample:

```csv
article_id,prod_name,product_type_name,product_group_name,colour_group_name,index_group_name,section_name,garment_group_name,detail_desc
0156231001,Box 4p Tights,Underwear Tights,Socks & Tights,Black,Ladieswear,"Womens Nightwear, Socks & Tigh",Socks and Tights,Matt tights with an elasticated waist. 20 denier.
```

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_transaction_color_metrics.csv`

- Layer: `processed`
- Rows: 50
- Columns: 3

| Column | Plain-language meaning |
|---|---|
| `colour_group_name` | 颜色组名称。 |
| `transactions` | 交易数。 |
| `share` | 比例类指标，用于对比不同类目或时间段。 |

First data row sample:

```csv
colour_group_name,transactions,share
Black,11036956,0.347202
```

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_transaction_daily_metrics.csv`

- Layer: `processed`
- Rows: 734
- Columns: 4

| Column | Plain-language meaning |
|---|---|
| `date` | 日期。 |
| `transactions` | 交易数。 |
| `price_sum` | 成交价格。 |
| `avg_price` | 平均价格。 |

First data row sample:

```csv
date,transactions,price_sum,avg_price
2018-09-20,48399,1415.345847,0.029243
```

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_transaction_index_group_metrics.csv`

- Layer: `processed`
- Rows: 5
- Columns: 3

| Column | Plain-language meaning |
|---|---|
| `index_group_name` | 业务线组名称。 |
| `transactions` | 交易数。 |
| `share` | 比例类指标，用于对比不同类目或时间段。 |

First data row sample:

```csv
index_group_name,transactions,share
Ladieswear,20415260,0.642225
```

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_transaction_product_group_metrics.csv`

- Layer: `processed`
- Rows: 19
- Columns: 3

| Column | Plain-language meaning |
|---|---|
| `product_group_name` | 商品大类。 |
| `transactions` | 交易数。 |
| `share` | 比例类指标，用于对比不同类目或时间段。 |

First data row sample:

```csv
product_group_name,transactions,share
Garment Upper body,12552755,0.394886
```

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_transaction_product_type_metrics.csv`

- Layer: `processed`
- Rows: 130
- Columns: 3

| Column | Plain-language meaning |
|---|---|
| `product_type_name` | 商品类型名称。 |
| `transactions` | 交易数。 |
| `share` | 比例类指标，用于对比不同类目或时间段。 |

First data row sample:

```csv
product_type_name,transactions,share
Trousers,4217017,0.132659
```

### `data/kaggle_hm_personalized/processed/kaggle_hm_personalized_transactions_sample.csv`

- Layer: `processed`
- Rows: 1,000
- Columns: 5

| Column | Plain-language meaning |
|---|---|
| `t_dat` | 交易日期。 |
| `customer_id` | 顾客匿名 ID。 |
| `article_id` | H&M 商品文章/SKU 编号。 |
| `price` | 成交价格。 |
| `sales_channel_id` | 销售渠道编号。 |

First data row sample:

```csv
t_dat,customer_id,article_id,price,sales_channel_id
2018-09-20,000058a12d5b43e67d225668fa1f8d618c13dc232df0cad8ffe7ad4a1091e318,0663713001,0.050830508474576264,2
```

## Kaggle Olist Brazilian E-Commerce

- Folder: `data/kaggle_olist/`
- Source: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
- Dashboard role: Provides the closest real commerce operations layer: orders, order lines, payment, delivery, freight, review score, seller/customer geography and fashion product-level detail.
- Boundary: No true return reason, product cost, gross margin, traffic, impression, or conversion funnel fields.

### `data/kaggle_olist/processed/olist_category_metrics.csv`

- Layer: `processed`
- Rows: 74
- Columns: 17

| Column | Plain-language meaning |
|---|---|
| `category` | 标准化业务类目。 |
| `scope` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `orders` | 订单数。 |
| `units` | 销售件数。 |
| `products` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `sellers` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `customers` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `revenue` | 销售额。 |
| `avg_item_price` | 成交价格。 |
| `freight_value` | 运费金额。 |
| `freight_ratio` | 运费占比。 |
| `avg_review_score` | 订单评分。 |
| `review_count` | 评论数。 |
| `on_time_rate` | 准时履约率。 |
| `late_delivery_rate` | 比例类指标，用于对比不同类目或时间段。 |
| `cancelled_line_rate` | 比例类指标，用于对比不同类目或时间段。 |
| `latest_order` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |

First data row sample:

```csv
category,scope,orders,units,products,sellers,customers,revenue,avg_item_price,freight_value,freight_ratio,avg_review_score,review_count,on_time_rate,late_delivery_rate,cancelled_line_rate,latest_order
health_beauty,other,8836,9670,2444,492,8836,1258681.34,130.16,182566.73,0.145046,4.142,9588,0.909456,0.090544,0.003723,2018-08-29 14:18:28
```

### `data/kaggle_olist/processed/olist_daily_metrics.csv`

- Layer: `processed`
- Rows: 616
- Columns: 7

| Column | Plain-language meaning |
|---|---|
| `date` | 日期。 |
| `orders` | 订单数。 |
| `units` | 销售件数。 |
| `revenue` | 销售额。 |
| `freight_value` | 运费金额。 |
| `avg_review_score` | 订单评分。 |
| `on_time_rate` | 准时履约率。 |

First data row sample:

```csv
date,orders,units,revenue,freight_value,avg_review_score,on_time_rate
2016-09-04,1,2,72.89,63.34,1.0,0
```

### `data/kaggle_olist/processed/olist_fashion_order_lines.csv`

- Layer: `processed`
- Rows: 2,642
- Columns: 17

| Column | Plain-language meaning |
|---|---|
| `line_id` | 唯一编号或关联键，用于连接不同表。 |
| `order_id` | 订单唯一编号，用来把订单、支付、评论、明细行关联起来。 |
| `order_time` | 时间字段，用于时间筛选和趋势分析。 |
| `order_status` | 订单状态，例如 delivered、shipped、canceled。 |
| `product_id` | 商品匿名 ID。 |
| `category` | 标准化业务类目。 |
| `seller_id` | 卖家匿名 ID。 |
| `customer_state` | 顾客州/省。 |
| `unit_price` | 单价。 |
| `freight_value` | 运费金额。 |
| `line_total` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `payment_type` | 支付方式。 |
| `installments` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `review_score` | 订单评分。 |
| `delivered_at` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `estimated_delivery` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `delivery_status` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |

First data row sample:

```csv
line_id,order_id,order_time,order_status,product_id,category,seller_id,customer_state,unit_price,freight_value,line_total,payment_type,installments,review_score,delivered_at,estimated_delivery,delivery_status
00b44ba3-01,00b44ba3d7c4a5e9a9ebafef9150781d,2018-08-28 21:10:46,delivered,d9a5a5120d4d357871acd5408cb10e18,fashion_bags_accessories,20d83f3ef0e6925fd74bfd59170babf7,SP,59.90,7.68,67.58,credit_card,1,5.0,2018-08-30 13:38:53,2018-09-26 00:00:00,on_time
```

### `data/kaggle_olist/processed/olist_order_status_metrics.csv`

- Layer: `processed`
- Rows: 8
- Columns: 3

| Column | Plain-language meaning |
|---|---|
| `order_status` | 订单状态，例如 delivered、shipped、canceled。 |
| `orders` | 订单数。 |
| `share` | 比例类指标，用于对比不同类目或时间段。 |

First data row sample:

```csv
order_status,orders,share
delivered,96478,0.970203
```

### `data/kaggle_olist/processed/olist_payment_metrics.csv`

- Layer: `processed`
- Rows: 5
- Columns: 3

| Column | Plain-language meaning |
|---|---|
| `payment_type` | 支付方式。 |
| `records` | 记录数。 |
| `payment_value` | 支付金额。 |

First data row sample:

```csv
payment_type,records,payment_value
credit_card,76795,12542084.19
```

### `data/kaggle_olist/processed/olist_product_metrics.csv`

- Layer: `processed`
- Rows: 1,221
- Columns: 12

| Column | Plain-language meaning |
|---|---|
| `product_id` | 商品匿名 ID。 |
| `category` | 标准化业务类目。 |
| `orders` | 订单数。 |
| `units` | 销售件数。 |
| `sellers` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `revenue` | 销售额。 |
| `avg_item_price` | 成交价格。 |
| `freight_ratio` | 运费占比。 |
| `avg_review_score` | 订单评分。 |
| `review_count` | 评论数。 |
| `on_time_rate` | 准时履约率。 |
| `latest_order` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |

First data row sample:

```csv
product_id,category,orders,units,sellers,revenue,avg_item_price,freight_ratio,avg_review_score,review_count,on_time_rate,latest_order
d017a2151d543a9885604dc62a3d9dcc,fashion_bags_accessories,138,140,1,6860.00,49.00,0.256337,4.064,140,0.913669,2018-08-24 14:59:37
```

### `data/kaggle_olist/processed/olist_summary.csv`

- Layer: `processed`
- Rows: 1
- Columns: 14

| Column | Plain-language meaning |
|---|---|
| `orders` | 订单数。 |
| `valid_orders` | 订单数。 |
| `delivered_orders` | 订单数。 |
| `cancelled_orders` | 订单数。 |
| `cancellation_rate` | 比例类指标，用于对比不同类目或时间段。 |
| `revenue` | 销售额。 |
| `average_order_value` | 顾客年龄。 |
| `on_time_delivery_rate` | 比例类指标，用于对比不同类目或时间段。 |
| `average_review_score` | 订单评分。 |
| `review_count` | 评论数。 |
| `fashion_order_lines` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `fashion_products` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `start_date` | 交易日期。 |
| `end_date` | 日期。 |

First data row sample:

```csv
orders,valid_orders,delivered_orders,cancelled_orders,cancellation_rate,revenue,average_order_value,on_time_delivery_rate,average_review_score,review_count,fashion_order_lines,fashion_products,start_date,end_date
99441,98207,96478,1234,0.012409,13494400.74,137.41,0.9188,4.086,99224,2642,1221,2016-09-04 21:15:19,2018-10-17 17:30:18
```

### `data/kaggle_olist/raw/olist_customers_dataset.csv`

- Layer: `raw`
- Rows: 99,441
- Columns: 5

| Column | Plain-language meaning |
|---|---|
| `customer_id` | 顾客匿名 ID。 |
| `customer_unique_id` | 跨订单识别同一匿名顾客的 ID。 |
| `customer_zip_code_prefix` | 顾客邮编前缀。 |
| `customer_city` | 顾客城市。 |
| `customer_state` | 顾客州/省。 |

First data row sample:

```csv
customer_id,customer_unique_id,customer_zip_code_prefix,customer_city,customer_state
# sample omitted for large raw file; open the CSV directly in GitHub or spreadsheet software
```

### `data/kaggle_olist/raw/olist_geolocation_dataset.csv`

- Layer: `raw`
- Rows: 1,000,163
- Columns: 5

| Column | Plain-language meaning |
|---|---|
| `geolocation_zip_code_prefix` | 地理邮编前缀。 |
| `geolocation_lat` | 纬度。 |
| `geolocation_lng` | 经度。 |
| `geolocation_city` | 地理城市。 |
| `geolocation_state` | 地理州/省。 |

First data row sample:

```csv
geolocation_zip_code_prefix,geolocation_lat,geolocation_lng,geolocation_city,geolocation_state
# sample omitted for large raw file; open the CSV directly in GitHub or spreadsheet software
```

### `data/kaggle_olist/raw/olist_order_items_dataset.csv`

- Layer: `raw`
- Rows: 112,650
- Columns: 7

| Column | Plain-language meaning |
|---|---|
| `order_id` | 订单唯一编号，用来把订单、支付、评论、明细行关联起来。 |
| `order_item_id` | 同一订单中的第几件商品。 |
| `product_id` | 商品匿名 ID。 |
| `seller_id` | 卖家匿名 ID。 |
| `shipping_limit_date` | 卖家最晚发货时间。 |
| `price` | 成交价格。 |
| `freight_value` | 运费金额。 |

First data row sample:

```csv
order_id,order_item_id,product_id,seller_id,shipping_limit_date,price,freight_value
# sample omitted for large raw file; open the CSV directly in GitHub or spreadsheet software
```

### `data/kaggle_olist/raw/olist_order_payments_dataset.csv`

- Layer: `raw`
- Rows: 103,886
- Columns: 5

| Column | Plain-language meaning |
|---|---|
| `order_id` | 订单唯一编号，用来把订单、支付、评论、明细行关联起来。 |
| `payment_sequential` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `payment_type` | 支付方式。 |
| `payment_installments` | 分期期数。 |
| `payment_value` | 支付金额。 |

First data row sample:

```csv
order_id,payment_sequential,payment_type,payment_installments,payment_value
# sample omitted for large raw file; open the CSV directly in GitHub or spreadsheet software
```

### `data/kaggle_olist/raw/olist_order_reviews_dataset.csv`

- Layer: `raw`
- Rows: 104,719
- Columns: 7

| Column | Plain-language meaning |
|---|---|
| `review_id` | 评论唯一编号。 |
| `order_id` | 订单唯一编号，用来把订单、支付、评论、明细行关联起来。 |
| `review_score` | 订单评分。 |
| `review_comment_title` | 评论标题。 |
| `review_comment_message` | 评论正文。 |
| `review_creation_date` | 评论创建时间。 |
| `review_answer_timestamp` | 商家/平台回复时间。 |

First data row sample:

```csv
review_id,order_id,review_score,review_comment_title,review_comment_message,review_creation_date,review_answer_timestamp
# sample omitted for large raw file; open the CSV directly in GitHub or spreadsheet software
```

### `data/kaggle_olist/raw/olist_orders_dataset.csv`

- Layer: `raw`
- Rows: 99,441
- Columns: 8

| Column | Plain-language meaning |
|---|---|
| `order_id` | 订单唯一编号，用来把订单、支付、评论、明细行关联起来。 |
| `customer_id` | 顾客匿名 ID。 |
| `order_status` | 订单状态，例如 delivered、shipped、canceled。 |
| `order_purchase_timestamp` | 下单时间。 |
| `order_approved_at` | 订单付款/审核通过时间。 |
| `order_delivered_carrier_date` | 交给物流承运商的时间。 |
| `order_delivered_customer_date` | 送达顾客的时间。 |
| `order_estimated_delivery_date` | 平台预计送达日期。 |

First data row sample:

```csv
order_id,customer_id,order_status,order_purchase_timestamp,order_approved_at,order_delivered_carrier_date,order_delivered_customer_date,order_estimated_delivery_date
# sample omitted for large raw file; open the CSV directly in GitHub or spreadsheet software
```

### `data/kaggle_olist/raw/olist_products_dataset.csv`

- Layer: `raw`
- Rows: 32,951
- Columns: 9

| Column | Plain-language meaning |
|---|---|
| `product_id` | 商品匿名 ID。 |
| `product_category_name` | 原始葡语商品类目。 |
| `product_name_lenght` | 商品名称长度，原字段拼写保留。 |
| `product_description_lenght` | 商品描述长度，原字段拼写保留。 |
| `product_photos_qty` | 商品图片数量。 |
| `product_weight_g` | 商品重量，单位克。 |
| `product_length_cm` | 商品长度，单位厘米。 |
| `product_height_cm` | 商品高度，单位厘米。 |
| `product_width_cm` | 商品宽度，单位厘米。 |

First data row sample:

```csv
product_id,product_category_name,product_name_lenght,product_description_lenght,product_photos_qty,product_weight_g,product_length_cm,product_height_cm,product_width_cm
# sample omitted for large raw file; open the CSV directly in GitHub or spreadsheet software
```

### `data/kaggle_olist/raw/olist_sellers_dataset.csv`

- Layer: `raw`
- Rows: 3,095
- Columns: 4

| Column | Plain-language meaning |
|---|---|
| `seller_id` | 卖家匿名 ID。 |
| `seller_zip_code_prefix` | 卖家邮编前缀。 |
| `seller_city` | 卖家城市。 |
| `seller_state` | 卖家州/省。 |

First data row sample:

```csv
seller_id,seller_zip_code_prefix,seller_city,seller_state
3442f8959a84dea7ee197c632cb2df15,13023,campinas,SP
```

### `data/kaggle_olist/raw/product_category_name_translation.csv`

- Layer: `raw`
- Rows: 71
- Columns: 2

| Column | Plain-language meaning |
|---|---|
| `product_category_name` | 原始葡语商品类目。 |
| `product_category_name_english` | 英文商品类目。 |

First data row sample:

```csv
product_category_name,product_category_name_english
beleza_saude,health_beauty
```

## Kaggle Women Clothing Reviews

- Folder: `data/kaggle_womens_reviews/`
- Source: https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews
- Dashboard role: Provides review class and sentiment benchmark metrics for the evidence and semantic views.
- Boundary: No order-line economics or fulfillment data.

### `data/kaggle_womens_reviews/processed/kaggle_womens_reviews_class_metrics.csv`

- Layer: `processed`
- Rows: 21
- Columns: 5

| Column | Plain-language meaning |
|---|---|
| `class_name` | 服装评论分类。 |
| `records` | 记录数。 |
| `avg_rating` | 平均评分。 |
| `recommended_rate` | 比例类指标，用于对比不同类目或时间段。 |
| `low_rating_rate` | 低评分占比。 |

First data row sample:

```csv
class_name,records,avg_rating,recommended_rate,low_rating_rate
Trend,119,3.815,0.7395,0.1849
```

### `data/kaggle_womens_reviews/processed/kaggle_womens_reviews_sentiment_metrics.csv`

- Layer: `processed`
- Rows: 3
- Columns: 2

| Column | Plain-language meaning |
|---|---|
| `sentiment_bucket` | 评论情绪或倾向。 |
| `records` | 记录数。 |

First data row sample:

```csv
sentiment_bucket,records
positive,18208
```

## Kaggle Women Clothing Ecommerce Sales

- Folder: `data/kaggle_womens_sales/`
- Source: https://www.kaggle.com/datasets/shilongzhuang/-women-clothing-ecommerce-sales-data
- Dashboard role: Provides SKU/order/date/size/color/price/quantity/revenue structure for order-detail and SKU drill-down design validation.
- Boundary: No native product-group taxonomy or returns.

### `data/kaggle_womens_sales/processed/kaggle_womens_sales_daily_metrics.csv`

- Layer: `processed`
- Rows: 116
- Columns: 6

| Column | Plain-language meaning |
|---|---|
| `date` | 日期。 |
| `orders` | 订单数。 |
| `line_items` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `units` | 销售件数。 |
| `revenue` | 销售额。 |
| `avg_order_line_revenue` | 销售额。 |

First data row sample:

```csv
date,orders,line_items,units,revenue,avg_order_line_revenue
2022-6-1,1,2,2,556.0,278.0
```

### `data/kaggle_womens_sales/processed/kaggle_womens_sales_size_metrics.csv`

- Layer: `processed`
- Rows: 10
- Columns: 5

| Column | Plain-language meaning |
|---|---|
| `size` | 尺码。 |
| `line_items` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `units` | 销售件数。 |
| `revenue` | 销售额。 |
| `share` | 比例类指标，用于对比不同类目或时间段。 |

First data row sample:

```csv
size,line_items,units,revenue,share
XL,164,166,45868.0,0.3112
```

### `data/kaggle_womens_sales/processed/kaggle_womens_sales_sku_metrics.csv`

- Layer: `processed`
- Rows: 24
- Columns: 8

| Column | Plain-language meaning |
|---|---|
| `sku` | SKU 编码。 |
| `orders` | 订单数。 |
| `line_items` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `units` | 销售件数。 |
| `revenue` | 销售额。 |
| `avg_unit_price` | 成交价格。 |
| `top_size` | 尺码。 |
| `size_missing_rate` | 尺码。 |

First data row sample:

```csv
sku,orders,line_items,units,revenue,avg_unit_price,top_size,size_missing_rate
799,216,283,287,79182.0,275.81,XL,0.0
```

### `data/kaggle_womens_sales/raw/kaggle_womens_sales_orders.csv`

- Layer: `raw`
- Rows: 527
- Columns: 8

| Column | Plain-language meaning |
|---|---|
| `order_id` | 订单唯一编号，用来把订单、支付、评论、明细行关联起来。 |
| `order_date` | 日期。 |
| `sku` | SKU 编码。 |
| `color` | 颜色。 |
| `size` | 尺码。 |
| `unit_price` | 单价。 |
| `quantity` | 数量。 |
| `revenue` | 销售额。 |

First data row sample:

```csv
order_id,order_date,sku,color,size,unit_price,quantity,revenue
1,2022/6/1 16:05:00,708,Dark Blue,2XL,298,1,298
```

## UCSD Clothing Fit Feedback

- Folder: `data/ucsd_clothing_fit/`
- Source: https://cseweb.ucsd.edu/~jmcauley/datasets.html#clothing_fit
- Dashboard role: Provides fit outcome, body type, size and review evidence used for fit-risk and review pain-point diagnosis.
- Boundary: Review/rental context is not a live store transaction table.

### `data/ucsd_clothing_fit/processed/ucsd_body_type_metrics.csv`

- Layer: `processed`
- Rows: 8
- Columns: 12

| Column | Plain-language meaning |
|---|---|
| `body_type` | 用户体型。 |
| `records` | 记录数。 |
| `display_eligible` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `fit_rate` | 合身率。 |
| `too_small_rate` | 偏小占比。 |
| `too_large_rate` | 偏大占比。 |
| `nonfit_rate` | 合身率。 |
| `low_signal_rate` | 比例类指标，用于对比不同类目或时间段。 |
| `pain_point_rate` | 评论痛点标签。 |
| `avg_rating` | 平均评分。 |
| `avg_quality` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `risk_score` | 评分/综合分，用于排序和诊断。 |

First data row sample:

```csv
body_type,records,display_eligible,fit_rate,too_small_rate,too_large_rate,nonfit_rate,low_signal_rate,pain_point_rate,avg_rating,avg_quality,risk_score
apple,4877,1,0.715,0.1487,0.1364,0.285,0.0956,0.7827,8.93,,32.77
```

### `data/ucsd_clothing_fit/processed/ucsd_category_metrics.csv`

- Layer: `processed`
- Rows: 60
- Columns: 12

| Column | Plain-language meaning |
|---|---|
| `category_group` | 标准化业务类目。 |
| `records` | 记录数。 |
| `display_eligible` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `fit_rate` | 合身率。 |
| `too_small_rate` | 偏小占比。 |
| `too_large_rate` | 偏大占比。 |
| `nonfit_rate` | 合身率。 |
| `low_signal_rate` | 比例类指标，用于对比不同类目或时间段。 |
| `pain_point_rate` | 评论痛点标签。 |
| `avg_rating` | 平均评分。 |
| `avg_quality` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `risk_score` | 评分/综合分，用于排序和诊断。 |

First data row sample:

```csv
category_group,records,display_eligible,fit_rate,too_small_rate,too_large_rate,nonfit_rate,low_signal_rate,pain_point_rate,avg_rating,avg_quality,risk_score
vest,278,1,0.5863,0.0072,0.4065,0.4137,0.1259,0.6043,9.01,,36.55
```

### `data/ucsd_clothing_fit/processed/ucsd_evidence_sample.csv`

- Layer: `processed`
- Rows: 1,000
- Columns: 25

| Column | Plain-language meaning |
|---|---|
| `dataset` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `item_id` | 唯一编号或关联键，用于连接不同表。 |
| `user_id` | 唯一编号或关联键，用于连接不同表。 |
| `category_raw` | 标准化业务类目。 |
| `category_group` | 标准化业务类目。 |
| `fit` | 用户反馈的合身结果。 |
| `is_fit` | 用户反馈的合身结果。 |
| `is_small` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `is_large` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `is_nonfit` | 用户反馈的合身结果。 |
| `rating` | 评分。 |
| `quality` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `low_signal` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `size` | 尺码。 |
| `height_inches` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `height_bucket` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `weight_lbs` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `weight_bucket` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `body_type` | 用户体型。 |
| `occasion` | 穿着场景。 |
| `length` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `review_summary` | 评论正文。 |
| `review_text` | 评论正文。 |
| `pain_points` | 评论痛点标签集合。 |
| `has_pain_point` | 评论痛点标签。 |

First data row sample:

```csv
dataset,item_id,user_id,category_raw,category_group,fit,is_fit,is_small,is_large,is_nonfit,rating,quality,low_signal,size,height_inches,height_bucket,weight_lbs,weight_bucket,body_type,occasion,length,review_summary,review_text,pain_points,has_pain_point
renttherunway,153475,273551,gown,dress,fit,1,0,0,0,10.0,,0,12,66,5_3_to_5_6,132.0,120_to_150,straight & narrow,other,unknown,I felt so glamourous!!!,"I rented this dress for a photo shoot. The theme was ""Hollywood Glam and Big Beautiful Hats"". The dress was very comfortable and easy to move around in. It is definitely on my list to rent again for another formal event.",length_issue;color_expectation,1
```

### `data/ucsd_clothing_fit/processed/ucsd_pain_point_metrics.csv`

- Layer: `processed`
- Rows: 7
- Columns: 2

| Column | Plain-language meaning |
|---|---|
| `pain_point` | 评论痛点标签。 |
| `records` | 记录数。 |

First data row sample:

```csv
pain_point,records
fabric_or_quality,104980
```

### `data/ucsd_clothing_fit/processed/ucsd_size_metrics.csv`

- Layer: `processed`
- Rows: 57
- Columns: 12

| Column | Plain-language meaning |
|---|---|
| `size` | 尺码。 |
| `records` | 记录数。 |
| `display_eligible` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `fit_rate` | 合身率。 |
| `too_small_rate` | 偏小占比。 |
| `too_large_rate` | 偏大占比。 |
| `nonfit_rate` | 合身率。 |
| `low_signal_rate` | 比例类指标，用于对比不同类目或时间段。 |
| `pain_point_rate` | 评论痛点标签。 |
| `avg_rating` | 平均评分。 |
| `avg_quality` | 源数据字段，保留原始命名；用于分析、筛选或追溯。 |
| `risk_score` | 评分/综合分，用于排序和诊断。 |

First data row sample:

```csv
size,records,display_eligible,fit_rate,too_small_rate,too_large_rate,nonfit_rate,low_signal_rate,pain_point_rate,avg_rating,avg_quality,risk_score
57,255,1,0.5882,0.3333,0.0784,0.4118,0.1294,0.8392,8.71,,41.25
```
