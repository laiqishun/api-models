---
title: "Lazada Choice Customized API"
description: "Choice Customized API"
---

# API List

- [BatchDeliverJitPurchaseOrder](operations/batch-deliver-jit-purchase-order.json) (GET/POST /jit/purchase_order/batch_pickup_deliver) — Batch Pickup Deliver Jit Purchase Order.
- [EditChoiceSkuStock](operations/edit-choice-sku-stock.json) (POST /choice/stock/edit) — batch update choice jit product stock by skuId
- [GetChoiceProductItem](operations/get-choice-product-item.json) (GET /choice/product/item/get) — Get single product by ItemId or SellerSku.
- [GetChoiceProducts](operations/get-choice-products.json) (GET/POST /choice/products/get) — Use this API to get detailed information of the specified products.
- [GetChoiceSeller](operations/get-choice-seller.json) (GET/POST /choice/seller/get) — Get choice seller information by seller ID and site
- [GetChoiceSkuItemRelationBySku](operations/get-choice-sku-item-relation-by-sku.json) (GET/POST /choice/sku_item_relation/get_by_sku) — get the relation between platformSku and item by sku
- [PackageJitPurchaseOrder](operations/package-jit-purchase-order.json) (POST /jit/purchase_order/package) — Package Jit Purchase Order.
- [PrintJitPurchaseOrderAndItem](operations/print-jit-purchase-order-and-item.json) (GET/POST /jit/purchase_order/print) — Print Jit Purchase Order And Item.
- [PrintPickuoOrder](operations/print-pickuo-order.json) (GET/POST /pickup_order/print) — Print Pickuo Order.
- [QueryListJitPurchaseOrder](operations/query-list-jit-purchase-order.json) (GET/POST /jit/purchase_order/query_list) — Query List Jit Purchase Order.
- [QueryListPurchaseItem](operations/query-list-purchase-item.json) (GET/POST /jit/purchase_order/query_list_purchase_item) — Query List Purchase Item.
- [QueryPickupOrder](operations/query-pickup-order.json) (GET/POST /pickup_order/query) — Query Pickup Order.

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
