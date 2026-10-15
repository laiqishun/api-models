# Promotions

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Manage promotions](https://global-selling.mercadolibre.com/devsite/manage-promotions-gs) | 16 | 0 | modeled |
| [Official: Deals](https://global-selling.mercadolibre.com/devsite/deals-gs) | 11 | 0 | modeled |
| [Official: Co-funded campaigns](https://global-selling.mercadolibre.com/devsite/cofunded-campaigns) | 6 | 0 | modeled |
| [Official: Pre-negotiated discount per item](https://global-selling.mercadolibre.com/devsite/pre-negotiated-discount-per-item-gs) | 6 | 0 | modeled |
| [Official: Unhealthy Stock Campaign](https://global-selling.mercadolibre.com/devsite/unhealthy-stock-campaign) | 6 | 0 | modeled |
| [Official: Price discount](https://global-selling.mercadolibre.com/devsite/price-discount) | 5 | 0 | modeled |
| [Official: Volume discount campaigns](https://global-selling.mercadolibre.com/devsite/volume-discount-campaigns-gs) | 10 | 0 | modeled |
| [Official: Deal of the day](https://global-selling.mercadolibre.com/devsite/deal-of-day-gs) | 8 | 0 | modeled |
| [Official: Lightning Deal](https://global-selling.mercadolibre.com/devsite/lightning-deal-gs) | 7 | 0 | modeled |
| [Official: Seller Campaign](https://global-selling.mercadolibre.com/devsite/seller-campaign) | 16 | 0 | modeled |
| [Official: Automated co-participation and competitive pricing campaign](https://global-selling.mercadolibre.com/devsite/automated-co-participation-and-competitive-pricing-campaign) | 7 | 0 | modeled |
| [Official: Clearance](https://global-selling.mercadolibre.com/devsite/clearance) | 5 | 0 | modeled |

## Operation models

| Host | Method | Path | Source pages | JSON |
|---|---|---|---:|---|
| `api.mercadolibre.com` | DELETE | `/marketplace/seller-promotions/items/massive/{id}` | 1 | [JSON](./operations/delete-b1dea54d25db.json) |
| `api.mercadolibre.com` | DELETE | `/marketplace/seller-promotions/items/massive/{itemid}` | 1 | [JSON](./operations/delete-78e673bcd07f.json) |
| `api.mercadolibre.com` | DELETE | `/marketplace/seller-promotions/items/{item_id}` | 10 | [JSON](./operations/delete-a4a71b0c6890.json) |
| `api.mercadolibre.com` | DELETE | `/marketplace/seller-promotions/items/{itemid}` | 5 | [JSON](./operations/delete-3cc51b9a9601.json) |
| `api.mercadolibre.com` | DELETE | `/marketplace/seller-promotions/seller-campaign/C-MLM360923` | 1 | [JSON](./operations/delete-5c5d4c5a4e8a.json) |
| `api.mercadolibre.com` | DELETE | `/marketplace/seller-promotions/seller-campaign/C-MLM703970` | 1 | [JSON](./operations/delete-91a0aee2d29f.json) |
| `api.mercadolibre.com` | DELETE | `/marketplace/seller-promotions/seller-campaign/{campaignid}` | 1 | [JSON](./operations/delete-6b34959a8c90.json) |
| `api.mercadolibre.com` | DELETE | `/marketplace/seller-promotions/seller-campaign/{promotion_id}` | 1 | [JSON](./operations/delete-82dccd2914e4.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/items/{item_id}` | 2 | [JSON](./operations/get-4e8962131dbb.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/items/{itemid}` | 1 | [JSON](./operations/get-f81df15f3ab0.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/C-MLM199082/items` | 1 | [JSON](./operations/get-fa34bb038d2c.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/C-MLM201059` | 1 | [JSON](./operations/get-98ef6745a1ca.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/C-MLM201059/items` | 1 | [JSON](./operations/get-005e32d75cfa.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/C-MLM614177` | 1 | [JSON](./operations/get-8b9f1740b03e.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/C-MLM703970` | 1 | [JSON](./operations/get-cf46cd6edae7.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/C-MLM703970/items` | 1 | [JSON](./operations/get-7c1301824b1e.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/DOD-MLM1000/items` | 1 | [JSON](./operations/get-5c626e88e653.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/LGH-MLM1000/items` | 1 | [JSON](./operations/get-b72466e9116d.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/P-MLC13457036` | 1 | [JSON](./operations/get-1341215fd301.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/P-MLC13457036/items` | 1 | [JSON](./operations/get-46daa8e89f5a.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/P-MLM13637333` | 2 | [JSON](./operations/get-ab9989b82a21.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/P-MLM13757022` | 1 | [JSON](./operations/get-c7fbf6aa79d4.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/P-MLM13757022/items` | 1 | [JSON](./operations/get-d75fd82aebad.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/P-MLM13765128` | 1 | [JSON](./operations/get-d463407b147b.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/P-MLM13765128/items` | 1 | [JSON](./operations/get-6f9e60b22734.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/P-MLM13773008` | 1 | [JSON](./operations/get-7154ca50359a.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/P-MLM13773008/items` | 2 | [JSON](./operations/get-4ddfa59331f3.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/P-MLM1806015` | 1 | [JSON](./operations/get-0c7ef4e34fc2.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/P-MLM1806015/items` | 1 | [JSON](./operations/get-c17870fbd433.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/P-MLM6276082` | 1 | [JSON](./operations/get-818007d12641.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/candidate/CANDIDATE-MLM2199514002-70027957276/{id}` | 1 | [JSON](./operations/get-e8778441c92d.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/candidates/{candidate_id}` | 1 | [JSON](./operations/get-8a06b30f819d.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/offer/OFFER-MLM1873971357-10078845289/{id}` | 1 | [JSON](./operations/get-0fdd44a08903.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/offer/{offerid}/{user_id}` | 1 | [JSON](./operations/get-10cc0f2667d2.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/{dodid}/items` | 1 | [JSON](./operations/get-2f3355eb7a4d.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/{promotion_id}` | 7 | [JSON](./operations/get-55406815a6e8.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/{promotion_id}/items` | 4 | [JSON](./operations/get-e0f824a08e60.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/{promotionid}` | 3 | [JSON](./operations/get-c0899fc1589a.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/promotions/{promotionid}/items` | 6 | [JSON](./operations/get-fafb6a0800fa.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/users/{user_id}` | 2 | [JSON](./operations/get-4bf572f5344c.json) |
| `api.mercadolibre.com` | GET | `/marketplace/seller-promotions/users/{user_id}/pricing-model` | 6 | [JSON](./operations/get-219d543dcb83.json) |
| `api.mercadolibre.com` | GET | `/seller-promotions/P-MLB2087012/items` | 1 | [JSON](./operations/get-0d9c4b171757.json) |
| `api.mercadolibre.com` | POST | `/marketplace/seller-promotions/items/{item_id}` | 9 | [JSON](./operations/post-a0b452b0db08.json) |
| `api.mercadolibre.com` | POST | `/marketplace/seller-promotions/items/{itemid}` | 8 | [JSON](./operations/post-efa4bd980ed6.json) |
| `api.mercadolibre.com` | POST | `/marketplace/seller-promotions/seller-campaign/{id}` | 2 | [JSON](./operations/post-d98264418add.json) |
| `api.mercadolibre.com` | POST | `/marketplace/seller-promotions/seller-campaign/{user_id}` | 2 | [JSON](./operations/post-d6846ed6e9fa.json) |
| `api.mercadolibre.com` | PUT | `/marketplace/seller-promotions/items/{item_id}` | 1 | [JSON](./operations/put-7806dc0b9ba4.json) |
| `api.mercadolibre.com` | PUT | `/marketplace/seller-promotions/items/{itemid}` | 7 | [JSON](./operations/put-4b3497ecd994.json) |
| `api.mercadolibre.com` | PUT | `/marketplace/seller-promotions/seller-campaign/C-MLM5689` | 1 | [JSON](./operations/put-f0f6b5232279.json) |
| `api.mercadolibre.com` | PUT | `/marketplace/seller-promotions/seller-campaign/C-MLM703970` | 1 | [JSON](./operations/put-64db99347bb4.json) |
| `api.mercadolibre.com` | PUT | `/marketplace/seller-promotions/seller-campaign/{campaignid}` | 1 | [JSON](./operations/put-6294fbb823ff.json) |
| `api.mercadolibre.com` | PUT | `/marketplace/seller-promotions/seller-campaign/{promotion_id}` | 1 | [JSON](./operations/put-660a72a309a5.json) |
