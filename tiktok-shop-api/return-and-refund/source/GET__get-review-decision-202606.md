# Path: /return_refund/202606/review_decision
# Method: [GET]
# Function Description
Description of [GET]/return_refund/:version/Get_Review_Decision

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
| seller_id | int | Y | 7494781899660428507 | The unique identifier of the seller/shop |
| return_or_cancel_id | string | Y | 4035319218955782461 | The TikTok Shop return or cancellation request ID to evaluate. Pass the request identifier for the target cancellation, refund, return, or other supported aftersales flow. Do not pass an order ID or order line ID in this field. |
| locale | string | N | en-US | The BCP-47 locale codes for displaying the return reason, delimited by commas. Default: en-US |
| Refer to [Locale codes](678e3a47bae28f030a8c7523) for the list of supported locale codes. |  |  |  |  |
| check_decisions | []string | N | APPROVE_REFUND,REJECT_RETURN | The seller decisions to evaluate for the specified aftersales request. Possible Values: |

* `APPROVE_REQUEST_CANCEL`
* `APPROVE_REFUND`
* `APPROVE_RETURN`
* `APPROVE_RECEIVED_PACKAGE`
* `APPROVE_REPLACEMENT`
* `ISSUE_REPLACEMENT_REFUND`
* `DIRECT_REFUND`
* `REJECT_REQUEST_CANCEL`
* `REJECT_REFUND`
* `REJECT_RETURN`
* `REJECT_RECEIVED_PACKAGE`
* `REJECT_REPLACEMENT`
   -`ISSUE_EXCHANGE_REFUND`
   -`OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG`
   **Note:** When omitted, the API evaluates all supported seller decisions for the request and returns one result per decision. |

# Request Sample
**Query**
```Plain Text
https://open-api.tiktokglobalshop.com/return_refund/202606/review_decision?app_key=123abc&sign=5361235029d141222525e303d742f9e38aea052d10896d3197ab9d6233730b8c&timestamp=1625484268&shop_cipher=ROW_RHkDDABBAAB8tKAVoAqsMTjsQZFLyNfY&seller_id=7494781899660428507&return_or_cancel_id=4035319218955782461&locale=en-US&check_decisions=APPROVE_REFUND,REJECT_RETURN
```

# Response Parameters
| Properties <!-- width:110px --> | Type <!-- width:90px --> | Sample <!-- width:289px --> | Properties description <!-- width:289px --> |
| --- | --- | --- | --- |
| code | int | 0 | The success or failure status code returned in API response. |
| message | string | Success | The success or failure messages returned in API response. Reasons of failure will be described in the message. |
| request_id | string | 202203070749000101890810281E8C70B7 | Request log |
| data | object |  | Specific return information |
| ^line_items | []object |  | Line items for which this decision applies. Decision details apply to each line item individually (e.g. a partial refund amount of $1.00 for 3 line items will result in a total partial refund amount of $3.00). |
| ^^return_line_item_id | string | 4035319218955782461 | Unique identifier for this item in the return. In the case of virtual bundle, this corresponds to the id of the original parent item bundle. |
| ^^sub_return_line_item_id | string | 4035227657962164815 | Unique identifier for this item in the return. In the case of virtual bundle, this corresponds to the id of the current child item being returned. |
| ^^decisions | []object |  | The list of candidate review decisions for this line item. |
| ^^^decision | string | OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG | Action/decision to be applied. |
| Possible values: |  |  |  |

* `APPROVE_REQUEST`
* `APPROVE_RETURN_PACKAGE`
* `REJECT_REQUEST`
* `REJECT_RETURN_PACKAGE`
* `REFUND_INSTEAD`
* `OFFER_PARTIAL_REFUND`
* `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG` |
   ^^^eligible |bool |false |Use this field to recognize whether an decision is eligible for an return or cancellation:
* TRUE
* FALSE |
   ^^^ineligible_code |int |25005020 |The reason code for an ineligible decision. |
   ^^^ineligible_reason |string |the return is already completed, you can't approve again. |The reason for an ineligible decision. |
   ^^^available_reject_reasons |[]object | |The reject reason name seller can use to reject buyer's return or cancellation request. |
   ^^^^name |string |seller_reject_apply_product_has_been_packed |The reject reason name seller can use to reject buyer's return or cancellation request. |
   ^^^^text |string |The display text for the reject reason. |Product shipped. Tracking updates will be available soon.The display text for the reject reason. |
   ^^^partial_refund_amount_range |object | |The allowed partial refund amount band. Returned for the `OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG` decision when it is eligible; omitted for all other decisions. |
   ^^^^min_amount |string |2.34 |The minimum partial refund amount the seller may offer. |
   ^^^^max_amount |string |3.33 |The maximum partial refund amount the seller may offer. |
   ^^^^currency |string |USD |The currency of the partial refund amount range, matching the currency of the current return request. |
   ^request_log_id |string |20260713225708FB… |The log id of this request, used for troubleshooting with TikTok Shop support. |
   ^errors |[]object | |Lists errors for partially failed requests. For example, if a request reviews multiple orders or items and only some fail, individual error details are returned here.
   **IMPORTANT**: Partial failures still return a top-level success code (0), so clients must also check this field to detect partial errors. For complete failures (e.g. validation errors), the top-level response code and message will indicate a failure, but this field will remain empty. |
   ^^code |string |98001004 |Error Code |
   ^^message |string |Invalid parameters. Please verify your input before retrying |Error Description |

# Response Sample
```json
{"code":0,"data":{"line_items":[{"return_line_item_id":"4035319218955782461","sub_return_line_item_id":"4035227657962164815","decisions":[{"decision":"OFFER_PARTIAL_REFUND_AFTER_RECEIVING_PKG","eligible":false,"ineligible_code":25005020,"ineligible_reason":"the return is already completed, you can't approve again.","available_reject_reasons":[{"name":"seller_reject_apply_product_has_been_packed","text":"The display text for the reject reason."}],"partial_refund_amount_range":{"min_amount":"2.34","max_amount":"3.33","currency":"USD"}}]}],"request_log_id":"20260713225708FB…","errors":[{"code":"98001004","message":"Invalid parameters. Please verify your input before retrying"}]},"message":"Success","request_id":"202203070749000101890810281E8C70B7"}
```

# Error Code
For common error codes, refer to [How to call TikTok Shop APIs - Common Error Code](https://partner.tiktokshop.com/docv2/page/64f199679495ef0281851ee5#Back%20To%20Top)
| Code <!-- width:250px --> | Message <!-- width:553px --> |
| --- | --- |
| 25001003 | Invalid order status. |
| 25005020 | reverse amount not support partial refund |
| 25005021 | partial refund only support single sku |
| 25011010 | request has been transferred to platform operator |
| 25011011 | reverse status cannot reject application |
| 25011012 | reverse status cannot approve application |

