---
title: Selling Partner API for Supply Sources
description: "Manage configurations and capabilities of seller supply sources."
---

# API List
- [getSupplySources](operations/getSupplySources.json) (GET /supplySources/2020-07-01/supplySources)：The path to retrieve paginated supply sources.
- [createSupplySource](operations/createSupplySource.json) (POST /supplySources/2020-07-01/supplySources)：Create a new supply source.
- [getSupplySource](operations/getSupplySource.json) (GET /supplySources/2020-07-01/supplySources/{supplySourceId})：Retrieve a supply source.
- [updateSupplySource](operations/updateSupplySource.json) (PUT /supplySources/2020-07-01/supplySources/{supplySourceId})：Update the configuration and capabilities of a supply source.
- [archiveSupplySource](operations/archiveSupplySource.json) (DELETE /supplySources/2020-07-01/supplySources/{supplySourceId})：Archive a supply source, making it inactive. Cannot be undone.
- [updateSupplySourceStatus](operations/updateSupplySourceStatus.json) (PUT /supplySources/2020-07-01/supplySources/{supplySourceId}/status)：Update the status of a supply source.
