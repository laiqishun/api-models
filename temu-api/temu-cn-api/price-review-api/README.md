---
title: Temu CN Price Review API
description: "Full-managed CN price-review/adjustment and Partner semi-managed supply-price, price-review, and price-adjustment operations."
---

# Price Review API

中国跨境核价、调价与供货价查询。全托能力走 CN 网关；半托核价/调价与 SKU 供货价走 Partner 网关。调用前按 operation 的 host/`x-temu-migration` 选择对应 token。

## 选择规则

- 全托核价：`bg.price.review.*`（CN）
- 全托调价：`bg.full.adjust.price.*`（CN）
- 半托核价：`bg.semi.price.review.*.order`（Partner）
- 半托调价：`bg.semi.adjust.price.*.order`（Partner）
- 查 SKU 供货价：`bg.glo.goods.price.list.get`（Partner）

不要因 type 名相似而混用全托与半托接口。

## API List

- [bg.full.adjust.price.batch.review](operations/bg.full.adjust.price.batch.review.json) — 批量处理全托调价单
- [bg.full.adjust.price.page.query](operations/bg.full.adjust.price.page.query.json) — 分页查询全托调价单
- [bg.glo.goods.price.list.get](operations/bg.glo.goods.price.list.get.json) — 批量查询货品 SKU 供货价
- [bg.price.review.confirm](operations/bg.price.review.confirm.json) — 全托同意核价单建议价
- [bg.price.review.page.query](operations/bg.price.review.page.query.json) — 分页查询全托核价单
- [bg.price.review.reject](operations/bg.price.review.reject.json) — 全托拒绝核价单建议价并提交新申报价
- [bg.semi.adjust.price.batch.review.order](operations/bg.semi.adjust.price.batch.review.order.json) — 批量确认或拒绝半托调价单
- [bg.semi.adjust.price.page.query.order](operations/bg.semi.adjust.price.page.query.order.json) — 分页查询半托调价单
- [bg.semi.price.review.confirm.order](operations/bg.semi.price.review.confirm.order.json) — 半托同意核价单建议价
- [bg.semi.price.review.page.query.order](operations/bg.semi.price.review.page.query.order.json) — 分页查询半托核价单
- [bg.semi.price.review.reject.order](operations/bg.semi.price.review.reject.order.json) — 半托拒绝核价单建议价并提交新申报价
