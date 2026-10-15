# 库存和销量 (1000003)

Official API category: [SHEIN developer reference](https://open.sheincorp.com/documents/apidoc/1000003).

6 records in the 2026-10-15 18:50 CST public catalog snapshot. Mode labels are copied per operation from official details; actual application access requires subscription and approval.

| Method | Name | Path / event | Official ID | Modes | Updated | Model |
|---|---|---|---:|---|---|---|
| GET | 商家仓库列表查询 | `/open-api/msc/warehouse/list` | 3002013 | 自运营, 半托管 | 2026-08-31 11:37:28 | [JSON](./operations/3002013.json) |
| POST | 商家库存查询接口 | `/open-api/stock/stock-query` | 3001695 | 自运营, 全托管, SHEIN自营, 半托管, POP | 2026-04-27 20:38:29 | [JSON](./operations/3001695.json) |
| POST | 更新商家库存接口v1 | `/open-api/gsp/goods/change-inventory` | 3001692 | 自运营, 半托管 | 2026-04-27 20:19:47 | [JSON](./operations/3001692.json) |
| POST | 更新商家库存接口v2 | `/open-api/stock/change-inventory/v2` | 3001738 | 自运营, 半托管 | 2026-06-01 21:33:50 | [JSON](./operations/3001738.json) |
| POST | 全托管/SHEIN自营商家库存更新 | `/open-api/goods/stock-update` | 3001304 | 全托管, SHEIN自营, POP | 2025-07-21 11:32:54 | [JSON](./operations/3001304.json) |
| POST | 根据SKU查询销量 | `/open-api/goods/query-sku-sales` | 3001305 | 全托管, SHEIN自营, 半托管, POP | 2025-07-21 11:33:00 | [JSON](./operations/3001305.json) |
