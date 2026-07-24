# Order API

Source group: `3、Order`.

## API List

- [bg.order.combinedshipment.list.get](operations/bg.order.combinedshipment.list.get.json) - The bg.order.combinedshipment.list.get interface is designed for merchants to retrieve combined shipping groups including lists of parent orders that can be combined for shipping.
- [bg.order.customization.get](operations/bg.order.customization.get.json) - Self developed sellers and third-party ISVs obtain customized product content information in bulk through Open API
- [bg.order.decryptshippinginfo.get](operations/bg.order.decryptshippinginfo.get.json) - bg.order.decryptshippinginfo.get interface is designed to retrieve sensitive shipping address information for a specific order.
- [bg.order.detail.v2.get](operations/bg.order.detail.v2.get.json) - The bg.order.detail.v2.get interface is designed for merchants to retrieve detailed information about a specific order within their respective stores. This functionality provide...
- [bg.order.list.v2.get](operations/bg.order.list.v2.get.json) - The bg.order.list.v2.get interface is designed for support batch return of corresponding order lists based on filtering criteria.
- [bg.order.shippinginfo.v2.get](operations/bg.order.shippinginfo.v2.get.json) - The bg.order.shippinginfo.get.V2 interface is designed to retrieve shipping address information for a specific order. This functionality is crucial for merchants and logistics p...
- [temu.order.cancel.appeal.apply](operations/temu.order.cancel.appeal.apply.json) - Support merchants to initiate cancellation requests through the interface
- [temu.order.cancel.appeal.result.get](operations/temu.order.cancel.appeal.result.get.json) - Merchant queries the status of cancellation order appeal records
- [temu.order.cancel.outofstock.apply](operations/temu.order.cancel.outofstock.apply.json) - The user takes the initiative to initiate a stock-out situation, which will be submitted to the risk control department for review.
- [temu.order.cancel.outofstock.result.get](operations/temu.order.cancel.outofstock.result.get.json) - After applying for out-of-stock, since out-of-stock itself is an asynchronous operation, you need to obtain the latest out-of-stock review status through the query interface
