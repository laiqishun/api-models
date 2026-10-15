# Mercado Ads

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: What is Mercado Ads?](https://global-selling.mercadolibre.com/devsite/mercado-ads) | 0 | 0 | guide-only |
| [Official: Product Ads](https://global-selling.mercadolibre.com/devsite/new-product-ads) | 15 | 0 | modeled |
| [Official: Display Ads](https://global-selling.mercadolibre.com/devsite/display-gs) | 8 | 0 | modeled |

## Operation models

| Host | Method | Path | Source pages | JSON |
|---|---|---|---:|---|
| `api.mercadolibre.com` | DELETE | `/marketplace/advertising/{site}/product_ads/campaigns/{campaign_id}/ad_groups` | 1 | [JSON](./operations/delete-cdd3baf42d4f.json) |
| `api.mercadolibre.com` | DELETE | `/marketplace/advertising/{site}/product_ads/campaigns/{campaign_id}/ad_groups/{ad_group_id}` | 1 | [JSON](./operations/delete-0f5554fa1ae5.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers` | 2 | [JSON](./operations/get-469786667fc6.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/61/display/campaigns` | 1 | [JSON](./operations/get-90f840f44d63.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/display/campaigns` | 1 | [JSON](./operations/get-a6fd2bd8b960.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/display/campaigns/80/metrics` | 1 | [JSON](./operations/get-67f824ce6770.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/display/campaigns/{campaign_id}/line_items` | 1 | [JSON](./operations/get-8fff164ead36.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/display/campaigns/{campaign_id}/line_items/{line_item_id}/creatives` | 1 | [JSON](./operations/get-ff6566923204.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/display/campaigns/{campaign_id}/metrics` | 1 | [JSON](./operations/get-7c562499a7c1.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/display/metrics` | 1 | [JSON](./operations/get-d10300451ed8.json) |
| `api.mercadolibre.com` | GET | `/marketplace/advertising/{advertiser_site_id}/advertisers/{advertiser_id}/product_ads/ads/search` | 1 | [JSON](./operations/get-ff48843a3e8e.json) |
| `api.mercadolibre.com` | GET | `/marketplace/advertising/{advertiser_site_id}/advertisers/{advertiser_id}/product_ads/campaigns/search` | 2 | [JSON](./operations/get-f7477c84437a.json) |
| `api.mercadolibre.com` | GET | `/marketplace/advertising/{advertiser_site_id}/product_ads/campaigns/{campaign_id}` | 1 | [JSON](./operations/get-b80944a0ca5a.json) |
| `api.mercadolibre.com` | GET | `/marketplace/advertising/{site}/advertisers/{adv}/product_ads/ad_groups/search` | 2 | [JSON](./operations/get-bf0633240483.json) |
| `api.mercadolibre.com` | GET | `/marketplace/advertising/{site}/advertisers/{adv}/product_ads/ads/search` | 1 | [JSON](./operations/get-0707ce01116a.json) |
| `api.mercadolibre.com` | GET | `/marketplace/advertising/{site}/product_ads/ad_groups/{ad_group_id}` | 1 | [JSON](./operations/get-d52969813b96.json) |
| `api.mercadolibre.com` | GET | `/marketplace/advertising/{site}/product_ads/ad_groups/{ad_group_id}/ads` | 1 | [JSON](./operations/get-67cb6ea5fa12.json) |
| `api.mercadolibre.com` | GET | `/marketplace/advertising/{site}/product_ads/campaigns/{campaign_id}/ad_groups/metrics` | 1 | [JSON](./operations/get-df8dbc637428.json) |
| `api.mercadolibre.com` | POST | `/marketplace/advertising/{advertiser_site_id}/advertisers/{advertiser_id}/product_ads/campaigns` | 1 | [JSON](./operations/post-8a929f193767.json) |
| `api.mercadolibre.com` | PUT | `/marketplace/advertising/{advertiser_site_id}/product_ads/campaigns/{campaign_id}` | 1 | [JSON](./operations/put-d46b0eddf79a.json) |
| `api.mercadolibre.com` | PUT | `/marketplace/advertising/{site}/advertisers/{adv}/product_ads/ad_groups` | 1 | [JSON](./operations/put-27f63e184fe8.json) |
| `api.mercadolibre.com` | PUT | `/marketplace/advertising/{site}/product_ads/ad_groups/{ad_group_id}` | 1 | [JSON](./operations/put-07e5cc364e6f.json) |
