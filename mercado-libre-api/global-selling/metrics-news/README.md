# Metrics & News

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Listings quality](https://global-selling.mercadolibre.com/devsite/listings-quality-gs) | 2 | 0 | modeled |
| [Official: Trends](https://global-selling.mercadolibre.com/devsite/trends-gs) | 4 | 0 | modeled |
| [Official: Visits](https://global-selling.mercadolibre.com/devsite/visits) | 4 | 0 | modeled |
| [Official: Product reviews](https://global-selling.mercadolibre.com/devsite/product-reviews) | 2 | 0 | modeled |
| [Official: Communications](https://global-selling.mercadolibre.com/devsite/seller-news) | 1 | 0 | modeled |
| [Official: Seller reputation](https://global-selling.mercadolibre.com/devsite/seller-reputation-global-selling) | 1 | 0 | modeled |
| [Official: Shopping experience](https://global-selling.mercadolibre.com/devsite/shopping-experience) | 3 | 0 | modeled |

## API List

- [checkGlobalAndMarketplaceSellersReputation](operations/checkGlobalAndMarketplaceSellersReputation.json) (GET /global/users/seller_reputation)：Check global and marketplace sellers reputation [Official](https://global-selling.mercadolibre.com/devsite/seller-reputation-global-selling)
- [getByItemIdPerformance](operations/getByItemIdPerformance.json) (GET /item/{item_id}/performance)：Quality detail by item [Official](https://global-selling.mercadolibre.com/devsite/listings-quality-gs)
- [getByResourceIdPurchaseExperience](operations/getByResourceIdPurchaseExperience.json) (GET /marketplace/user_products/MLAU1391786841/purchase_experience)：Call [Official](https://global-selling.mercadolibre.com/devsite/shopping-experience)
- [getByUpIdPurchaseExperience](operations/getByUpIdPurchaseExperience.json) (GET /marketplace/user_products/{up_id}/purchase_experience)：Call [Official](https://global-selling.mercadolibre.com/devsite/shopping-experience)
- [getCommunicationsNotices](operations/getCommunicationsNotices.json) (GET /communications/notices)：Optional parameters [Official](https://global-selling.mercadolibre.com/devsite/seller-news)
- [getDatedVisitsByItem](operations/getDatedVisitsByItem.json) (GET /items/{item_id}/visits/time_window)：Dated visits by item [Official](https://global-selling.mercadolibre.com/devsite/visits)
- [getItemById](operations/getItemById.json) (GET /reviews/item/{id})：Optional query parameters [Official](https://global-selling.mercadolibre.com/devsite/product-reviews)
- [getItemByItemId](operations/getItemByItemId.json) (GET /reviews/item/{item_id})：Functional flow [Official](https://global-selling.mercadolibre.com/devsite/product-reviews)
- [getItemsVisits](operations/getItemsVisits.json) (GET /items/visits)：Total visits by item between date ranges [Official](https://global-selling.mercadolibre.com/devsite/visits)
- [getMlaById](operations/getMlaById.json) (GET /trends/MLA/{id})：Trends by country and category [Official](https://global-selling.mercadolibre.com/devsite/trends-gs)
- [getQualityDetailByItem](operations/getQualityDetailByItem.json) (GET /item/{id}/performance)：Quality detail by item [Official](https://global-selling.mercadolibre.com/devsite/listings-quality-gs)
- [getShoppingExperience](operations/getShoppingExperience.json) (GET /marketplace/items/{item_id}/purchase_experience)：Shopping experience [Official](https://global-selling.mercadolibre.com/devsite/shopping-experience)
- [getTotalVisitsByItem](operations/getTotalVisitsByItem.json) (GET /visits/items)：Total visits by item [Official](https://global-selling.mercadolibre.com/devsite/visits)
- [getTrendsByCountryAndCategory](operations/getTrendsByCountryAndCategory.json) (GET /trends/{site_id}/{category_id})：Trends by country and category [Official](https://global-selling.mercadolibre.com/devsite/trends-gs)
- [getTrendsBySiteId](operations/getTrendsBySiteId.json) (GET /trends/{site_id})：Search for trends by country [Official](https://global-selling.mercadolibre.com/devsite/trends-gs)
- [getVisitsTimeWindow](operations/getVisitsTimeWindow.json) (GET /items/MCO471870973/visits/time_window)：Dated visits by item [Official](https://global-selling.mercadolibre.com/devsite/visits)
- [searchTrendsByCountry](operations/searchTrendsByCountry.json) (GET /trends/MLA)：Search for trends by country [Official](https://global-selling.mercadolibre.com/devsite/trends-gs)
