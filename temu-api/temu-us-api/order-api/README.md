---
title: Temu US Order API
description: "US order search, detail, shipping-address, customization, consolidation, and cancellation workflows."
---

# Order API

适用于美国本土店铺，以及目标站点为美国的中国跨境半托消费者订单（orders, order detail, shipping address, cancellation）。

## 选择规则

- 批量分页查订单：`bg.order.list.v2.get`
- 查单个订单完整详情：`bg.order.detail.v2.get`
- 查普通收货信息：`bg.order.shippinginfo.v2.get`
- 查敏感解密地址：`bg.order.decryptshippinginfo.get`，需要对应权限
- 查定制内容：`bg.order.customization.get`
- 查可合并发货订单组：`bg.order.combinedshipment.list.get`
- 缺货取消或取消申诉：使用对应 `temu.order.cancel.*` 提交接口，再调用 result 接口轮询异步结果

库存不足但尚未确定取消时，不要用订单取消接口代替 [CN 半托库存更新](../../temu-cn-api/inventory-api-pa/README.md)。

## API List

- [bg.order.combinedshipment.list.get](operations/bg.order.combinedshipment.list.get.json) — 查询可合并发货的父订单组
- [bg.order.customization.get](operations/bg.order.customization.get.json) — 批量获取定制商品内容
- [bg.order.decryptshippinginfo.get](operations/bg.order.decryptshippinginfo.get.json) — 获取订单敏感收货地址
- [bg.order.detail.v2.get](operations/bg.order.detail.v2.get.json) — 获取指定订单详情
- [bg.order.list.v2.get](operations/bg.order.list.v2.get.json) — 按筛选条件分页查询订单
- [bg.order.shippinginfo.v2.get](operations/bg.order.shippinginfo.v2.get.json) — 获取指定订单收货信息
- [temu.order.cancel.appeal.apply](operations/temu.order.cancel.appeal.apply.json) — 提交订单取消申诉
- [temu.order.cancel.appeal.result.get](operations/temu.order.cancel.appeal.result.get.json) — 查询取消申诉结果
- [temu.order.cancel.outofstock.apply](operations/temu.order.cancel.outofstock.apply.json) — 提交缺货取消申请
- [temu.order.cancel.outofstock.result.get](operations/temu.order.cancel.outofstock.result.get.json) — 查询缺货取消审核结果
