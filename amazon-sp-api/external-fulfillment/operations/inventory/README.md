---
title: The Selling Partner API for External Fulfillment Inventory Management
description: "You can use the Amazon External Fulfillment Inventory API to manage inventory operations in Amazon's External Fulfillment network, including batch inventory updates and retrievals."
---

# API List
- [batchInventory](batchInventory.json) (POST /externalFulfillment/inventory/2024-09-11/inventories)：Make up to 10 inventory requests. The response includes the set of responses that correspond to requests. The response for each successful request in the set includes the inventory count for the provided `sku` and `locationId` pair.
