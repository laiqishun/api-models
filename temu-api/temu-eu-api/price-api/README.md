---
title: Temu EU Price API
description: "EU local pricing, price-order, appeal, recommended-price, and order-amount operations."
---

# Price API

欧洲本土商品定价、报价单、价格申诉与订单金额（pricing, price order, appeal, order amount）。

## 订单金额版本

`bg.order.amount.query` 与 `temu.order.amount.v2.query` 均由官方文档提供，但返回字段结构不同。需要订单收益/金额数据时，先按调用方已对接的响应模型选择；新接入可优先评估更新时间更晚的 V2，但本地文档不把旧接口标记为已废弃。

## API List

- [bg.local.goods.priceorder.accept](operations/bg.local.goods.priceorder.accept.json) - Support merchants within the white list to accept the price offer through the interface.
- [bg.local.goods.priceorder.change.sku.price](operations/bg.local.goods.priceorder.change.sku.price.json) - Support merchants within the white list to modify sku base prices in batches.
- [bg.local.goods.priceorder.negotiate](operations/bg.local.goods.priceorder.negotiate.json) - Support merchants within the whitelist to negotiate price through interfaces
- [bg.local.goods.priceorder.query](operations/bg.local.goods.priceorder.query.json) - Support businesses within the white list to query the price offer list.
- [bg.local.goods.sku.list.price.query](operations/bg.local.goods.sku.list.price.query.json) - Query local goods SKU prices
- [bg.order.amount.query](operations/bg.order.amount.query.json) - Query order amount using the earlier response model
- [temu.local.goods.appealorder.create](operations/temu.local.goods.appealorder.create.json) - Support merchants in appealing against the recommended supply prices of low traffic goods
- [temu.local.goods.appealorder.query](operations/temu.local.goods.appealorder.query.json) - Support merchants in querying appeal orders
- [temu.local.goods.appealorder.record.query](operations/temu.local.goods.appealorder.record.query.json) - Support merchants in querying appeal order records
- [temu.local.goods.priceorder.reject](operations/temu.local.goods.priceorder.reject.json) - Support merchants in rejecting price orders
- [temu.local.goods.recommendedprice.query](operations/temu.local.goods.recommendedprice.query.json) - Support merchants in querying the recommended supply prices.
- [temu.order.amount.v2.query](operations/temu.order.amount.v2.query.json) - Query order amount using the V2 response model
