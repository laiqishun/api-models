---
title: "SHEIN MES API"
description: "SHEIN official category 1000015, with one JSON model per named operation."
---

# API List

Official category: [MES (1000015)](https://open.sheincorp.com/documents/apidoc/1000015). 25 records. Official IDs, applicable modes, and update times remain in the [manifest](../manifest.md) and each JSON file.

- [batchQuerySkcInformation](operations/batchQuerySkcInformation.json) (POST /open-api/spss/skc-info-query)：Batch query SKC information（批量查询SKC信息）
- [checkSupplierFinalStock](operations/checkSupplierFinalStock.json) (POST /open-api/mes/order-inventory-surplus/list)：Check supplier’s final stock（查询供应商尾货）
- [cuttingBedCompleted](operations/cuttingBedCompleted.json) (POST /open-api/mes/end-cut-bed)：Cutting bed completed（裁床完成）
- [inboundOrderConfirm](operations/inboundOrderConfirm.json) (POST /open-api/sims/inbound-order-confirm)：自营供应商入库单确认
- [inboundOrderModify](operations/inboundOrderModify.json) (POST /open-api/sims/inbound-order-modify)：自营供应商待入库数量修改
- [inboundOrderQuery](operations/inboundOrderQuery.json) (POST /open-api/sims/inbound-order-query)：入库单列表查询
- [informationQuery](operations/informationQuery.json) (POST /open-api/mes/bundle-info)：Information query interface（扎信息查询接口）
- [locationQuery](operations/locationQuery.json) (POST /open-api/sims/location-query)：库位列表数据
- [mesFac001OrderDataAcquisition](operations/mesFac001OrderDataAcquisition.json) (POST /open-api/mes/get-order-info)：MES-FAC-001 order data acquisition interface（MES-FAC-001 订单数据获取接口）
- [mesFac002ProcurementInformation](operations/mesFac002ProcurementInformation.json) (POST /open-api/mes/get-purchase-info)：MES-FAC-002 Procurement information interface（MES-FAC-002 采购信息接口）
- [mesFac003PickingInformation](operations/mesFac003PickingInformation.json) (POST /open-api/mes/get-material-info)：MES-FAC-003 Picking information interface（MES-FAC-003 领料信息接口）
- [mesFac004SecondaryProcess](operations/mesFac004SecondaryProcess.json) (POST /open-api/mes/get-second-precess)：MES-FAC-004 secondary process interface（MES-FAC-004 二次工艺接口）
- [mesFac005BulkGoodsBom](operations/mesFac005BulkGoodsBom.json) (POST /open-api/mes/get-big-goods-bom)：MES-FAC-005 bulk goods BOM interface（MES-FAC-005 大货bom接口）
- [outboundOrderQuery](operations/outboundOrderQuery.json) (POST /open-api/sims/outbound-order-query)：出库订单列表查询
- [queryInvoiceInformation](operations/queryInvoiceInformation.json) (POST /open-api/mes/deliver-order/list)：Query invoice information（查询发货单信息）
- [queryMaterialExceptionDetailed](operations/queryMaterialExceptionDetailed.json) (POST /open-api/mes/material-anomalous/list)：Query material exception detailed interface（查询物料异常详细接口）
- [queryOrderInformationBasedOnOrderNumber](operations/queryOrderInformationBasedOnOrderNumber.json) (POST /open-api/mes/query-produce-order-info-by-id)：Query order information based on order number（根据订单号查询订单信息）
- [queryProductionOrderNumberByTime](operations/queryProductionOrderNumberByTime.json) (POST /open-api/mes/query-produce-order-ids)：Query production order number by time（按时间查询生产制单号）
- [queryProductionOrders](operations/queryProductionOrders.json) (POST /open-api/mes/get-produce-order-info)：Query production orders（查询生产订单）
- [queryPurchaseOrderDetails](operations/queryPurchaseOrderDetails.json) (POST /open-api/mes/purchase-detail-info-list)：Query purchase order details interface（查询采购单详细接口）
- [sewingCompleted](operations/sewingCompleted.json) (POST /open-api/mes/sew-end)：Sewing completed（车缝完工）
- [simsStockQuery](operations/simsStockQuery.json) (POST /open-api/sims/stock-query)：库存结余列表查询
- [simsStockUpdate](operations/simsStockUpdate.json) (POST /open-api/sims/stock-update)：自营供应商库存更新
- [skcPageQuery](operations/skcPageQuery.json) (POST /open-api/spss/skc-page-query)：分页查询商家SKC列表
- [updateSupplierTailGoods](operations/updateSupplierTailGoods.json) (POST /open-api/mes/order-inventory-surplus/update)：Update supplier tail goods（更新供应商尾货）
