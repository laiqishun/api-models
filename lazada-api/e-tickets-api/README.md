---
title: "Lazada E-Tickets API"
description: "E-Tickets API for digital voucher and e-ticketing service"
---

# API List

- [GetOrderItemsFromBarCode](operations/get-order-items-from-bar-code.json) (GET/POST /eticket/code/query) — E-Ticcket certificate query Open API
- [GlobalEticketMerchantMaAvailable](operations/global-eticket-merchant-ma-available.json) (GET/POST /eticket/ma/available) — the callback interface before consume  code
- [GlobalEticketMerchantMaConsume](operations/global-eticket-merchant-ma-consume.json) (POST /eticket/ma/consume) — consume ma
- [GlobalEticketMerchantMaFailsend](operations/global-eticket-merchant-ma-failsend.json) (POST /eticket/ma/failsend) — the callback interface when send code failed
- [GlobalEticketMerchantMaQuery](operations/global-eticket-merchant-ma-query.json) (GET/POST /eticket/ma/query) — the callback interface that query lazada platform ma
- [GlobalEticketMerchantMaQueryTbMa](operations/global-eticket-merchant-ma-query-tb-ma.json) (GET/POST /eticket/ma/queryTbMa) — the callback interface that query tb ma
- [GlobalEticketMerchantMaSend](operations/global-eticket-merchant-ma-send.json) (GET/POST /eticket/ma/send) — the callback interface when merchant send code successful
- [RedeemOrderItems](operations/redeem-order-items.json) (GET/POST /eticket/code/consume) — Certificate Consume Open API

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
