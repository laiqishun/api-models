---
title: Temu CN Semi-Managed Inventory PA API
description: "Partner-gateway inventory operations for Chinese cross-border semi-managed stores."
---

# Inventory PA API

中国跨境**半托管库存**的首选入口（inventory, stock, warehouse binding）。即使消费者订单属于 US/EU/Global，半托库存仍使用本组，不按订单目的地区域分流。

Gateway: `https://openapi-b-partner.temu.com/openapi/router`

## 推荐流程

1. 按站点查询可绑定仓库。
2. 建立商品、站点与仓库的库存路由关系。
3. 查询或更新销售库存。

`siteId`、`siteIdList` 等固定站点值见 [CN 数据字典：半托管站点列表](../offline-docs/data-dictionary.md#半托管站点列表)。

## API List

- [bg.btg.goods.stock.quantity.get](operations/bg.btg.goods.stock.quantity.get.json) — 查询半托商品销售库存
- [bg.btg.goods.stock.quantity.update](operations/bg.btg.goods.stock.quantity.update.json) — 更新半托商品销售库存
- [bg.btg.goods.stock.route.add](operations/bg.btg.goods.stock.route.add.json) — 新增半托商品仓站关系并填写库存
- [bg.btg.goods.stock.warehouse.list.get](operations/bg.btg.goods.stock.warehouse.list.get.json) — 按站点查询自发货商品可绑定仓库
