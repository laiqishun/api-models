---
title: Selling Partner API for Delivery Shipment Invoicing
description: "The Selling Partner API for Delivery Shipment Invoicing helps you programmatically retrieve shipment invoice information in the Brazil marketplace for a selling partner’s orders."
---

# API List
- [submitInvoice](operations/submitInvoice.json) (POST /delivery/2022-07-01/invoice)：Submits a shipment invoice for a given order or shipment. You must specify either an `orderId` or `shipmentId` as query parameter. If both parameters are supplied, `orderId` takes precedence over `shipmentId`.
- [getInvoiceStatus](operations/getInvoiceStatus.json) (GET /delivery/2022-07-01/invoice/status)：Returns the invoice status for the order or shipment you specify. You must specify either an `orderId` or `shipmentId` as query parameter. If both parameters are supplied, `orderId` takes precedence over `shipmentId`.
