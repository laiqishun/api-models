# API resources

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Items & Searches](https://global-selling.mercadolibre.com/devsite/items-and-searches-global-selling) | 7 | 0 | modeled |
| [Official: Location](https://global-selling.mercadolibre.com/devsite/location-global-selling) | 4 | 0 | modeled |
| [Official: Shipping](https://global-selling.mercadolibre.com/devsite/shipping-global-selling) | 6 | 0 | modeled |
| [Official: Paging results](https://global-selling.mercadolibre.com/devsite/paging-results-global-selling) | 1 | 0 | modeled |
| [Official: Receive notifications](https://global-selling.mercadolibre.com/devsite/receive-notifications) | 15 | 0 | modeled |
| [Official: Moderations](https://global-selling.mercadolibre.com/devsite/moderations-gs) | 2 | 0 | modeled |
| [Official: What is the Brand Protection Program?](https://global-selling.mercadolibre.com/devsite/what-is-the-brand-protection-program) | 0 | 0 | guide-only |
| [Official: Program Members](https://global-selling.mercadolibre.com/devsite/program-members) | 6 | 0 | modeled |
| [Official: Reported listings](https://global-selling.mercadolibre.com/devsite/reported-listings) | 5 | 0 | modeled |
| [Official: Official Stores](https://global-selling.mercadolibre.com/devsite/official-storesglobal-selling) | 4 | 0 | modeled |

## Operation models

| Host | Method | Path | Source pages | JSON |
|---|---|---|---:|---|
| `api.mercadolibre.com` | GET | `/cities/Q04tQkpCZWlqaW5n` | 1 | [JSON](./operations/get-9f8f9591b062.json) |
| `api.mercadolibre.com` | GET | `/countries` | 1 | [JSON](./operations/get-ad912a1126b6.json) |
| `api.mercadolibre.com` | GET | `/countries/AR` | 1 | [JSON](./operations/get-42fa6fe386af.json) |
| `api.mercadolibre.com` | GET | `/items` | 2 | [JSON](./operations/get-c70f544338e1.json) |
| `api.mercadolibre.com` | GET | `/items/{item_id}` | 6 | [JSON](./operations/get-24093a256605.json) |
| `api.mercadolibre.com` | GET | `/items/{item_id}/marketplace_items` | 1 | [JSON](./operations/get-82ecbd88c241.json) |
| `api.mercadolibre.com` | GET | `/marketplace/benchmarks/items/{item_id}/details` | 2 | [JSON](./operations/get-1a9e6404d206.json) |
| `api.mercadolibre.com` | GET | `/marketplace/claims/{resource}` | 1 | [JSON](./operations/get-041da0cf2e89.json) |
| `api.mercadolibre.com` | GET | `/marketplace/items/{item_id}` | 8 | [JSON](./operations/get-b69893803b3d.json) |
| `api.mercadolibre.com` | GET | `/marketplace/messages/{resource}` | 1 | [JSON](./operations/get-e3cdcd15cb84.json) |
| `api.mercadolibre.com` | GET | `/marketplace/moderations/infractions/{id}` | 2 | [JSON](./operations/get-2051b02028b9.json) |
| `api.mercadolibre.com` | GET | `/marketplace/moderations/infractions/{user_id}` | 2 | [JSON](./operations/get-c2250ae245a6.json) |
| `api.mercadolibre.com` | GET | `/marketplace/orders/{order_id}` | 5 | [JSON](./operations/get-dbbfab70c032.json) |
| `api.mercadolibre.com` | GET | `/marketplace/questions/{question_id}` | 2 | [JSON](./operations/get-bea48825a97a.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/candidate/{candidate_id}/&USER_ID` | 1 | [JSON](./operations/get-7b43592d22f0.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/offer/{offer_id}/{user_id}` | 1 | [JSON](./operations/get-8944e0055665.json) |
| `api.mercadolibre.com` | GET | `/marketplace/shipments/{resource}` | 1 | [JSON](./operations/get-8abbe63d9ec8.json) |
| `api.mercadolibre.com` | GET | `/marketplace/shipments/{shipment_id}` | 2 | [JSON](./operations/get-2dd46edff25c.json) |
| `api.mercadolibre.com` | GET | `/marketplace/shipments/{shipment_id}/labels` | 2 | [JSON](./operations/get-7cb891608b72.json) |
| `api.mercadolibre.com` | GET | `/marketplace/user_products/{up_id}` | 1 | [JSON](./operations/get-5f094e1bd9e1.json) |
| `api.mercadolibre.com` | GET | `/marketplace/users/{merchant_id}` | 1 | [JSON](./operations/get-8861fea8bb39.json) |
| `api.mercadolibre.com` | GET | `/marketplace/users/{merchant_id}/items/search` | 1 | [JSON](./operations/get-0560a5b2c32a.json) |
| `api.mercadolibre.com` | GET | `/marketplace/users/{user_id}/items/search` | 10 | [JSON](./operations/get-48bc8567ec0e.json) |
| `api.mercadolibre.com` | GET | `/moderations/pppi/case/{case_id}` | 1 | [JSON](./operations/get-dc9c350701c3.json) |
| `api.mercadolibre.com` | GET | `/moderations/pppi/case/{denounce_id}` | 1 | [JSON](./operations/get-83e31c72e1ce.json) |
| `api.mercadolibre.com` | GET | `/moderations/pppi/case/{id}` | 2 | [JSON](./operations/get-e4d5f145aa39.json) |
| `api.mercadolibre.com` | GET | `/moderations/pppi/cases` | 1 | [JSON](./operations/get-0dca6539d0df.json) |
| `api.mercadolibre.com` | GET | `/moderations/pppi/denounces/MLA/ITM/options` | 1 | [JSON](./operations/get-819777236f5e.json) |
| `api.mercadolibre.com` | GET | `/moderations/pppi/denounces/{site_id}/ITM/options` | 1 | [JSON](./operations/get-3b2bccd6d9ef.json) |
| `api.mercadolibre.com` | GET | `/myfeeds` | 1 | [JSON](./operations/get-a8eaf6d3682e.json) |
| `api.mercadolibre.com` | GET | `/sites/MLM/shipping_methods` | 1 | [JSON](./operations/get-e111a64e99be.json) |
| `api.mercadolibre.com` | GET | `/sites/MLM/shipping_options` | 1 | [JSON](./operations/get-3cca3a20fc74.json) |
| `api.mercadolibre.com` | GET | `/sites/{site_id}/search` | 1 | [JSON](./operations/get-e535c9767241.json) |
| `api.mercadolibre.com` | GET | `/states/AR-B` | 1 | [JSON](./operations/get-a91b5345f10b.json) |
| `api.mercadolibre.com` | GET | `/user-products-families/{family_id}` | 1 | [JSON](./operations/get-47956e9695bf.json) |
| `api.mercadolibre.com` | GET | `/users` | 1 | [JSON](./operations/get-af3ea6d0a7c3.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/brands/aaaaa` | 1 | [JSON](./operations/get-57e621c7bc79.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/brands/{brand_id}` | 1 | [JSON](./operations/get-cf2f1b8b25fb.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/brands/{id}` | 1 | [JSON](./operations/get-35e0c391c1e3.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/shipping_preferences` | 1 | [JSON](./operations/get-09a127c18215.json) |
| `api.mercadolibre.com` | GET | `/{resource}` | 3 | [JSON](./operations/get-a36bfb91460e.json) |
| `api.mercadolibre.com` | POST | `/marketplace/shipments/{shipment_id}/tracking` | 2 | [JSON](./operations/post-6830d5ab9253.json) |
| `api.mercadolibre.com` | POST | `/moderations/pppi/case/{denounce_id}` | 1 | [JSON](./operations/post-afa47ab63657.json) |
| `api.mercadolibre.com` | POST | `/moderations/pppi/case/{id}` | 1 | [JSON](./operations/post-b950da823a97.json) |
| `api.mercadolibre.com` | POST | `/moderations/pppi/denounces/items/{item_id}` | 1 | [JSON](./operations/post-c97d808f870e.json) |
| `api.mercadolibre.com` | PUT | `/moderations/pppi/case/files` | 1 | [JSON](./operations/put-0b15e576df28.json) |
