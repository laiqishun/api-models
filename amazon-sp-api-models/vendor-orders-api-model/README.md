---
title: Selling Partner API for Retail Procurement Orders
description: "The Selling Partner API for Retail Procurement Orders provides programmatic access to vendor orders data."
---

# API List
- [getPurchaseOrders](operations/getPurchaseOrders.json) (GET /vendor/orders/v1/purchaseOrders)：Returns a list of purchase orders created or changed during the time frame that you specify. You define the time frame using the `createdAfter`, `createdBefore`, `changedAfter` and `changedBefore` parameters. The date range to search must not be more than 7 days. You can choose to get only the purchase order numbers by setting `includeDetails` to false. You can then use the `getPurchaseOrder` operation to receive details for a specific purchase order.
- [getPurchaseOrder](operations/getPurchaseOrder.json) (GET /vendor/orders/v1/purchaseOrders/{purchaseOrderNumber})：Returns a purchase order based on the `purchaseOrderNumber` value that you specify.
- [submitAcknowledgement](operations/submitAcknowledgement.json) (POST /vendor/orders/v1/acknowledgements)：Submits acknowledgements for one or more purchase orders.
- [getPurchaseOrdersStatus](operations/getPurchaseOrdersStatus.json) (GET /vendor/orders/v1/purchaseOrdersStatus)：Returns purchase order statuses based on the filters that you specify. Date range to search must not be more than 7 days. You can return a list of purchase order statuses using the available filters, or a single purchase order status by providing the purchase order number.
