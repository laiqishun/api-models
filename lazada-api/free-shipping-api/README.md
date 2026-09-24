---
title: "Lazada Free Shipping API"
description: "for Free Shipping API"
---

# API List

- [FreeShippingActivate](operations/free-shipping-activate.json) (POST /promotion/freeshipping/activate) — activate free shipping promotion
- [FreeShippingAddSelectedProductSKU](operations/free-shipping-add-selected-product-sku.json) (POST /promotion/freeshipping/product/sku/add) — add sku for free shipping promotion
- [FreeShippingCreate](operations/free-shipping-create.json) (POST /promotion/freeshipping/create) — create a new free shipping promotion
- [FreeShippingDeactivate](operations/free-shipping-deactivate.json) (POST /promotion/freeshipping/deactivate) — deactivate free shipping promotion
- [FreeShippingDeleteSelectedProductSKU](operations/free-shipping-delete-selected-product-sku.json) (POST /promotion/freeshipping/product/sku/remove) — delete sku for free shipping promotion
- [FreeShippingDeliveryOptionsQuery](operations/free-shipping-delivery-options-query.json) (GET /promotion/freeshipping/deliveryoptions/get) — query free shipping promotion delivery options
- [FreeShippingGet](operations/free-shipping-get.json) (GET /promotion/freeshipping/get) — get free shipping promotion
- [FreeShippingList](operations/free-shipping-list.json) (GET /promotion/freeshippings/get) — query free shipping promotion list
- [FreeShippingRegionsQuery](operations/free-shipping-regions-query.json) (GET /promotion/freeshipping/regions/get) — query free shipping promotion regions
- [FreeShippingSelectedProductList](operations/free-shipping-selected-product-list.json) (GET /promotion/freeshipping/products/get) — query free shipping promotion selected product list
- [FreeShippingUpdate](operations/free-shipping-update.json) (POST /promotion/freeshipping/update) — update free shipping promotion

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
