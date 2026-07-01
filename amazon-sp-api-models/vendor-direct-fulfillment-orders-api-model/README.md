---
title: Selling Partner API for Direct Fulfillment Orders
description: "The Selling Partner API for Direct Fulfillment Orders provides programmatic access to a direct fulfillment vendor's order data."
---

# API List
- [getOrders](operations/getOrders.json) (GET /vendor/directFulfillment/orders/2021-12-28/purchaseOrders)：Returns a list of purchase orders created during the time frame that you specify. You define the time frame using the createdAfter and createdBefore parameters. You must use both parameters. You can choose to get only the purchase order numbers by setting the includeDetails parameter to false. In that case, the operation returns a list of purchase order numbers. You can then call the getOrder operation to return the details of a specific order.
- [getOrder](operations/getOrder.json) (GET /vendor/directFulfillment/orders/2021-12-28/purchaseOrders/{purchaseOrderNumber})：Returns purchase order information for the purchaseOrderNumber that you specify.
- [submitAcknowledgement](operations/submitAcknowledgement.json) (POST /vendor/directFulfillment/orders/2021-12-28/acknowledgements)：Submits acknowledgements for one or more purchase orders.
