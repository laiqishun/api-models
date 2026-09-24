---
title: "Lazada Cross Boarder Product API"
description: "API group for crossborder APIs (Cross Boarder Sellers Only)"
---

# API List

- [CreateGlobalProduct](operations/create-global-product.json) (POST /product/global/create) — Use this API to create a single new global product to multiple Lazada sites. (For cross boarder sellers ONLY)
- [deleteMerchantProduct](operations/delete-merchant-product.json) (POST /product/global/delete) — Use this API to delete the product。(CrossBoarderSellersOnly)
- [GetGlobalProductExtension](operations/get-global-product-extension.json) (GET /product/global/extension) — Use this API to query the extension info of the specified global product. (CrossBoarderSellersOnly)
- [GetGlobalProductStatus](operations/get-global-product-status.json) (GET /product/global/status/get) — Use this API to query the status of the specified global product. It takes several minutes for the global product to be created on each site. (CrossBoarderSellersOnly)
- [GetRecommendPrice](operations/get-recommend-price.json) (GET/POST /product/global/semi/recommend/price/get) — get recommend price
- [GetUnfilledAttribute](operations/get-unfilled-attribute.json) (GET /product/global/unfilled/attribute/get) — get the product which have attribute not filled （for cross boarder sellers Only）
- [GetUpgradableGlobalPlusProductList](operations/get-upgradable-global-plus-product-list.json) (GET/POST /product/global/semi/avaible/get) — get an upgradeable global plus product list
- [SemiProductUpdate](operations/semi-product-update.json) (POST /product/global/semi/update) — SemiProductUpdate
- [SemiProductUpgrade](operations/semi-product-upgrade.json) (GET/POST /product/global/semi/upgrade) — SemiProductUpgrade
- [UpdateGlobalProductAttribute](operations/update-global-product-attribute.json) (POST /product/global/attribute/update) — update global product attribute (For cross boarder sellers only)
- [updateProductStatus](operations/update-product-status.json) (POST /product/global/update/status) — product up shelf or down shelf，(CrossBoarderSellersOnly)

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
