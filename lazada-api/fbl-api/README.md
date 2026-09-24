---
title: "Lazada FBL API"
description: "FBL API group"
---

# API List

- [BuildFulfillmentSkuRelation](operations/build-fulfillment-sku-relation.json) (POST /fbl/fulfillment_sku_relation/write) — build the relation between platformSku and fulfillmentSku
- [CancelFulfillmentOrderForMCL](operations/cancel-fulfillment-order-for-mcl.json) (POST /fbl/fulfillment_order/cancel) — Cancel Fulfillment Order
- [CancelInboundReservation](operations/cancel-inbound-reservation.json) (POST /fbl/inbound_reservation/cancel) — cancel reservation order
- [CancelnBoundOrder](operations/canceln-bound-order.json) (POST /fbl/inbound_order/cancel) — Cancel inbound order
- [CancelOutboundOrder](operations/cancel-outbound-order.json) (POST /fbl/outbound_order/cancel) — Cancel outbound order
- [CancelVasOrder4FBL](operations/cancel-vas-order4-fbl.json) (GET/POST /fbl/vas/cancelVasOrder) — 取消增值服务
- [CheckInboundReservationSlot](operations/check-inbound-reservation-slot.json) (GET /fbl/inbound_reservation/check) — Check Available Reservation Slots for Inbound Order
- [CreateFulfillmentOrderForMCL](operations/create-fulfillment-order-for-mcl.json) (POST /fbl/fulfillment_order/create) — Create Fulfillment Order
- [CreateFulfillmentOrderForMCLV2PNF](operations/create-fulfillment-order-for-mclv2-pnf.json) (POST /fbl/fulfillment_order_pnf/create) — Create Fulfillment Order for MCL2.0 PNF
- [CreateFulfillmentSkuDecouple](operations/create-fulfillment-sku-decouple.json) (POST /fbl/fulfillment_sku/create) — create fulfillment sku without product
- [CreateFulfillmentSkuForFBL](operations/create-fulfillment-sku-for-fbl.json) (POST /fbl/fulfillment_sku_fbl/create) — create fulfillment sku for specified platform product
- [CreateInboundOrder](operations/create-inbound-order.json) (POST /fbl/inbound_order/create) — Create inbound order
- [CreateInboundReservation](operations/create-inbound-reservation.json) (POST /fbl/inbound_reservation/create) — create reservation order
- [CreateOutBoundOrder](operations/create-out-bound-order.json) (POST /fbl/outbound_order/create) — Create outbound order
- [CreateProductReinboundOrderForMCL](operations/create-product-reinbound-order-for-mcl.json) (POST /fbl/product_reinbound/create) — Create Product Reinbound Order on Failed Delivery for MCL
- [CreateVasOrder4FBL](operations/create-vas-order4-fbl.json) (GET/POST /fbl/vas/createVasOrder) — FBL增值服务创建
- [GetChannelStocksForMCL](operations/get-channel-stocks-for-mcl.json) (GET /fbl/channel_stocks/get) — Query Channel Stocks
- [GetFulfillmentProductDetail](operations/get-fulfillment-product-detail.json) (GET /fbl/fulfillment_products/get) — GET  fulfillment product Detail；Call Get Platform Products for fulfillment_sku first
- [GetFulfillmentSkuListForMCL](operations/get-fulfillment-sku-list-for-mcl.json) (GET /fbl/fulfillment_sku_list/get) — Get Fulfillment SKU List for LAZADA Partner
- [GetFulfillmentSkuRelationByScItem](operations/get-fulfillment-sku-relation-by-sc-item.json) (GET/POST /fbl/fulfillment_sku_relation/get_by_sc_item) — get the relation between platformSku and fulfillmentSku by scItem
- [GetFulfillmentSkuRelationBySku](operations/get-fulfillment-sku-relation-by-sku.json) (GET/POST /fbl/fulfillment_sku_relation/get_by_sku) — get the relation between platformSku and fulfillmentSku by sku
- [GetFulfillmentSkuRelationsByScItems](operations/get-fulfillment-sku-relations-by-sc-items.json) (GET/POST /fbl/fulfillment_sku_relation/get_by_sc_items) — get fulfillmentSku Relations By ScItems
- [GetFulfillmentSkuRelationsBySkus](operations/get-fulfillment-sku-relations-by-skus.json) (GET/POST /fbl/fulfillment_sku_relation/get_by_skus) — get fulfillmentSku Relations By Skus
- [GetIcpOrderFile](operations/get-icp-order-file.json) (GET /fbl/icp_order/file) — Get Inbound/Outbound order print PDF file
- [GetInboundOrderDetail](operations/get-inbound-order-detail.json) (GET /fbl/inbound_order_detail/get) — Use this API to get the Inbound Order Detail
- [GetInboundOrderList](operations/get-inbound-order-list.json) (GET /fbl/inbound_orders/get) — Use this API to get inbound order list
- [GetInboundReservationFile](operations/get-inbound-reservation-file.json) (GET /fbl/inbound_reservation/file) — get inbound reservation order file
- [GetInventoryChangedSKU](operations/get-inventory-changed-sku.json) (GET /fbl/inventory_changed_sku/get) — Use this API to get SKU list
- [GetInventoryOccupyDetails](operations/get-inventory-occupy-details.json) (GET /fbl/inventory_occupy_details/get) — Use this API to get a sku's inventory occupy details
- [GetInventoryOperateLog](operations/get-inventory-operate-log.json) (GET /fbl/inventory_operate_log/get) — Use this API to get a sku's inventory operate log
- [GetOutboundOrderDetail](operations/get-outbound-order-detail.json) (GET /fbl/outbound_order_detail/get) — Use this API to Get outbound order detail; shoud call GetOutboundOrderList for outbound_order_no first
- [GetOutboundOrderList](operations/get-outbound-order-list.json) (GET /fbl/outbound_orders/get) — Use this API to get outbound order list
- [GetPlatformProductsV2](operations/get-platform-products-v2.json) (GET /fbl/platform_products/get2) — Search products list
- [GetProductBatchList](operations/get-product-batch-list.json) (GET/POST /fbl/product_batch/query) — query product batch list
- [GetShipperInfo](operations/get-shipper-info.json) (GET /fbl/shipper/get) — Get Shipper Info for LAZADA Partner
- [GetStockRule](operations/get-stock-rule.json) (GET /fbl/stock_rule/get) — Get SKU stock rule by sku and warehouse
- [GetVasOrderByNo4FBL](operations/get-vas-order-by-no4-fbl.json) (GET/POST /fbl/vas/getVasOrderByNo) — get vasOrder by orderNo
- [GetWarehouseListForMCL](operations/get-warehouse-list-for-mcl.json) (GET /fbl/warehouses/get) — Get Warehouse List By Country And Multi-Channel
- [GetWarehouseStock](operations/get-warehouse-stock.json) (GET /fbl/stocks/get) — Get SKU list and stock by warehouse code
- [GetWarehouseStockV3](operations/get-warehouse-stock-v3.json) (GET /fbl/stocks/getV3) — Get SKU list and stock by warehouse code, this version separates pending inbound and stock in transit in return json.
- [ListIcpWarehouse](operations/list-icp-warehouse.json) (GET /fbl/icp_warehouse/list) — List warehouses for create InboundOrder and outboundOrder
- [QueryFulfillmentOrderForMCL](operations/query-fulfillment-order-for-mcl.json) (GET /fbl/fulfillment_order_list/get) — Query list of Fulfillment Orders by shipper
- [QueryInboundBatch](operations/query-inbound-batch.json) (GET/POST /fbl/inbound_batch/query) — query inbound batch
- [QueryInboundReservationOrder](operations/query-inbound-reservation-order.json) (GET /fbl/inbound_reservation/get) — get inbound reservation order
- [QueryReverseOrderForMCL](operations/query-reverse-order-for-mcl.json) (GET /fbl/reverse_order/get) — Query Reverse Order for MCL
- [RemoveFulfillmentSkuRelation](operations/remove-fulfillment-sku-relation.json) (POST /fbl/fulfillment_sku_relation/remove) — remove the relation between platformSku and fulfillmentSku
- [ReturnCancellation](operations/return-cancellation.json) (POST /fbl/returns/cancel) — Return order cancellation
- [ReturnOrderCreation](operations/return-order-creation.json) (POST /fbl/returns/create) — Api to create customer returns
- [SetStockRule](operations/set-stock-rule.json) (POST /fbl/stock_rule/set) — set channel ratio by sku and warehouse
- [UpdateFulfillmentSkuDecouple](operations/update-fulfillment-sku-decouple.json) (POST /fbl/fulfillment_sku/update) — update fulfillment sku without product
- [UploadWaybill](operations/upload-waybill.json) (GET/POST /fbl/waybill/upload) — Use this API to upload a waybill pdf to Lazada site. The maximum size of an pdf file is 1MB.

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
