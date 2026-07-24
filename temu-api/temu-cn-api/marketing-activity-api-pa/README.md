---
title: Temu CN Marketing Activity PA API
description: "Partner-gateway campaign discovery, product lookup, enrollment, and enrollment-record operations."
---

# Marketing Activity PA API

中国跨境店铺通过 Partner 网关查询活动、活动场次和活动商品，并提交或查询报名记录（marketing activity, campaign, enrollment）。

Gateway: `https://openapi-b-partner.temu.com/openapi/router`

## 推荐流程

1. 查询活动列表和详情。
2. 查询活动场次与可参与商品。
3. 提交活动报名。
4. 查询报名记录和处理状态。

## API List

- [bg.marketing.activity.detail.get.global](operations/bg.marketing.activity.detail.get.global.json) — 查询活动详情
- [bg.marketing.activity.enroll.list.get.global](operations/bg.marketing.activity.enroll.list.get.global.json) — 查询活动报名记录
- [bg.marketing.activity.enroll.submit.global](operations/bg.marketing.activity.enroll.submit.global.json) — 提交活动报名
- [bg.marketing.activity.list.get.global](operations/bg.marketing.activity.list.get.global.json) — 查询活动列表
- [bg.marketing.activity.product.get.global](operations/bg.marketing.activity.product.get.global.json) — 查询活动商品
- [bg.marketing.activity.session.list.get.global](operations/bg.marketing.activity.session.list.get.global.json) — 查询活动场次列表
