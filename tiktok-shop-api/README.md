---
title: TikTok Shop ERP API Models
description: "TikTok Shop Partner Center API models relevant to Enterprise Resource Planning (ERP) apps."
---

# TikTok Shop ERP API Models

This catalog contains 193 operation-level Swagger 2.0 JSON files in 12 business modules. Start with a module below, then select an operation from its API List. Each operation JSON includes the official documentation URL in `x-tiktok-source.officialPage`.

The catalog is organized around the TikTok Shop **Enterprise Resource Planning (ERP)** app category. Actual access also depends on the app's approved scopes, registration country, target market, seller type, and shop authorization. Check [Manage API / API Scopes](https://partner.tiktokshop.com/) for the app before calling an endpoint. An operation's presence here does not guarantee access for every shop or market; for example, FBT and some promotion APIs have additional availability requirements.

See TikTok Shop's [App Category Selection Guide](https://partner.tiktokshop.com/docv2/page/hulvi36o) and [ERP integration guide](https://partner.tiktokshop.com/docv2/page/enterprise-resource-planning-erp) for category guidance.

## Shop connection and access

- [TikTok Shop Authorization API](./authorization/README.md) — Authorized seller shops. (1 operation)
- [TikTok Shop Event API](./event/README.md) — Shop webhook configuration and lifecycle. (3 operations)
- [TikTok Shop Seller API](./seller/README.md) — Seller shops, permissions, and shop groups. (3 operations)

## Core shop operations

- [TikTok Shop Finance API](./finance/README.md) — Statements, withdrawals, payments, and transactions. (6 operations)
- [TikTok Shop Fulfilled by TikTok API](./fulfilled-by-tiktok-fbt/README.md) — FBT inventory, inbound, and fulfillment. (23 operations)
- [TikTok Shop Fulfillment API](./fulfillment/README.md) — Packages, shipping, delivery, customs, invoices, and tracking. (28 operations)
- [TikTok Shop Logistics API](./logistics/README.md) — Warehouses, shipping providers, delivery options, templates, and tracking. (7 operations)
- [TikTok Shop Orders API](./orders/README.md) — Order lists, details, prices, and external references. (8 operations)
- [TikTok Shop Products API](./products/README.md) — Categories, attributes, brands, listings, inventory, global products, and product quality. (63 operations)
- [TikTok Shop Return and Refund API](./return-and-refund/README.md) — Returns, cancellations, refunds, reviews, and aftersales. (18 operations)

## Shop analytics and promotions

- [TikTok Shop Analytics API](./analytics/README.md) — Shop, product, SKU, video, LIVE, and bestselling analytics. (23 operations)
- [TikTok Shop Promotion API](./promotion/README.md) — Promotion activities, coupons, and discounts. (10 operations)
