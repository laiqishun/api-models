---
title: Temu API Models
description: "AI-friendly Temu API entry point: determine seller mode and destination region, select one regional module and business group, then open one operation-level Swagger JSON file."
---

# Temu API Models

本目录按“用户意图 → 店铺模式 → 目标区域 → 业务组 → operation Swagger”渐进加载。不要在四个区域中仅凭 `type` 全局搜索：US、EU、Global 有大量同名 type，但网关和部分字段不同。

## 1. 选择接口前必须知道

按顺序确认以下信息；缺少会改变路由的信息时，先向用户追问，不要猜测。

1. **店铺主体**：中国跨境店铺，还是目标市场本土店铺。
2. **经营模式**：中国跨境店铺是全托管（full-managed）还是半托管（semi-managed）。
3. **业务意图**：库存/货品/供货链，还是订单/履约/物流/售后。
4. **目标站点**：半托订单相关能力必须知道消费者订单所属国家或 `siteId`。

## 2. 区域路由决策

| 店铺与意图 | 使用模块 | 说明 |
| --- | --- | --- |
| 中国跨境全托：库存、货品、备货、供货、核价、发货单 | [temu-cn-api](./temu-cn-api/README.md) | 使用 CN 能力；已迁移接口按 CN README 选择 PA 或保留的 CN type |
| 中国跨境半托：库存、货品、供货价、核价/调价、CN 侧营销能力 | [temu-cn-api](./temu-cn-api/README.md) | 半托库存仍属于 CN；迁移后的库存 type 使用 PA 网关 |
| 中国跨境半托：消费者订单、履约、物流、退货退款/售后 | 订单目标站点对应的 US、EU 或 Global | 禁止在 `temu-cn-api` 中寻找消费者订单接口 |
| 美国本土店铺，或半托订单目标站点为美国 | [temu-us-api](./temu-us-api/README.md) | US 网关 |
| 欧洲本土店铺，或半托订单目标站点为欧洲国家（含英国） | [temu-eu-api](./temu-eu-api/README.md) | EU 网关 |
| 除 US/EU 外的其他本土店铺或半托目标站点 | [temu-global-api](./temu-global-api/README.md) | Global 网关；包括加拿大、墨西哥及其他非 US/EU 站点 |

