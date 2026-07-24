---
title: Temu Global API
description: "Global gateway API for local stores and Chinese semi-managed destination-order capabilities outside the dedicated US and EU modules."
---

# Temu Global API

本模块使用 Global 网关。按当前文档路由约定，除 US/EU 外的其他本土店铺，以及中国跨境半托的非 US/EU 消费者订单侧能力，使用本模块。

Default gateway: `https://openapi-b-global.temu.com/openapi/router`

## 适用边界

- **加拿大、墨西哥及其他非 US/EU 本土店铺**：按业务意图使用本模块。
- **中国跨境半托 + 非 US/EU 目标站点**：订单、履约、物流、退货退款/售后使用本模块。
- **美国本土或美国目标站点**：使用 [Temu US API](../temu-us-api/README.md)。
- **欧洲本土或欧洲目标站点**：使用 [Temu EU API](../temu-eu-api/README.md)。
- **中国跨境半托库存**：不使用本模块，返回 [Temu CN API](../temu-cn-api/README.md)。
- **中国跨境半托发品/供货链**：优先按 CN/PA 文档选择；Global 中仅标为 `Local` 的商品接口不能自动用于半托。

## 渐进式选择

1. 排除 US 和欧洲目标站点。
2. 根据用户意图进入一个业务组。
3. 在组 README 中选择 operation。
4. 打开一个 operation JSON，使用其中的 Global host、type、audience、字段和示例。

Global 与 US/EU 有大量同名 type。已进入本模块后，唯一调用身份是：

```text
(temu-global-api, openapi-b-global.temu.com, type)
```

禁止使用旧的 `openapi-b.temu.com` 文档值，也不能把 US/EU 同名 operation 的区域网关带入本模块。目标区域字段优先；其他区域同名 model 仅在契约兼容时补齐缺失信息。

## 按意图选择 API 组

- **授权信息、换取 token / authorization**：[Authorization](./authorization-api/README.md)
- **查订单、订单详情、收货信息 / orders**：[Order](./order-api/README.md)
- **创建/更新发货、确认包裹、预约揽收 / fulfillment**：[Fulfillment](./fulfillment-api/README.md)
- **物流商、物流服务、仓库 / logistics**：[Logistics](./logistics-api/README.md)
- **本土商品发布、编辑、上下架、库存 / local product**：[Product](./product-api/README.md)
- **报价、基础价、订单金额 / price**：[Price](./price-api/README.md)
- **退货、退款、售后 / return and refund**：[Return And Refund](./return-refund-api/README.md)
- **活动、报名、促销 / promotion**：[Promotion](./promotion-api/README.md)

## 调用规则

- 所有 operation 使用 `POST https://openapi-b-global.temu.com/openapi/router`。
- 公共参数与业务字段位于同一个 JSON body，不添加额外的 `request` wrapper。
- `type` 必须使用当前 operation JSON 中的 enum 值。
- `x-temu-audience` 用于判断 `Local`、`Cross Border`、`Fully Manage` 等适用范围；纯 `Cross Border` operation 不应路由给 Local 店铺。
- 时间字段单位以当前 operation 为准；公共 `timestamp` 为 10 位 UNIX 秒。
- 签名规则见 [Temu API 根文档](../README.md#6-通用调用与签名)。

## API Groups

- [Authorization](./authorization-api/README.md) — 2 operations
- [Fulfillment](./fulfillment-api/README.md) — 16 operations
- [Logistics](./logistics-api/README.md) — 4 operations
- [Order](./order-api/README.md) — 6 operations
- [Price](./price-api/README.md) — 11 operations
- [Product](./product-api/README.md) — 43 operations
- [Promotion](./promotion-api/README.md) — 6 operations
- [Return And Refund](./return-refund-api/README.md) — 10 operations

## 证据来源

- `Temu全球API文档.md`
