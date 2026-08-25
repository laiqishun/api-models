# Path: /analytics/202606/shop_performances/metrics
# Method: [GET]
# Function Description
Returns SPS metric details and benchmark thresholds for the authorized shop. Supported only for US-region shops.

---


# Common Parameters
For common parameters, refer to [How to call TikTok Shop APIs - Common Parameters](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Properties <!-- width:110px --> | Location <!-- width:75px --> | Type <!-- width:75px --> | Require <!-- width:60px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- | --- |
| shop_cipher | query | string | Y | GCP_XF90igAAAABh00qsWgtvOiGFNqyubMt3 | Use this property to pass shop information in requesting the API. Failure in passing the correct value when requesting the API for cross-border shops will return incorrect response. |
| Get by API [Get Authorization Shop](https://partner.tiktokshop.com/docv2/page/6507ead7b99d5302be949ba9?external_id=6507ead7b99d5302be949ba9) |  |  |  |  |  |
| content-type | header | string | Y | application/json | Allowed type: application/json |
# Request Query Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| locale | string | N | en-US | Locale code used to localize response text. If omitted, the default locale is resolved from the request context. |
# Request Sample
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202606/shop_performances/metrics?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en-US
```

# Response Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | The success or failure status code returned in API response. |
| message | string | Success | The success or failure messages returned in API response. Reasons of failure will be described in the message. |
| request_id | string | 202203070749000101890810281E8C70B7 | Request log |
| data | object |  | Specific return information |
| ^metrics | []object |  | Fixed complete SPS metric set for the authorized shop. |
| ^^benchmarks | object |  | Benchmark thresholds for the metric. |
| ^^^excellent_threshold | string | 0.02 | Excellent tier threshold. |
| ^^^poor_threshold | string | 0.08 | Poor tier threshold. |
| ^^dimension | string | Product satisfaction | SPS dimension that the metric belongs to. |
| ^^evaluate_duration_days | int | 30 | Number of days included in this metric's evaluation period. |
| ^^end_evaluation_time | int | 1761264000 | Metric evaluation period end time. Unix timestamp in seconds. |
| ^^start_evaluation_time | int | 1758672000 | Metric evaluation period start time. Unix timestamp in seconds. |
| ^^metric_code | string | NRR | Stable metric code. Possible values include NRR, NBFR, SFCR, OTDR, AHT, and IM_DSAT. |
| ^^metric_name | string | 60-day negative review rate | Localized metric display name. |
| ^^score | string | 4.7 | Metric score, from 0 to 5. |
| ^^status | string | EXCELLENT | Metric status. Possible values include EXCELLENT, GOOD, POOR, CRITICAL and NIL. |
| ^^status_text | string | Excellent | Metric status text. Values like Excellent, Good, Normal, Attention. |
| ^^value | string | 0.97 | Metric value. Hours are represented as values; percentages are represented as values from 0 to 100. |
| ^^value_unit | string | PERCENT | Unit of the metric value. Possible values include PERCENT and HOURS. |
| ^^top_reason_text | string | Top opportunity | Indicates that this metric is a key contributor to SPS. |
# Response Sample
```json
{"code":0,"data":{"metrics":[{"benchmarks":{"excellent_threshold":"0.02","poor_threshold":"0.08"},"dimension":"Product satisfaction","evaluate_duration_days":30,"end_evaluation_time":1761264000,"start_evaluation_time":1758672000,"metric_code":"NRR","metric_name":"60-day negative review rate","score":"4.7","status":"EXCELLENT","status_text":"Excellent","value":"0.97","value_unit":"PERCENT","top_reason_text":"Top opportunity"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# Error Code
For common error codes, refer to [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

