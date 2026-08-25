# Path: /analytics/202606/shop_performances/metrics/{metric_code}/problem_details
# Method: [GET]
# Function Description
Returns problem order or chat details for a selected SPS metric. Supported only for US-region shops.

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
| metric_code | string | Y | NRR | Metric code. Possible values include NRR, NBFR, SFCR, OTDR, AHT, and IM_DSAT. |
# Request Query Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| locale | string | N | en-US | Locale code used to localize response text. If omitted, the default locale is resolved from the request context. |
| page_token | string | N | 2 | Token used to retrieve the next page of results. Leave empty for the first page. |
| page_size | int | N | 10 | The number of results to return per page. Default value is 10. Maximum value is 50. |
# Request Sample
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202606/shop_performances/metrics/NRR/problem_details?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en-US&page_token=2&page_size=10
```

# Response Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | The success or failure status code returned in API response. |
| message | string | Success | The success or failure messages returned in API response. Reasons of failure will be described in the message. |
| request_id | string | 202203070749000101890810281E8C70B7 | Request log |
| data | object |  | Specific return information |
| ^aht_problem_order_items | []object |  | AHT problem order items. |
| ^^aftersales_type_name | string | Only Return | Aftersales type returned by TikTok Shop aftersales classification. |
| ^^approve_duration_hours | string | 12.5 | Approval duration in hours. |
| ^^inspect_duration_hours | string | 30.0 | Inspection duration in hours. |
| ^^order_id | string | 576461413038785752 | Order ID. |
| ^^return_order_id | string | 576461413038785753 | Return order ID. |
| ^^review_count | int | 2 | Number of review rounds. |
| ^^total_handle_duration_hours | string | 42.5 | Total aftersales handle duration in hours. |
| ^im_dsat_chat_items | []object |  | IM_DSAT chat session items. |
| ^^chat_duration_hours | string | 1.5 | Chat duration in hours. |
| ^^chat_record_id | string | 745961413038785752 | Chat record ID. |
| ^^customer_name | string | J*** D*** | Masked customer name. |
| ^^customer_rating | int | 2 | Customer rating from 1 to 5. |
| ^^first_reply_time | int | 1761264060 | First reply time. Unix timestamp in seconds. |
| ^^rating_reasons | []string | other | Customer rating reasons. |
| ^^service_agent | string | Agent A | Service agent name. |
| ^metric_code | string | NRR | Stable metric code. Possible values include NRR, NBFR, SFCR, OTDR, AHT, and IM_DSAT. |
| ^nbfr_problem_order_items | []object |  | NBFR problem order items. |
| ^^deliver_time | int | 1761523200 | Delivery time. Unix timestamp in seconds. |
| ^^order_create_time | int | 1761264000 | Order creation time. Unix timestamp in seconds. |
| ^^order_id | string | 576461413038785752 | Order ID. |
| ^^product_id | string | 1729592969712207010 | Product ID, when available. |
| ^^product_name | string | Cotton T-Shirt | Product name. |
| ^^return_refund_reason | string | Wrong size | Return or refund reason. |
| ^^sku_id | string | 1729592969712207013 | SKU ID. |
| ^next_page_token | string | b2Zmc2V0PTAK | An opaque token used to retrieve the next page of a paginated result set. Returns an empty string when there are no more results. |
| ^nrr_problem_order_items | []object |  | NRR problem order items. |
| ^^deliver_time | int | 1761523200 | Delivery time. Unix timestamp in seconds. |
| ^^order_create_time | int | 1761264000 | Order creation time. Unix timestamp in seconds. |
| ^^order_id | string | 576461413038785752 | Order ID. |
| ^^product_id | string | 1729592969712207008 | Product ID, when available. |
| ^^product_name | string | Wireless Headphones | Product name. |
| ^^sku_id | string | 1729592969712207012 | SKU ID. |
| ^^user_review_rating | int | 2 | User review rating from 1 to 5. |
| ^otdr_problem_order_items | []object |  | OTDR problem order items. |
| ^^actual_deliver_time | int | 1761609600 | Actual deliver time. Unix timestamp in seconds. |
| ^^expect_deliver_time | int | 1761523200 | Expected deliver time. Unix timestamp in seconds. |
| ^^order_id | string | 576461413038785752 | Order ID. |
| ^^product_name | string | Wireless Headphones | Product name. |
| ^^sku_id | string | 1729592969712207014 | SKU ID. |
| ^sfcr_problem_order_items | []object |  | SFCR problem order items. |
| ^^cancellation_reasons | []string | Defective item | Cancellation reasons. |
| ^^order_create_time | int | 1761264000 | Order creation time. Unix timestamp in seconds. |
| ^^order_id | string | 576461413038785752 | Order ID. |
| ^^product_id | string | 1729592969712207011 | Product ID, when available. |
| ^^product_name | string | Smart Watch | Product name. |
| ^^sku_id | string | 1729592969712207014 | SKU ID. |
| ^total_count | int | 200 | Total number of available records. |
# Response Sample
```json
{"code":0,"data":{"aht_problem_order_items":[{"aftersales_type_name":"Only Return","approve_duration_hours":"12.5","inspect_duration_hours":"30.0","order_id":"576461413038785752","return_order_id":"576461413038785753","review_count":2,"total_handle_duration_hours":"42.5"}],"im_dsat_chat_items":[{"chat_duration_hours":"1.5","chat_record_id":"745961413038785752","customer_name":"J*** D***","customer_rating":2,"first_reply_time":1761264060,"rating_reasons":"other","service_agent":"Agent A"}],"metric_code":"NRR","nbfr_problem_order_items":[{"deliver_time":1761523200,"order_create_time":1761264000,"order_id":"576461413038785752","product_id":"1729592969712207010","product_name":"Cotton T-Shirt","return_refund_reason":"Wrong size","sku_id":"1729592969712207013"}],"next_page_token":"b2Zmc2V0PTAK","nrr_problem_order_items":[{"deliver_time":1761523200,"order_create_time":1761264000,"order_id":"576461413038785752","product_id":"1729592969712207008","product_name":"Wireless Headphones","sku_id":"1729592969712207012","user_review_rating":2}],"otdr_problem_order_items":[{"actual_deliver_time":1761609600,"expect_deliver_time":1761523200,"order_id":"576461413038785752","product_name":"Wireless Headphones","sku_id":"1729592969712207014"}],"sfcr_problem_order_items":[{"cancellation_reasons":"Defective item","order_create_time":1761264000,"order_id":"576461413038785752","product_id":"1729592969712207011","product_name":"Smart Watch","sku_id":"1729592969712207014"}],"total_count":200},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# Error Code
For common error codes, refer to [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

