---
title: Temu US API
description: "US gateway API for US local stores and destination-region order capabilities of Chinese semi-managed stores whose consumer orders belong to the United States."
---

# Temu US API

本模块使用 US 网关，适用于美国本土店铺，也适用于中国跨境半托店铺的美国消费者订单侧能力。

Default gateway: `https://openapi-b-us.temu.com/openapi/router`

## 适用边界

- **美国本土店铺**：按业务意图使用本模块的商品、价格、订单、履约、物流、售后和促销能力。
- **中国跨境半托 + 美国目标站点**：订单、履约、物流、退货退款/售后使用本模块。
- **中国跨境半托库存**：不使用本模块，返回 [Temu CN API](../temu-cn-api/README.md)。
- **中国跨境半托发品/供货链**：优先按 CN/PA 文档选择能力；不要因为目标站点是美国就默认使用 US 的 `Local` 商品接口。
- **非美国目标站点**：欧洲使用 EU，其余使用 Global；返回 [根路由](../README.md)。

## 渐进式选择

1. 确认目标站点是美国。
2. 根据用户意图进入一个业务组。
3. 在组 README 中选择 operation。
4. 打开一个 operation JSON，使用其中的 US host、type、audience、字段和示例。

同名 type 可能同时存在于 EU/Global。已进入本模块后，只使用 `temu-us-api` 下的文件，不能把其他区域网关或字段合并进 US 契约。跨区域资料只在 US 字段缺失且契约完全兼容时用于补齐。

## 按意图选择 API 组

- **授权信息、换取 token / authorization**：[Authorization](./authorization-api/README.md)
- **查订单、订单详情、收货信息、取消申诉 / orders**：[Order](./order-api/README.md)
- **创建/更新发货、面单、scanform、确认发货 / fulfillment**：[Fulfillment](./fulfillment-api/README.md)
- **物流商、物流服务、仓库 / logistics**：[Logistics](./logistics-api/README.md)
- **本土商品发布、编辑、上下架、库存 / local product**：[Product](./product-api/README.md)
- **报价、基础价、订单金额 / price**：[Price](./price-api/README.md)
- **退货、退款、售后 / return and refund**：[Return And Refund](./return-refund-api/README.md)
- **活动、报名、促销 / promotion**：[Promotion](./promotion-api/README.md)

## 调用规则

- 所有 operation 使用 `POST https://openapi-b-us.temu.com/openapi/router`。
- 公共参数与业务字段位于同一个 JSON body，不添加额外的 `request` wrapper。
- `type` 必须使用当前 operation JSON 中的 enum 值。
- `x-temu-audience` 用于判断 `Local`、`Cross Border`、`Fully Manage` 等适用范围；源文档未提供 audience 时不自行推断。
- 时间字段的单位以 operation 说明为准；公共 `timestamp` 为 10 位 UNIX 秒。
- 签名规则见 [Temu API 根文档](../README.md#6-通用调用与签名)。

## API Groups

- [Authorization](./authorization-api/README.md) — 2 operations
- [Fulfillment](./fulfillment-api/README.md) — 20 operations
- [Logistics](./logistics-api/README.md) — 4 operations
- [Order](./order-api/README.md) — 10 operations
- [Price](./price-api/README.md) — 11 operations
- [Product](./product-api/README.md) — 41 operations
- [Promotion](./promotion-api/README.md) — 6 operations
- [Return And Refund](./return-refund-api/README.md) — 10 operations

## 证据来源

- `Temu美国本土API文档.md`
- `Temu Open APIs.postman_collection (1).json`（仅补充 US 请求样例与签名流程）
