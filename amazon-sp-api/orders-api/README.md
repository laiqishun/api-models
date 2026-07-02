---
title: The Selling Partner API for Orders
description: "The Selling Partner API for Orders returns orders information. This API supports the following types of orders: - FBM (Fulfilled by Merchant) - FBA (Fulfilled by Amazon) - read only - Amazon Fresh This API does not display order data that is more than two years old, except in the JP, AU, and SG marketplaces, for which data from 2016 and after is available."
---

# API List
- [searchOrders](operations/searchOrders.json) (GET /orders/2026-01-01/orders)：Returns orders created or updated during the time period that you specify. You can filter the response for specific types of orders.
- [getOrder](operations/getOrder.json) (GET /orders/2026-01-01/orders/{orderId})：Returns the order that you specify.
