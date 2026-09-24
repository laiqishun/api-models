---
title: "Lazada Lazada Wallet Corporate Top-up API"
description: "Lazada Wallet Corporate Top-up"
---

# API List

- [DirectTransferQuery](operations/direct-transfer-query.json) (GET/POST /wallet/transfer/query) — Direct Transfer - Query
- [DirectTransferRequest](operations/direct-transfer-request.json) (GET/POST /wallet/transfer/request) — Direct Transfer - Request to transfer
- [GiftCodeQuery](operations/gift-code-query.json) (GET/POST /wallet/giftcode/query) — Gift Code - Query
- [GiftCodeRequest](operations/gift-code-request.json) (GET/POST /wallet/giftcode/request) — Gift Code - Request
- [Reconciliation](operations/reconciliation.json) (GET/POST /wallet/open/reconciliation) — Corporate TopUp - Reconciliation

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
