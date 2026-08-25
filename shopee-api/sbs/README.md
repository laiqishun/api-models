---
title: Shopee SBS API
description: "SBS inventory, expiry, aging, movement, and warehouse mapping operations."
---

# API List

- [v2.sbs.get_bound_whs_info](operations/v2-sbs-get-bound-whs-info.json) (GET /api/v2/sbs/get_bound_whs_info)：get bound warehouse by shop id
- [v2.sbs.get_current_inventory](operations/v2-sbs-get-current-inventory.json) (GET /api/v2/sbs/get_current_inventory)：Get Seller Center Current Inventory Page Data
- [v2.sbs.get_expiry_report](operations/v2-sbs-get-expiry-report.json) (GET /api/v2/sbs/get_expiry_report)：Seller Center Expiry Report page data
- [v2.sbs.get_fulfillment_mapping_inventory_list](operations/v2-sbs-get-fulfillment-mapping-inventory-list.json) (GET /api/v2/sbs/get_fulfillment_mapping_inventory_list)：This API is designed for sellers using Fulfillment Mapping and their ERP systems. It allows callers to query the corresponding mapping and inventory information using the MTSKU ID of either a Bundle SKU or a Parent SKU, supporting automated inventory reconciliation and planning, improving Parent SKU inventory visibility, and reducing manual operations and cross-channel overselling risks.
- [v2.sbs.get_stock_aging](operations/v2-sbs-get-stock-aging.json) (GET /api/v2/sbs/get_stock_aging)：Get Seller Center Stock Aging page data
- [v2.sbs.get_stock_movement](operations/v2-sbs-get-stock-movement.json) (GET /api/v2/sbs/get_stock_movement)：Get Seller Center，Stock Movement page data
