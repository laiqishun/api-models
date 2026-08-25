---
title: Shopee FBS API
description: "Brazil FBS enrollment, invoice, shop block, and SKU block operations."
---

# API List

- [v2.fbs.query_br_shop_block_status](operations/v2-fbs-query-br-shop-block-status.json) (GET /api/v2/fbs/query_br_shop_block_status)：This API checks whether an FBS shop is blocked due to invoice-related issues. When blocked, the shop cannot create new Inbound Requests, and its warehouse inventory is restricted from being sold.
- [v2.fbs.query_br_shop_enrollment_status](operations/v2-fbs-query-br-shop-enrollment-status.json) (GET /api/v2/fbs/query_br_shop_enrollment_status)：This API checks whether a given shop_id is eligible to enroll in the Brazil Fulfilled-by-Shopee (FBS) service.
- [v2.fbs.query_br_shop_invoice_error](operations/v2-fbs-query-br-shop-invoice-error.json) (GET /api/v2/fbs/query_br_shop_invoice_error)：This API handles failed invoice issuance for FBS-related processes, covering Inbound Requests, RTS Requests, Sales Orders, and Move Transfer Orders.
- [v2.fbs.query_br_sku_block_status](operations/v2-fbs-query-br-sku-block-status.json) (GET /api/v2/fbs/query_br_sku_block_status)：This API checks whether an FBS product is blocked due to invoice-related issues. When blocked, the product cannot be included in new Inbound Requests, and its warehouse inventory is restricted from being sold.
