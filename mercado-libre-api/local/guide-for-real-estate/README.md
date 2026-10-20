# Guide for real estate

Local seller official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Introduction](https://developers.mercadolibre.com.ar/en_us/introduction-real-estate) | 0 | 0 | guide-only |
| [Official: Real estate experience](https://developers.mercadolibre.com.ar/en_us/real-estate-experience) | 10 | 0 | modeled |
| [Official: Manage users](https://developers.mercadolibre.com.ar/en_us/real-estate-manage-users) | 9 | 1 | partial |
| [Official: Search for vehicles](https://developers.mercadolibre.com.ar/en_us/search-for-vehicles) | 9 | 0 | modeled |
| [Official: Manage packages (Real Estate)](https://developers.mercadolibre.com.ar/en_us/manage-packages) | 4 | 0 | modeled |
| [Official: Categories and Attributes](https://developers.mercadolibre.com.ar/en_us/categories-and-attributes) | 3 | 0 | modeled |
| [Official: Locate properties](https://developers.mercadolibre.com.ar/en_us/locate-property) | 10 | 0 | modeled |
| [Official: List properties](https://developers.mercadolibre.com.ar/en_us/list-properties) | 3 | 0 | modeled |
| [Official: Sync listings](https://developers.mercadolibre.com.ar/en_us/real-estate-sync-listings) | 1 | 0 | modeled |
| [Official: Manage questions & contacts](https://developers.mercadolibre.com.ar/en_us/real-estate-manage-questions-contacts) | 13 | 1 | partial |
| [Official: Subscribe to our feeds](https://developers.mercadolibre.com.ar/en_us/real-estate-subscribe-to-our-feeds) | 6 | 0 | modeled |
| [Official: Real Estate developments](https://developers.mercadolibre.com.ar/en_us/real-estate-developments) | 10 | 0 | modeled |
| [Official: Details about the Whatsapp field for classifieds item](https://developers.mercadolibre.com.ar/en_us/details-about-the-whatsapp-field-for-classifieds-item) | 2 | 0 | modeled |
| [Official: Credits pre-approved](https://developers.mercadolibre.com.ar/en_us/credits-pre-approved) | 3 | 0 | modeled |

## API List

- [createCheckingAndUncheckingItems](operations/createCheckingAndUncheckingItems.json) (POST /vis-transactions-hub/{providerid}/entities/item-candidates)：Checking and unchecking items [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-experience)
- [createNewSettings](operations/createNewSettings.json) (POST /vis-transactions-hub/configurations/provider)：Create new settings [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-experience)
- [deleteBlockedUser](operations/deleteBlockedUser.json) (DELETE /users/{your_cust_id}/order_blacklist/{seller_id})：Delete blocked user [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-manage-users)
- [deleteQuotation](operations/deleteQuotation.json) (PUT /quotations/{quotationid})：Delete a quotation [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-developments)
- [generateSchedule](operations/generateSchedule.json) (GET /oauth/token)：Generate schedule [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-experience)
- [getBrowseNeighborhoods](operations/getBrowseNeighborhoods.json) (GET /classified_locations/neighborhoods/{neighborhoods_id})：Browse neighborhoods [Official](https://developers.mercadolibre.com.ar/en_us/locate-property)
- [getByUserIdContactsWhatsappTimeWindow](operations/getByUserIdContactsWhatsappTimeWindow.json) (GET /users/{user_id}/contacts/whatsapp/time_window)：By user [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-manage-questions-contacts)
- [getCategoryDump](operations/getCategoryDump.json) (GET /sites/{site_id}/categories/all)：Category Dump [Official](https://developers.mercadolibre.com.ar/en_us/categories-and-attributes)
- [getCitiesByCityId](operations/getCitiesByCityId.json) (GET /classified_locations/cities/{city_id})：City information [Official](https://developers.mercadolibre.com.ar/en_us/search-for-vehicles)
- [getClassifiedCityById](operations/getClassifiedCityById.json) (GET /classified_locations/cities/TUxBQ0NBUGZlZG1sYQ)：City information [Official](https://developers.mercadolibre.com.ar/en_us/search-for-vehicles)
- [getCollectionsByPaymentId](operations/getCollectionsByPaymentId.json) (GET /collections/{payment_id})：payments [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-subscribe-to-our-feeds)
- [getConsultAvailableCreditsSellerItems](operations/getConsultAvailableCreditsSellerItems.json) (GET /vis/loans/search)：Consult available credits for the seller's items [Official](https://developers.mercadolibre.com.ar/en_us/credits-pre-approved)
- [getConsultBlockedUsers](operations/getConsultBlockedUsers.json) (GET /users/{cuyour_cust_idst_id}/order_blacklist)：Consult blocked users [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-manage-users)
- [getContactsPhoneViews](operations/getContactsPhoneViews.json) (GET /items/{item_id}/contacts/phone_views)：By item [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-manage-questions-contacts)
- [getContactsPhoneViewsTimeWindow](operations/getContactsPhoneViewsTimeWindow.json) (GET /items/{item_id}/contacts/phone_views/time_window)：By item [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-manage-questions-contacts)
- [getContactsQuestions](operations/getContactsQuestions.json) (GET /users/{user_id}/contacts/questions)：By user [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-manage-questions-contacts)
- [getContactsWhatsapp](operations/getContactsWhatsapp.json) (GET /items/{item_id}/contacts/whatsapp)：By item [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-manage-questions-contacts)
- [getContactsWhatsappTimeWindow](operations/getContactsWhatsappTimeWindow.json) (GET /items/{item_id}/contacts/whatsapp/time_window)：By item [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-manage-questions-contacts)
- [getCountriesAr](operations/getCountriesAr.json) (GET /classified_locations/countries/AR)：Country information [Official](https://developers.mercadolibre.com.ar/en_us/search-for-vehicles)
- [getCountriesByCountryId](operations/getCountriesByCountryId.json) (GET /classified_locations/countries/{country_id})：Country information [Official](https://developers.mercadolibre.com.ar/en_us/search-for-vehicles)
- [getFeedHistoryApi](operations/getFeedHistoryApi.json) (GET /myfeeds)：Feed History API [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-subscribe-to-our-feeds)
- [getLoansByLoanId](operations/getLoansByLoanId.json) (GET /vis/loans/14b52fd8-85dc-11eb-8436-2753cb1f9665)：Details of the available credi [Official](https://developers.mercadolibre.com.ar/en_us/credits-pre-approved)
- [getNeighborhoodsByNeighborhoodId](operations/getNeighborhoodsByNeighborhoodId.json) (GET /classified_locations/neighborhoods/{neighborhood_id})：Neighborhood information [Official](https://developers.mercadolibre.com.ar/en_us/search-for-vehicles)
- [getClassifiedNeighborhoodById](operations/getClassifiedNeighborhoodById.json) (GET /classified_locations/neighborhoods/TUxBQkNBQjM4MDda)：Neighborhood information [Official](https://developers.mercadolibre.com.ar/en_us/search-for-vehicles)
- [getObtainingScheduleDetail](operations/getObtainingScheduleDetail.json) (GET /vis-transactions-hub/{providerid}/entities/schedules/{scheduleid})：Obtaining schedule detail [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-experience)
- [getObtainingStatusCheckedItems](operations/getObtainingStatusCheckedItems.json) (GET /vis-transactions-hub/{providerid}/entities/item-candidates/seller/{sellerid})：Obtaining status checked items [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-experience)
- [getPhoneViewsTimeWindow](operations/getPhoneViewsTimeWindow.json) (GET /users/{user_id}/contacts/phone_views/time_window)：By user [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-manage-questions-contacts)
- [getQuestionsTimeWindow](operations/getQuestionsTimeWindow.json) (GET /users/{user_id}/contacts/questions/time_window)：By user [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-manage-questions-contacts)
- [getSiteIdCategories](operations/getSiteIdCategories.json) (GET /sites/Site_id/categories)：Categories [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-developments)
- [getStatesByStateId](operations/getStatesByStateId.json) (GET /classified_locations/states/{state_id})：State information [Official](https://developers.mercadolibre.com.ar/en_us/search-for-vehicles)
- [getClassifiedStateById](operations/getClassifiedStateById.json) (GET /classified_locations/states/TUxBUENBUGw3M2E1)：State information [Official](https://developers.mercadolibre.com.ar/en_us/search-for-vehicles)
- [getThroughSellerId](operations/getThroughSellerId.json) (GET /vis-transactions-hub/configurations/seller/{sellerid})：Through sellerId [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-experience)
- [getWhatsappTimeWindow](operations/getWhatsappTimeWindow.json) (GET /items/contacts/whatsapp/time_window)：By item [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-manage-questions-contacts)
- [getWithProviderId](operations/getWithProviderId.json) (GET /vis-transactions-hub/configurations/provider/{providerid})：With providerId [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-experience)
- [queryListingPackagesEngagedByUser](operations/queryListingPackagesEngagedByUser.json) (GET /users/{user_id}/classifieds_promotion_packs/{listing_type})：Query listing packages engaged by a user [Official](https://developers.mercadolibre.com.ar/en_us/manage-packages)
- [searchQuotation](operations/searchQuotation.json) (GET /quotations/{id})：Search a quotation [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-developments)
- [searchQuotationGetByQuotationid](operations/searchQuotationGetByQuotationid.json) (GET /quotations/{quotationid})：Search a quotation [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-developments)
- [searchQuotationsPerItemId](operations/searchQuotationsPerItemId.json) (GET /quotations/items_ids)：Search quotations per item id [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-developments)
- [searchReportQuotationsPerSeller](operations/searchReportQuotationsPerSeller.json) (GET /quotations/report)：Search report of quotations per seller [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-developments)
- [updateHowLoadWhatsappFieldViaApi](operations/updateHowLoadWhatsappFieldViaApi.json) (PUT /items/ITEM)：4. How to load the Whatsapp field via API? [Official](https://developers.mercadolibre.com.ar/en_us/details-about-the-whatsapp-field-for-classifieds-item)
- [updatePriceEditingIncreaseOrDecreaseUnits](operations/updatePriceEditingIncreaseOrDecreaseUnits.json) (PUT /vis-transactions-hub/{providerid}/entities/items)：Price editing, increase or decrease of units [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-experience)
- [updateSettings](operations/updateSettings.json) (PATCH /vis-transactions-hub/configurations/provider/{providerid})：Update Settings [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-experience)
- [updateVisitFail](operations/updateVisitFail.json) (PUT /vis-transactions-hub/{providerid}/entities/schedules)：Visit_fail [Official](https://developers.mercadolibre.com.ar/en_us/real-estate-experience)
