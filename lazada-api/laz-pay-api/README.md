---
title: "Lazada LazPay API"
description: "Payment information"
---

# API List

- [collectBenefit](operations/collect-benefit.json) (GET/POST /insurance/promotion/collectBenefit) — collect lazada marketplace benefit
- [ConsultPayment](operations/consult-payment.json) (GET/POST /lazadapay/v1/debit/consult_payment) — The interface is used for consult pay view. Will return pay view info including balance, coupon, credit card etc. If we have no available coupon, we will return pay method view with an empty list of coupon.
- [CreateSubscriptionToFusion](operations/create-subscription-to-fusion.json) (POST /insurance/subscription/create) — Create User Subscription To Fusion
- [DGUtiityPreCreateOrder](operations/dg-utiity-pre-create-order.json) (GET/POST /digital/service/createorder) — This API provides an open interface for partner users to create DG orders
- [DGUtilityPreGetPaymentStatus](operations/dg-utility-pre-get-payment-status.json) (GET/POST /digital/service/getPaymentStatus) — get payment status
- [DGUtilityPreUpdateFulfillemtStatus](operations/dg-utility-pre-update-fulfillemt-status.json) (GET/POST /digital/service/updateFulfillemtStatus) — update fulfillemt status
- [DigitalAlterOrderStatus](operations/digital-alter-order-status.json) (GET/POST /digital/order/alterStatus) — Change Lazada Digital Order Status
- [DigitalCreateOrder](operations/digital-create-order.json) (GET/POST /digital/order/create) — Create Digital Virtual Order
- [DigitalQueryOrder](operations/digital-query-order.json) (GET/POST /digital/order/getStatus) — Query Lazada Digital Order Status
- [GetSubscriptionToFusion](operations/get-subscription-to-fusion.json) (GET/POST /insurance/subscription/getSubscription) — Get User Subscription To Fusion
- [InsuranceAlterOrderStatus](operations/insurance-alter-order-status.json) (GET/POST /insurance/order/alterStatus) — Change Lazada Insurance Order Status
- [InsuranceCreateOrder](operations/insurance-create-order.json) (GET/POST /insurance/order/create) — Lazada Insurance Create Order
- [InsuranceGetPromotions](operations/insurance-get-promotions.json) (GET/POST /insurance/promotion/getPromotions) — get lazada marketplace  ump promotions
- [InsuranceQueryOrder](operations/insurance-query-order.json) (GET/POST /insurance/order/getStatus) — Query Lazada Insurance Order Status
- [insuranceRealTimeCDP](operations/insurance-real-time-cdp.json) (GET/POST /insurance/syncCDP) — 用户完成操作后，实时更新CDP人群
- [LazadaCFOInvoiceRpaCallback](operations/lazada-cfo-invoice-rpa-callback.json) (GET/POST /rpa/id/tax/callback) — Call RPA and return the official invoice
- [OpenServiceBalanceQuery](operations/open-service-balance-query.json) (GET/POST /wallet/open/service/balance/query) — Open Service Account Balance Info Query
- [OpenServiceKycQuery](operations/open-service-kyc-query.json) (GET/POST /wallet/open/service/kyc/query) — Open Service User KYC Info Query
- [OpenServiceWithdrawApply](operations/open-service-withdraw-apply.json) (GET/POST /wallet/open/service/withdraw) — Open Service Withdraw Apply
- [OpenServiceWithdrawQuery](operations/open-service-withdraw-query.json) (GET/POST /wallet/open/service/withdraw/query) — Open Service Withdraw Query
- [queryAddonOrder](operations/query-addon-order.json) (GET/POST /insurance/addon/orders/query) — list user  addon order detail
- [queryBenefit](operations/query-benefit.json) (GET/POST /insurance/promotion/queryBenefit) — get lazada marketplace benefit
- [Reconciliation](operations/reconciliation.json) (GET/POST /wallet/open/service/reconciliation) — Reconciliation
- [redeemMpVoucher](operations/redeem-mp-voucher.json) (GET/POST /insurance/voucher/redeemVoucher) — 商城险域外voucher核销

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
