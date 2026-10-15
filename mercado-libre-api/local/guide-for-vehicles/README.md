# Guide for vehicles

Local seller official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Introduction](https://developers.mercadolibre.com.ar/en_us/introduction-vehicles) | 0 | 0 | guide-only |
| [Official: Manage users](https://developers.mercadolibre.com.ar/en_us/vehicles-manage-users) | 6 | 0 | modeled |
| [Official: Manage packages vehicles](https://developers.mercadolibre.com.ar/en_us/vehicles-manage-packages) | 4 | 1 | partial |
| [Official: Categories & attributes](https://developers.mercadolibre.com.ar/en_us/categories-attributes) | 8 | 0 | modeled |
| [Official: List vehicles](https://developers.mercadolibre.com.ar/en_us/list-vehicles) | 3 | 0 | modeled |
| [Official: Sync listings](https://developers.mercadolibre.com.ar/en_us/vehicles-sync-listings) | 1 | 0 | modeled |
| [Official: Manage questions & contacts](https://developers.mercadolibre.com.ar/en_us/vehicles-manage-contacts) | 13 | 1 | partial |
| [Official: Subscribe to our feeds](https://developers.mercadolibre.com.ar/en_us/vehicles-subscribe-to-our-feeds) | 6 | 0 | modeled |
| [Official: Interested persons](https://developers.mercadolibre.com.ar/en_us/interested-persons) | 3 | 0 | modeled |
| [Official: Credits pre-approved](https://developers.mercadolibre.com.ar/en_us/credits-pre-approved-vehicles) | 3 | 0 | modeled |

## Operation models

| Host | Method | Path | Source pages | JSON |
|---|---|---|---:|---|
| `api.mercadolibre.com` | DELETE | `/users/{user_id}/immediate_payment/by_user` | 1 | [JSON](./operations/delete-90819a67cf91.json) |
| `api.mercadolibre.com` | GET | `/sites/{site_id}/all` | 1 | [JSON](./operations/get-5c08a0c28e94.json) |
| `api.mercadolibre.com` | GET | `/vis/leads/3f2dedf2-dfbd-4981-a726-40b13aa172ff` | 1 | [JSON](./operations/get-6c34fd0066da.json) |
| `api.mercadolibre.com` | GET | `/vis/leads/{lead_id}` | 1 | [JSON](./operations/get-bb3bdba6bdee.json) |
| `api.mercadolibre.com` | GET | `/vis/users/{user_id}/leads/buyers` | 1 | [JSON](./operations/get-30df5827be1d.json) |
| `api.mercadolibre.com` | POST | `/users/{user_id}/immediate_payment` | 1 | [JSON](./operations/post-e1c4bb0086f0.json) |
