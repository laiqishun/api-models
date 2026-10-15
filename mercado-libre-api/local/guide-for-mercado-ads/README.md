# Guide for Mercado Ads

Local seller official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Mercado Ads introduction](https://developers.mercadolibre.com.ar/en_us/mercado-ads-introduction) | 0 | 0 | guide-only |
| [Official: Brand Ads](https://developers.mercadolibre.com.ar/en_us/ads-bads) | 8 | 0 | modeled |
| [Official: Display Ads](https://developers.mercadolibre.com.ar/en_us/display-ads) | 8 | 0 | modeled |
| [Official: Product Ads](https://developers.mercadolibre.com.ar/en_us/product-ads-us-read) | 5 | 0 | modeled |

## Operation models

| Host | Method | Path | Source pages | JSON |
|---|---|---|---:|---|
| `api.mercadolibre.com` | GET | `/advertising/advertisers` | 3 | [JSON](./operations/get-ac2f1e3bed20.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/61/display/campaigns` | 1 | [JSON](./operations/get-b6d75db746ad.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/brand_ads/campaigns` | 1 | [JSON](./operations/get-1abdb2606c27.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/brand_ads/campaigns/metrics` | 1 | [JSON](./operations/get-4eb59a870c39.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/brand_ads/campaigns/{campaign_id}` | 1 | [JSON](./operations/get-c274823cf97c.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/brand_ads/campaigns/{campaign_id}/items` | 1 | [JSON](./operations/get-facbc3f2f79b.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/brand_ads/campaigns/{campaign_id}/keywords` | 1 | [JSON](./operations/get-40a916b68892.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/brand_ads/campaigns/{campaign_id}/keywords/metrics` | 1 | [JSON](./operations/get-2170dae7329e.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/brand_ads/campaigns/{campaign_id}/metrics` | 1 | [JSON](./operations/get-df1dc9d7b107.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/display/campaigns` | 1 | [JSON](./operations/get-7d129f914fa3.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/display/campaigns/80/metrics` | 1 | [JSON](./operations/get-9d3b202dcb33.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/display/campaigns/{campaign_id}/line_items` | 1 | [JSON](./operations/get-b875d3231647.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/display/campaigns/{campaign_id}/line_items/{line_item_id}/creatives` | 1 | [JSON](./operations/get-2463a54305ea.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/display/campaigns/{campaign_id}/metrics` | 1 | [JSON](./operations/get-69372acbaceb.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/display/metrics` | 1 | [JSON](./operations/get-8e7d32e6f62c.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/product_ads/campaigns` | 3 | [JSON](./operations/get-4903a2ea26f7.json) |
| `api.mercadolibre.com` | GET | `/advertising/advertisers/{advertiser_id}/product_ads/items` | 3 | [JSON](./operations/get-c2236dbb4406.json) |
| `api.mercadolibre.com` | GET | `/advertising/product_ads/campaigns/{campaign_id}` | 2 | [JSON](./operations/get-c47f5d374e6e.json) |
| `api.mercadolibre.com` | GET | `/advertising/product_ads/items/{item_id}` | 3 | [JSON](./operations/get-618d4a605033.json) |
