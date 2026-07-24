# Fulfillment API

Source group: `7、Fulfillment`.

## 使用范围

区域发货、面单、包裹确认、揽收与履约（fulfillment, shipment, label, pickup）。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## API List

- [bg.logistics.shipment.create](operations/bg.logistics.shipment.create.json) - The bg.logistics.shipment.create interface is for sellers to place online logistics orders and receive package numbers, which enables to effortlessly place logistics orders with...
- [bg.logistics.shipment.document.get](operations/bg.logistics.shipment.document.get.json) - The bg.logistics.shipment.document.get interface is for sellers to obtain the express delivery waybill which has been fulfilled successfully by Temu-integrated channel so as to ...
- [bg.logistics.shipment.result.get](operations/bg.logistics.shipment.result.get.json) - The bg.logistics.shipment.result.get interface is for sellers to query the result of placing online logistics orders, with the shipping label status including in-progress{0}, su...
- [bg.logistics.shipment.shippingtype.update](operations/bg.logistics.shipment.shippingtype.update.json) - The bg.logistics.shipment.shippingtype.update interface is used by sellers to update logistics tracking numbers, supporting the following scenarios: non-integrated logistics upd...
- [bg.logistics.shipment.sub.confirm](operations/bg.logistics.shipment.sub.confirm.json) - The bg.logistics.shipment.sub.confirm interface should only be used in scenarios where the smallest sku needs to be shipped as split packages, and can append the sub-parcel info...
- [bg.logistics.shipment.update](operations/bg.logistics.shipment.update.json) - The bg.logistics.shipment.update interface is for sellers to create shipment logistics orders later, and to re-order online if the order fails.
- [bg.logistics.shipment.v2.confirm](operations/bg.logistics.shipment.v2.confirm.json) - The bg.logistic.shipment.v2.confirm interface is designed to synchronize and return order fulfillment information through this interface. Switch the order status from pending sh...
- [bg.logistics.shipment.v2.get](operations/bg.logistics.shipment.v2.get.json) - The bg.logistics.shipment.v2.get interface is for sellers to verify shipped info after self-fulfillment.
- [bg.logistics.shipped.package.confirm](operations/bg.logistics.shipped.package.confirm.json) - The bg.logistics.shipped.package.confirm interface is for sellers to support batch conversion of packages that have been fulfilled successfully by Temu-integrated channel but no...
- [bg.order.unshipped.package.get](operations/bg.order.unshipped.package.get.json) - The bg.order.unshipped.package.get interface is for sellers to query information about packages that have been fulfilled successfully by Temu-integrated channel.
- [temu.logistics.label.list.get](operations/temu.logistics.label.list.get.json) - You can use this interface to query the package information that has been fulfilled using the temu shipping form.
- [temu.logistics.self.delivery.pod.audit.result.get](operations/temu.logistics.self.delivery.pod.audit.result.get.json) - Self-delivery merchants query POD upload record
- [temu.logistics.self.delivery.pod.upload](operations/temu.logistics.self.delivery.pod.upload.json) - Self-delivery merchants upload POD
- [temu.logistics.self.delivery.pod.upload.signature.query](operations/temu.logistics.self.delivery.pod.upload.signature.query.json) - Self-delivery merchants upload POD
- [temu.logistics.shipment.pickup.reservation.cancel](operations/temu.logistics.shipment.pickup.reservation.cancel.json) - The temu.logistics.shipment.pickup.reservation.cancel API enables sellers to cancel reservationSn.
- [temu.logistics.shipment.pickup.reservation.create](operations/temu.logistics.shipment.pickup.reservation.create.json) - The temu.logistics.shipment.pickup.reservation.create API enables sellers to schedule package pickups. When multiple packages meet the criteria for consolidated pickup appointme...
- [temu.logistics.shipment.pickup.reservation.result.get](operations/temu.logistics.shipment.pickup.reservation.result.get.json) - The temu.logistics.shipment.pickup.reservation.result.get API retrieves reservation details for the current package. When multiple packages correspond to one reservationSn, the ...
- [temu.track.trackinginfo.get](operations/temu.track.trackinginfo.get.json) - Logistics trajectory detail query interface
