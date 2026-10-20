# Refunds, Claims & Returns

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Returns](https://global-selling.mercadolibre.com/devsite/manage-returns) | 6 | 0 | modeled |
| [Official: Manage Claims](https://global-selling.mercadolibre.com/devsite/manage-claims) | 8 | 0 | modeled |
| [Official: Claims Messages](https://global-selling.mercadolibre.com/devsite/manage-claims-messages) | 8 | 0 | modeled |
| [Official: Claims Resolutions](https://global-selling.mercadolibre.com/devsite/manage-claim-resolutions) | 6 | 0 | modeled |

## API List

- [checkReturn](operations/checkReturn.json) (GET /marketplace/v2/claims/{claim_id}/returns)：Check a return [Official](https://global-selling.mercadolibre.com/devsite/manage-returns)
- [createFullRefund](operations/createFullRefund.json) (POST /marketplace/v2/claims/{claim_id}/expected-resolutions/refund)：Full Refund [Official](https://global-selling.mercadolibre.com/devsite/manage-claim-resolutions)
- [createHowOfferPartialRefund](operations/createHowOfferPartialRefund.json) (POST /marketplace/v2/claims/{claim_id}/expected-resolutions/partial-refund)：How to Offer a Partial Refund [Official](https://global-selling.mercadolibre.com/devsite/manage-claim-resolutions)
- [createMessageWithUploadedFile](operations/createMessageWithUploadedFile.json) (POST /marketplace/v2/claims/{claim_id}/actions/send-message)：Create a Message with the Uploaded File [Official](https://global-selling.mercadolibre.com/devsite/manage-claims-messages)
- [createPerformReturnReview](operations/createPerformReturnReview.json) (POST /post-purchase/v1/returns/{return_id}/return-review)：Perform a return review [Official](https://global-selling.mercadolibre.com/devsite/manage-returns)
- [createProductReturn](operations/createProductReturn.json) (POST /marketplace/v2/claims/{claim_id}/expected-resolutions/allow-return)：Product Return [Official](https://global-selling.mercadolibre.com/devsite/manage-claim-resolutions)
- [createUploadingAttachments](operations/createUploadingAttachments.json) (POST /marketplace/v2/claims/{claim}/attachments)：Uploading Attachments [Official](https://global-selling.mercadolibre.com/devsite/manage-claims-messages)
- [downloadFile](operations/downloadFile.json) (GET /post-purchase/v1/claims/{claim_id}/attachments/1517482146_31489bf8-95e3-4a2d-bcff-3c57771fb7c4.png/download)：Download the file [Official](https://global-selling.mercadolibre.com/devsite/manage-claims-messages)
- [getAttachmentsByAttachmentsId](operations/getAttachmentsByAttachmentsId.json) (GET /post-purchase/v1/claims/{claim_id}/attachments/{attachments_id})：Get file information [Official](https://global-selling.mercadolibre.com/devsite/manage-claims-messages)
- [getByAttachmentsIdDownload](operations/getByAttachmentsIdDownload.json) (GET /marketplace/v2/claims/{claim_id}/attachments/{attachments_id}/download)：Download the file [Official](https://global-selling.mercadolibre.com/devsite/manage-claims-messages)
- [getClaimActionHistory](operations/getClaimActionHistory.json) (GET /marketplace/v2/claims/{claim_id}/actions-history)：Claim action history [Official](https://global-selling.mercadolibre.com/devsite/manage-claims)
- [getClaimsDetails](operations/getClaimsDetails.json) (GET /marketplace/v2/claims/{claim_id}/detail)：Claims details [Official](https://global-selling.mercadolibre.com/devsite/manage-claims)
- [getClaimsSearch](operations/getClaimsSearch.json) (GET /marketplace/v2/claims/search)：Parameters: [Official](https://global-selling.mercadolibre.com/devsite/manage-claims)
- [getClaimStatusHistory](operations/getClaimStatusHistory.json) (GET /marketplace/v2/claims/{claim_id}/status-history)：Claim status history [Official](https://global-selling.mercadolibre.com/devsite/manage-claims)
- [getConsultExpectedResolutions](operations/getConsultExpectedResolutions.json) (GET /marketplace/v2/claims/{claim_id}/expected-resolutions)：Consult expected resolutions [Official](https://global-selling.mercadolibre.com/devsite/manage-claim-resolutions)
- [getConsultSpecificClaim](operations/getConsultSpecificClaim.json) (GET /marketplace/v2/claims/{claim_id})：Consult an specific claim [Official](https://global-selling.mercadolibre.com/devsite/manage-claims)
- [getEvidenceFileNameAttachFailedReturnReview](operations/getEvidenceFileNameAttachFailedReturnReview.json) (POST /post-purchase/v1/claims/{claim_id}/returns/attachments)：Get the evidence file name to attach to a failed return review [Official](https://global-selling.mercadolibre.com/devsite/manage-returns)
- [getFileInformation](operations/getFileInformation.json) (GET /post-purchase/v1/claims/{claim_id}/attachments/example.png)：Get file information [Official](https://global-selling.mercadolibre.com/devsite/manage-claims-messages)
- [getHowIdentifyIfClaimAffectsReputation](operations/getHowIdentifyIfClaimAffectsReputation.json) (GET /marketplace/v2/claims/{claim_id}/affects-reputation)：How to identify if a claim affects reputation [Official](https://global-selling.mercadolibre.com/devsite/manage-claims)
- [getHowOfferPartialRefund](operations/getHowOfferPartialRefund.json) (GET /marketplace/v2/claims/{claim_id}/partial-refund/available-offers)：How to Offer a Partial Refund [Official](https://global-selling.mercadolibre.com/devsite/manage-claim-resolutions)
- [getReasonsByReasonId](operations/getReasonsByReasonId.json) (GET /marketplace/v2/claims/reasons/{reason_id})：Params: [Official](https://global-selling.mercadolibre.com/devsite/manage-claims)
- [getReasonsCreateFailedReturnReview](operations/getReasonsCreateFailedReturnReview.json) (GET /post-purchase/v1/returns/reasons)：Get reasons to create a failed return review [Official](https://global-selling.mercadolibre.com/devsite/manage-returns)
- [getClaimReasons](operations/getClaimReasons.json) (GET /marketplace/v2/claims/reasons/PNR9502)：Params: [Official](https://global-selling.mercadolibre.com/devsite/manage-claims)
- [postActionsOpenDispute](operations/postActionsOpenDispute.json) (POST /marketplace/v2/claims/{claim_id}/actions/open-dispute)：Request Mediation (Dispute Resolution) [Official](https://global-selling.mercadolibre.com/devsite/manage-claim-resolutions)
- [postByClaimIdAttachments](operations/postByClaimIdAttachments.json) (POST /marketplace/v2/claims/{claim_id}/attachments)：Uploading Attachments [Official](https://global-selling.mercadolibre.com/devsite/manage-claims-messages)
- [retrieveAllMessagesClaim](operations/retrieveAllMessagesClaim.json) (GET /marketplace/v2/claims/{claim_id}/messages)：Retrieve all messages of a claim [Official](https://global-selling.mercadolibre.com/devsite/manage-claims-messages)
- [returnShippingCost](operations/returnShippingCost.json) (GET /post-purchase/v1/claims/{claim_id}/charges/return-cost)：Return Shipping Cost [Official](https://global-selling.mercadolibre.com/devsite/manage-returns)
- [reviewOkProductArrivedAsExpected](operations/reviewOkProductArrivedAsExpected.json) (POST /post-purchase/v1/returns/{id}/return-review)：Review OK (Product arrived as expected) [Official](https://global-selling.mercadolibre.com/devsite/manage-returns)
