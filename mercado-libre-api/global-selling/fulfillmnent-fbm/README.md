# Fulfillmnent (FBM)

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Replenishment Plans Inbound](https://global-selling.mercadolibre.com/devsite/replenishment-plans-inbound) | 1 | 0 | modeled |
| [Official: Fulfilment Inbound Creation](https://global-selling.mercadolibre.com/devsite/fulfilment-inbound-creation) | 2 | 0 | modeled |
| [Official: Fulfillment stock](https://global-selling.mercadolibre.com/devsite/fulfillment-stock-gs) | 7 | 0 | modeled |

## API List

- [checkDetailStockNotAvailable](operations/checkDetailStockNotAvailable.json) (GET /marketplace/inventories/YLXH33638/stock/fulfillment)：Check the detail of stock not available [Official](https://global-selling.mercadolibre.com/devsite/fulfillment-stock-gs)
- [createInbound](operations/createInbound.json) (POST /marketplace/fbm/inbounds)：Create Inbound [Official](https://global-selling.mercadolibre.com/devsite/fulfilment-inbound-creation)
- [getByIdReplenishment](operations/getByIdReplenishment.json) (GET /marketplace/fbm/user-products/{id}/replenishment)：Examples [Official](https://global-selling.mercadolibre.com/devsite/replenishment-plans-inbound)
- [getOperationsById](operations/getOperationsById.json) (GET /marketplace/stock/fulfillment/operations/{id})：Parameters [Official](https://global-selling.mercadolibre.com/devsite/fulfillment-stock-gs)
- [getOperationsByOperationId](operations/getOperationsByOperationId.json) (GET /marketplace/stock/fulfillment/operations/{operation_id})：Parameters [Official](https://global-selling.mercadolibre.com/devsite/fulfillment-stock-gs)
- [getOperationsSearch](operations/getOperationsSearch.json) (GET /marketplace/stock/fulfillment/operations/search)：Parameters [Official](https://global-selling.mercadolibre.com/devsite/fulfillment-stock-gs)
- [getProcessStatus](operations/getProcessStatus.json) (GET /marketplace/fbm/inbounds/process/{process_id})：Get Process Status [Official](https://global-selling.mercadolibre.com/devsite/fulfilment-inbound-creation)
- [getStockFulfillment](operations/getStockFulfillment.json) (GET /marketplace/inventories/{inventory_id}/stock/fulfillment)：Parameters [Official](https://global-selling.mercadolibre.com/devsite/fulfillment-stock-gs)
- [getFulfillmentStockByInventoryId](operations/getFulfillmentStockByInventoryId.json) (GET /marketplace/inventories/TKQK18938/stock/fulfillment)：Parameters [Official](https://global-selling.mercadolibre.com/devsite/fulfillment-stock-gs)
