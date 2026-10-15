# Fulfillmnent (FBM)

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Replenishment Plans Inbound](https://global-selling.mercadolibre.com/devsite/replenishment-plans-inbound) | 1 | 0 | modeled |
| [Official: Fulfilment Inbound Creation](https://global-selling.mercadolibre.com/devsite/fulfilment-inbound-creation) | 2 | 0 | modeled |
| [Official: Fulfillment stock](https://global-selling.mercadolibre.com/devsite/fulfillment-stock-gs) | 7 | 0 | modeled |

## Operation models

| Host | Method | Path | Source pages | JSON |
|---|---|---|---:|---|
| `api.mercadolibre.com` | GET | `/marketplace/fbm/inbounds/process/{process_id}` | 2 | [JSON](./operations/get-96269fcf05aa.json) |
| `api.mercadolibre.com` | GET | `/marketplace/fbm/user-products/{id}/replenishment` | 1 | [JSON](./operations/get-8bab5b5ef14e.json) |
| `api.mercadolibre.com` | GET | `/marketplace/inventories/TKQK18938/stock/fulfillment` | 1 | [JSON](./operations/get-c1ea372cbc3e.json) |
| `api.mercadolibre.com` | GET | `/marketplace/inventories/YLXH33638/stock/fulfillment` | 1 | [JSON](./operations/get-10b049faab6c.json) |
| `api.mercadolibre.com` | GET | `/marketplace/inventories/{inventory_id}/stock/fulfillment` | 2 | [JSON](./operations/get-138dd47f322d.json) |
| `api.mercadolibre.com` | GET | `/marketplace/stock/fulfillment/operations/search` | 2 | [JSON](./operations/get-23c0f7912f5e.json) |
| `api.mercadolibre.com` | GET | `/marketplace/stock/fulfillment/operations/{id}` | 1 | [JSON](./operations/get-754682403c2c.json) |
| `api.mercadolibre.com` | GET | `/marketplace/stock/fulfillment/operations/{operation_id}` | 1 | [JSON](./operations/get-ed53eab06ffb.json) |
| `api.mercadolibre.com` | POST | `/marketplace/fbm/inbounds` | 2 | [JSON](./operations/post-9b447b97cb28.json) |
