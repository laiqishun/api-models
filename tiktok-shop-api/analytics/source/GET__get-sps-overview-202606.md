# Path: /analytics/202606/shop_performances/overview
# Method: [GET]
# Function Description
Returns the SPS overview for the authorized shop, including the score, tier, dimensions, benefits, and top issues. Supported only for US-region shops.

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
https://open-api.tiktokglobalshop.com/analytics/202606/shop_performances/overview?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&locale=en-US
```

# Response Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | The success or failure status code returned in API response. |
| message | string | Success | The success or failure messages returned in API response. Reasons of failure will be described in the message. |
| request_id | string | 202203070749000101890810281E8C70B7 | Request log |
| data | object |  | Specific return information |
| ^benefits | []object |  | Fixed complete set of benefits associated with the shop SPS score. |
| ^^benefit_name | string | LIVE giveaway | Benefit display name localized by the requested locale. |
| ^^is_unlocked | bool | true | Whether the shop has unlocked this benefit. |
| ^^unlock_score | string | 4.5 | Score required to unlock the benefit, from 0 to 5. |
| ^dimensions | []object |  | Score details by SPS dimension. |
| ^^name | string | Product satisfaction | Dimension name. |
| ^^score | string | 4.8 | Dimension score, from 0 to 5. |
| ^^status | string | EXCELLENT | Dimension status enum. Possible values include EXCELLENT, GOOD, POOR, CRITICAL and NIL. |
| ^^status_text | string | Excellent | Dimension status text. Values like Excellent, Good, Normal, Attention. |
| ^^weight | string | 70 | Dimension weight as a percent from 0 to 100. |
| ^evaluate_duration_days | int | 90 | The number of days included in the score evaluation period. |
| ^end_evaluation_time | int | 1782518400 | The evaluation period end time. Unix timestamp in seconds. |
| ^start_evaluation_time | int | 1774828800 | The evaluation period start time. Unix timestamp in seconds. |
| ^peer_percentile | string | 86.5 | The shop's percentile among peers, from 0 to 100. |
| ^primary_category | object |  | The shop's primary category. |
| ^^category_id | string | 601450 | The primary category ID. |
| ^^category_name | string | Home Supplies | The primary category name. |
| ^sps_score | string | 4.6 | The shop SPS score, from 0 to 5 with one decimal place. |
| ^sps_tier | string | GOOD | The SPS tier. Possible values include EXCELLENT, GOOD, POOR, CRITICAL and NIL. |
| ^sps_tier_text | string | Excellent | The SPS tier. Values like Excellent, Good, Normal, Attention. |
| ^top_issues | object |  | Top SPS issues that contributed to the current score. |
| ^^issues | []object |  | Ranked issue list. |
| ^^^description | string | Your on-time delivery performance is lower than peer shops. | Localized issue description. |
| ^^^evaluate_duration_days | int | 30 | Number of days included in this issue's evaluation period. |
| ^^^end_evaluation_time | int | 1761264000 | Issue evaluation period end time. Unix timestamp in seconds. |
| ^^^start_evaluation_time | int | 1758672000 | Issue evaluation period start time. Unix timestamp in seconds. |
| ^^^metric_code | string | OTDR | Related metric code. Possible values include NRR, NBFR, SFCR, OTDR, AHT, and IM_DSAT. |
| ^^^metric_name | string | On-time delivery rate | Localized metric display name. |
| ^^^percentile | string | 72.4 | Metric percentile among peer shops, from 0 to 100. |
| ^^^rank | int | 1 | Issue rank, where 1 is the top issue. |
| ^^summary | string | Improve late dispatch and negative reviews to increase your SPS score. | Localized summary of the top issues. |
| ^update_time | int | 1761264000 | The latest score refresh time. Unix timestamp in seconds. |
# Response Sample
```json
{"code":0,"data":{"benefits":[{"benefit_name":"LIVE giveaway","is_unlocked":true,"unlock_score":"4.5"}],"dimensions":[{"name":"Product satisfaction","score":"4.8","status":"EXCELLENT","status_text":"Excellent","weight":"70"}],"evaluate_duration_days":90,"end_evaluation_time":1782518400,"start_evaluation_time":1774828800,"peer_percentile":"86.5","primary_category":{"category_id":"601450","category_name":"Home Supplies"},"sps_score":"4.6","sps_tier":"GOOD","sps_tier_text":"Excellent","top_issues":{"issues":[{"description":"Your on-time delivery performance is lower than peer shops.","evaluate_duration_days":30,"end_evaluation_time":1761264000,"start_evaluation_time":1758672000,"metric_code":"OTDR","metric_name":"On-time delivery rate","percentile":"72.4","rank":1}],"summary":"Improve late dispatch and negative reviews to increase your SPS score."},"update_time":1761264000},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# Error Code
For common error codes, refer to [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |

