---
title: "Lazada Finance API"
description: "Finance"
---

# API List

- [GetPayoutStatus](operations/get-payout-status.json) (GET /finance/payout/status/get) — Get your transaction statements  created after the provided date
- [QueryAccountTransactions](operations/query-account-transactions.json) (POST /finance/transaction/accountTransactions/query) — Query Account Transactions
- [QueryLogisticsFeeDetail](operations/query-logistics-fee-detail.json) (GET/POST /lbs/slb/queryLogisticsFeeDetail) — Api is provided for finance and seller to query logistics fee details from slb.
- [QueryTransactionDetails](operations/query-transaction-details.json) (GET /finance/transaction/details/get) — API to query seller transaction details within specific date range.

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
