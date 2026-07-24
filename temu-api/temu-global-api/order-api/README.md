---
title: Temu Global Order API
description: "Global-region order search, detail, shipping-address, customization, and combined-shipment operations."
---

# Order API

适用于非 US/EU 本土店铺，以及目标站点为非 US/EU 的中国跨境半托消费者订单（orders, order detail, shipping address）。

## 选择规则

- 批量分页查订单：`bg.order.list.v2.get`
- 查指定订单详情：`bg.order.detail.v2.get`
- 查普通收货信息：`bg.order.shippinginfo.v2.get`
- 查敏感解密地址：`bg.order.decryptshippinginfo.get`
- 查定制商品内容：`bg.order.customization.get`
- 查可合并发货订单组：`bg.order.combinedshipment.list.get`

Global 官方文档未提供 US/EU 中的四个 `temu.order.cancel.*` operation，不要从其他区域复制后使用 Global 网关。

## API List

- [bg.order.combinedshipment.list.get](operations/bg.order.combinedshipment.list.get.json) — 查询可合并发货的父订单组
- [bg.order.customization.get](operations/bg.order.customization.get.json) — 批量获取定制商品内容
- [bg.order.decryptshippinginfo.get](operations/bg.order.decryptshippinginfo.get.json) — 获取订单敏感收货地址
- [bg.order.detail.v2.get](operations/bg.order.detail.v2.get.json) — 获取指定订单详情
- [bg.order.list.v2.get](operations/bg.order.list.v2.get.json) — 按筛选条件分页查询订单
- [bg.order.shippinginfo.v2.get](operations/bg.order.shippinginfo.v2.get.json) — 获取指定订单收货信息
