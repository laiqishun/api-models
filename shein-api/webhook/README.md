---
title: "SHEIN Webhook Webhook"
description: "SHEIN official category 2000003, with one JSON model per named operation."
---

# Webhook List

Official category: [Webhook (2000003)](https://open.sheincorp.com/documents/msgdoc/2000003). 24 records. Official IDs, applicable modes, and update times remain in the [manifest](../manifest.md) and each JSON file.

Webhook entries describe inbound events and decrypted business payloads; the path below is the official event path, not a callable SHEIN endpoint.

- [cteInvoiceNotification](operations/cteInvoiceNotification.json) (POST /invoice_status_notice)：cte Invoice Notification（cte开票通知）
- [deliveryOrderChangeNotification](operations/deliveryOrderChangeNotification.json) (POST /delivery_modify_notice)：Delivery Order Change Notification（发货单变更通知）
- [orderSynchronizationNotification](operations/orderSynchronizationNotification.json) (POST /order_push_notice)：Order synchronization notification（订单同步通知）
- [productComplianceInformationExpirationNotice](operations/productComplianceInformationExpirationNotice.json) (POST /product_compliance_change_notice)：Product compliance information expiration notice（商品合规信息失效通知）
- [productDeletionReviewNotification](operations/productDeletionReviewNotification.json) (POST /product_delete_audit)：Product deletion review notification（商品删除审核通知）
- [productListingAndDelistingNotification](operations/productListingAndDelistingNotification.json) (POST /product_shelves_notice)：Product Listing and Delisting Notification（商品上下架通知）
- [productPriceAnomalyNotification](operations/productPriceAnomalyNotification.json) (POST /product_prices_abnormal_notice)：Product price anomaly notification（商品价格异常通知）
- [productPriceAuditStatusNotice](operations/productPriceAuditStatusNotice.json) (POST /product_price_audit_status_notice)：Product price audit status notice（商品涨价审批结果通知）
- [productPublishingDocumentReviewNotificationAllChannels](operations/productPublishingDocumentReviewNotificationAllChannels.json) (POST /product_document_audit_status_notice_all_channels)：Product Publishing Document Review Notification (All Channels)（商品发布公文审核通知（全渠道））
- [productQuotaChangeNotification](operations/productQuotaChangeNotification.json) (POST /product_quota_change_notice)：Product quota change notification（商品额度变动通知）
- [productReceiveNotification](operations/productReceiveNotification.json) (POST /product_document_receive_status_notice)：Product receive notification（商品接收通知）
- [productReviewNotification](operations/productReviewNotification.json) (POST /product_document_audit_status_notice)：Product review notification（商品审核通知）
- [productVideoTaskCompleted](operations/productVideoTaskCompleted.json) (POST /product_video_conversion_completed)：Product video task completed（商品视频任务完成）
- [purchaseOrderLogisticsCooperationNotice](operations/purchaseOrderLogisticsCooperationNotice.json) (POST /logistics_forecast_result_notice)：Purchase Order Logistics Cooperation Notice（采购单合作物流通知）
- [purchaseOrderNotification](operations/purchaseOrderNotification.json) (POST /purchase_order_notice)：Purchase Order Notification（采购单通知）
- [purchaseReturnOrderStatusNotification](operations/purchaseReturnOrderStatusNotification.json) (POST /purchase_order_return_notice)：Purchase Return Order Status Notification（采购退货单状态通知）
- [purchaseReturnRequestFormStatusNotification](operations/purchaseReturnRequestFormStatusNotification.json) (POST /purchase_order_return_application_notice)：Purchase return request form status notification（采购退货申请单状态通知）
- [pushOutOfStockDemandInventoryCountNew](operations/pushOutOfStockDemandInventoryCountNew.json) (POST /out_of_stock_notice)：Push out-of-stock demand inventory count (New)（推送缺货需求库存数（新））
- [recommendedRetailPriceReviewStatusUpdate](operations/recommendedRetailPriceReviewStatusUpdate.json) (POST /product_rrp_review_status_changed)：Recommended retail price review status update（建议零售价审核状态更新）
- [recommendedRetailPriceValidityPeriodChange](operations/recommendedRetailPriceValidityPeriodChange.json) (POST /product_rrp_validity_changed)：Recommended retail price validity period change（建议零售价有效期变更）
- [returnOrderSynchronizationNotification](operations/returnOrderSynchronizationNotification.json) (POST /return_order_push_notice)：Return Order Synchronization Notification（退货单同步通知）
- [sheinCooperationLogisticsOrderNotification](operations/sheinCooperationLogisticsOrderNotification.json) (POST /logistics_order_result_notice)：SHEIN cooperation logistics order notification（SHEIN合作物流单下单通知）
- [skuInventoryWarningNotice](operations/skuInventoryWarningNotice.json) (POST /inventory_warning_notice)：SKU inventory warning notice（SKU库存预警通知）
- [storeAuthorizationRelationshipChangeNotification](operations/storeAuthorizationRelationshipChangeNotification.json) (POST /authorization_change_notice)：Store Authorization Relationship Change Notification（店铺授权关系变更通知）
