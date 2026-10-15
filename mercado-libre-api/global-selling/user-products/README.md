# User Products

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Introduction](https://global-selling.mercadolibre.com/devsite/user-products-cbt) | 1 | 0 | modeled |
| [Official: Price per Variation](https://global-selling.mercadolibre.com/devsite/price-per-variation-cbt) | 14 | 0 | modeled |
| [Official: UPTIN Migration](https://global-selling.mercadolibre.com/devsite/uptin-migration) | 2 | 0 | modeled |

## Operation models

| Host | Method | Path | Source pages | JSON |
|---|---|---|---:|---|
| `api.mercadolibre.com` | GET | `/marketplace/items/{cbt_item_id}` | 1 | [JSON](./operations/get-78b1447104db.json) |
| `api.mercadolibre.com` | GET | `/marketplace/items/{item_id}/migration_live_listing` | 1 | [JSON](./operations/get-11f8e2508744.json) |
| `api.mercadolibre.com` | GET | `/marketplace/user-products/{siteless_user_product_id}/mapping` | 1 | [JSON](./operations/get-cc8aea239e6b.json) |
| `api.mercadolibre.com` | GET | `/sites/{site_id}/user-products-families/{family_id}` | 1 | [JSON](./operations/get-e89e93f0deed.json) |
| `api.mercadolibre.com` | GET | `/user-products-families/tasks/{task_id}` | 1 | [JSON](./operations/get-e56f0b1b806d.json) |
| `api.mercadolibre.com` | GET | `/user-products/{siteless_user_product_id}` | 1 | [JSON](./operations/get-805946484695.json) |
| `api.mercadolibre.com` | POST | `/global/user-products/families/{siteless_family_id}` | 1 | [JSON](./operations/post-228d11115979.json) |
| `api.mercadolibre.com` | POST | `/global/user-products/{siteless_user_product_id}` | 1 | [JSON](./operations/post-376ae657cb75.json) |
| `api.mercadolibre.com` | PUT | `/global/user-products/families/{family_id}` | 6 | [JSON](./operations/put-6cbe614d4563.json) |
| `api.mercadolibre.com` | PUT | `/global/user-products/{siteless_user_product_id}` | 5 | [JSON](./operations/put-2bfa9d3e2756.json) |
| `api.mercadolibre.com` | PUT | `/global/user-products/{user_product_id}` | 11 | [JSON](./operations/put-9c6aebc4d86e.json) |
