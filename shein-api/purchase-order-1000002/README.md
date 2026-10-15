# 采购单 (1000002)

Official API category: [SHEIN developer reference](https://open.sheincorp.com/documents/apidoc/1000002).

20 records in the 2026-10-15 18:50 CST public catalog snapshot. Mode labels are copied per operation from official details; actual application access requires subscription and approval.

| Method | Name | Path / event | Official ID | Modes | Updated | Model |
|---|---|---|---:|---|---|---|
| GET | 获取采购单信息 | `/open-api/order/purchase-order-infos` | 3002009 | 自运营, 全托管, SHEIN自营, 半托管, POP | 2026-08-28 17:44:45 | [JSON](./operations/3002009.json) |
| GET | JIT母单及子单对应关系查询接口 | `/open-api/order/get-mothe-child-orders` | 3001813 | 全托管, SHEIN自营, POP | 2026-06-15 10:04:14 | [JSON](./operations/3001813.json) |
| GET | 发货基本信息查询接口 | `/open-api/shipping/basic` | 3001981 | 自运营, 全托管, SHEIN自营, 半托管, POP | 2026-08-21 19:58:22 | [JSON](./operations/3001981.json) |
| POST | 创建发货单 | `/open-api/shipping/orderToShipping` | 3002010 | 自运营, 全托管, SHEIN自营, 半托管, POP | 2026-08-28 18:02:11 | [JSON](./operations/3002010.json) |
| POST | 修改和取消发货单订单 | `/open-api/shipping/modify-delivery-order-info` | 3002049 | 自运营, 全托管, SHEIN自营, 半托管, POP | 2026-10-13 15:11:45 | [JSON](./operations/3002049.json) |
| POST | 查询智能拆包结果接口 | `/open-api/purchase/intelligent-packing-result` | 3002042 | 全托管, SHEIN自营, POP | 2026-09-23 21:49:44 | [JSON](./operations/3002042.json) |
| GET | 查询发货单列表 | `/open-api/shipping/delivery` | 3002045 | 自运营, 全托管, SHEIN自营, 半托管, POP | 2026-09-24 14:26:06 | [JSON](./operations/3002045.json) |
| POST | 查询SHEIN合作物流产品 | `/open-api/shipping/express-company-list-v2` | 3001973 | 自运营, 全托管, SHEIN自营, 半托管, POP | 2026-08-19 22:25:40 | [JSON](./operations/3001973.json) |
| POST | 查询SHEIN合作物流预估运费 | `/open-api/openapi-business-backend/purchase-estimated-fee` | 3002011 | 全托管, SHEIN自营, POP | 2026-08-28 18:03:40 | [JSON](./operations/3002011.json) |
| GET | 收货仓信息查询 | `/open-api/shipping/warehouse` | 3001982 | 自运营, 全托管, SHEIN自营, 半托管, POP | 2026-08-21 20:02:11 | [JSON](./operations/3001982.json) |
| POST | 发货单维度打印面单 | `/open-api/shipping/delivery/print-package` | 3001293 | 自运营, 全托管, SHEIN自营, 半托管, POP | 2025-07-21 11:31:41 | [JSON](./operations/3001293.json) |
| POST | ​查询货代信息 | `/open-api/pfmp/shipping/thirdPartyAndChannelList` | 3002043 | 全托管, SHEIN自营, POP | 2026-09-23 21:55:03 | [JSON](./operations/3002043.json) |
| POST | 打印物流面单 | `/open-api/pfmp/print-purchase-logisticsLabel` | 3001943 | 全托管, SHEIN自营, POP | 2026-08-05 15:21:25 | [JSON](./operations/3001943.json) |
| POST | 商品打印条码 | `/open-api/goods/print-barcode` | 3001653 | 全托管, SHEIN自营, POP | 2026-03-31 21:27:36 | [JSON](./operations/3001653.json) |
| POST | 手工下备货单 | `/open-api/idms/create-order` | 3002040 | 自运营, 全托管, SHEIN自营, 半托管, POP | 2026-09-23 21:40:03 | [JSON](./operations/3002040.json) |
| POST | 备货单审核列表 | `/open-api/idms/review-orders` | 3002041 | 自运营, 全托管, SHEIN自营, 半托管, POP | 2026-09-23 21:43:48 | [JSON](./operations/3002041.json) |
| POST | 查询商品备货信息列表 | `/open-api/openapi-business-backend/stock-goods-list` | 3001985 | 全托管, SHEIN自营, POP | 2026-08-21 20:40:11 | [JSON](./operations/3001985.json) |
| POST | 打印箱唛或包裹面单 | `/open-api/order/print-package` | 3001659 | 全托管, SHEIN自营, POP | 2026-04-07 20:28:19 | [JSON](./operations/3001659.json) |
| GET | 物流公司信息查询（即将废弃） | `/open-api/shipping/express-company-list` | 3001300 | Not listed | 2025-07-21 11:32:22 | [JSON](./operations/3001300.json) |
| GET | 查询SHEIN仓库的收件信息 | `/open-api/order/storage-receiver-info` | 3001660 | 全托管, SHEIN自营, POP | 2026-04-07 20:31:49 | [JSON](./operations/3001660.json) |
