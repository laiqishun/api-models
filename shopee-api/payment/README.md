---
title: Shopee Payment API
description: "Escrow, payout, wallet, installment, billing, income, and payment method operations."
---

# API List

- [v2.payment.generate_income_report](operations/v2-payment-generate-income-report.json) (GET /api/v2/payment/generate_income_report)：Trigger income report generation.
- [v2.payment.generate_income_statement](operations/v2-payment-generate-income-statement.json) (GET /api/v2/payment/generate_income_statement)：Trigger income statement generation.
- [v2.payment.get_billing_transaction_info](operations/v2-payment-get-billing-transaction-info.json) (POST /api/v2/payment/get_billing_transaction_info)：This API is applicable for Cross Border (CB) sellers only to get the detailed payout transaction data, both released and to-be released transaction can be found in here
- [v2.payment.get_escrow_detail_batch](operations/v2-payment-get-escrow-detail-batch.json) (GET /api/v2/payment/get_escrow_detail_batch)：Use this API to fetch the details of order income by batch.
- [v2.payment.get_escrow_detail](operations/v2-payment-get-escrow-detail.json) (GET /api/v2/payment/get_escrow_detail)：Use this API to fetch the accounting detail of order.
- [v2.payment.get_escrow_list](operations/v2-payment-get-escrow-list.json) (GET /api/v2/payment/get_escrow_list)：Use this API to fetch the accounting list of order.
- [v2.payment.get_income_detail](operations/v2-payment-get-income-detail.json) (GET /api/v2/payment/get_income_detail)：Retrieves detailed order-level income information across various income statuses for a specified time period. This API enables partners to display granular transaction-level income data consistent with Seller Center’s “Income Details” view, segmented by income status and payout stage. The API dynamically adapts data fields based on the seller’s shop type (Local or Cross Border) and the selected income status (e.g., Pending, To Release, Released).
- [v2.payment.get_income_overview](operations/v2-payment-get-income-overview.json) (GET /api/v2/payment/get_income_overview)：Retrieves a consolidated snapshot of the seller’s income amounts categorized by income status for a specified shop. This API provides a holistic overview similar to Seller Center’s “Income Overview” section, allowing external systems to reflect the same current payout view. Data is dynamically determined based on the shop type (Local or Cross Border) and the income status requested. Historical income results are not retrievable, providing consistent information as Seller Centre.
- [v2.payment.get_income_report](operations/v2-payment-get-income-report.json) (GET /api/v2/payment/get_income_report)：To query income report status and provide file link if the income report is ready to be downloaded.
- [v2.payment.get_income_statement](operations/v2-payment-get-income-statement.json) (GET /api/v2/payment/get_income_statement)：To query income statement status and provide file link if the income statement is ready to be downloaded.
- [v2.payment.get_item_installment_status](operations/v2-payment-get-item-installment-status.json) (POST /api/v2/payment/get_item_installment_status)：Get item installment tenures.Only for TH、TW.
- [v2.payment.get_payment_method_list](operations/v2-payment-get-payment-method-list.json) (GET /api/v2/payment/get_payment_method_list)：Obtain payment method (no authentication required)
- [v2.payment.get_payout_detail](operations/v2-payment-get-payout-detail.json) (GET /api/v2/payment/get_payout_detail)：This API is applicable for Cross Border (CB) sellers only to get the shop's payout data, such as the payout amount, currency, FX rate, the payout's associated order income and adjustment records etc.
- [v2.payment.get_payout_info](operations/v2-payment-get-payout-info.json) (GET /api/v2/payment/get_payout_info)：This is a new API which applicable for Cross Border (CB) sellers only to get the shop's payout data, will be used for the original API v2.get_payout_details replacement, we provide data such as the payout amount, currency, FX rate, the payout's associated order income and adjustment records etc.
- [v2.payment.get_shop_installment_status](operations/v2-payment-get-shop-installment-status.json) (GET /api/v2/payment/get_shop_installment_status)：Get the installment state of shop.
- [v2.payment.get_wallet_transaction_list](operations/v2-payment-get-wallet-transaction-list.json) (GET /api/v2/payment/get_wallet_transaction_list)：Use this API to get the transaction records of wallet. Only applicable for local shops
- [v2.payment.set_item_installment_status](operations/v2-payment-set-item-installment-status.json) (POST /api/v2/payment/set_item_installment_status)：Set item installment.Only for TH、TW.
- [v2.payment.set_shop_installment_status](operations/v2-payment-set-shop-installment-status.json) (POST /api/v2/payment/set_shop_installment_status)：Sets the staging capability of shop level.
