---
title: Amazon Shipping API
description: "The Amazon Shipping API is designed to support outbound shipping use cases both for orders originating on Amazon-owned marketplaces as well as external channels/marketplaces. With these APIs, you can request shipping rates, create shipments, cancel shipments, and track shipments."
---

# API List
- [getRates](operations/getRates.json) (POST /shipping/v2/shipments/rates)：Returns the available shipping service offerings.
- [directPurchaseShipment](operations/directPurchaseShipment.json) (POST /shipping/v2/shipments/directPurchase)：Purchases the shipping service for a shipment using the best fit service offering. Returns purchase related details and documents.
- [purchaseShipment](operations/purchaseShipment.json) (POST /shipping/v2/shipments)：Purchases a shipping service and returns purchase related details and documents.
- [oneClickShipment](operations/oneClickShipment.json) (POST /shipping/v2/oneClickShipment)：Purchases a shipping service identifier and returns purchase-related details and documents.
- [getTracking](operations/getTracking.json) (GET /shipping/v2/tracking)：Returns tracking information for a purchased shipment.
- [getShipmentDocuments](operations/getShipmentDocuments.json) (GET /shipping/v2/shipments/{shipmentId}/documents)：Returns the shipping documents associated with a package in a shipment.
- [cancelShipment](operations/cancelShipment.json) (PUT /shipping/v2/shipments/{shipmentId}/cancel)：Cancels a purchased shipment. Returns an empty object if the shipment is successfully cancelled.
- [getAdditionalInputs](operations/getAdditionalInputs.json) (GET /shipping/v2/shipments/additionalInputs/schema)：Returns the JSON schema to use for providing additional inputs when needed to purchase a shipping offering. Call the getAdditionalInputs operation when the response to a previous call to the getRates operation indicates that additional inputs are required for the rate (shipping offering) that you want to purchase.
- [getCarrierAccountFormInputs](operations/getCarrierAccountFormInputs.json) (GET /shipping/v2/carrierAccountFormInputs)：This API will return a list of input schema required to register a shipper account with the carrier.
- [getCarrierAccounts](operations/getCarrierAccounts.json) (PUT /shipping/v2/carrierAccounts)：This API will return Get all carrier accounts for a merchant.
- [linkCarrierAccount](operations/linkCarrierAccount.json) (PUT /shipping/v2/carrierAccounts/{carrierId})：This API associates/links the specified carrier account with the merchant.
- [linkCarrierAccount](operations/linkCarrierAccount-2.json) (POST /shipping/v2/carrierAccounts/{carrierId})：This API associates/links the specified carrier account with the merchant.
- [unlinkCarrierAccount](operations/unlinkCarrierAccount.json) (PUT /shipping/v2/carrierAccounts/{carrierId}/unlink)：This API Unlink the specified carrier account with the merchant.
- [generateCollectionForm](operations/generateCollectionForm.json) (POST /shipping/v2/collectionForms)：This API Call to generate the collection form.
- [getCollectionFormHistory](operations/getCollectionFormHistory.json) (PUT /shipping/v2/collectionForms/history)：This API Call to get the history of the previously generated collection forms.
- [getUnmanifestedShipments](operations/getUnmanifestedShipments.json) (PUT /shipping/v2/unmanifestedShipments)：This API Get all unmanifested carriers with shipment locations. Any locations which has unmanifested shipments with an eligible carrier for manifesting shall be returned.
- [getCollectionForm](operations/getCollectionForm.json) (GET /shipping/v2/collectionForms/{collectionFormId})：This API reprint a collection form.
- [getAccessPoints](operations/getAccessPoints.json) (GET /shipping/v2/accessPoints)：Returns a list of access points in proximity of input postal code.
- [submitNdrFeedback](operations/submitNdrFeedback.json) (POST /shipping/v2/ndrFeedback)：This API submits the NDR (Non-delivery Report) Feedback for any eligible shipment.
- [createClaim](operations/createClaim.json) (POST /shipping/v2/claims)：This API will be used to create claim for single eligible shipment.
