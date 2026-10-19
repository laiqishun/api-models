---
title: "SHEIN 库存和销量 API"
description: "SHEIN official category 1000003, with one JSON model per named operation."
---

# API List

Official category: [库存和销量 (1000003)](https://open.sheincorp.com/documents/apidoc/1000003). 6 records. Official IDs, applicable modes, and update times remain in the [manifest](../manifest.md) and each JSON file.

- [inventoryUpdateForSheinOwnedAndAgencyOperationMode](operations/inventoryUpdateForSheinOwnedAndAgencyOperationMode.json) (POST /open-api/goods/stock-update)：Inventory Update for “SHEIN-Owned” and “Agency Operation” mode（全托管/SHEIN自营商家库存更新）
- [merchantInventoryQuery](operations/merchantInventoryQuery.json) (POST /open-api/stock/stock-query)：Merchant inventory query API（商家库存查询接口）
- [merchantWarehouseListQuery](operations/merchantWarehouseListQuery.json) (GET /open-api/msc/warehouse/list)：Merchant warehouse list query（商家仓库列表查询）
- [searchSalesBySku](operations/searchSalesBySku.json) (POST /open-api/goods/query-sku-sales)：Search sales by SKU（根据SKU查询销量）
- [updateMerchantInventoryV1](operations/updateMerchantInventoryV1.json) (POST /open-api/gsp/goods/change-inventory)：Update merchant inventory API v1（更新商家库存接口v1）
- [updateMerchantInventoryV2](operations/updateMerchantInventoryV2.json) (POST /open-api/stock/change-inventory/v2)：Update merchant inventory API v2（更新商家库存接口v2）
