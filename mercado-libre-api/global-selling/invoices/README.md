# Invoices

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Billing Reports by Orders and Packs](https://global-selling.mercadolibre.com/devsite/billing-reports-by-orders-and-packs) | 1 | 0 | modeled |
| [Official: Billing data](https://global-selling.mercadolibre.com/devsite/gs-billing-data) | 1 | 0 | modeled |

## Operation models

| Host | Method | Path | Source pages | JSON |
|---|---|---|---:|---|
| `api.mercadolibre.com` | GET | `/billing/integration/group/ML/order/details` | 2 | [JSON](./operations/get-ff6ac3ae6804.json) |
| `api.mercadolibre.com` | GET | `/marketplace/orders/{order_id}/billing_info` | 1 | [JSON](./operations/get-fa8919d74f20.json) |
