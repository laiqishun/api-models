# Orders & Shipments

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Orders](https://global-selling.mercadolibre.com/devsite/manage-orders-cbt) | 8 | 0 | modeled |
| [Official: Packs](https://global-selling.mercadolibre.com/devsite/packs) | 2 | 0 | modeled |
| [Official: Shipments](https://global-selling.mercadolibre.com/devsite/manage-shipments) | 20 | 0 | modeled |
| [Official: Compensations](https://global-selling.mercadolibre.com/devsite/compensations) | 2 | 0 | modeled |
| [Official: Dispatch Information](https://global-selling.mercadolibre.com/devsite/dispatch-information) | 8 | 0 | modeled |
| [Official: Export evidence](https://global-selling.mercadolibre.com/devsite/export-evidence) | 1 | 0 | modeled |

## API List

- [addProductInformation](operations/addProductInformation.json) (POST /marketplace/orders/{order_id}/attributes)：Add product information [Official](https://global-selling.mercadolibre.com/devsite/manage-orders-cbt)
- [associatePickUpAddress](operations/associatePickUpAddress.json) (POST /marketplace/shipments/dispatch_preferences/pick_up_addresses)：Associate pick-up address [Official](https://global-selling.mercadolibre.com/devsite/dispatch-information)
- [associatePickUpAsDispatchPreference](operations/associatePickUpAsDispatchPreference.json) (PUT /marketplace/shipments/dispatch_preferences/carriers/cainiao)：Associate Pick-Up as dispatch preference [Official](https://global-selling.mercadolibre.com/devsite/dispatch-information)
- [checkIfPackWasSplit](operations/checkIfPackWasSplit.json) (GET /marketplace/orders/pack/{family_pack_id})：4. Check if the Pack Was Split [Official](https://global-selling.mercadolibre.com/devsite/manage-shipments)
- [createOrUpdateReturnAddressUpsert](operations/createOrUpdateReturnAddressUpsert.json) (POST /marketplace/shipments/dispatch_preferences/return_address)：POST — Create or Update Return Address (Upsert) [Official](https://global-selling.mercadolibre.com/devsite/dispatch-information)
- [getByItemIdShippingCompensation](operations/getByItemIdShippingCompensation.json) (GET /marketplace/items/{item_id}/shipping_compensation)：Parameters [Official](https://global-selling.mercadolibre.com/devsite/compensations)
- [getByOrderIdShipments](operations/getByOrderIdShipments.json) (GET /orders/{order_id}/shipments)：Call [Official](https://global-selling.mercadolibre.com/devsite/manage-orders-cbt)
- [getByShipmentIdCompensationCosts](operations/getByShipmentIdCompensationCosts.json) (GET /marketplace/shipments/{shipment_id}/compensation_costs)：Parameters [Official](https://global-selling.mercadolibre.com/devsite/compensations)
- [getByShipmentIdOrders](operations/getByShipmentIdOrders.json) (GET /shipments/{shipment_id}/orders)：Call [Official](https://global-selling.mercadolibre.com/devsite/manage-shipments)
- [getByShipmentIdSla](operations/getByShipmentIdSla.json) (GET /marketplace/shipments/{shipment_id}/sla)：Call [Official](https://global-selling.mercadolibre.com/devsite/manage-shipments)
- [getCarrierInformation](operations/getCarrierInformation.json) (GET /marketplace/shipments/{shipment_id}/carrier)：Get carrier information [Official](https://global-selling.mercadolibre.com/devsite/manage-shipments)
- [getItemShippingCost](operations/getItemShippingCost.json) (GET /marketplace/items/{item_id}/shipping_options/cost)：Item´s shipping cost [Official](https://global-selling.mercadolibre.com/devsite/manage-shipments)
- [getLeadTime](operations/getLeadTime.json) (GET /marketplace/shipments/{shipment_id}/lead_time)：Get lead time [Official](https://global-selling.mercadolibre.com/devsite/manage-shipments)
- [getMlmPaymentMethods](operations/getMlmPaymentMethods.json) (GET /sites/MLM/payment_methods)：Returns data for a payment [Official](https://global-selling.mercadolibre.com/devsite/manage-orders-cbt)
- [getOrderInvoice](operations/getOrderInvoice.json) (GET /marketplace/orders/{order_id}/invoice)：Get an order invoice [Official](https://global-selling.mercadolibre.com/devsite/manage-orders-cbt)
- [getOrdersByOrderId](operations/getOrdersByOrderId.json) (GET /orders/{order_id})：Example response with gross_price [Official](https://global-selling.mercadolibre.com/devsite/manage-orders-cbt)
- [getPackByPackId](operations/getPackByPackId.json) (GET /marketplace/orders/pack/{pack_id})：View cart sales [Official](https://global-selling.mercadolibre.com/devsite/packs)
- [getPaymentMethod](operations/getPaymentMethod.json) (GET /sites/MLM/payment_methods/visa)：Get payment method [Official](https://global-selling.mercadolibre.com/devsite/manage-orders-cbt)
- [getPickUpAddress](operations/getPickUpAddress.json) (GET /marketplace/shipments/dispatch_preferences/pick_up_addresses)：Get pick-up address [Official](https://global-selling.mercadolibre.com/devsite/dispatch-information)
- [getShipmentCost](operations/getShipmentCost.json) (GET /marketplace/shipments/{shipment_id}/costs)：Shipment cost [Official](https://global-selling.mercadolibre.com/devsite/manage-shipments)
- [getShipmentItems](operations/getShipmentItems.json) (GET /marketplace/shipments/{shipment_id}/items)：Get shipment items [Official](https://global-selling.mercadolibre.com/devsite/manage-shipments)
- [getShippingOptionsCost](operations/getShippingOptionsCost.json) (GET /users/{user_id}/shipping_options/cost)：Item´s shipping cost [Official](https://global-selling.mercadolibre.com/devsite/manage-shipments)
- [getStatusHistory](operations/getStatusHistory.json) (GET /marketplace/shipments/{shipment_id}/history)：Get status history [Official](https://global-selling.mercadolibre.com/devsite/manage-shipments)
- [getWorkingDays](operations/getWorkingDays.json) (GET /marketplace/sellers/{seller_id}/working_days)：Get Working Days [Official](https://global-selling.mercadolibre.com/devsite/manage-shipments)
- [informStatus](operations/informStatus.json) (POST /marketplace/shipments/{shipment_id}/tracking/status)：Inform Status [Official](https://global-selling.mercadolibre.com/devsite/manage-shipments)
- [listExportDeclarationsByMerchant](operations/listExportDeclarationsByMerchant.json) (GET /marketplace)：GET — List Export Declarations by Merchant [Official](https://global-selling.mercadolibre.com/devsite/export-evidence)
- [postByShipmentIdSplit](operations/postByShipmentIdSplit.json) (POST /marketplace/shipments/{shipment_id}/split)：Possible values in the "reason" field [Official](https://global-selling.mercadolibre.com/devsite/manage-shipments)
- [putCarriersByCarrierName](operations/putCarriersByCarrierName.json) (PUT /marketplace/shipments/dispatch_preferences/carriers/{carrier_name})：Associate Pick-Up as dispatch preference [Official](https://global-selling.mercadolibre.com/devsite/dispatch-information)
- [putCarriersMailamericas](operations/putCarriersMailamericas.json) (PUT /marketplace/shipments/dispatch_preferences/carriers/mailamericas)：Possible errors when associating Drop Off Agency as dispatch preference [Official](https://global-selling.mercadolibre.com/devsite/dispatch-information)
- [retrieveReturnAddress](operations/retrieveReturnAddress.json) (GET /marketplace/shipments/dispatch_preferences/return_address)：GET — Retrieve Return Address [Official](https://global-selling.mercadolibre.com/devsite/dispatch-information)
- [searchDispatchPreferences](operations/searchDispatchPreferences.json) (GET /marketplace/shipments/dispatch_preferences/carriers)：Search dispatch preferences [Official](https://global-selling.mercadolibre.com/devsite/dispatch-information)
- [searchOrdersBySeller](operations/searchOrdersBySeller.json) (GET /marketplace/orders/search)：Search the orders by seller [Official](https://global-selling.mercadolibre.com/devsite/manage-orders-cbt)
- [updateWorkingDays](operations/updateWorkingDays.json) (PUT /marketplace/sellers/{$seller_id}/working_days)：Update Working Days [Official](https://global-selling.mercadolibre.com/devsite/manage-shipments)
- [viewCartSales](operations/viewCartSales.json) (GET /marketplace/orders/pack/{id})：View cart sales [Official](https://global-selling.mercadolibre.com/devsite/packs)
