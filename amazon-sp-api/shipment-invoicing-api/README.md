---
title: Selling Partner API for Shipment Invoicing
description: "The Selling Partner API for Shipment Invoicing helps you programmatically retrieve shipment invoice information in the Brazil marketplace for a selling partner’s Fulfillment by Amazon (FBA) orders."
---

# API List
- [getShipmentDetails](operations/getShipmentDetails.json) (GET /fba/outbound/brazil/v0/shipments/{shipmentId})：Returns the shipment details required to issue an invoice for the specified shipment.
- [submitInvoice](operations/submitInvoice.json) (POST /fba/outbound/brazil/v0/shipments/{shipmentId}/invoice)：Submits a shipment invoice document for a given shipment.
- [getInvoiceStatus](operations/getInvoiceStatus.json) (GET /fba/outbound/brazil/v0/shipments/{shipmentId}/invoice/status)：Returns the invoice status for the shipment you specify.
