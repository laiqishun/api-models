# Refunds, Claims & Returns

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Returns](https://global-selling.mercadolibre.com/devsite/manage-returns) | 6 | 0 | modeled |
| [Official: Manage Claims](https://global-selling.mercadolibre.com/devsite/manage-claims) | 8 | 0 | modeled |
| [Official: Claims Messages](https://global-selling.mercadolibre.com/devsite/manage-claims-messages) | 8 | 0 | modeled |
| [Official: Claims Resolutions](https://global-selling.mercadolibre.com/devsite/manage-claim-resolutions) | 6 | 0 | modeled |

## Operation models

| Host | Method | Path | Source pages | JSON |
|---|---|---|---:|---|
| `api.mercadolibre.com` | GET | `/marketplace/v2/claims/reasons/PNR9502` | 1 | [JSON](./operations/get-fea89f6a03fe.json) |
| `api.mercadolibre.com` | GET | `/marketplace/v2/claims/reasons/{reason_id}` | 1 | [JSON](./operations/get-f67a83116144.json) |
| `api.mercadolibre.com` | GET | `/marketplace/v2/claims/search` | 2 | [JSON](./operations/get-e8321d9dc9c7.json) |
| `api.mercadolibre.com` | GET | `/marketplace/v2/claims/{claim_id}` | 1 | [JSON](./operations/get-2d62f90e07c8.json) |
| `api.mercadolibre.com` | GET | `/marketplace/v2/claims/{claim_id}/actions-history` | 1 | [JSON](./operations/get-2d6abf3ec758.json) |
| `api.mercadolibre.com` | GET | `/marketplace/v2/claims/{claim_id}/affects-reputation` | 1 | [JSON](./operations/get-1c12edfb09ac.json) |
| `api.mercadolibre.com` | GET | `/marketplace/v2/claims/{claim_id}/attachments/{attachments_id}/download` | 1 | [JSON](./operations/get-3efcf3e2312d.json) |
| `api.mercadolibre.com` | GET | `/marketplace/v2/claims/{claim_id}/detail` | 1 | [JSON](./operations/get-3f922c8cfdda.json) |
| `api.mercadolibre.com` | GET | `/marketplace/v2/claims/{claim_id}/expected-resolutions` | 1 | [JSON](./operations/get-2c22cc42fb70.json) |
| `api.mercadolibre.com` | GET | `/marketplace/v2/claims/{claim_id}/messages` | 1 | [JSON](./operations/get-e810b87d8282.json) |
| `api.mercadolibre.com` | GET | `/marketplace/v2/claims/{claim_id}/partial-refund/available-offers` | 1 | [JSON](./operations/get-4420895699bf.json) |
| `api.mercadolibre.com` | GET | `/marketplace/v2/claims/{claim_id}/returns` | 1 | [JSON](./operations/get-936972f762dc.json) |
| `api.mercadolibre.com` | GET | `/marketplace/v2/claims/{claim_id}/status-history` | 1 | [JSON](./operations/get-704d168b33b7.json) |
| `api.mercadolibre.com` | GET | `/post-purchase/v1/claims/{claim_id}/attachments/1517482146_31489bf8-95e3-4a2d-bcff-3c57771fb7c4.png/download` | 1 | [JSON](./operations/get-12787a7593eb.json) |
| `api.mercadolibre.com` | GET | `/post-purchase/v1/claims/{claim_id}/attachments/example.png` | 1 | [JSON](./operations/get-23a4ed9af640.json) |
| `api.mercadolibre.com` | GET | `/post-purchase/v1/claims/{claim_id}/attachments/{attachments_id}` | 1 | [JSON](./operations/get-ccd7d1bf3079.json) |
| `api.mercadolibre.com` | GET | `/post-purchase/v1/claims/{claim_id}/charges/return-cost` | 3 | [JSON](./operations/get-0c271f39e78a.json) |
| `api.mercadolibre.com` | GET | `/post-purchase/v1/returns/reasons` | 1 | [JSON](./operations/get-1cf5ad0cbe96.json) |
| `api.mercadolibre.com` | POST | `/marketplace/v2/claims/{claim_id}/actions/open-dispute` | 1 | [JSON](./operations/post-eee45710a934.json) |
| `api.mercadolibre.com` | POST | `/marketplace/v2/claims/{claim_id}/actions/send-message` | 1 | [JSON](./operations/post-1643025b2ba8.json) |
| `api.mercadolibre.com` | POST | `/marketplace/v2/claims/{claim_id}/attachments` | 1 | [JSON](./operations/post-b376850a98ea.json) |
| `api.mercadolibre.com` | POST | `/marketplace/v2/claims/{claim_id}/expected-resolutions/allow-return` | 1 | [JSON](./operations/post-ab7b1fbd3401.json) |
| `api.mercadolibre.com` | POST | `/marketplace/v2/claims/{claim_id}/expected-resolutions/partial-refund` | 1 | [JSON](./operations/post-118e9b7c76e0.json) |
| `api.mercadolibre.com` | POST | `/marketplace/v2/claims/{claim_id}/expected-resolutions/refund` | 1 | [JSON](./operations/post-b3f4c003b819.json) |
| `api.mercadolibre.com` | POST | `/marketplace/v2/claims/{claim}/attachments` | 1 | [JSON](./operations/post-765c60fa3bf3.json) |
| `api.mercadolibre.com` | POST | `/post-purchase/v1/claims/{claim_id}/returns/attachments` | 1 | [JSON](./operations/post-d3e3c09ccd6c.json) |
| `api.mercadolibre.com` | POST | `/post-purchase/v1/returns/{id}/return-review` | 2 | [JSON](./operations/post-56b09aea598b.json) |
| `api.mercadolibre.com` | POST | `/post-purchase/v1/returns/{return_id}/return-review` | 1 | [JSON](./operations/post-c6b2e79c7d54.json) |
