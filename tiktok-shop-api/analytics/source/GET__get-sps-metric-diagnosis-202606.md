# Path: /analytics/202606/shop_performances/metrics/{metric_code}/diagnosis
# Method: [GET]
# Function Description
Returns diagnosis details for a single SPS metric, including benchmark thresholds, trends, calculation details, and distribution details. Supported only for US-region shops.

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
| metric_code | string | Y | OTDR | Metric code. Possible values include NRR, NBFR, SFCR, OTDR, AHT, and IM_DSAT. |
# Request Query Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Require <!-- width:90px --> | Sample <!-- width:254px --> | Properties description <!-- width:254px --> |
| --- | --- | --- | --- | --- |
| locale | string | N | en-US | Locale code used to localize response text. If omitted, the default locale is resolved from the request context. |
| trend_duration_days | int | N | 30 | Number of days to look back for metric trend data. Default value is 30. |
# Request Sample
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/analytics/202606/shop_performances/metrics/OTDR/diagnosis?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en-US&trend_duration_days=30
```

# Response Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | The success or failure status code returned in API response. |
| message | string | Success | The success or failure messages returned in API response. Reasons of failure will be described in the message. |
| request_id | string | 202203070749000101890810281E8C70B7 | Request log |
| data | object |  | Specific return information |
| ^benchmarks | object |  | Benchmark thresholds for this metric. |
| ^^excellent_threshold | string | 0.98 | Excellent tier threshold. |
| ^^poor_threshold | string | 0.80 | Poor tier threshold. |
| ^calculation_rule | object |  | Calculation details used to derive this metric. |
| ^^denominator_label | string | Delivered orders | Denominator label. |
| ^^denominator_value | string | 1000 | Denominator value. |
| ^^numerator_label | string | On-time delivered orders | Numerator label. |
| ^^numerator_value | string | 947 | Numerator value. |
| ^dimension | string | Product satisfaction | SPS dimension that the metric belongs to. |
| ^distribution_details | []object |  | Additional distribution details for the metric. |
| ^^count | int | 820 | Number of items in the distribution bucket. |
| ^^name | string | Dispatch 24-48 Hours | Distribution detail name. |
| ^^percent | string | 82.0 | Percentage of items in the distribution bucket, from 0 to 100. |
| ^evaluate_duration_days | int | 30 | Number of days included in the metric evaluation period. |
| ^end_evaluation_time | int | 1761264000 | Metric evaluation period end time. Unix timestamp in seconds. |
| ^start_evaluation_time | int | 1758672000 | Metric evaluation period start time. Unix timestamp in seconds. |
| ^metric_code | string | OTDR | Stable metric code. Possible values include NRR, NBFR, SFCR, OTDR, AHT, and IM_DSAT. |
| ^score | string | 4.3 | Metric score, from 0 to 5. |
| ^status | string | GOOD | Metric status. Possible values include EXCELLENT, GOOD, POOR, CRITICAL and NIL. |
| ^status_text | string | Excellent | Metric status text. Values like Excellent, Good, Normal, Attention. |
| ^trend | object |  | Metric trend over the requested lookback range. |
| ^^data_points | []object |  | Metric trend data points. |
| ^^^record_date | string | 20260601 | Trend date in yyyyMMdd format. |
| ^^^value | string | 0.947 | Metric value on the trend date, using the same unit as value_unit. |
| ^value | string | 0.947 | Metric value. Ratios are represented as values from 0 to 1; percentages are represented as values from 0 to 100. |
| ^value_unit | string | PERCENT | Unit of the metric value. Possible values include PERCENT and HOURS. |
| ^analyses | []object |  | Diagnostic insights for the selected metric. |
| ^^summaries | []string | Stable performance. Top 3 issues to address. | Summarized causes affecting the selected metric. |
| ^^details | []string | Your 30-day on-time delivery rate is only higher than **% of peers, which is hurting your SPS. | Detailed explanations for the selected metric diagnosis. |
# Response Sample
```json
{"code":0,"data":{"benchmarks":{"excellent_threshold":"0.98","poor_threshold":"0.80"},"calculation_rule":{"denominator_label":"Delivered orders","denominator_value":"1000","numerator_label":"On-time delivered orders","numerator_value":"947"},"dimension":"Product satisfaction","distribution_details":[{"count":820,"name":"Dispatch 24-48 Hours","percent":"82.0"}],"evaluate_duration_days":30,"end_evaluation_time":1761264000,"start_evaluation_time":1758672000,"metric_code":"OTDR","score":"4.3","status":"GOOD","status_text":"Excellent","trend":{"data_points":[{"record_date":"20260601","value":"0.947"}]},"value":"0.947","value_unit":"PERCENT","analyses":[{"summaries":"Stable performance. Top 3 issues to address.","details":"Your 30-day on-time delivery rate is only higher than **% of peers, which is hurting your SPS."}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# Error Code
For common error codes, refer to [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

