# Path: /analytics/202606/shop_performances/metrics/{metric_code}/top_items
# Method: [GET]
# Function Description
Returns top products, logistics providers, or aftersales types for a selected SPS metric. Supported only for US-region shops.

---


# Common Parameters
For common parameters, refer to [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | Use this property to pass shop information in requesting the API. Failure in passing the correct value when requesting the API for cross-border shops will return incorrect response. |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | Allowed type: application/json |
# Request Path Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| metric_code | string | Y | NRR | Metric code. Possible values include NRR, NBFR, OTDR, and AHT. |
# Request Query Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| locale | string | N | en-US | Locale code used to localize response text. If omitted, the default locale is resolved from the request context. |
# Request Sample
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202606/shop_performances/metrics/NRR/top_items?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en-US
```

# Response Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | The success or failure status code returned in API response. |
| message | string | Success | The success or failure messages returned in API response. Reasons of failure will be described in the message. |
| request_id | string | 202203070749000101890810281E8C70B7 | Request log |
| data | object |  | Specific return information |
| ^aht_aftersales_type_items | []object |  | AHT aftersales type items. |
| ^^handle_duration_hours | string | 18.5 | Average handle duration in hours. |
| ^^product_id | string | 1729592969712207011 | Product ID. |
| ^^product_name | string | Smart Watch | Product name. |
| ^^return_order_count | int | 30 | Total number of return orders. |
| ^^top_aftersales_type_name | string | Only Refund | Top aftersales type returned by TikTok Shop aftersales classification. |
| ^^top_type_order_count | int | 20 | Number of orders associated with the top aftersales type. |
| ^^image_url | string | https://example.com/product.jpg | Product image URL. |
| ^metric_code | string | NRR | Stable metric code. Possible values include NRR, NBFR, OTDR, and AHT. |
| ^nbfr_top_product_items | []object |  | NBFR top product items. |
| ^^product_id | string | 1729592969712207010 | Product ID. |
| ^^product_name | string | Cotton T-Shirt | Product name. |
| ^^return_order_count | int | 8 | Number of return or refund orders. |
| ^^top_reason_order_count | int | 5 | Number of orders associated with the top return or refund reason. |
| ^^top_return_reasons | []string | Item doesn't match description | Top return or refund reasons. |
| ^^image_url | string | https://example.com/product.jpg | Product image URL. |
| ^nrr_top_product_items | []object |  | NRR top product items. |
| ^^delivered_order_count | int | 300 | Total number of delivered orders. |
| ^^image_url | string | https://example.com/product.jpg | Product image URL. |
| ^^negative_order_count | int | 12 | Number of orders with negative reviews. |
| ^^product_id | string | 1729592969712207008 | Product ID. |
| ^^product_name | string | Wireless Headphones | Product name. |
| ^^top_review_reasons | []string | Item doesn't match description | Top negative review reasons. |
| ^otdr_logistics_items | []object |  | OTDR logistics provider items. |
| ^^delivered_order_count | int | 1000 | Total number of delivered orders. |
| ^^logistics_provider | string | TikTok Shipping | Logistics provider name. |
| ^^on_time_deliver_order_count | int | 947 | Number of orders delivered on time. |
| ^^on_time_deliver_rate | string | 0.947 | On-time delivery rate as a ratio from 0 to 1. |
| ^total_count | int | 120 | Total number of available records. |
# Response Sample
```json
{"code":0,"data":{"aht_aftersales_type_items":[{"handle_duration_hours":"18.5","product_id":"1729592969712207011","product_name":"Smart Watch","return_order_count":30,"top_aftersales_type_name":"Only Refund","top_type_order_count":20,"image_url":"https://example.com/product.jpg"}],"metric_code":"NRR","nbfr_top_product_items":[{"product_id":"1729592969712207010","product_name":"Cotton T-Shirt","return_order_count":8,"top_reason_order_count":5,"top_return_reasons":"Item doesn't match description","image_url":"https://example.com/product.jpg"}],"nrr_top_product_items":[{"delivered_order_count":300,"image_url":"https://example.com/product.jpg","negative_order_count":12,"product_id":"1729592969712207008","product_name":"Wireless Headphones","top_review_reasons":"Item doesn't match description"}],"otdr_logistics_items":[{"delivered_order_count":1000,"logistics_provider":"TikTok Shipping","on_time_deliver_order_count":947,"on_time_deliver_rate":"0.947"}],"total_count":120},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# Error Code
For common error codes, refer to [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

