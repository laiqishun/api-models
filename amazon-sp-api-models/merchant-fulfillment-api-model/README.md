---
title: Selling Partner API for Merchant Fulfillment
description: "With the Selling Partner API for Merchant Fulfillment, you can build applications that sellers can use to purchase shipping for non-Prime and Prime orders using Amazon's Buy Shipping Services."
---

# API List
- [getEligibleShipmentServices](operations/getEligibleShipmentServices.json) (POST /mfn/v0/eligibleShippingServices)：Returns a list of shipping service offers that satisfy the specified shipment request details.
- [getShipment](operations/getShipment.json) (GET /mfn/v0/shipments/{shipmentId})：Returns the shipment information for an existing shipment.
- [cancelShipment](operations/cancelShipment.json) (DELETE /mfn/v0/shipments/{shipmentId})：Cancel the shipment indicated by the specified shipment identifier.
- [createShipment](operations/createShipment.json) (POST /mfn/v0/shipments)：Create a shipment with the information provided.
- [getAdditionalSellerInputs](operations/getAdditionalSellerInputs.json) (POST /mfn/v0/additionalSellerInputs)：Gets a list of additional seller inputs required for a ship method. This is generally used for international shipping.
