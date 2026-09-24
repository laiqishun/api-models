---
title: "Lazada Product Review API"
description: "For product review record and reply API"
---

# API List

- [GetHistoryReviewIdList](operations/get-history-review-id-list.json) (GET/POST /review/seller/history/list) — Get history review id list for one seller(reviews within 3 months can be get)
- [GetReviewListByIdList](operations/get-review-list-by-id-list.json) (GET /review/seller/list/v2) — get review list by id list, need get id list first
- [SubmitSellerReply](operations/submit-seller-reply.json) (GET /review/seller/reply/add) — submit seller reply for customers review

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
