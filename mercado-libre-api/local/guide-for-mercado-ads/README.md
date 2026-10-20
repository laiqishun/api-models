# Guide for Mercado Ads

Local seller official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Mercado Ads introduction](https://developers.mercadolibre.com.ar/en_us/mercado-ads-introduction) | 0 | 0 | guide-only |
| [Official: Brand Ads](https://developers.mercadolibre.com.ar/en_us/ads-bads) | 8 | 0 | modeled |
| [Official: Display Ads](https://developers.mercadolibre.com.ar/en_us/display-ads) | 8 | 0 | modeled |
| [Official: Product Ads](https://developers.mercadolibre.com.ar/en_us/product-ads-us-read) | 5 | 0 | modeled |

## API List

- [getAdDetails](operations/getAdDetails.json) (GET /advertising/product_ads/items/{item_id})：Ad Details [Official](https://developers.mercadolibre.com.ar/en_us/product-ads-us-read)
- [getAdSearchAndMetrics](operations/getAdSearchAndMetrics.json) (GET /advertising/advertisers/{advertiser_id}/product_ads/items)：Ad Search and Metrics [Official](https://developers.mercadolibre.com.ar/en_us/product-ads-us-read)
- [getAdvertisersByAdvertiserIdDisplayCampaigns](operations/getAdvertisersByAdvertiserIdDisplayCampaigns.json) (GET /advertising/advertisers/{advertiser_id}/display/campaigns)：Optional Parameters [Official](https://developers.mercadolibre.com.ar/en_us/display-ads)
- [getAvailableFilters](operations/getAvailableFilters.json) (GET /advertising/advertisers/{advertiser_id}/brand_ads/campaigns/metrics)：Available filters [Official](https://developers.mercadolibre.com.ar/en_us/ads-bads)
- [getBrandAdsCampaigns](operations/getBrandAdsCampaigns.json) (GET /advertising/advertisers/{advertiser_id}/brand_ads/campaigns)：Search campaigns [Official](https://developers.mercadolibre.com.ar/en_us/ads-bads)
- [getBrandAdsCampaignsByCampaignIdMetrics](operations/getBrandAdsCampaignsByCampaignIdMetrics.json) (GET /advertising/advertisers/{advertiser_id}/brand_ads/campaigns/{campaign_id}/metrics)：Optional parameters [Official](https://developers.mercadolibre.com.ar/en_us/ads-bads)
- [getByAdvertiserIdDisplayMetrics](operations/getByAdvertiserIdDisplayMetrics.json) (GET /advertising/advertisers/{advertiser_id}/display/metrics)：Optional Parameters [Official](https://developers.mercadolibre.com.ar/en_us/display-ads)
- [getByResourceIdDisplayCampaigns](operations/getByResourceIdDisplayCampaigns.json) (GET /advertising/advertisers/61/display/campaigns)：Optional Parameters [Official](https://developers.mercadolibre.com.ar/en_us/display-ads)
- [getByResourceIdMetrics](operations/getByResourceIdMetrics.json) (GET /advertising/advertisers/{advertiser_id}/display/campaigns/80/metrics)：Mandatory Parameters [Official](https://developers.mercadolibre.com.ar/en_us/display-ads)
- [getCampaignDetail](operations/getCampaignDetail.json) (GET /advertising/advertisers/{advertiser_id}/brand_ads/campaigns/{campaign_id})：Campaign detail [Official](https://developers.mercadolibre.com.ar/en_us/ads-bads)
- [getCampaignsByCampaignId](operations/getCampaignsByCampaignId.json) (GET /advertising/product_ads/campaigns/{campaign_id})：Available filters [Official](https://developers.mercadolibre.com.ar/en_us/product-ads-us-read)
- [getCampaignsByCampaignIdLineItems](operations/getCampaignsByCampaignIdLineItems.json) (GET /advertising/advertisers/{advertiser_id}/display/campaigns/{campaign_id}/line_items)：Optional Parameters [Official](https://developers.mercadolibre.com.ar/en_us/display-ads)
- [getCampaignsByCampaignIdMetrics](operations/getCampaignsByCampaignIdMetrics.json) (GET /advertising/advertisers/{advertiser_id}/display/campaigns/{campaign_id}/metrics)：Mandatory Parameters [Official](https://developers.mercadolibre.com.ar/en_us/display-ads)
- [getCampaignSearchAndMetrics](operations/getCampaignSearchAndMetrics.json) (GET /advertising/advertisers/{advertiser_id}/product_ads/campaigns)：Campaign Search and Metrics [Official](https://developers.mercadolibre.com.ar/en_us/product-ads-us-read)
- [getConsultAdvertiser](operations/getConsultAdvertiser.json) (GET /advertising/advertisers)：Consult advertiser [Official](https://developers.mercadolibre.com.ar/en_us/ads-bads)
- [getConsultCampaignAds](operations/getConsultCampaignAds.json) (GET /advertising/advertisers/{advertiser_id}/brand_ads/campaigns/{campaign_id}/items)：Consult campaign ads [Official](https://developers.mercadolibre.com.ar/en_us/ads-bads)
- [getConsultCampaignKeywords](operations/getConsultCampaignKeywords.json) (GET /advertising/advertisers/{advertiser_id}/brand_ads/campaigns/{campaign_id}/keywords)：Consult campaign keywords [Official](https://developers.mercadolibre.com.ar/en_us/ads-bads)
- [getKeywordsMetrics](operations/getKeywordsMetrics.json) (GET /advertising/advertisers/{advertiser_id}/brand_ads/campaigns/{campaign_id}/keywords/metrics)：Optional parameters [Official](https://developers.mercadolibre.com.ar/en_us/ads-bads)
- [getLineItemsByLineItemIdCreatives](operations/getLineItemsByLineItemIdCreatives.json) (GET /advertising/advertisers/{advertiser_id}/display/campaigns/{campaign_id}/line_items/{line_item_id}/creatives)：Optional Parameters [Official](https://developers.mercadolibre.com.ar/en_us/display-ads)
