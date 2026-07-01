---
title: Selling Partner API for Vendor Direct Fulfillment Sandbox Test Data
description: "The Selling Partner API for Vendor Direct Fulfillment Sandbox Test Data provides programmatic access to vendor direct fulfillment sandbox test data."
---

# API List
- [generateOrderScenarios](operations/generateOrderScenarios.json) (POST /vendor/directFulfillment/sandbox/2021-10-28/orders)：Submits a request to generate test order data for Vendor Direct Fulfillment API entities.
- [getOrderScenarios](operations/getOrderScenarios.json) (GET /vendor/directFulfillment/sandbox/2021-10-28/transactions/{transactionId})：Returns the status of the transaction indicated by the specified transactionId. If the transaction was successful, also returns the requested test order data.
