---
title: Temu CN Price Review API
description: "Full-managed CN price-review and price-adjustment operations."
---

# Price Review API

中国跨境全托核价与调价，使用卖家应用配置的 CN 网关及 CN 授权 token。

## 选择规则

- 全托核价：`bg.price.review.*`（CN）
- 全托调价：`bg.full.adjust.price.*`（CN）

第三方 ERP 不提供半托核价/调价及 CN/Partner SKU 供货价查询；全托核价接口仅供全托店铺使用，不作为半托核价的替代。

## API List

- [bg.full.adjust.price.batch.review](operations/bg.full.adjust.price.batch.review.json) — 批量处理全托调价单
- [bg.full.adjust.price.page.query](operations/bg.full.adjust.price.page.query.json) — 分页查询全托调价单
- [bg.price.review.confirm](operations/bg.price.review.confirm.json) — 全托同意核价单建议价
- [bg.price.review.page.query](operations/bg.price.review.page.query.json) — 分页查询全托核价单
- [bg.price.review.reject](operations/bg.price.review.reject.json) — 全托拒绝核价单建议价并提交新申报价
