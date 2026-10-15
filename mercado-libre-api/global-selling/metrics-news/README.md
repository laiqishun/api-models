# Metrics & News

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Listings quality](https://global-selling.mercadolibre.com/devsite/listings-quality-gs) | 2 | 0 | modeled |
| [Official: Trends](https://global-selling.mercadolibre.com/devsite/trends-gs) | 4 | 0 | modeled |
| [Official: Visits](https://global-selling.mercadolibre.com/devsite/visits) | 4 | 0 | modeled |
| [Official: Product reviews](https://global-selling.mercadolibre.com/devsite/product-reviews) | 2 | 0 | modeled |
| [Official: Communications](https://global-selling.mercadolibre.com/devsite/seller-news) | 1 | 0 | modeled |
| [Official: Seller reputation](https://global-selling.mercadolibre.com/devsite/seller-reputation-global-selling) | 1 | 0 | modeled |
| [Official: Shopping experience](https://global-selling.mercadolibre.com/devsite/shopping-experience) | 3 | 0 | modeled |

## Operation models

| Host | Method | Path | Source pages | JSON |
|---|---|---|---:|---|
| `api.mercadolibre.com` | GET | `/communications/notices` | 1 | [JSON](./operations/get-c9fd6c5ed167.json) |
| `api.mercadolibre.com` | GET | `/global/users/seller_reputation` | 1 | [JSON](./operations/get-8b871531b0b7.json) |
| `api.mercadolibre.com` | GET | `/item/{id}/performance` | 1 | [JSON](./operations/get-52f1fb431a05.json) |
| `api.mercadolibre.com` | GET | `/item/{item_id}/performance` | 1 | [JSON](./operations/get-97992d7227a5.json) |
| `api.mercadolibre.com` | GET | `/items/MCO471870973/visits/time_window` | 1 | [JSON](./operations/get-1eb82b2a2747.json) |
| `api.mercadolibre.com` | GET | `/items/visits` | 1 | [JSON](./operations/get-7bf2ad4e26e9.json) |
| `api.mercadolibre.com` | GET | `/items/{item_id}/visits/time_window` | 1 | [JSON](./operations/get-1a954d63d966.json) |
| `api.mercadolibre.com` | GET | `/marketplace/items/{item_id}/purchase_experience` | 1 | [JSON](./operations/get-00dbdefeeb8b.json) |
| `api.mercadolibre.com` | GET | `/marketplace/user_products/MLAU1391786841/purchase_experience` | 1 | [JSON](./operations/get-bdfe0ac90f6e.json) |
| `api.mercadolibre.com` | GET | `/marketplace/user_products/{up_id}/purchase_experience` | 1 | [JSON](./operations/get-ba58b578f200.json) |
| `api.mercadolibre.com` | GET | `/reviews/item/{id}` | 2 | [JSON](./operations/get-2782cfce49ab.json) |
| `api.mercadolibre.com` | GET | `/reviews/item/{item_id}` | 1 | [JSON](./operations/get-d85a78d08d40.json) |
| `api.mercadolibre.com` | GET | `/trends/MLA` | 1 | [JSON](./operations/get-21b14ffd5953.json) |
| `api.mercadolibre.com` | GET | `/trends/MLA/{id}` | 1 | [JSON](./operations/get-d89325522471.json) |
| `api.mercadolibre.com` | GET | `/trends/{site_id}` | 1 | [JSON](./operations/get-8c8442c79b84.json) |
| `api.mercadolibre.com` | GET | `/trends/{site_id}/{category_id}` | 1 | [JSON](./operations/get-47f77484b8ce.json) |
| `api.mercadolibre.com` | GET | `/visits/items` | 1 | [JSON](./operations/get-80d9cb6ebdb0.json) |
