# Price API

Source group: `2、Price`.

## 使用范围

区域报价、价格单、价格申诉与订单金额（pricing, price order, appeal）。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## API List

- [bg.local.goods.priceorder.accept](operations/bg.local.goods.priceorder.accept.json) - Support merchants within the white list to accept the price offer through the interface.
- [bg.local.goods.priceorder.change.sku.price](operations/bg.local.goods.priceorder.change.sku.price.json) - Support merchants within the white list to modify sku base prices in batches.
- [bg.local.goods.priceorder.negotiate](operations/bg.local.goods.priceorder.negotiate.json) - Support merchants within the whitelist to negotiate price through interfaces
- [bg.local.goods.priceorder.query](operations/bg.local.goods.priceorder.query.json) - Support merchants within the white list to query the price offer list.
- [bg.local.goods.sku.list.price.query](operations/bg.local.goods.sku.list.price.query.json) - This is an API for batch querying the latest supply prices of SKUs for local-to-local goods.
- [bg.order.amount.query](operations/bg.order.amount.query.json) - Provide the supply price information corresponding to the orders for the self-developed ERP
- [temu.local.goods.appealorder.create](operations/temu.local.goods.appealorder.create.json) - Support merchants in appealing against the recommended supply prices of low traffic goods
- [temu.local.goods.appealorder.query](operations/temu.local.goods.appealorder.query.json) - Support merchants in querying appeal orders
- [temu.local.goods.appealorder.record.query](operations/temu.local.goods.appealorder.record.query.json) - Support merchants in querying appeal order records
- [temu.local.goods.priceorder.reject](operations/temu.local.goods.priceorder.reject.json) - Support merchants in rejecting price orders
- [temu.local.goods.recommendedprice.query](operations/temu.local.goods.recommendedprice.query.json) - Support merchants in querying the recommended supply prices.
