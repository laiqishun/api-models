---
title: "SHEIN 客单 API"
description: "SHEIN official category 2000001, with one JSON model per named operation."
---

# API List

Official category: [客单 (2000001)](https://open.sheincorp.com/documents/apidoc/2000001). 17 records. Official IDs, applicable modes, and update times remain in the [manifest](../manifest.md) and each JSON file.

- [cancelSplittingOrderPackages](operations/cancelSplittingOrderPackages.json) (POST /open-api/order/unpacking-group-remove)：Cancel splitting order packages（取消超限拆分包裹）
- [confirmationOfNoGoods](operations/confirmationOfNoGoods.json) (POST /open-api/order/confirm-no-stock)：Confirmation of no goods API（确认无货接口）
- [confirmSplittingOrderPackages](operations/confirmSplittingOrderPackages.json) (POST /open-api/order/unpacking-group-confirm)：Confirm splitting order packages（确认超限拆分包裹）
- [customerOrderLogisticsTrackingInquiry](operations/customerOrderLogisticsTrackingInquiry.json) (GET /open-api/gsp/logistics-track)：Customer order logistics tracking inquiry（客单物流轨迹查询）
- [exportAddress](operations/exportAddress.json) (POST /open-api/order/export-address)：Export address API（导出地址接口）
- [onlineOrder](operations/onlineOrder.json) (POST /open-api/gsp/place-express-order)：Online order（在线下单）
- [printExpressInfo](operations/printExpressInfo.json) (POST /open-api/order/print-express-info)：Print express info API（打印面单接口）
- [queryAvailableLogisticsInformationForOrder](operations/queryAvailableLogisticsInformationForOrder.json) (POST /open-api/gsp/order-mapping-channels)：Query available logistics information for the order（查询订单可用物流信息）
- [queryAvailableShippingWarehousesForOrder](operations/queryAvailableShippingWarehousesForOrder.json) (POST /open-api/gsp/available-shipping-warehouse)：Query available shipping warehouses for the order（查询订单可用发货仓库）
- [queryChannelInformationAtMerchantLevel](operations/queryChannelInformationAtMerchantLevel.json) (POST /open-api/order/express-channel)：Query channel information at the merchant level（商家维度查渠道信息）
- [queryOrderDetail](operations/queryOrderDetail.json) (POST /open-api/order/order-detail)：Query order detail API（请求订单详情）
- [queryOrderList](operations/queryOrderList.json) (POST /open-api/order/order-list)：Query order list API（请求订单列表）
- [queryOrderResult](operations/queryOrderResult.json) (POST /open-api/gsp/check-express-order)：Query order result（查询下单结果）
- [queryWarehouseAddress](operations/queryWarehouseAddress.json) (POST /open-api/gsp/warehouse-address)：Query warehouse address（查询仓库地址）
- [switchExportAddressToShipping](operations/switchExportAddressToShipping.json) (POST /open-api/gsp/switch-self-shipping)：Switch export address to shipping（切换导出地址发货）
- [syncInvoiceInfoToShein](operations/syncInvoiceInfoToShein.json) (POST /open-api/order/sync-invoice-info)：Sync invoice info to SHEIN API（回传发票信息）
- [uploadExpressesInfo](operations/uploadExpressesInfo.json) (POST /open-api/order/import-batch-multiple-express)：Upload expresses info API（批量上传运单号）
