# Mercado Ads

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: What is Mercado Ads?](https://global-selling.mercadolibre.com/devsite/mercado-ads) | 0 | 0 | guide-only |
| [Official: Product Ads](https://global-selling.mercadolibre.com/devsite/new-product-ads) | 15 | 0 | modeled |
| [Official: Display Ads](https://global-selling.mercadolibre.com/devsite/display-gs) | 8 | 0 | modeled |

## API List

- [addMoveAndUpdateAdsInCampaign](operations/addMoveAndUpdateAdsInCampaign.json) (PUT /marketplace/advertising/{site}/product_ads/ad_groups/{ad_group_id})：Add, move and update ads in campaign [Official](https://global-selling.mercadolibre.com/devsite/new-product-ads)
- [addMoveAndUpdateAdsInCampaignBulk](operations/addMoveAndUpdateAdsInCampaignBulk.json) (PUT /marketplace/advertising/{site}/advertisers/{adv}/product_ads/ad_groups)：Add, move and update ads in campaign — bulk [Official](https://global-selling.mercadolibre.com/devsite/new-product-ads)
- [createCampaign](operations/createCampaign.json) (POST /marketplace/advertising/{advertiser_site_id}/advertisers/{advertiser_id}/product_ads/campaigns)：Create campaign [Official](https://global-selling.mercadolibre.com/devsite/new-product-ads)
- [deleteAdFromCampaign](operations/deleteAdFromCampaign.json) (DELETE /marketplace/advertising/{site}/product_ads/campaigns/{campaign_id}/ad_groups/{ad_group_id})：Delete ad from campaign [Official](https://global-selling.mercadolibre.com/devsite/new-product-ads)
- [deleteMultipleAdsFromCampaign](operations/deleteMultipleAdsFromCampaign.json) (DELETE /marketplace/advertising/{site}/product_ads/campaigns/{campaign_id}/ad_groups)：Delete multiple ads from campaign [Official](https://global-selling.mercadolibre.com/devsite/new-product-ads)
- [getAdGroupDetail](operations/getAdGroupDetail.json) (GET /marketplace/advertising/{site}/product_ads/ad_groups/{ad_group_id})：Ad Group detail [Official](https://global-selling.mercadolibre.com/devsite/new-product-ads)
- [getAdGroupsCampaign](operations/getAdGroupsCampaign.json) (GET /marketplace/advertising/{site}/product_ads/campaigns/{campaign_id}/ad_groups/metrics)：Ad Groups of a campaign [Official](https://global-selling.mercadolibre.com/devsite/new-product-ads)
- [getAdGroupsSearch](operations/getAdGroupsSearch.json) (GET /marketplace/advertising/{site}/advertisers/{adv}/product_ads/ad_groups/search)：Search Ad Groups by items [Official](https://global-selling.mercadolibre.com/devsite/new-product-ads)
- [getAdsAdGroup](operations/getAdsAdGroup.json) (GET /marketplace/advertising/{site}/product_ads/ad_groups/{ad_group_id}/ads)：Ads of an Ad Group [Official](https://global-selling.mercadolibre.com/devsite/new-product-ads)
- [getAdsMetrics](operations/getAdsMetrics.json) (GET /marketplace/advertising/{advertiser_site_id}/advertisers/{advertiser_id}/product_ads/ads/search)：Ads metrics [Official](https://global-selling.mercadolibre.com/devsite/new-product-ads)
- [getAdvertisingAdvertisers](operations/getAdvertisingAdvertisers.json) (GET /advertising/advertisers)：Required parameters [Official](https://global-selling.mercadolibre.com/devsite/new-product-ads)
- [getByAdvertiserIdDisplayCampaigns](operations/getByAdvertiserIdDisplayCampaigns.json) (GET /advertising/advertisers/{advertiser_id}/display/campaigns)：Optional parameters [Official](https://global-selling.mercadolibre.com/devsite/display-gs)
- [getByCampaignIdLineItems](operations/getByCampaignIdLineItems.json) (GET /advertising/advertisers/{advertiser_id}/display/campaigns/{campaign_id}/line_items)：Optional parameters [Official](https://global-selling.mercadolibre.com/devsite/display-gs)
- [getByCampaignIdMetrics](operations/getByCampaignIdMetrics.json) (GET /advertising/advertisers/{advertiser_id}/display/campaigns/{campaign_id}/metrics)：Metrics of a campaign [Official](https://global-selling.mercadolibre.com/devsite/display-gs)
- [getByLineItemIdCreatives](operations/getByLineItemIdCreatives.json) (GET /advertising/advertisers/{advertiser_id}/display/campaigns/{campaign_id}/line_items/{line_item_id}/creatives)：Optional parameters [Official](https://global-selling.mercadolibre.com/devsite/display-gs)
- [getCampaignMetrics](operations/getCampaignMetrics.json) (GET /marketplace/advertising/{advertiser_site_id}/product_ads/campaigns/{campaign_id})：Campaign metrics [Official](https://global-selling.mercadolibre.com/devsite/new-product-ads)
- [getDisplayCampaigns](operations/getDisplayCampaigns.json) (GET /advertising/advertisers/61/display/campaigns)：Optional parameters [Official](https://global-selling.mercadolibre.com/devsite/display-gs)
- [getDisplayMetrics](operations/getDisplayMetrics.json) (GET /advertising/advertisers/{advertiser_id}/display/metrics)：Optional parameters [Official](https://global-selling.mercadolibre.com/devsite/display-gs)
- [getMetricsCampaign](operations/getMetricsCampaign.json) (GET /advertising/advertisers/{advertiser_id}/display/campaigns/80/metrics)：Metrics of a campaign [Official](https://global-selling.mercadolibre.com/devsite/display-gs)
- [modifyCampaign](operations/modifyCampaign.json) (PUT /marketplace/advertising/{advertiser_site_id}/product_ads/campaigns/{campaign_id})：Modify campaign [Official](https://global-selling.mercadolibre.com/devsite/new-product-ads)
- [searchAdGroupsByItems](operations/searchAdGroupsByItems.json) (GET /marketplace/advertising/{site}/advertisers/{adv}/product_ads/ads/search)：Search Ad Groups by items [Official](https://global-selling.mercadolibre.com/devsite/new-product-ads)
- [searchCampaigns](operations/searchCampaigns.json) (GET /marketplace/advertising/{advertiser_site_id}/advertisers/{advertiser_id}/product_ads/campaigns/search)：Search campaigns [Official](https://global-selling.mercadolibre.com/devsite/new-product-ads)
