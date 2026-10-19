---
title: "SHEIN 采购单 API"
description: "SHEIN official category 1000002, with one JSON model per named operation."
---

# API List

Official category: [采购单 (1000002)](https://open.sheincorp.com/documents/apidoc/1000002). 20 records. Official IDs, applicable modes, and update times remain in the [manifest](../manifest.md) and each JSON file.

- [checkEstimatedShippingFeesForSheinPartnerLogistics](operations/checkEstimatedShippingFeesForSheinPartnerLogistics.json) (POST /open-api/openapi-business-backend/purchase-estimated-fee)：Check estimated shipping fees for SHEIN partner logistics（查询SHEIN合作物流预估运费）
- [createShippingOrder](operations/createShippingOrder.json) (POST /open-api/shipping/orderToShipping)：Create shipping order（创建发货单）
- [forQueryingIntelligentUnpackingResults](operations/forQueryingIntelligentUnpackingResults.json) (POST /open-api/purchase/intelligent-packing-result)：API for querying intelligent unpacking results（查询智能拆包结果接口）
- [getPurchaseOrderInformation](operations/getPurchaseOrderInformation.json) (GET /open-api/order/purchase-order-infos)：Obtain purchase order information（获取采购单信息）
- [jitParentOrderAndChildOrderCorrespondenceQuery](operations/jitParentOrderAndChildOrderCorrespondenceQuery.json) (GET /open-api/order/get-mothe-child-orders)：JIT parent order and child order correspondence query interface（JIT母单及子单对应关系查询接口）
- [logisticsCompanyInformationQueryToBeAbandoned](operations/logisticsCompanyInformationQueryToBeAbandoned.json) (GET /open-api/shipping/express-company-list)：Logistics company information query (to be abandoned)（物流公司信息查询（即将废弃））
- [manuallyPlaceStockingOrders](operations/manuallyPlaceStockingOrders.json) (POST /open-api/idms/create-order)：Manually place stocking orders（手工下备货单）
- [modifyAndCancelShippingOrders](operations/modifyAndCancelShippingOrders.json) (POST /open-api/shipping/modify-delivery-order-info)：Modify and cancel shipping orders（修改和取消发货单订单）
- [printBoxMarkingsOrParcelLabels](operations/printBoxMarkingsOrParcelLabels.json) (POST /open-api/order/print-package)：Print box markings or parcel labels（打印箱唛或包裹面单）
- [printLogisticsWaybill](operations/printLogisticsWaybill.json) (POST /open-api/pfmp/print-purchase-logisticsLabel)：Print logistics waybill（打印物流面单）
- [productPrintingBarcode](operations/productPrintingBarcode.json) (POST /open-api/goods/print-barcode)：Product printing barcode（商品打印条码）
- [queryReceivingInformationOfSheinWarehouse](operations/queryReceivingInformationOfSheinWarehouse.json) (GET /open-api/order/storage-receiver-info)：Query the receiving information of SHEIN warehouse（查询SHEIN仓库的收件信息）
- [querySheinPartnerLogisticsProducts](operations/querySheinPartnerLogisticsProducts.json) (POST /open-api/shipping/express-company-list-v2)：Query SHEIN’s partner logistics products（查询SHEIN合作物流产品）
- [queryShippingOrderList](operations/queryShippingOrderList.json) (GET /open-api/shipping/delivery)：Query shipping order list（查询发货单列表）
- [queryStockPreparationProducts](operations/queryStockPreparationProducts.json) (POST /open-api/openapi-business-backend/stock-goods-list)：查询商品备货信息列表
- [receivingWarehouseInformationQuery](operations/receivingWarehouseInformationQuery.json) (GET /open-api/shipping/warehouse)：Receiving warehouse information query（收货仓信息查询）
- [searchForFreightForwarderInformation](operations/searchForFreightForwarderInformation.json) (POST /open-api/pfmp/shipping/thirdPartyAndChannelList)：Search for freight forwarder information（​查询货代信息）
- [shippingBasicInformationQuery](operations/shippingBasicInformationQuery.json) (GET /open-api/shipping/basic)：Shipping basic information query interface（发货基本信息查询接口）
- [shippingOrderDimensionPrintingForm](operations/shippingOrderDimensionPrintingForm.json) (POST /open-api/shipping/delivery/print-package)：Shipping order dimension printing form（发货单维度打印面单）
- [stockingOrderReviewList](operations/stockingOrderReviewList.json) (POST /open-api/idms/review-orders)：Stocking order review list（备货单审核列表）
