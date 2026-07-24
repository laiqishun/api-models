---
title: Temu CN Full-Managed Price Review API
description: "CN full-managed price-review and price-adjustment operations; semi-managed sellers must use the PA price-review group."
---

# Price Review API

适用于中国跨境**全托管**核价/调价（price review, price adjustment）。半托核价与调价已迁移到 [Price Review PA](../price-review-api-pa/README.md)，不要因 type 名相似而混用。

## 选择规则

- 查询/同意/拒绝全托核价单：使用 `bg.price.review.*`。
- 查询/批量处理全托调价单：使用 `bg.full.adjust.price.*`。
- 半托核价：使用 `bg.semi.price.review.*.order`。
- 半托调价：使用 `bg.semi.adjust.price.*.order`。

## API List

- [bg.full.adjust.price.batch.review](operations/bg.full.adjust.price.batch.review.json) — 批量处理全托调价单
- [bg.full.adjust.price.page.query](operations/bg.full.adjust.price.page.query.json) — 分页查询全托调价单
- [bg.price.review.confirm](operations/bg.price.review.confirm.json) — 全托同意核价单建议价
- [bg.price.review.page.query](operations/bg.price.review.page.query.json) — 分页查询全托核价单
- [bg.price.review.reject](operations/bg.price.review.reject.json) — 全托拒绝核价单建议价并提交新申报价