站点名称与 `siteId` 的完整值表见 [CN 数据字典：半托管站点列表](./temu-cn-api/offline-docs/data-dictionary.md#半托管站点列表)。路由时先按国家归属选择模块，再在 operation 请求中使用官方要求的 `siteId`/`regionId`。

## 3. 常见用户意图索引

| 用户意图 / Intent | 中国跨境全托或半托 | US/EU/Global 本土或半托订单侧 |
| --- | --- | --- |
| 查库存、改库存、绑定仓库 / inventory, stock | 半托销售库存使用 CN `inventory-api-pa`；全托 JIT/备货库存按单据场景使用 `jit-api` 或 `stock-shipping-api`，不要把全托路由到半托 Inventory PA | 本土店铺使用所选区域的 `product-api` 库存 operation；中国半托库存不要走区域 API |
| 发品、改商品、类目属性、图片、尺码 / listing, product | CN 的 `product-api-pa`、`product-edit-api-pa`、`category-attribute-api-pa` 及相关组 | 所选区域的 `product-api` |
| 核价、调价、供货价 / price review, pricing | CN 的 `price-review-api` 或 `price-review-api-pa`，先判断全托/半托 | 所选区域的 `price-api` |
| 查订单、订单详情、收货地址 / orders | 半托按目标站点进入区域 `order-api`；全托 CN 供货单不是消费者订单 | 所选区域的 `order-api` |
| 发货、面单、合单、scanform / fulfillment, shipping label | 全托 CN 供货链使用 `stock-shipping-api`、`waybill-box-label-api` | 所选区域的 `fulfillment-api` 或 `logistics-api` |
| 退货、退款、售后 / return, refund, aftersales | CN 的质检退供等供应链场景使用 `sample-quality-return-api` | 所选区域的 `return-refund-api` |
| 活动报名、促销 / promotion, campaign | CN 的 `marketing-activity-api-pa` | 所选区域的 `promotion-api` |
| 税务 / tax | 按 operation 说明；CN 发品字段按 CN 文档 | EU 独有 `tax-api`，其他区域先检查 `product-api` 中的税码能力 |
| 授权信息 / authorization, token permissions | 先选择 CN 或 PA 授权 type | 所选区域的 `authorization-api` |

选择业务组后，读取该组 README；只打开与意图匹配的 operation JSON。需要固定枚举时，再按 operation 的离线引用读取数据字典对应锚点，不要一次加载整份字典。

## 4. 唯一 operation 规则

一个可调用接口由以下三项共同确定：

```text
(region module, gateway host, type)
```

- `type` 相同不代表区域契约相同。
- 已选 US 时只读取 `temu-us-api` 下的同名文件；EU、Global 同理。
- 跨区域补齐字段时，目标区域参数表优先；同名 model 只有在字段层级、类型、必填和语义一致时才能互相参考。
- 如果目标区域与参考区域冲突，保留目标区域定义。

## 5. CN 与 PA 网关选择

CN 官方迁移表优先于旧 type：

1. 迁移表列出的新 type 使用 `https://openapi-b-partner.temu.com/openapi/router`，并重新授权取得 PA token。
2. 未列入迁移表的 CN type 继续使用卖家应用配置的 CN `/openapi/router`。
3. `type` 与网关必须成对，不能把 PA type 发到 CN 网关，也不能用旧 CN token 调 PA type。
4. 三个核价接口为明确例外：
   - 全托分页核价：`bg.price.review.page.query`
   - 全托同意核价：`bg.price.review.confirm`
   - 全托拒绝核价：`bg.price.review.reject`
   - 半托分别使用 `bg.semi.price.review.page.query.order`、`bg.semi.price.review.confirm.order`、`bg.semi.price.review.reject.order`

完整分组和迁移边界见 [Temu CN API](./temu-cn-api/README.md)。

## 6. 通用调用与签名

Temu router API 使用 `POST /openapi/router`，公共参数和业务参数位于同一个 JSON body。operation JSON 中的 `type` enum、host、必填字段和示例是最终调用依据。

常见公共参数：

- `type`：当前 operation 的完整 API type。
- `app_key`、`access_token`：应用与卖家授权信息。
- `timestamp`：10 位 UNIX 秒时间戳，通常要求在当前时间前后 300 秒内。
- `data_type`：通常为 `JSON`。
- `version`：是否必填以当前 operation 为准。
- `sign`：签名结果；`app_secret` 只参与本地签名，绝不能发送或写入文档。

签名流程：

1. 组装最终顶层请求参数，先移除旧的 `sign`。
2. 按参数名 ASCII 升序排列。
3. 逐项按 `key + value` 无分隔拼接；数组和对象使用与官方示例一致的紧凑 JSON。
4. 在拼接结果前后各追加一次 `app_secret`。
5. 计算 MD5，并转换为大写十六进制字符串。

官方材料没有完整规定空值、Unicode 转义及所有语言的对象规范化细节。实现签名时必须使用固定请求向量自测，不要记录 secret、token 或待签名明文。

## 7. 常见错误定位

- `type not exists`：先检查区域模块、网关和 type 是否匹配，再检查是否已迁移到 PA。
- `access_token don't have this api access`：确认 token 属于当前 CN/PA/区域网关，并重新授权所需 type。
- 接口存在多个同名文件：回到第 2 节确定目标区域，不按更新时间随意选择。
- 用户只说“查订单”但未给店铺模式/目标站点：先追问；不要默认 CN 或 Global。
- 用户只说“查库存”且是中国跨境全托/半托：固定进入 CN，不按订单目的国分流。

## 8. 模块

- [Temu CN API](./temu-cn-api/README.md) — 124 operations
- [Temu US API](./temu-us-api/README.md) — 104 operations
- [Temu EU API](./temu-eu-api/README.md) — 109 operations
- [Temu Global API](./temu-global-api/README.md) — 98 operations

## 9. 离线参考

- [Temu CN 数据字典](./temu-cn-api/offline-docs/data-dictionary.md) — CN 商品、库存、站点、尺码及其他固定值。
