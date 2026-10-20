# API resources

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Items & Searches](https://global-selling.mercadolibre.com/devsite/items-and-searches-global-selling) | 7 | 0 | modeled |
| [Official: Location](https://global-selling.mercadolibre.com/devsite/location-global-selling) | 4 | 0 | modeled |
| [Official: Shipping](https://global-selling.mercadolibre.com/devsite/shipping-global-selling) | 6 | 0 | modeled |
| [Official: Paging results](https://global-selling.mercadolibre.com/devsite/paging-results-global-selling) | 1 | 0 | modeled |
| [Official: Receive notifications](https://global-selling.mercadolibre.com/devsite/receive-notifications) | 15 | 0 | modeled |
| [Official: Moderations](https://global-selling.mercadolibre.com/devsite/moderations-gs) | 2 | 0 | modeled |
| [Official: What is the Brand Protection Program?](https://global-selling.mercadolibre.com/devsite/what-is-the-brand-protection-program) | 0 | 0 | guide-only |
| [Official: Program Members](https://global-selling.mercadolibre.com/devsite/program-members) | 6 | 0 | modeled |
| [Official: Reported listings](https://global-selling.mercadolibre.com/devsite/reported-listings) | 5 | 0 | modeled |
| [Official: Official Stores](https://global-selling.mercadolibre.com/devsite/official-storesglobal-selling) | 4 | 0 | modeled |

## API List

- [checkReportStatus](operations/checkReportStatus.json) (GET /moderations/pppi/case/{denounce_id})：Check report status [Official](https://global-selling.mercadolibre.com/devsite/program-members)
- [createRespondSeller](operations/createRespondSeller.json) (POST /moderations/pppi/case/{denounce_id})：Respond to the seller [Official](https://global-selling.mercadolibre.com/devsite/program-members)
- [getAllowsPrintTicketSendOrder](operations/getAllowsPrintTicketSendOrder.json) (GET /marketplace/shipments/{shipment_id}/labels)：Allows print the ticket for send the order. [Official](https://global-selling.mercadolibre.com/devsite/shipping-global-selling)
- [getGlobalStoreBrandDetails](operations/getGlobalStoreBrandDetails.json) (GET /users/{user_id}/brands/aaaaa)：Obtain all information about a specific brand [Official](https://global-selling.mercadolibre.com/devsite/official-storesglobal-selling)
- [getBrandsByBrandId](operations/getBrandsByBrandId.json) (GET /users/{user_id}/brands/{brand_id})：Obtain all information about a specific brand [Official](https://global-selling.mercadolibre.com/devsite/official-storesglobal-selling)
- [getByUserIdShippingPreferences](operations/getByUserIdShippingPreferences.json) (GET /users/{user_id}/shipping_preferences)：Retrieves all shipping modes and services available to user. [Official](https://global-selling.mercadolibre.com/devsite/shipping-global-selling)
- [getCaseById](operations/getCaseById.json) (GET /moderations/pppi/case/{id})：Check report status [Official](https://global-selling.mercadolibre.com/devsite/program-members)
- [getFilterByTopic](operations/getFilterByTopic.json) (GET /myfeeds)：Filter by topic [Official](https://global-selling.mercadolibre.com/devsite/receive-notifications)
- [getInfractionsByUser](operations/getInfractionsByUser.json) (GET /marketplace/moderations/infractions/{id})：Get infractions by user [Official](https://global-selling.mercadolibre.com/devsite/moderations-gs)
- [getInfractionsByUserId](operations/getInfractionsByUserId.json) (GET /marketplace/moderations/infractions/{user_id})：Get infractions by user [Official](https://global-selling.mercadolibre.com/devsite/moderations-gs)
- [getItemsByItemId](operations/getItemsByItemId.json) (GET /items/{item_id})：items [Official](https://global-selling.mercadolibre.com/devsite/receive-notifications)
- [getItemsBySearchQuery](operations/getItemsBySearchQuery.json) (GET /marketplace/users/{user_id}/items/search)：Get items by a search query. [Official](https://global-selling.mercadolibre.com/devsite/items-and-searches-global-selling)
- [getItemsFromListingsByNickname](operations/getItemsFromListingsByNickname.json) (GET /sites/{site_id}/search)：Get items from the listings by nickname. [Official](https://global-selling.mercadolibre.com/devsite/items-and-searches-global-selling)
- [getItemsMappings](operations/getItemsMappings.json) (GET /items/{item_id}/marketplace_items)：Get the items mappings. [Official](https://global-selling.mercadolibre.com/devsite/items-and-searches-global-selling)
- [getItemsSearch](operations/getItemsSearch.json) (GET /marketplace/users/{merchant_id}/items/search)：Call [Official](https://global-selling.mercadolibre.com/devsite/items-and-searches-global-selling)
- [getItmOptions](operations/getItmOptions.json) (GET /moderations/pppi/denounces/MLA/ITM/options)：View available reasons [Official](https://global-selling.mercadolibre.com/devsite/program-members)
- [getMarketplaceClaims](operations/getMarketplaceClaims.json) (GET /marketplace/claims/{resource})：marketplace claims [Official](https://global-selling.mercadolibre.com/devsite/receive-notifications)
- [getMarketplaceFbmStock](operations/getMarketplaceFbmStock.json) (GET /{resource})：marketplace fbm stock [Official](https://global-selling.mercadolibre.com/devsite/receive-notifications)
- [getMarketplaceItems](operations/getMarketplaceItems.json) (GET /marketplace/items/{item_id})：marketplace items [Official](https://global-selling.mercadolibre.com/devsite/receive-notifications)
- [getMarketplaceMessages](operations/getMarketplaceMessages.json) (GET /marketplace/messages/{resource})：marketplace messages [Official](https://global-selling.mercadolibre.com/devsite/receive-notifications)
- [getMarketplaceOrders](operations/getMarketplaceOrders.json) (GET /marketplace/orders/{order_id})：marketplace orders [Official](https://global-selling.mercadolibre.com/devsite/receive-notifications)
- [getMarketplacePricingSuggestion](operations/getMarketplacePricingSuggestion.json) (GET /marketplace/benchmarks/items/{item_id}/details)：marketplace pricing suggestion [Official](https://global-selling.mercadolibre.com/devsite/receive-notifications)
- [getMarketplaceQuestions](operations/getMarketplaceQuestions.json) (GET /marketplace/questions/{question_id})：marketplace questions [Official](https://global-selling.mercadolibre.com/devsite/receive-notifications)
- [getMarketplaceShipments](operations/getMarketplaceShipments.json) (GET /marketplace/shipments/{resource})：marketplace shipments [Official](https://global-selling.mercadolibre.com/devsite/receive-notifications)
- [getMarketplaceUserProducts](operations/getMarketplaceUserProducts.json) (GET /marketplace/user_products/{up_id})：Marketplace User Products: [Official](https://global-selling.mercadolibre.com/devsite/receive-notifications)
- [getMarketplaceUserProductsFamilies](operations/getMarketplaceUserProductsFamilies.json) (GET /user-products-families/{family_id})：Marketplace User Products Families: [Official](https://global-selling.mercadolibre.com/devsite/receive-notifications)
- [getMlmShippingOptions](operations/getMlmShippingOptions.json) (GET /sites/MLM/shipping_options)：Retrieves the cost of a shipping. Shipping cost calculator per country. [Official](https://global-selling.mercadolibre.com/devsite/shipping-global-selling)
- [getMultigetWithMultipleNumbersItems](operations/getMultigetWithMultipleNumbersItems.json) (GET /items)：Multiget with multiple numbers of items. [Official](https://global-selling.mercadolibre.com/devsite/items-and-searches-global-selling)
- [getMultigetWithMultipleNumbersUsers](operations/getMultigetWithMultipleNumbersUsers.json) (GET /users)：Multiget with multiple numbers of users. [Official](https://global-selling.mercadolibre.com/devsite/items-and-searches-global-selling)
- [getPppiCases](operations/getPppiCases.json) (GET /moderations/pppi/cases)：Required parameters [Official](https://global-selling.mercadolibre.com/devsite/reported-listings)
- [getPublicCandidates](operations/getPublicCandidates.json) (GET /marketplace/seller-promotions/promotions/candidate/{candidate_id}/&USER_ID)：public candidates [Official](https://global-selling.mercadolibre.com/devsite/receive-notifications)
- [getPublicOffers](operations/getPublicOffers.json) (GET /marketplace/seller-promotions/promotions/offer/{offer_id}/{user_id})：public offers [Official](https://global-selling.mercadolibre.com/devsite/receive-notifications)
- [getRetrievesAllDeliveryData](operations/getRetrievesAllDeliveryData.json) (GET /marketplace/shipments/{shipment_id})：Retrieves all delivery data. [Official](https://global-selling.mercadolibre.com/devsite/shipping-global-selling)
- [getRetrievesShippingModesAvailableInCountry](operations/getRetrievesShippingModesAvailableInCountry.json) (GET /sites/MLM/shipping_methods)：Retrieves shipping modes available in a country. [Official](https://global-selling.mercadolibre.com/devsite/shipping-global-selling)
- [getUsersByMerchantId](operations/getUsersByMerchantId.json) (GET /marketplace/users/{merchant_id})：Required Parameters [Official](https://global-selling.mercadolibre.com/devsite/items-and-searches-global-selling)
- [obtainAllInformationAboutSpecificBrand](operations/obtainAllInformationAboutSpecificBrand.json) (GET /users/{user_id}/brands/{id})：Obtain all information about a specific brand [Official](https://global-selling.mercadolibre.com/devsite/official-storesglobal-selling)
- [postByShipmentIdTracking](operations/postByShipmentIdTracking.json) (POST /marketplace/shipments/{shipment_id}/tracking)：This endpoint allows you to report the tracking of a shipment, which must be entered by parameter. [Official](https://global-selling.mercadolibre.com/devsite/shipping-global-selling)
- [putCaseFiles](operations/putCaseFiles.json) (PUT /moderations/pppi/case/files)：Required parameters [Official](https://global-selling.mercadolibre.com/devsite/reported-listings)
- [searchCityById](operations/searchCityById.json) (GET /cities/Q04tQkpCZWlqaW5n)：Search for a city by id [Official](https://global-selling.mercadolibre.com/devsite/location-global-selling)
- [searchCountry](operations/searchCountry.json) (GET /countries)：Search for a country [Official](https://global-selling.mercadolibre.com/devsite/location-global-selling)
- [searchCountryById](operations/searchCountryById.json) (GET /countries/AR)：Search for a country by id [Official](https://global-selling.mercadolibre.com/devsite/location-global-selling)
- [searchStateById](operations/searchStateById.json) (GET /states/AR-B)：Search for a state by id [Official](https://global-selling.mercadolibre.com/devsite/location-global-selling)
- [submitReport](operations/submitReport.json) (POST /moderations/pppi/denounces/items/{item_id})：Submit a report [Official](https://global-selling.mercadolibre.com/devsite/program-members)
- [submitResponseReport](operations/submitResponseReport.json) (POST /moderations/pppi/case/{id})：3. Submit a response to the report [Official](https://global-selling.mercadolibre.com/devsite/reported-listings)
- [viewAvailableReasons](operations/viewAvailableReasons.json) (GET /moderations/pppi/denounces/{site_id}/ITM/options)：View available reasons [Official](https://global-selling.mercadolibre.com/devsite/program-members)
- [viewDetailsReportedItem](operations/viewDetailsReportedItem.json) (GET /moderations/pppi/case/{case_id})：View details of a reported item [Official](https://global-selling.mercadolibre.com/devsite/reported-listings)
