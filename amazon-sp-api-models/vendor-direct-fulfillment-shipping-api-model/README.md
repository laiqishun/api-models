---
title: Selling Partner API for Direct Fulfillment Shipping
description: "Use the Selling Partner API for Direct Fulfillment Shipping to access a direct fulfillment vendor's shipping data."
---

# API List
- [getShippingLabels](operations/getShippingLabels.json) (GET /vendor/directFulfillment/shipping/2021-12-28/shippingLabels)：Returns a list of shipping labels created during the time frame that you specify. Use the `createdAfter` and `createdBefore` parameters to define the time frame. You must use both of these parameters. The date range to search must not be more than seven days.
- [submitShippingLabelRequest](operations/submitShippingLabelRequest.json) (POST /vendor/directFulfillment/shipping/2021-12-28/shippingLabels)：Creates a shipping label for a purchase order and returns a `transactionId` for reference.
- [getShippingLabel](operations/getShippingLabel.json) (GET /vendor/directFulfillment/shipping/2021-12-28/shippingLabels/{purchaseOrderNumber})：Returns a shipping label for the `purchaseOrderNumber` that you specify.
- [createShippingLabels](operations/createShippingLabels.json) (POST /vendor/directFulfillment/shipping/2021-12-28/shippingLabels/{purchaseOrderNumber})：Creates shipping labels for a purchase order and returns the labels.
- [submitShipmentConfirmations](operations/submitShipmentConfirmations.json) (POST /vendor/directFulfillment/shipping/2021-12-28/shipmentConfirmations)：Submits one or more shipment confirmations for vendor orders.
- [submitShipmentStatusUpdates](operations/submitShipmentStatusUpdates.json) (POST /vendor/directFulfillment/shipping/2021-12-28/shipmentStatusUpdates)：This operation is only to be used by Vendor-Own-Carrier (VOC) vendors. Calling this API submits a shipment status update for the package that a vendor has shipped. It will provide the Amazon customer visibility on their order, when the package is outside of Amazon Network visibility.
- [getCustomerInvoices](operations/getCustomerInvoices.json) (GET /vendor/directFulfillment/shipping/2021-12-28/customerInvoices)：Returns a list of customer invoices created during a time frame that you specify. You define the time frame using the createdAfter and createdBefore parameters. You must use both of these parameters. The date range to search must be no more than 7 days.
- [getCustomerInvoice](operations/getCustomerInvoice.json) (GET /vendor/directFulfillment/shipping/2021-12-28/customerInvoices/{purchaseOrderNumber})：Returns a customer invoice based on the purchaseOrderNumber that you specify.
- [getPackingSlips](operations/getPackingSlips.json) (GET /vendor/directFulfillment/shipping/2021-12-28/packingSlips)：Returns a list of packing slips for the purchase orders that match the criteria specified. Date range to search must not be more than 7 days.
- [getPackingSlip](operations/getPackingSlip.json) (GET /vendor/directFulfillment/shipping/2021-12-28/packingSlips/{purchaseOrderNumber})：Returns a packing slip based on the purchaseOrderNumber that you specify.
- [createContainerLabel](operations/createContainerLabel.json) (POST /vendor/directFulfillment/shipping/2021-12-28/containerLabel)：Creates a container (pallet) label for the associated shipment package.
