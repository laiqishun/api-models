---
title: "Lazada Sponsored Solutions API"
description: "The API to createCampaign,updateCampaign."
---

# API List

- [addAdgroupBatch](operations/add-adgroup-batch.json) (GET/POST /sponsor/solutions/adgroup/addAdgroupBatch) — Do add adgroup for one campaign.
- [addSolution](operations/add-solution.json) (POST /sponsor/solutions/addSolution) — Add sponsor solution
- [clickserver](operations/clickserver.json) (GET/POST /gproject/ads/aidc/click) — aidc click server interface
- [deleteAdgroupBatch](operations/delete-adgroup-batch.json) (GET/POST /sponsor/solutions/adgroup/deleteAdgroupBatch) — Delete adgroup batch.
- [deleteCampaign](operations/delete-campaign.json) (GET/POST /sponsor/solutions/campaign/deleteCampaign) — Delete campaign.
- [getAccountSignInfo](operations/get-account-sign-info.json) (GET /sponsor/solutions/account/getAccountSignInfo) — Get seller account sign status.
- [getAutoTopUpOptionOneConfig](operations/get-auto-top-up-option-one-config.json) (GET/POST /sponsor/solutions/wallet/getAutoTopUpOptionOneConfig) — Get auto top up option one config.
- [getCampaign](operations/get-campaign.json) (GET/POST /sponsor/solutions/campaign/getCampaign) — Get campaign list with bizCode by seller.
- [getCampaignCount](operations/get-campaign-count.json) (GET/POST /sponsor/solutions/campaign/getCampaignCount) — Get campaign count with bizCode for each solution type.
- [getDiscoveryReportAdgroup](operations/get-discovery-report-adgroup.json) (GET/POST /sponsor/solutions/report/getDiscoveryReportAdgroup) — Get sponsored discovery report adgroup level
- [getDiscoveryReportAudience](operations/get-discovery-report-audience.json) (GET/POST /sponsor/solutions/report/getDiscoveryReportAudience) — Get sponsored discovery report audience level
- [getDiscoveryReportCampaign](operations/get-discovery-report-campaign.json) (GET/POST /sponsor/solutions/report/getDiscoveryReportCampaign) — Get sponsored discovery report campaign level
- [getDiscoveryReportKeyword](operations/get-discovery-report-keyword.json) (GET/POST /sponsor/solutions/report/getDiscoveryReportKeyword) — Get sponsored discovery report keyword level
- [getLatestSignInfo](operations/get-latest-sign-info.json) (GET /sponsor/solutions/account/getLatestSignInfo) — Get the latest url of sign(T&C).
- [getReportCampaignOnFIrstSlot](operations/get-report-campaign-on-f-irst-slot.json) (GET/POST /sponsor/solutions/report/getReportCampaignOnPrePlacement) — Get sponsored discovery report campaign first slot
- [getReportOverview](operations/get-report-overview.json) (GET/POST /sponsor/solutions/report/getReportOverview) — Get report overview.
- [getReportOverviewMetric](operations/get-report-overview-metric.json) (GET/POST /sponsor/solutions/report/getReportOverviewMetric) — get report overview metric
- [listCategory](operations/list-category.json) (GET/POST /sponsor/solutions/category/listCategory) — list category
- [listKeywordByAdgroup](operations/list-keyword-by-adgroup.json) (GET/POST /sponsor/solutions/keyword/listKeywordByAdgroup) — List keyword by adgroup.
- [listKeywordByItem](operations/list-keyword-by-item.json) (GET/POST /sponsor/solutions/keyword/listKeywordByItem) — List keyword by item.
- [modifyAutoTopUpOptionOneConfig](operations/modify-auto-top-up-option-one-config.json) (GET/POST /sponsor/solutions/wallet/modifyAutoTopUpOptionOneConfig) — Modify auto top up option one config.1. each country has differect tax rate
2. we have minimum and maximam top-up amount limitation.For SG, min=5, max = 8,333,333,330;for PH, min=100,Max=17,895,600;for TH, min=100,max=8,
- [searchAdgroupList](operations/search-adgroup-list.json) (GET/POST /sponsor/solutions/adgroup/searchAdgroupList) — Search adgroup with bizCode by seller.
- [searchCampaignList](operations/search-campaign-list.json) (GET/POST /sponsor/solutions/campaign/searchCampaignList) — Search campaign list with bizCode for sellers.
- [searchKeyword](operations/search-keyword.json) (GET/POST /sponsor/solutions/keyword/searchKeyword) — Search keyword with specific word.
- [searchProductWithPage](operations/search-product-with-page.json) (GET/POST /sponsor/solutions/product/searchProductWithPage) — Search product.
- [sign](operations/sign.json) (GET/POST /sponsor/solutions/account/sign) — Description: Do sign for seller. Seller or agencies can use this api to sign up the t&c.
Timeout Period： the api timeout is 10s, max qps is 300, make sure do not over these num, especially qps, otherwise you may be black
- [updateAdgroupBatch](operations/update-adgroup-batch.json) (GET/POST /sponsor/solutions/adgroup/updateAdgroupBatch) — Update adgroup batch.
- [updateCampaign](operations/update-campaign.json) (GET/POST /sponsor/solutions/campaign/updateCampaign) — Update campaign with status field.

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
