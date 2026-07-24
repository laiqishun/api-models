---
title: Temu CN Semi-Managed Price Review PA API
description: "Partner-gateway supply-price, semi-managed price-review, and semi-managed price-adjustment operations."
---

# Price Review PA API

适用于 Partner 网关的供货价查询，以及中国跨境**半托管**核价/调价（semi-managed price review, price adjustment）。全托核价仍使用 [CN Price Review](../price-review-api/README.md) 中保留的 `bg.price.review.*` type。

Gateway: `https://openapi-b-partner.temu.com/openapi/router`

## 选择规则

- 查 SKU 供货价：`bg.glo.goods.price.list.get`
- 查询/批量处理半托调价单：`bg.semi.adjust.price.*.order`
- 查询/同意/拒绝半托核价单：`bg.semi.price.review.*.order`

## API List

- [bg.glo.goods.price.list.get](operations/bg.glo.goods.price.list.get.json) — 批量查询货品 SKU 供货价
- [bg.semi.adjust.price.batch.review.order](operations/bg.semi.adjust.price.batch.review.order.json) — 批量确认或拒绝半托调价单
- [bg.semi.adjust.price.page.query.order](operations/bg.semi.adjust.price.page.query.order.json) — 分页查询半托调价单
- [bg.semi.price.review.confirm.order](operations/bg.semi.price.review.confirm.order.json) — 半托同意核价单建议价
- [bg.semi.price.review.page.query.order](operations/bg.semi.price.review.page.query.order.json) — 分页查询半托核价单
- [bg.semi.price.review.reject.order](operations/bg.semi.price.review.reject.order.json) — 半托拒绝核价单建议价并提交新申报价
