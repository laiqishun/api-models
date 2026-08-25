---
title: Shopee Returns API
description: "Return, dispute, cancellation, proof, shipping carrier, and reverse tracking operations."
---

# API List

- [v2.returns.accept_offer](operations/v2-returns-accept-offer.json) (POST /api/v2/returns/accept_offer)：v2.returns.accept_offer
- [v2.returns.cancel_dispute](operations/v2-returns-cancel-dispute.json) (POST /api/v2/returns/cancel_dispute)：Sellers can only cancel compensation disputes, not normal disputes. This means that sellers can only cancel disputes when the return_status is ACCEPTED and the compensation_status is COMPENSATION_REQUESTED.
- [v2.returns.confirm](operations/v2-returns-confirm.json) (POST /api/v2/returns/confirm)：Confirm refund
- [v2.returns.convert_image](operations/v2-returns-convert-image.json) (POST /api/v2/returns/convert_image)：Convert a specific format and pictures within 10M into url.
- [v2.returns.dispute](operations/v2-returns-dispute.json) (POST /api/v2/returns/dispute)：Dispute return. Support to raise dispute when return_status in REQUESTED / PROCESSING/ACCEPTED
- [v2.returns.get_available_solutions](operations/v2-returns-get-available-solutions.json) (GET /api/v2/returns/get_available_solutions)：Get the available solutions offered to buyers.
- [v2.returns.get_return_detail](operations/v2-returns-get-return-detail.json) (GET /api/v2/returns/get_return_detail)：Use this api to get detail information of a return by return sn.
- [v2.returns.get_return_dispute_reason](operations/v2-returns-get-return-dispute-reason.json) (GET /api/v2/returns/get_return_dispute_reason)：To get the dispute return reason.
- [v2.returns.get_return_list](operations/v2-returns-get-return-list.json) (GET /api/v2/returns/get_return_list)：Use this api to get detail information of many return by shop id.
- [v2.returns.get_reverse_tracking_info](operations/v2-returns-get-reverse-tracking-info.json) (GET /api/v2/returns/get_reverse_tracking_info)：Get reverse and post-return logistics information of return request. For Normal RR, return complete reverse logistics information, for In-transit RR and Return-on-the-Spot, only return latest reverse logistics status, without providing complete reverse logistics information. For seller_validation, only one segment of reverse (buyer to seller), use tracking_info, for warehouse_validation, two segment of reverse (buyer to warehouse and warehouse to seller), use post_return_logistics_tracking_info.
- [v2.returns.get_shipping_carrier](operations/v2-returns-get-shipping-carrier.json) (GET /api/v2/returns/get_shipping_carrier)：Use this API to get the list of shipping carriers and request parameters needed before calling v2.returns.upload_shipping_proof. Only for TW and BR returns with is_seller_arrange = true.
- [v2.returns.offer](operations/v2-returns-offer.json) (POST /api/v2/returns/offer)：v2.returns.offer
- [v2.returns.query_proof](operations/v2-returns-query-proof.json) (GET /api/v2/returns/query_proof)：Support sellers to query the evidence uploaded through the upload evidence API.
- [v2.returns.upload_proof](operations/v2-returns-upload-proof.json) (POST /api/v2/returns/upload_proof)：Support sellers to upload evidence, including text and pictures and videos converted into URLs.
- [v2.returns.upload_shipping_proof](operations/v2-returns-upload-shipping-proof.json) (POST /api/v2/returns/upload_shipping_proof)：Use this API to upload shipping proof (Only for TW and BR returns with is_seller_arrange = true). This is not to upload evidence for disputes.
