# Stock And Shipping API

Source group: `备货及发货API组`.

## 使用范围

全托备货单、发货单、地址、物流与包裹操作（stock order, shipping order）。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## API List

- [bg.logistics.company.get](operations/bg.logistics.company.get.json) - 快递公司查询
- [bg.mall.address.add](operations/bg.mall.address.add.json) - 卖家发货地址创建
- [bg.mall.address.get](operations/bg.mall.address.get.json) - -
- [bg.predict.volume.get](operations/bg.predict.volume.get.json) - ERP在下发货单前调用该接口获取预估体积
- [bg.purchaseorder.apply](operations/bg.purchaseorder.apply.json) - 卖家创建备货单
- [bg.purchaseorder.edit](operations/bg.purchaseorder.edit.json) - [B] BG-318905 【OPEN API】支持待创建备货单修改数量
- [bg.purchaseorderv2.get](operations/bg.purchaseorderv2.get.json) - 查询卖家的备货单列表
- [bg.shiporder.cancel](operations/bg.shiporder.cancel.json) - 发货单取消
- [bg.shiporder.logistics.change](operations/bg.shiporder.logistics.change.json) - 修改发货单物流信息
- [bg.shiporder.logistics.get](operations/bg.shiporder.logistics.get.json) - 当发货方式为自行委托第三方物流时需要提供接口给到商家查询可用的物流公司名单
- [bg.shiporder.logisticsorder.match](operations/bg.shiporder.logisticsorder.match.json) - 当发货方式为自行委托第三方物流时，商家录入物流单号后需要提供接口校验所选择的物流公司是否匹配
- [bg.shiporder.package.edit](operations/bg.shiporder.package.edit.json) - 用以支持商家创建发货单之后调整对应发货单的包裹信息
- [bg.shiporder.package.get](operations/bg.shiporder.package.get.json) - 用以支持商家创建发货单之后查询发货单对应的包裹信息
- [bg.shiporder.packing.match](operations/bg.shiporder.packing.match.json) - 物流发货前置校验是否满足发货条件
- [bg.shiporder.packing.send](operations/bg.shiporder.packing.send.json) - 物流下单接口
- [bg.shiporder.receiveaddressv2.get](operations/bg.shiporder.receiveaddressv2.get.json) - 供应商创建发货单时需要先获取大仓收货地址信息
- [bg.shiporder.staging.add](operations/bg.shiporder.staging.add.json) - 加入发货台接口
- [bg.shiporder.staging.get](operations/bg.shiporder.staging.get.json) - 新增查询发货台功能
- [bg.shiporderv2.get](operations/bg.shiporderv2.get.json) - 按批次查询对应发货单信息
- [bg.shiporderv3.create](operations/bg.shiporderv3.create.json) - 当前openapi为老发货流程，需要支持创建发货单、物流下单分步操作
- [bg.shiporderv3.logisticsmatch.get](operations/bg.shiporderv3.logisticsmatch.get.json) - 卖家发货-装箱发货-获取推荐物流承运商
