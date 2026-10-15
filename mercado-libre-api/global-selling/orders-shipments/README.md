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

## Operation models

| Host | Method | Path | Source pages | JSON |
|---|---|---|---:|---|
| `api.mercadolibre.com` | GET | `/marketplace` | 1 | [JSON](./operations/get-b049eb85d108.json) |
| `api.mercadolibre.com` | GET | `/marketplace/items/{item_id}/shipping_compensation` | 1 | [JSON](./operations/get-a62970c21f46.json) |
| `api.mercadolibre.com` | GET | `/marketplace/items/{item_id}/shipping_options/cost` | 1 | [JSON](./operations/get-17db246bbf02.json) |
| `api.mercadolibre.com` | GET | `/marketplace/orders/pack/{family_pack_id}` | 1 | [JSON](./operations/get-a7d0a2ce8683.json) |
| `api.mercadolibre.com` | GET | `/marketplace/orders/pack/{id}` | 3 | [JSON](./operations/get-9aef4c77e23a.json) |
| `api.mercadolibre.com` | GET | `/marketplace/orders/pack/{pack_id}` | 2 | [JSON](./operations/get-fa353b27d131.json) |
| `api.mercadolibre.com` | GET | `/marketplace/orders/search` | 4 | [JSON](./operations/get-cb7901029f19.json) |
| `api.mercadolibre.com` | GET | `/marketplace/orders/{order_id}/invoice` | 2 | [JSON](./operations/get-960974faf013.json) |
| `api.mercadolibre.com` | GET | `/marketplace/sellers/{seller_id}/working_days` | 1 | [JSON](./operations/get-98c96e6f773e.json) |
| `api.mercadolibre.com` | GET | `/marketplace/shipments/dispatch_preferences/carriers` | 1 | [JSON](./operations/get-e0e3e2fdf686.json) |
| `api.mercadolibre.com` | GET | `/marketplace/shipments/dispatch_preferences/pick_up_addresses` | 1 | [JSON](./operations/get-99cfc6644a06.json) |
| `api.mercadolibre.com` | GET | `/marketplace/shipments/{shipment_id}/carrier` | 1 | [JSON](./operations/get-da92636478e8.json) |
| `api.mercadolibre.com` | GET | `/marketplace/shipments/{shipment_id}/compensation_costs` | 1 | [JSON](./operations/get-202443ee946f.json) |
| `api.mercadolibre.com` | GET | `/marketplace/shipments/{shipment_id}/costs` | 1 | [JSON](./operations/get-f929b18055d8.json) |
| `api.mercadolibre.com` | GET | `/marketplace/shipments/{shipment_id}/history` | 1 | [JSON](./operations/get-a023e54b22db.json) |
| `api.mercadolibre.com` | GET | `/marketplace/shipments/{shipment_id}/items` | 1 | [JSON](./operations/get-35c433d6c16c.json) |
| `api.mercadolibre.com` | GET | `/marketplace/shipments/{shipment_id}/lead_time` | 1 | [JSON](./operations/get-9ffd67949317.json) |
| `api.mercadolibre.com` | GET | `/marketplace/shipments/{shipment_id}/sla` | 1 | [JSON](./operations/get-abe6ca4cdae4.json) |
| `api.mercadolibre.com` | GET | `/orders/{order_id}` | 1 | [JSON](./operations/get-38ac2d327b47.json) |
| `api.mercadolibre.com` | GET | `/orders/{order_id}/shipments` | 1 | [JSON](./operations/get-a7d2acc2422e.json) |
| `api.mercadolibre.com` | GET | `/shipments/{shipment_id}/orders` | 1 | [JSON](./operations/get-cb3ba1ade08a.json) |
| `api.mercadolibre.com` | GET | `/sites/MLM/payment_methods` | 1 | [JSON](./operations/get-476971c4837c.json) |
| `api.mercadolibre.com` | GET | `/sites/MLM/payment_methods/visa` | 1 | [JSON](./operations/get-09613497e8d1.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/shipping_options/cost` | 1 | [JSON](./operations/get-be20c18aba6c.json) |
| `api.mercadolibre.com` | POST | `/marketplace/orders/{order_id}/attributes` | 1 | [JSON](./operations/post-6b71c3b60b00.json) |
| `api.mercadolibre.com` | POST | `/marketplace/shipments/dispatch_preferences/pick_up_addresses` | 1 | [JSON](./operations/post-1cae2c9d849e.json) |
| `api.mercadolibre.com` | POST | `/marketplace/shipments/{shipment_id}/split` | 1 | [JSON](./operations/post-b72b6d9c88e5.json) |
| `api.mercadolibre.com` | POST | `/marketplace/shipments/{shipment_id}/tracking/status` | 3 | [JSON](./operations/post-8e2e802e11e4.json) |
| `api.mercadolibre.com` | PUT | `/marketplace/sellers/{$seller_id}/working_days` | 1 | [JSON](./operations/put-71f839311819.json) |
| `api.mercadolibre.com` | PUT | `/marketplace/shipments/dispatch_preferences/carriers/cainiao` | 3 | [JSON](./operations/put-5c1fedc2018e.json) |
| `api.mercadolibre.com` | PUT | `/marketplace/shipments/dispatch_preferences/carriers/mailamericas` | 1 | [JSON](./operations/put-9bd4239e8fcd.json) |
| `api.mercadolibre.com` | PUT | `/marketplace/shipments/dispatch_preferences/carriers/{carrier_name}` | 2 | [JSON](./operations/put-9d115c720d0f.json) |
| `cbt-shipping-op-api.melisystems.com` | GET | `/marketplace/shipments/dispatch_preferences/return_address` | 1 | [JSON](./operations/get-15fbd1fe924f.json) |
| `cbt-shipping-op-api.melisystems.com` | POST | `/marketplace/shipments/dispatch_preferences/return_address` | 1 | [JSON](./operations/post-1e8a2a1f9146.json) |
