---
title: "Lazada Order API"
description: "Order Information"
---

# API List

- [GetDocument](operations/get-document.json) (GET /order/document/get) — Use this API to retrieve order-related documents, including invoices and shipping labels.
- [GetMultipleOrderItems](operations/get-multiple-order-items.json) (GET /orders/items/get) — Use this API to get the item information of one or more orders.（No more than 50 at a time）
- [GetOrder](operations/get-order.json) (GET /order/get) — Use this API to get the list of items for a single order.
- [GetOrderItems](operations/get-order-items.json) (GET /order/items/get) — Use this API to get the item information of an order.
- [GetOrders](operations/get-orders.json) (GET /orders/get) — Use this API to get the list of items for a range of orders1..
- [GetOVOOrders](operations/get-ovo-orders.json) (GET/POST /orders/ovo/get) — This interface is only applicable to the merchant side of the business and is used to set the maximum number of SKUs that certain merchants can sell per day
- [OrderCancelValidate](operations/order-cancel-validate.json) (GET /order/reverse/cancel/validate) — Seller can check whether the order can be canceled through this API and get corresponding reasons if not.
- [SetInvoiceNumber](operations/set-invoice-number.json) (POST /order/invoice_number/set) — Use this API to set the invoice number for the specified order.

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
