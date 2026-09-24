---
title: "Lazada Store Flash Sale API"
description: "店铺闪购API"
---

# API List

- [ActivateStoreFlashSale](operations/activate-store-flash-sale.json) (POST /promotion/storeflashsale/activate) — activate Store Flash Sale
- [CreateStoreFlashSale](operations/create-store-flash-sale.json) (POST /promotion/storeflashsale/create) — create a new Store Flash Sale
- [DeactivateStoreFlashSale](operations/deactivate-store-flash-sale.json) (POST /promotion/storeflashsale/deactivate) — deactivate Store Flash Sale
- [getStoreFlashSale](operations/get-store-flash-sale.json) (GET /promotion/storeflashsale/get) — getStoreFlashSale
- [ListStoreFlashSale](operations/list-store-flash-sale.json) (GET /promotion/storeflashsale/list) — list Store Flash Sale
- [UpdateStoreFlashSale](operations/update-store-flash-sale.json) (POST /promotion/storeflashsale/update) — update storeflashsale

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
