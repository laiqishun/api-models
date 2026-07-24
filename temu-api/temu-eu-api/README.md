---
title: Temu EU API
description: "EU gateway API for European local stores and destination-region order capabilities of Chinese semi-managed stores whose consumer orders belong to Europe."
---

# Temu EU API

本模块使用 EU 网关，适用于欧洲本土店铺，也适用于中国跨境半托店铺的欧洲消费者订单侧能力。接口集合包含 0416 新增的四个 scanform 物流接口。

Default gateway: `https://openapi-b-eu.temu.com/openapi/router`

## 适用边界

- **欧洲本土店铺（含英国）**：按业务意图使用本模块。
- **中国跨境半托 + 欧洲目标站点**：订单、履约、物流、退货退款/售后使用本模块。
- **中国跨境半托库存**：不使用本模块，返回 [Temu CN API](../temu-cn-api/README.md)。
- **中国跨境半托发品/供货链**：优先按 CN/PA 文档选择能力；`Local` 商品 operation 不因目标站点为欧洲而自动适用于半托。
- **美国目标站点**：使用 US；其他非 US/EU 目标站点使用 Global。完整规则见 [根路由](../README.md)。

## 渐进式选择

1. 确认本土店铺位于欧洲，或半托消费者订单的目标站点位于欧洲。
2. 根据用户意图进入一个业务组。
3. 在组 README 中选择 operation；同功能多版本先阅读版本差异。
4. 打开一个 operation JSON，使用其中的 EU host、type、audience、字段和示例。

EU 与 Global/US 有大量同名 type。已进入本模块后，唯一调用身份是：

```text
(temu-eu-api, openapi-b-eu.temu.com, type)
```

目标区域字段优先；其他区域同名 model 只有在层级、类型、必填和语义一致时才能补齐缺失信息。

## 按意图选择 API 组

- **授权信息、换取 token / authorization**：[Authorization](./authorization-api/README.md)
- **查订单、订单详情、收货信息 / orders**：[Order](./order-api/README.md)
- **创建/更新发货、确认包裹、预约揽收 / fulfillment**：[Fulfillment](./fulfillment-api/README.md)
- **物流商、物流服务、仓库、scanform / logistics**：[Logistics](./logistics-api/README.md)
- **本土商品发布、编辑、上下架、库存 / local product**：[Product](./product-api/README.md)
- **报价、基础价、订单金额 / price**：[Price](./price-api/README.md)
- **退货、退款、售后 / return and refund**：[Return And Refund](./return-refund-api/README.md)
- **活动、报名、促销 / promotion**：[Promotion](./promotion-api/README.md)
- **欧盟税务、VAT / tax**：[Tax](./tax-api/README.md)

## 调用规则

- 所有 operation 使用 `POST https://openapi-b-eu.temu.com/openapi/router`。
- 公共参数与业务字段位于同一个 JSON body，不添加额外的 `request` wrapper。
- `type` 必须使用当前 operation JSON 中的 enum 值。
- `x-temu-audience` 用于判断 `Local`、`Cross Border`、`Fully Manage` 等适用范围。
- scanform 四接口以 0416 增量文档为 EU 目标区域依据；同名 US 资料仅用于兼容字段的补齐。
- 时间字段单位以当前 operation 为准；公共 `timestamp` 为 10 位 UNIX 秒。
- 签名规则见 [Temu API 根文档](../README.md#6-通用调用与签名)。

## API Groups

- [Authorization](./authorization-api/README.md) — 3 operations
- [Fulfillment](./fulfillment-api/README.md) — 18 operations
- [Logistics](./logistics-api/README.md) — 8 operations
- [Order](./order-api/README.md) — 10 operations
- [Price](./price-api/README.md) — 12 operations
- [Product](./product-api/README.md) — 41 operations
- [Promotion](./promotion-api/README.md) — 6 operations
- [Return And Refund](./return-refund-api/README.md) — 9 operations
- [Tax](./tax-api/README.md) — 2 operations

## 证据来源

- `Temu欧洲本土API文档.md`
- `Temu欧洲API文档新增接口-0416.md`
