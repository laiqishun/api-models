# Logistics API

Source group: `5、Logistics`.

## 使用范围

区域物流商、物流服务、仓库与物流类型（carrier, shipping service, warehouse）。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## API List

- [bg.logistics.companies.get](operations/bg.logistics.companies.get.json) - Obtain full logistics providers that support shipping at the corresponding regoin
- [bg.logistics.shippingservices.get](operations/bg.logistics.shippingservices.get.json) - The bg.logistics.shippingservices.get interface is for sellers to retrieve supported shipping carriers based on package dimensions and weight, which allows sellers to quickly de...
- [bg.logistics.warehouse.list.get](operations/bg.logistics.warehouse.list.get.json) - Sellers can use this API to obtain the shop's warehouse information.
- [temu.logistics.shiplogisticstype.get](operations/temu.logistics.shiplogisticstype.get.json) - You can get all online ship logistics type information from this api. After that, they can call "bg.logistics.shipment.create" to buy-shipping on Temu. Once you choose to buy-sh...
