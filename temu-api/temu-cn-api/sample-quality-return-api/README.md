# Sample Quality Return API

Source group: `寄样/质检/退供API组`.

## 使用范围

样品单、质检单与供应链退供包裹（sample, quality inspection, supplier return）。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## API List

- [bg.goods.qualityinspection.get](operations/bg.goods.qualityinspection.get.json) - 新增卖家中心直接结果查询接口，用于卖家跟进不合格质检备货单，优化生产
- [bg.goods.qualityinspectiondetail.get](operations/bg.goods.qualityinspectiondetail.get.json) - 备货单质检详细信息，用于卖家跟进不合格质检备货单，优化生产
- [bg.refund.returnpackage.get](operations/bg.refund.returnpackage.get.json) - 当前开平外部商家对接，需要查询发货至仓库，被退货的数据情况，确保自有库存数据准确
- [bg.refund.returnpackagedetail.get](operations/bg.refund.returnpackagedetail.get.json) - 当前开平外部商家对接，需要查询发货至仓库，被退货的数据情况，确保自有库存数据准确
- [bg.refund.returnpackagelist.get](operations/bg.refund.returnpackagelist.get.json) - 当前开平外部商家对接，需要查询发货至仓库，被退货的数据情况，确保自有库存数据准确
- [bg.sample.order.get](operations/bg.sample.order.get.json) - 寄样单查询
- [bg.sample.send](operations/bg.sample.send.json) - 寄样发货
