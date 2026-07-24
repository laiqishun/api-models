# Logistics API

Source group: `6、Logistics`.

## API List

- [bg.logistics.companies.get](operations/bg.logistics.companies.get.json) - Obtain full logistics providers that support shipping at the corresponding regoin
- [bg.logistics.shippingservices.get](operations/bg.logistics.shippingservices.get.json) - The bg.logistics.shippingservices.get interface is for sellers to retrieve supported shipping carriers based on package dimensions and weight, which allows sellers to quickly de...
- [bg.logistics.warehouse.list.get](operations/bg.logistics.warehouse.list.get.json) - Sellers can use this API to obtain the shop's warehouse information.
- [temu.logistics.candidate.scanform.list.get](operations/temu.logistics.candidate.scanform.list.get.json) - The "temu.logistics.candidate.scanform.list.get" interface is for sellers to get lists of package numbers that can be used to generate a scanform based on shipCompanyId and ware...
- [temu.logistics.scanform.create](operations/temu.logistics.scanform.create.json) - The "temu.logistics.scanform.create" interface is for sellers to create scanforms according to the check conditions after entering lists packages.
- [temu.logistics.scanform.document.get](operations/temu.logistics.scanform.document.get.json) - The "temu.logistics.scanform.document.get" interface is for sellers to get scanform documents with package numbers.
- [temu.logistics.scanform.get](operations/temu.logistics.scanform.get.json) - The "temu.logistics.scanform.get" interface is for sellers to get detail information of scanforms such as status of the scanform.
- [temu.logistics.shiplogisticstype.get](operations/temu.logistics.shiplogisticstype.get.json) - You can get all online ship logistics type information from this api. After that, they can call "bg.logistics.shipment.create" to buy-shipping on Temu. Once you choose to buy-sh...
