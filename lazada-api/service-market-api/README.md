---
title: "Lazada Service Market API"
description: "Lazada Service Market API"
---

# API List

- [ServiceMarketAppKeyOrderQuery](operations/service-market-app-key-order-query.json) (GET/POST /service/market/order/query) — Query user order list for specific App on Service Market
- [ServiceMarketAppKeySubQuery](operations/service-market-app-key-sub-query.json) (GET/POST /service/market/subs/query) — Query user subscription info for specific App on Service Market

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
