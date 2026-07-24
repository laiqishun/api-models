---
title: Temu EU Logistics API
description: "EU carrier, shipping-service, warehouse, ship-logistics-type, and scanform operations."
---

# Logistics API

欧洲本土和半托欧向订单的物流基础数据与 scanform（carrier, shipping service, warehouse, manifest/scanform）。购买面单和确认发货等操作见 [Fulfillment](../fulfillment-api/README.md)。

## Scanform 流程

1. `temu.logistics.candidate.scanform.list.get` 查询可合并生成 scanform 的包裹。
2. `temu.logistics.scanform.create` 创建 scanform。
3. `temu.logistics.scanform.get` 查询 scanform 详情和状态。
4. `temu.logistics.scanform.document.get` 获取 scanform 文档。

四个 scanform operation 来自 0416 EU 增量文档；同名 US model 只在字段契约兼容时补充缺失结构。

## API List

- [bg.logistics.companies.get](operations/bg.logistics.companies.get.json) — 按地区查询可用物流服务商
- [bg.logistics.shippingservices.get](operations/bg.logistics.shippingservices.get.json) — 按包裹尺寸和重量查询可用物流服务
- [bg.logistics.warehouse.list.get](operations/bg.logistics.warehouse.list.get.json) — 查询店铺仓库
- [temu.logistics.candidate.scanform.list.get](operations/temu.logistics.candidate.scanform.list.get.json) — 查询可生成同一 scanform 的候选包裹
- [temu.logistics.scanform.create](operations/temu.logistics.scanform.create.json) — 创建 scanform
- [temu.logistics.scanform.document.get](operations/temu.logistics.scanform.document.get.json) — 获取 scanform 文档
- [temu.logistics.scanform.get](operations/temu.logistics.scanform.get.json) — 查询 scanform 详情和状态
- [temu.logistics.shiplogisticstype.get](operations/temu.logistics.shiplogisticstype.get.json) — 查询在线发货物流类型
