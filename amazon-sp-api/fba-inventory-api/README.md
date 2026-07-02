---
title: Selling Partner API for FBA Inventory
description: "The Selling Partner API for FBA Inventory lets you programmatically retrieve information about inventory in Amazon's fulfillment network."
---

# API List
- [getInventorySummaries](operations/getInventorySummaries.json) (GET /fba/inventory/v1/summaries)：Returns a list of inventory summaries. The summaries returned depend on the presence or absence of the startDateTime, sellerSkus and sellerSku parameters:
- [createInventoryItem](operations/createInventoryItem.json) (POST /fba/inventory/v1/items)：Requests that Amazon create product-details in the Sandbox Inventory in the sandbox environment. This is a sandbox-only operation and must be directed to a sandbox endpoint. Refer to [Selling Partner API sandbox](https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox) for more information.
- [deleteInventoryItem](operations/deleteInventoryItem.json) (DELETE /fba/inventory/v1/items/{sellerSku})：Requests that Amazon Deletes an item from the Sandbox Inventory in the sandbox environment. This is a sandbox-only operation and must be directed to a sandbox endpoint. Refer to [Selling Partner API sandbox](https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox) for more information.
- [addInventory](operations/addInventory.json) (POST /fba/inventory/v1/items/inventory)：Requests that Amazon add items to the Sandbox Inventory with desired amount of quantity in the sandbox environment. This is a sandbox-only operation and must be directed to a sandbox endpoint. Refer to [Selling Partner API sandbox](https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox) for more information.
