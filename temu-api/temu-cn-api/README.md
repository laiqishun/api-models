---
title: Temu CN API
description: "China cross-border Temu API entry point for full-managed and semi-managed inventory, product, pricing, and supply-chain capabilities, including CN-to-PA migrations."
---

# Temu CN API

本模块服务中国跨境店铺，包含仍在 CN 网关的能力和已迁移到 Partner（PA）网关的能力。业务组不再按 `-pa` 拆分子目录；同一业务组内可能同时包含 CN 与 PA operation，调用时以各 operation 的 host/`x-temu-migration` 为准。

## 适用边界

| 场景 | 是否使用本模块 | 路由 |
| --- | --- | --- |
| 中国跨境全托库存、供货、备货、发货单、核价 | 是 | CN；已迁移能力按 operation 选择 Partner |
| 中国跨境半托库存、货品、供货价、核价/调价 | 是 | 迁移后的半托能力通常使用 Partner |
| 中国跨境半托消费者订单、区域履约、区域物流、售后 | 否 | 返回 [根路由](../README.md)，按订单目标站点进入 US/EU/Global |
| US/EU/其他地区本土店铺 | 否 | 使用对应区域模块 |

“发货单/备货单”可能是 CN 供应链单据，不等同于半托消费者订单。用户说“查订单”时必须先确认是哪一种。

## 网关与授权

| 接口来源 | 网关 | Token |
| --- | --- | --- |
| 未迁移的 CN type | 卖家应用配置的 CN `/openapi/router` | CN 授权 token |
| 迁移后的 PA type | `https://openapi-b-partner.temu.com/openapi/router` | 在 Partner 授权路径重新取得的 PA token |

`type`、网关和 token 必须属于同一体系。出现 `type not exists` 或无权限错误时，先检查是否把迁移后的 PA type 发到了 CN 网关，或仍在使用旧 token。

同一业务组内如何区分：打开目标 operation JSON，优先看 `x-temu-gateway` / `host`，以及是否带有 `x-temu-migration`。

## 全托与半托的关键例外

官方迁移表明确保留以下全托 CN 核价 type（与半托 PA type 同属 [Price Review](./price-review-api/README.md)）：

| 意图 | 全托 CN | 半托 PA |
| --- | --- | --- |
| 分页查询核价单 | `bg.price.review.page.query` | `bg.semi.price.review.page.query.order` |
| 同意核价建议价 | `bg.price.review.confirm` | `bg.semi.price.review.confirm.order` |
| 拒绝核价并重新报价 | `bg.price.review.reject` | `bg.semi.price.review.reject.order` |

半托调价使用 `bg.semi.adjust.price.*.order` PA type，不要调用已迁移的旧调价 type。

## 按意图选择 API 组

- **半托库存、改库存、绑定仓库**：优先 [Inventory](./inventory-api/README.md)。
- **发品、商品详情、商品搬运与 CN 补充查询**：[Product](./product-api/README.md)。
- **类目与必填属性**：[Category Attribute](./category-attribute-api/README.md)。
- **商品修改**：[Product Edit](./product-edit-api/README.md)。
- **核价/调价/供货价**：按托管模式在 [Price Review](./price-review-api/README.md) 中选择全托 CN 或半托 PA type。
- **全托 JIT 与备货发货**：[JIT](./jit-api/README.md)、[Stock And Shipping](./stock-shipping-api/README.md)。
- **面单与箱唛**：[Waybill And Box Label](./waybill-box-label-api/README.md)。
- **尺码表**：[Size Chart](./size-chart-api/README.md)。
- **图片/视频**：[Image Processing](./image-processing-api/README.md)、[Video Upload](./video-upload-api/README.md)。
- **营销活动**：[Marketing Activity](./marketing-activity-api/README.md)。
- **商品条码**：[Product Barcode](./product-barcode-api/README.md)。
- **授权信息**：[Authorization](./authorization-api/README.md)。
- **质检退供/样品退回**：[Sample Quality Return](./sample-quality-return-api/README.md)。

## 调用方式

operation 文件是单接口 Swagger 2.0 文档。调用时：

1. 使用 operation 中的 `type` enum。
2. 公共鉴权字段与业务字段放在同一个 JSON body。
3. PA operation 使用文件中的绝对 Partner host；CN operation 的相对 `/openapi/router` 由卖家应用配置 CN host。
4. `app_secret` 只参与签名，禁止发送。
5. 字段固定值按 operation 的离线引用读取 [CN 数据字典](./offline-docs/data-dictionary.md) 对应章节。

## API Groups

- [Authorization](./authorization-api/README.md) — 2 operations
- [Category Attribute](./category-attribute-api/README.md) — 15 operations
- [Image Processing](./image-processing-api/README.md) — 10 operations
- [Instruction File](./instruction-file-api/README.md) — 5 operations
- [Inventory](./inventory-api/README.md) — 4 operations
- [JIT](./jit-api/README.md) — 5 operations
- [Marketing Activity](./marketing-activity-api/README.md) — 6 operations
- [Model Fitting](./model-fitting-api/README.md) — 4 operations
- [PA Gateway](./partner-gateway-api/README.md) — 1 operation
- [Price Review](./price-review-api/README.md) — 11 operations
- [Product](./product-api/README.md) — 10 operations
- [Product Barcode](./product-barcode-api/README.md) — 2 operations
- [Product Edit](./product-edit-api/README.md) — 8 operations
- [Sales](./sales-api/README.md) — 1 operation
- [Sample Quality Return](./sample-quality-return-api/README.md) — 7 operations
- [Size Chart](./size-chart-api/README.md) — 8 operations
- [Stock And Shipping](./stock-shipping-api/README.md) — 21 operations
- [Video Upload](./video-upload-api/README.md) — 2 operations
- [Waybill And Box Label](./waybill-box-label-api/README.md) — 2 operations

## 迁移资料边界

迁移表列出的 12 个 PA type 没有独立详细章节，本模块按迁移表指定的 legacy 对应关系保留其请求与响应契约。它们作为正常 operation 参与上方分组索引；调用时仍必须使用新 PA type、Partner 网关和 PA token。

## 证据来源

- `Temu CN API文档.md`
- [Temu CN 数据字典](./offline-docs/data-dictionary.md)
