# Ads API

Source group: `Ads`.

## 使用范围

搜索推荐广告（Temu Ads / Product Ads）的投放、修改、资格校验、ROAS 预估、操作日志与店铺/商品报表（searchrec ads, product ads, ROAS, advertising reports）。

Temu Ads 用于帮助卖家获取流量、吸引顾客并推动销售增长，卖家可以快速创建和优化广告活动。可在 [ads.temu.com](https://ads.temu.com/) 或商家后台 **Product ADS** 中操作，也可以通过本组 Advertising API 完成同等能力。

本目录对应 Partner 文档 [Ads Introduction](https://partner.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=be630d94cf2748c5a8544b50783296be)，解决的是搜索推荐广告的创建、修改和效果查询，而不是商品发布、订单、库存或物流。区域促销报名仍在 [Promotion](../promotion-api/README.md)；CN 营销活动仍在 [Marketing Activity](../../temu-cn-api/marketing-activity-api/README.md)。

`x-temu-audience` 为 `Fully Manage` 与 `Cross Border`。不要把本组接口路由给纯 Local 本土店铺。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## 推荐调用顺序

1. 创建前先用 `temu.searchrec.ad.goods.create.query` 校验商品是否可投（官方要求的前置检查）。
2. 用 `temu.searchrec.ad.roas.pred` 查询分级 ROAS 建议；创建活动时优先使用系统推荐 ROAS。
3. 用 `temu.searchrec.ad.create` 按商品创建广告，配置 Daily Budget 和 ROAS bid。
4. 用 `temu.searchrec.ad.detail.query` 查询活动详情（当前日预算、目标 ROAS 等）。
5. 用 `temu.searchrec.ad.modify` 调整进行中活动的 ROAS 与日预算。
6. 用店铺/商品报表接口查看 ROAS、订单量、曝光、点击和 CTR。
7. 排障时用 `temu.searchrec.ad.log.query` 查询操作日志。

控制台侧还需要主账号签署 Advertising Services Agreement，并在 Billing 中配置 Advertising Reserve；这些不是本组 API。

Ads Introduction 另列出 `temu.searchrec.ad.batch.modify`（批量修改 ROAS/日预算/状态，非原子、限频 1 次/5 秒）。本目录当前未收录该 operation。

## API List

- [temu.searchrec.ad.goods.create.query](operations/temu.searchrec.ad.goods.create.query.json) - Product Advertising Eligibility Check：校验商品是否可投，创建前必须先调
- [temu.searchrec.ad.roas.pred](operations/temu.searchrec.ad.roas.pred.json) - Query Advertising ROAS：查询商品分级 ROAS 建议
- [temu.searchrec.ad.create](operations/temu.searchrec.ad.create.json) - Create Advertising Campaign：按商品创建广告，配置日预算和 ROAS
- [temu.searchrec.ad.detail.query](operations/temu.searchrec.ad.detail.query.json) - Query Campaign Status：查询广告活动详情（日预算、目标 ROAS 等）
- [temu.searchrec.ad.modify](operations/temu.searchrec.ad.modify.json) - Modify Advertising Campaign：修改进行中活动的 ROAS 与日预算
- [temu.searchrec.ad.log.query](operations/temu.searchrec.ad.log.query.json) - Query Advertising Operation Logs：查询广告操作日志
- [temu.searchrec.ad.reports.mall.query](operations/temu.searchrec.ad.reports.mall.query.json) - Store-Level Campaign Analytics：店铺维度广告报表（ROAS、订单、曝光、点击、CTR）
- [temu.searchrec.ad.reports.goods.query](operations/temu.searchrec.ad.reports.goods.query.json) - Product-Level Campaign Analytics：商品维度广告报表（ROAS、订单、曝光、点击、CTR）
