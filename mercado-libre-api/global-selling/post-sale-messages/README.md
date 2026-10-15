# Post-sale messages

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Post-sale Messages](https://global-selling.mercadolibre.com/devsite/messaging-after-sale-global-selling) | 7 | 0 | modeled |
| [Official: Pending messages](https://global-selling.mercadolibre.com/devsite/pending-messages-gs) | 2 | 0 | modeled |
| [Official: Blocked messages](https://global-selling.mercadolibre.com/devsite/blocked-messages-gs) | 1 | 0 | modeled |

## Operation models

| Host | Method | Path | Source pages | JSON |
|---|---|---|---:|---|
| `api.mercadolibre.com` | GET | `/marketplace/messages/2d45a5ad186041659e9a608f0c109dff` | 1 | [JSON](./operations/get-f6da8e7419d3.json) |
| `api.mercadolibre.com` | GET | `/marketplace/messages/attachments/76601286_5946e4c4-168a-45fd-945e-b8f0c306c58d.png` | 1 | [JSON](./operations/get-8243e6a4ba4e.json) |
| `api.mercadolibre.com` | GET | `/marketplace/messages/attachments/{attachment_id}` | 1 | [JSON](./operations/get-25c8155df58e.json) |
| `api.mercadolibre.com` | GET | `/marketplace/messages/packs/{pack_id}` | 1 | [JSON](./operations/get-b33dd94953cd.json) |
| `api.mercadolibre.com` | GET | `/marketplace/messages/unread` | 2 | [JSON](./operations/get-fc4c683f1bc1.json) |
| `api.mercadolibre.com` | GET | `/marketplace/messages/{message_id}` | 1 | [JSON](./operations/get-61c57b279fab.json) |
| `api.mercadolibre.com` | GET | `/messages/packs/{pack_id}/sellers/{seller_id}` | 2 | [JSON](./operations/get-5c3daa42527f.json) |
| `api.mercadolibre.com` | POST | `/marketplace/messages/attachments` | 1 | [JSON](./operations/post-e6c333c3a2a0.json) |
| `api.mercadolibre.com` | POST | `/marketplace/messages/packs/{pack_id}` | 1 | [JSON](./operations/post-ff3805f5d4e7.json) |
