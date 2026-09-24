---
title: "Lazada Return and Refund API"
description: "The APIs to manage return orders"
---

# API List

- [GetReverseOrderDetail](operations/get-reverse-order-detail.json) (GET /order/reverse/return/detail/list) — Get the detailed information for a specific reverse order
- [GetReverseOrderHistoryList](operations/get-reverse-order-history-list.json) (GET /order/reverse/return/history/list) — Get the communication history of the reverse order
- [GetReverseOrderReasonList](operations/get-reverse-order-reason-list.json) (GET /order/reverse/reason/list) — Get the list of reject reason. Need to be used in all refuse refund actions
- [GetReverseOrdersForSeller](operations/get-reverse-orders-for-seller.json) (GET/POST /reverse/getreverseordersforseller) — Use this API to get the list of items for a range of reverse orders.
- [InitReverseOrderCancel](operations/init-reverse-order-cancel.json) (GET /order/reverse/cancel/create) — Seller initiates a cancelation
- [InitReverseOrderCancelDecide](operations/init-reverse-order-cancel-decide.json) (GET /order/reverse/cancel/seller/decide) — Seller initiates a cancelation
- [ReverseOrderOnlyRefundDecide](operations/reverse-order-only-refund-decide.json) (GET /order/reverse/onlyrefund/seller/decide) — Seller can use this API to operate only refund requests
- [ReverseOrderReturnUpdate](operations/reverse-order-return-update.json) (GET /order/reverse/return/update) — Seller can use this API to action on return and refund related.

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
