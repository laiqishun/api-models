# Ads API

Source group: `Ads`.

## 使用范围

欧洲站搜索推荐广告（Temu Ads / Product Ads）的资格校验、ROAS 预估、创建、修改、操作日志和店铺/商品报表。

适用于欧洲本土和中国跨境半托卖家的欧洲站广告能力。`x-temu-audience` 为 `Local` 与 `Cross Border`，官方权限包包括 `Advertising Management` 和 `Semi Advertising Management`；当前标签未标注全托支持。

固定调用 `POST https://openapi-b-eu.temu.com/openapi/router`。公共参数与业务字段放在同一个 JSON body，`type` 使用所选 operation 的完整 API 名称，不添加额外的 `request` 包装层。

美国投放进入 [US Ads](../../temu-us-api/ads-api/README.md)，其余区域进入 [Global Ads](../../temu-global-api/ads-api/README.md)。同名 type 不代表参数和必填约束一致；EU 接口以本目录文件为准。活动促销报名使用 [Promotion](../promotion-api/README.md)。

## 推荐调用顺序

1. 创建前调用 `temu.searchrec.ad.goods.create.query`，校验商品广告投放资格。
2. 调用 `temu.searchrec.ad.roas.pred` 获取分级 ROAS 建议。
3. 调用 `temu.searchrec.ad.create` 创建活动，设置日预算和目标 ROAS。
4. 调用 `temu.searchrec.ad.detail.query` 查询活动状态、预算和 ROAS。
5. 调用 `temu.searchrec.ad.modify` 修改预算或 ROAS，以及删除、暂停、开启广告；具体操作由 `status` 指定。
6. 使用店铺或商品报表查询效果；使用 `temu.searchrec.ad.log.query` 排查操作记录。

控制台开通流程参考 [Ads Introduction](https://partner-us.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a&sub_menu_code=be630d94cf2748c5a8544b50783296be)：主账号签署 Advertising Services Agreement，在 Billing 中配置 Advertising Reserve。EU 请求参数和网关以本目录的 EU 官方文档数据为准。

## 参数注意事项

- 创建广告的 `roas` 为实际值乘以 10,000；预算单位和特殊值以对应字段说明为准。
- 两个报表接口的 `startTs`、`endTs` 为毫秒时间戳；公共签名参数 `timestamp` 为秒。
- 活动详情、操作日志和两个报表接口提供 `selectedAdManagedType`：`0` 或不传表示单商品广告，`1` 表示全店推广。字段含义以各 operation 为准。
- EU 修改广告的 `modifyAdDTO.goodsId` 为必填；EU 商品报表包含 `result.goodsInfo.grayReason`（`type`、`reason`）。这些区域差异不能用 US 文件覆盖。
- 官方示例中的占位 `type: "test"` 已替换为实际 API 名称。其他示例值仍为占位值，不可直接作为真实业务请求。

## API List

- [temu.searchrec.ad.goods.create.query](operations/temu.searchrec.ad.goods.create.query.json) - 校验商品广告投放资格
- [temu.searchrec.ad.roas.pred](operations/temu.searchrec.ad.roas.pred.json) - 查询广告 ROAS 建议
- [temu.searchrec.ad.create](operations/temu.searchrec.ad.create.json) - 创建广告活动
- [temu.searchrec.ad.detail.query](operations/temu.searchrec.ad.detail.query.json) - 查询广告活动详情
- [temu.searchrec.ad.modify](operations/temu.searchrec.ad.modify.json) - 修改广告活动、预算、ROAS 和状态
- [temu.searchrec.ad.log.query](operations/temu.searchrec.ad.log.query.json) - 查询广告操作日志
- [temu.searchrec.ad.reports.mall.query](operations/temu.searchrec.ad.reports.mall.query.json) - 查询店铺维度广告报表
- [temu.searchrec.ad.reports.goods.query](operations/temu.searchrec.ad.reports.goods.query.json) - 查询商品维度广告报表

## 来源与同步范围

2026-09-09 从 [EU 官方文档数据接口](https://partner-eu.temu.com/riemann/api/v2/api/doc/detail/get) 逐项 POST `{"api_id":"上述接口名称"}` 获取。每个 JSON 保留独立的 EU 网关、完整请求/响应层级、错误码、权限包、示例、更新时间和来源哈希。

本组同步上述 8 个接口。官方权限包另列 `temu.searchrec.ad.batch.modify`，不在本次指定的接口清单中，未生成 operation。
