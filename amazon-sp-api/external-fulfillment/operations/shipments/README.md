---
title: The Selling Partner API for Amazon External Fulfillment Shipments Processing
description: "You can use the External Fulfillment Shipments API to retrieve, manage, and track shipments processed through Amazon's external fulfillment network. Use this API to get shipment details, monitor status changes, and access fulfillment requirements."
---

# API List
- [getShipments](getShipments.json) (GET /externalFulfillment/2024-09-11/shipments)：Get a list of shipments created for the seller in the status you specify. Shipments can be further filtered based on the fulfillment node or the time of the shipments' last update.
- [getShipment](getShipment.json) (GET /externalFulfillment/2024-09-11/shipments/{shipmentId})：Get a single shipment with the ID you specify.
- [processShipment](processShipment.json) (POST /externalFulfillment/2024-09-11/shipments/{shipmentId})：Confirm or reject the specified shipment.
- [createPackages](createPackages.json) (POST /externalFulfillment/2024-09-11/shipments/{shipmentId}/packages)：Provide details about the packages in the specified shipment.
- [updatePackage](updatePackage.json) (PUT /externalFulfillment/2024-09-11/shipments/{shipmentId}/packages/{packageId})：Updates the details about the packages that will be used to fulfill the specified shipment.
- [updatePackageStatus](updatePackageStatus.json) (PATCH /externalFulfillment/2024-09-11/shipments/{shipmentId}/packages/{packageId})：Updates the status of the packages.
- [retrieveShippingOptions](retrieveShippingOptions.json) (GET /externalFulfillment/2024-09-11/shipments/{shipmentId}/shippingOptions)：Get a list of shipping options for a package in a shipment given the shipment's marketplace and channel. If the marketplace and channel have a pre-determined shipping option, then this operation returns an empty response.
- [generateInvoice](generateInvoice.json) (POST /externalFulfillment/2024-09-11/shipments/{shipmentId}/invoice)：Get invoices for the shipment you specify.
- [retrieveInvoice](retrieveInvoice.json) (GET /externalFulfillment/2024-09-11/shipments/{shipmentId}/invoice)：Retrieve invoices for the shipment you specify.
- [generateShipLabels](generateShipLabels.json) (PUT /externalFulfillment/2024-09-11/shipments/{shipmentId}/shipLabels)：Generate and retrieve all shipping labels for one or more packages in the shipment you specify.
