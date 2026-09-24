---
title: "Lazada System API"
description: "System API"
---

# API List

- [GenerateAccessToken](operations/generate-access-token.json) (GET/POST /auth/token/create) — generate access_token for call api
- [GenerateAccessTokenWithOpenId](operations/generate-access-token-with-open-id.json) (GET/POST /auth/token/createWithOpenId) — generate access_token with openId for call api
- [RefreshAccessToken](operations/refresh-access-token.json) (GET/POST /auth/token/refresh) — refresh access_token, the endpoint is https://auth.lazada.com/rest
- [startExportByDataset](operations/start-export-by-dataset.json) (GET/POST /fbi/download/startExportByDataset) — Open the download operation

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
