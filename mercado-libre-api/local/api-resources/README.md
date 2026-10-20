# API resources

Local seller official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Users & Apps](https://developers.mercadolibre.com.ar/en_us/usuarios-y-aplicaciones) | 14 | 0 | modeled |
| [Official: Manage users](https://developers.mercadolibre.com.ar/en_us/services-manage-users) | 4 | 0 | modeled |
| [Official: User´s addresess](https://developers.mercadolibre.com.ar/en_us/users-addresses) | 1 | 0 | modeled |
| [Official: Bookmarks](https://developers.mercadolibre.com.ar/en_us/bookmarks) | 3 | 0 | modeled |
| [Official: Attributes](https://developers.mercadolibre.com.ar/en_us/attributes) | 10 | 3 | partial |
| [Official: Domains and Categories](https://developers.mercadolibre.com.ar/en_us/categories-and-listings) | 9 | 0 | modeled |
| [Official: Locations & Currencies](https://developers.mercadolibre.com.ar/en_us/locations-and-currencies) | 9 | 0 | modeled |
| [Official: Items & Searches](https://developers.mercadolibre.com.ar/en_us/items-and-searches) | 6 | 0 | modeled |
| [Official: Questions & Answers](https://developers.mercadolibre.com.ar/en_us/questions) | 9 | 0 | modeled |
| [Official: Orders & Feedback](https://developers.mercadolibre.com.ar/en_us/order-management) | 12 | 1 | partial |
| [Official: Metrics](https://developers.mercadolibre.com.ar/en_us/metrics) | 9 | 0 | modeled |
| [Official: Shipping](https://developers.mercadolibre.com.ar/en_us/shipping) | 6 | 0 | modeled |
| [Official: Notifications](https://developers.mercadolibre.com.ar/en_us/products-receive-notifications) | 15 | 0 | modeled |
| [Official: Sellers news](https://developers.mercadolibre.com.ar/en_us/know-the-news-that-sellers-receive) | 1 | 0 | modeled |
| [Official: Manage moderations](https://developers.mercadolibre.com.ar/en_us/manage-moderations) | 4 | 0 | modeled |
| [Official: Moderation with pause](https://developers.mercadolibre.com.ar/en_us/moderations-paused) | 4 | 0 | modeled |
| [Official: Image diagnostics](https://developers.mercadolibre.com.ar/en_us/image-diagnostics) | 1 | 0 | modeled |
| [Official: Image Moderation](https://developers.mercadolibre.com.ar/en_us/image-moderation) | 1 | 0 | modeled |
| [Official: Whats is Brand Protection Program?](https://developers.mercadolibre.com.ar/en_us/whats-is-brand-protection-program) | 0 | 0 | guide-only |
| [Official: Member of the program](https://developers.mercadolibre.com.ar/en_us/member-of-the-program) | 7 | 0 | modeled |
| [Official: Complained publications](https://developers.mercadolibre.com.ar/en_us/complained-publications) | 6 | 0 | modeled |

## API List

- [changeAndOrAddAttributes](operations/changeAndOrAddAttributes.json) (PUT /items/{item_id})：Change and/or add attributes [Official](https://developers.mercadolibre.com.ar/en_us/attributes)
- [checkComplaintStatus](operations/checkComplaintStatus.json) (GET /moderations/pppi/case/{denounce_id})：Check a complaint status [Official](https://developers.mercadolibre.com.ar/en_us/member-of-the-program)
- [checkUserQuestionsBlacklistWithLimitAndOffset](operations/checkUserQuestionsBlacklistWithLimitAndOffset.json) (GET /users/{seller_id}/questions_blacklist)：Check user's questions blacklist (With limit and offset). [Official](https://developers.mercadolibre.com.ar/en_us/questions)
- [checkUserQuestionsBlacklistWithoutOffsetAndLimit](operations/checkUserQuestionsBlacklistWithoutOffsetAndLimit.json) (GET /users/${seller_id}/questions_blacklist)：Check user's questions blacklist (Without offset and limit) [Official](https://developers.mercadolibre.com.ar/en_us/questions)
- [createAnswerQuestion](operations/createAnswerQuestion.json) (POST /answers)：Answer a question. [Official](https://developers.mercadolibre.com.ar/en_us/questions)
- [createBookmarkItem](operations/createBookmarkItem.json) (POST /users/me/bookmarks)：Bookmark an item [Official](https://developers.mercadolibre.com.ar/en_us/bookmarks)
- [createDarUnaOpinionSobreUnPedido](operations/createDarUnaOpinionSobreUnPedido.json) (POST /orders/{order_id}/feedback)：Dar una opinión sobre un pedido [Official](https://developers.mercadolibre.com.ar/en_us/order-management)
- [createItemWithAttributesPostItems](operations/createItemWithAttributesPostItems.json) (POST /items)：Create an item with attributes [Official](https://developers.mercadolibre.com.ar/en_us/attributes)
- [createMakeComplaint](operations/createMakeComplaint.json) (POST /moderations/pppi/denounces/items/{item_id})：Make a complaint [Official](https://developers.mercadolibre.com.ar/en_us/member-of-the-program)
- [createMakeQuestion](operations/createMakeQuestion.json) (POST /questions)：Make a question [Official](https://developers.mercadolibre.com.ar/en_us/questions)
- [createWhenAndHowUseIt](operations/createWhenAndHowUseIt.json) (POST /moderations/pictures/diagnostic)：When and how to use it [Official](https://developers.mercadolibre.com.ar/en_us/image-diagnostics)
- [deleteApplicationsByAppId](operations/deleteApplicationsByAppId.json) (DELETE /users/{cust_id}/applications/{app_id})：Revoke permissions to an application. [Official](https://developers.mercadolibre.com.ar/en_us/usuarios-y-aplicaciones)
- [deleteOrderBlacklistById](operations/deleteOrderBlacklistById.json) (DELETE /users/{user_id}/order_blacklist/{id})：Desbloquear a usuarios para hacer una oferta en un ítem. [Official](https://developers.mercadolibre.com.ar/en_us/order-management)
- [getAllowsPrintTicketSendOrderGetShipmentLabels](operations/getAllowsPrintTicketSendOrderGetShipmentLabels.json) (GET /shipment_labels)：Allows print the ticket for send the order. [Official](https://developers.mercadolibre.com.ar/en_us/shipping)
- [getAllSitesGetSites](operations/getAllSitesGetSites.json) (GET /sites)：Get all sites. [Official](https://developers.mercadolibre.com.ar/en_us/categories-and-listings)
- [getAllZipCodesBetweenTwoGivenValuesZipCodes](operations/getAllZipCodesBetweenTwoGivenValuesZipCodes.json) (GET /country/AR/zip_codes/search_between)：Get all zip codes between two given values of zip codes. [Official](https://developers.mercadolibre.com.ar/en_us/locations-and-currencies)
- [getAssignmentV1](operations/getAssignmentV1.json) (GET /flex/sites/{site_id}/shipments/{shipment_id}/assignment/v1)：public offers [Official](https://developers.mercadolibre.com.ar/en_us/products-receive-notifications)
- [getAvailabilityListingTypeAvailabilityByUserAndCategory](operations/getAvailabilityListingTypeAvailabilityByUserAndCategory.json) (GET /users/{user_id}/classifieds_promotion_packs/silver)：Get the availability Listing Type availability by user and category. [Official](https://developers.mercadolibre.com.ar/en_us/usuarios-y-aplicaciones)
- [getBuscarLosPedidosPorVendedor](operations/getBuscarLosPedidosPorVendedor.json) (GET /orders/search)：Buscar los pedidos por vendedor [Official](https://developers.mercadolibre.com.ar/en_us/order-management)
- [getByItemIdShippingOptions](operations/getByItemIdShippingOptions.json) (GET /items/{item_id}/shipping_options)：Get visits by user and time [Official](https://developers.mercadolibre.com.ar/en_us/shipping)
- [getByOrderIdProduct](operations/getByOrderIdProduct.json) (GET /orders/{order_id}/product)：Obtener información específica del producto vendido dentro del pedido. [Official](https://developers.mercadolibre.com.ar/en_us/order-management)
- [getByResource](operations/getByResource.json) (GET /{resource})：payments [Official](https://developers.mercadolibre.com.ar/en_us/products-receive-notifications)
- [getBySellerIdItemsSearch](operations/getBySellerIdItemsSearch.json) (GET /users/{seller_id}/items/search)：Items with loss of exposure [Official](https://developers.mercadolibre.com.ar/en_us/items-and-searches)
- [getBySiteIdShippingMethods](operations/getBySiteIdShippingMethods.json) (GET /sites/{site_id}/shipping_methods)：Retrieves shipping modes available in a country. [Official](https://developers.mercadolibre.com.ar/en_us/shipping)
- [getByUserIdAcceptedPaymentMethods](operations/getByUserIdAcceptedPaymentMethods.json) (GET /users/{user_id}/accepted_payment_methods)：Get accepted payment methods by user. [Official](https://developers.mercadolibre.com.ar/en_us/usuarios-y-aplicaciones)
- [getByUserIdAddresses](operations/getByUserIdAddresses.json) (GET /users/{user_id}/addresses)：Get user addresses. [Official](https://developers.mercadolibre.com.ar/en_us/usuarios-y-aplicaciones)
- [getByUserIdBrands](operations/getByUserIdBrands.json) (GET /users/{user_id}/brands)：Get brands by user. [Official](https://developers.mercadolibre.com.ar/en_us/usuarios-y-aplicaciones)
- [getByUserIdOrderBlacklist](operations/getByUserIdOrderBlacklist.json) (GET /users/:userID/order_blacklist)：Respuesta [Official](https://developers.mercadolibre.com.ar/en_us/order-management)
- [getCandidatesByCandidateId](operations/getCandidatesByCandidateId.json) (GET /seller-promotions/candidates/{candidate_id})：public candidates [Official](https://developers.mercadolibre.com.ar/en_us/products-receive-notifications)
- [getCaseByCaseId](operations/getCaseByCaseId.json) (GET /moderations/pppi/case/{case_id})：Consult details of a reported item [Official](https://developers.mercadolibre.com.ar/en_us/complained-publications)
- [getCatalogSuggestions](operations/getCatalogSuggestions.json) (GET /catalog_suggestions/{suggestion_id})：catalog suggestions [Official](https://developers.mercadolibre.com.ar/en_us/products-receive-notifications)
- [getCategoryAvailability](operations/getCategoryAvailability.json) (GET /users/{user_id}/available_listing_type/gold_special)：Get category availability. [Official](https://developers.mercadolibre.com.ar/en_us/usuarios-y-aplicaciones)
- [getCategoryPredictor](operations/getCategoryPredictor.json) (GET /sites/{site_id}/domain_discovery/search)：Category predictor. [Official](https://developers.mercadolibre.com.ar/en_us/categories-and-listings)
- [getCityInformation](operations/getCityInformation.json) (GET /classified_locations/cities/TUxVQ0NBQjY1MmQ1)：Get city information. [Official](https://developers.mercadolibre.com.ar/en_us/locations-and-currencies)
- [getConsultDetailsReportedItem](operations/getConsultDetailsReportedItem.json) (GET /moderations/pppi/case/{id})：Consult details of a reported item [Official](https://developers.mercadolibre.com.ar/en_us/complained-publications)
- [getConsultEnabledMotives](operations/getConsultEnabledMotives.json) (GET /moderations/pppi/denounces/{site_id}/ITM/options)：Consult enabled motives [Official](https://developers.mercadolibre.com.ar/en_us/member-of-the-program)
- [getConsultUserInfractionHistory](operations/getConsultUserInfractionHistory.json) (GET /moderations/infractions/{user_id})：Consult user infraction history [Official](https://developers.mercadolibre.com.ar/en_us/manage-moderations)
- [getCountryDetail](operations/getCountryDetail.json) (GET /classified_locations/countries/UY)：Get country detail [Official](https://developers.mercadolibre.com.ar/en_us/locations-and-currencies)
- [getCurrencyDetails](operations/getCurrencyDetails.json) (GET /currencies/CLP)：Get currency details. [Official](https://developers.mercadolibre.com.ar/en_us/locations-and-currencies)
- [getDetalleDeMetodoDePago](operations/getDetalleDeMetodoDePago.json) (GET /sites/{site_id}/payment_methods/amex)：Detalle de método de pago [Official](https://developers.mercadolibre.com.ar/en_us/order-management)
- [getGetsCategoryDetail](operations/getGetsCategoryDetail.json) (GET /categories/{category_id})：Gets category detail. [Official](https://developers.mercadolibre.com.ar/en_us/categories-and-listings)
- [getGetsCategoryTreeBySite](operations/getGetsCategoryTreeBySite.json) (GET /sites/{site_id}/categories)：Gets the category tree by site. [Official](https://developers.mercadolibre.com.ar/en_us/categories-and-listings)
- [getGetsPriceList](operations/getGetsPriceList.json) (GET /sites/{site_id}/listing_prices)：Gets price list. [Official](https://developers.mercadolibre.com.ar/en_us/categories-and-listings)
- [getHistoricNotificationsByAppGetMissedFeeds](operations/getHistoricNotificationsByAppGetMissedFeeds.json) (GET /missed_feeds)：Get historic of notifications by app. [Official](https://developers.mercadolibre.com.ar/en_us/usuarios-y-aplicaciones)
- [getInformationAboutCountries](operations/getInformationAboutCountries.json) (GET /classified_locations/countries)：Get information about countries. [Official](https://developers.mercadolibre.com.ar/en_us/locations-and-currencies)
- [getInfractionsById](operations/getInfractionsById.json) (GET /moderations/infractions/{id})：Consult user infraction history [Official](https://developers.mercadolibre.com.ar/en_us/manage-moderations)
- [getItemCompetition](operations/getItemCompetition.json) (GET /items/{item_id}/price_to_win)：item competition [Official](https://developers.mercadolibre.com.ar/en_us/products-receive-notifications)
- [getItems](operations/getItems.json) (GET /items)：Multiget [Official](https://developers.mercadolibre.com.ar/en_us/items-and-searches)
- [getItemsPrices](operations/getItemsPrices.json) (GET /items/{item_id}/prices)：items_prices [Official](https://developers.mercadolibre.com.ar/en_us/products-receive-notifications)
- [getItemsWithLossExposure](operations/getItemsWithLossExposure.json) (GET /users/{user_id}/items/search)：Items with loss of exposure [Official](https://developers.mercadolibre.com.ar/en_us/items-and-searches)
- [getItemVisits](operations/getItemVisits.json) (GET /items/{item_id}/visits/time_window)：Get item's visits. [Official](https://developers.mercadolibre.com.ar/en_us/metrics)
- [getItemVisitsMultiGet](operations/getItemVisitsMultiGet.json) (GET /items/visits/time_window)：Get item's visits (Multi Get) [Official](https://developers.mercadolibre.com.ar/en_us/metrics)
- [getLastModerationByModerationReferenceId](operations/getLastModerationByModerationReferenceId.json) (GET /moderations/last_moderation/{moderation_reference_id})：Recommended flow [Official](https://developers.mercadolibre.com.ar/en_us/manage-moderations)
- [getLeadsCredits](operations/getLeadsCredits.json) (GET /vis/loans/{credit_id})：Leads credits [Official](https://developers.mercadolibre.com.ar/en_us/products-receive-notifications)
- [getLocationInformationByZipCode](operations/getLocationInformationByZipCode.json) (GET /countries/AR/zip_codes/{id})：Get location information by zip code. [Official](https://developers.mercadolibre.com.ar/en_us/locations-and-currencies)
- [getMandatoryParameters](operations/getMandatoryParameters.json) (GET /moderations/pppi/cases)：Mandatory parameters [Official](https://developers.mercadolibre.com.ar/en_us/complained-publications)
- [getMessagesByResource](operations/getMessagesByResource.json) (GET /messages/{resource})：Messages: [Official](https://developers.mercadolibre.com.ar/en_us/products-receive-notifications)
- [getMlaItmOptions](operations/getMlaItmOptions.json) (GET /moderations/pppi/denounces/MLA/ITM/options)：Consult enabled motives [Official](https://developers.mercadolibre.com.ar/en_us/member-of-the-program)
- [getMlaJacketsAndCoatsTechnicalSpecs](operations/getMlaJacketsAndCoatsTechnicalSpecs.json) (GET /domains/MLA-JACKETS_AND_COATS/technical_specs)：Obtains domain information. [Official](https://developers.mercadolibre.com.ar/en_us/categories-and-listings)
- [getModerationItemWithoutSales](operations/getModerationItemWithoutSales.json) (GET /moderations/last_moderation/MLA123444123-ITM)：Moderation for item without sales [Official](https://developers.mercadolibre.com.ar/en_us/moderations-paused)
- [getModerationUnusualPriceChange](operations/getModerationUnusualPriceChange.json) (GET /moderations/last_moderation/MLA926647862-ITM)：Moderation for unusual price change [Official](https://developers.mercadolibre.com.ar/en_us/moderations-paused)
- [getObtainsListExposuresBySite](operations/getObtainsListExposuresBySite.json) (GET /sites/{site_id}/listing_exposures)：Obtains list of exposures by site. [Official](https://developers.mercadolibre.com.ar/en_us/categories-and-listings)
- [getObtenerMetodoDePago](operations/getObtenerMetodoDePago.json) (GET /sites/{site_id}/payment_methods)：Obtener método de pago [Official](https://developers.mercadolibre.com.ar/en_us/order-management)
- [getObtenerOpinionesPorPedido](operations/getObtenerOpinionesPorPedido.json) (GET /orders/{order_id}/feedback)：Obtener opiniones por pedido [Official](https://developers.mercadolibre.com.ar/en_us/order-management)
- [getPppiCaseByCaseId](operations/getPppiCaseByCaseId.json) (GET /moderations/pppi/case/123)：Check a complaint status [Official](https://developers.mercadolibre.com.ar/en_us/member-of-the-program)
- [getPromotionalPacksByCategory](operations/getPromotionalPacksByCategory.json) (GET /categories/{category_id}/classifieds_promotion_packs)：Get promotional packs by category. [Official](https://developers.mercadolibre.com.ar/en_us/categories-and-listings)
- [getPromotionsPacksEngagedByUser](operations/getPromotionsPacksEngagedByUser.json) (GET /users/{user_id}/classifieds_promotion_packs)：Get promotions packs engaged by user. [Official](https://developers.mercadolibre.com.ar/en_us/usuarios-y-aplicaciones)
- [getQuestionDetails](operations/getQuestionDetails.json) (GET /questions/{question_id})：Get question details. [Official](https://developers.mercadolibre.com.ar/en_us/questions)
- [getQuestionsMadeOnSellerClassifiedItemsWithinTimeWindow](operations/getQuestionsMadeOnSellerClassifiedItemsWithinTimeWindow.json) (GET /items/{item_id}/contacts/questions/time_window)：Get questions made on a seller classified items within a time window. [Official](https://developers.mercadolibre.com.ar/en_us/metrics)
- [getQuestionsMadeOnYourItems](operations/getQuestionsMadeOnYourItems.json) (GET /my/received_questions/search)：Get questions made on your items. [Official](https://developers.mercadolibre.com.ar/en_us/questions)
- [getQuotationsByQuotationId](operations/getQuotationsByQuotationId.json) (GET /quotations/{quotation_id})：quotations [Official](https://developers.mercadolibre.com.ar/en_us/products-receive-notifications)
- [getRatioConversionBetweenCurrencies](operations/getRatioConversionBetweenCurrencies.json) (GET /currency_conversions/search)：Get ratio conversion between currencies. [Official](https://developers.mercadolibre.com.ar/en_us/locations-and-currencies)
- [getRetrievesDeliveryInformationIntoOrder](operations/getRetrievesDeliveryInformationIntoOrder.json) (GET /orders/{order_id}/shipments)：Retrieves the delivery information into order. [Official](https://developers.mercadolibre.com.ar/en_us/shipping)
- [getRetrievesItemVisitsMultiGet](operations/getRetrievesItemVisitsMultiGet.json) (GET /items/visits)：>Retrieves item's visits (Multi Get) [Official](https://developers.mercadolibre.com.ar/en_us/metrics)
- [getSeePhoneViewsByDate](operations/getSeePhoneViewsByDate.json) (GET /users/{user_id}/contacts/phone_views)：Get "See phone" views by date. [Official](https://developers.mercadolibre.com.ar/en_us/metrics)
- [getSeePhoneViewsWithinTimeWindow](operations/getSeePhoneViewsWithinTimeWindow.json) (GET /items/contacts/phone_views/time_window)：Get "See Phone" views within a time window. [Official](https://developers.mercadolibre.com.ar/en_us/metrics)
- [getShipmentsByShipmentId](operations/getShipmentsByShipmentId.json) (GET /shipments/{shipment_id})：Retrieves all delivery data. [Official](https://developers.mercadolibre.com.ar/en_us/shipping)
- [getSpecifyNotApplicableAttributes](operations/getSpecifyNotApplicableAttributes.json) (GET /items/{item_id})：Specify not applicable attributes [Official](https://developers.mercadolibre.com.ar/en_us/attributes)
- [getStateInformation](operations/getStateInformation.json) (GET /classified_locations/states/UY-RO)：Get state information. [Official](https://developers.mercadolibre.com.ar/en_us/locations-and-currencies)
- [getStockLocations](operations/getStockLocations.json) (GET /user-products/{user_product_id}/stock)：stock_locations [Official](https://developers.mercadolibre.com.ar/en_us/products-receive-notifications)
- [getTechnicalSpecsInput](operations/getTechnicalSpecsInput.json) (GET /categories/{category_id}/technical_specs/input)：Mandatory attributes [Official](https://developers.mercadolibre.com.ar/en_us/attributes)
- [getTotalAmountQuestionsByUser](operations/getTotalAmountQuestionsByUser.json) (GET /items/{item_id}/contacts/questions)：Get total amount of questions by user. [Official](https://developers.mercadolibre.com.ar/en_us/metrics)
- [getUserProductsFamilies](operations/getUserProductsFamilies.json) (GET /sites/{site_id}/user-products-families/{family_id})：user products families [Official](https://developers.mercadolibre.com.ar/en_us/products-receive-notifications)
- [getUsers](operations/getUsers.json) (GET /users)：Multiget [Official](https://developers.mercadolibre.com.ar/en_us/items-and-searches)
- [getUsersByUserIdAvailableListingTypes](operations/getUsersByUserIdAvailableListingTypes.json) (GET /users/{user_id}/available_listing_types)：Get available listing types. [Official](https://developers.mercadolibre.com.ar/en_us/usuarios-y-aplicaciones)
- [getUsersByUserIdOrderBlacklist](operations/getUsersByUserIdOrderBlacklist.json) (GET /users/{user_id}/order_blacklist)：Recupera todos los usuarios bloqueados de la oferta en los ítems de un vendedor. [Official](https://developers.mercadolibre.com.ar/en_us/order-management)
- [getUsersByUserIdShippingPreferences](operations/getUsersByUserIdShippingPreferences.json) (GET /users/{user_id}/shipping_preferences)：Retrieves all shipping modes and services available to user. [Official](https://developers.mercadolibre.com.ar/en_us/shipping)
- [getVisitsByUser](operations/getVisitsByUser.json) (GET /users/{user_id}/items_visits)：Get visits by user [Official](https://developers.mercadolibre.com.ar/en_us/metrics)
- [getVisitsByUserAndTime](operations/getVisitsByUserAndTime.json) (GET /users/{user_id}/items_visits/time_window)：Get visits by user and time. [Official](https://developers.mercadolibre.com.ar/en_us/metrics)
- [getWhatIsAttribute](operations/getWhatIsAttribute.json) (GET /categories/{category_id}/attributes)：What is an attribute? [Official](https://developers.mercadolibre.com.ar/en_us/attributes)
- [getYourBookmarks](operations/getYourBookmarks.json) (GET /users/me/bookmarks)：Get your bookmarks [Official](https://developers.mercadolibre.com.ar/en_us/bookmarks)
- [localCommunicationsNotices](operations/localCommunicationsNotices.json) (GET /communications/notices)：Optional parameters [Official](https://developers.mercadolibre.com.ar/en_us/know-the-news-that-sellers-receive)
- [localOrdersByOrderId](operations/localOrdersByOrderId.json) (GET /orders/{order_id})：orders [Official](https://developers.mercadolibre.com.ar/en_us/products-receive-notifications)
- [postAttributesConditional](operations/postAttributesConditional.json) (POST /categories/{category_id}/attributes/conditional)：Required attributes by condition [Official](https://developers.mercadolibre.com.ar/en_us/attributes)
- [postBrandTopValues](operations/postBrandTopValues.json) (POST /catalog_domains/MLA-CELLPHONES/attributes/BRAND/top_values)：Optional parameters [Official](https://developers.mercadolibre.com.ar/en_us/attributes)
- [postByAttributeIdTopValue](operations/postByAttributeIdTopValue.json) (POST /catalog_domains/{doamain_id}/attributes/{attribute_id}/top_value)：Optional parameters [Official](https://developers.mercadolibre.com.ar/en_us/attributes)
- [postByAttributeIdTopValues](operations/postByAttributeIdTopValues.json) (POST /catalog_domains/{domain_id}/attributes/{attribute_id}/top_values)：Optional parameters [Official](https://developers.mercadolibre.com.ar/en_us/attributes)
- [postByIdReply](operations/postByIdReply.json) (POST /feedback/{id}/reply)：Devuelve datos de una opinión dada por un vendedor. [Official](https://developers.mercadolibre.com.ar/en_us/order-management)
- [postByUserIdClassifiedsPromotionPacks](operations/postByUserIdClassifiedsPromotionPacks.json) (POST /users/{user_id}/classifieds_promotion_packs)：You can associate an existing pack with a user. A commercial advisor performs the creation of packs. [Official](https://developers.mercadolibre.com.ar/en_us/usuarios-y-aplicaciones)
- [postByUserIdOrderBlacklist](operations/postByUserIdOrderBlacklist.json) (POST /users/{user_id}/order_blacklist)：Bloquear a usuarios para hacer una oferta en un ítem. [Official](https://developers.mercadolibre.com.ar/en_us/order-management)
- [postCaseByDenounceId](operations/postCaseByDenounceId.json) (POST /moderations/pppi/case/{denounce_id})：Respond to a seller's [Official](https://developers.mercadolibre.com.ar/en_us/member-of-the-program)
- [postCaseById](operations/postCaseById.json) (POST /moderations/pppi/case/{id})：3. Send a response to a complaint [Official](https://developers.mercadolibre.com.ar/en_us/complained-publications)
- [createBrandProtectionComplaint](operations/createBrandProtectionComplaint.json) (POST /moderations/pppi/denounces/items/MLA123)：Make a complaint [Official](https://developers.mercadolibre.com.ar/en_us/member-of-the-program)
- [postModelTopValue](operations/postModelTopValue.json) (POST /catalog_domains/MLA-CELLPHONES/attributes/MODEL/top_value)：Optional parameters [Official](https://developers.mercadolibre.com.ar/en_us/attributes)
- [putUsersByUserId](operations/putUsersByUserId.json) (PUT /users/{user_id})：Update user information. [Official](https://developers.mercadolibre.com.ar/en_us/usuarios-y-aplicaciones)
- [removeBookmark](operations/removeBookmark.json) (DELETE /users/me/bookmarks/{id})：Remove a bookmark [Official](https://developers.mercadolibre.com.ar/en_us/bookmarks)
- [removeUserFromYourQuestionBlacklist](operations/removeUserFromYourQuestionBlacklist.json) (DELETE /users/{seller_id}/questions_blacklist/{user_id})：Remove user from your question blacklist. [Official](https://developers.mercadolibre.com.ar/en_us/questions)
- [searchAbove1000Records](operations/searchAbove1000Records.json) (GET /questions/search)：Search above 1000 records [Official](https://developers.mercadolibre.com.ar/en_us/items-and-searches)
- [sendResponseComplaint](operations/sendResponseComplaint.json) (POST /moderations/pppi/case/{case_id})：3. Send a response to a complaint [Official](https://developers.mercadolibre.com.ar/en_us/complained-publications)
- [sendUsersQuestionsBlacklist](operations/sendUsersQuestionsBlacklist.json) (POST /users/{seller_id}/questions_blacklist)：Send users to questions blacklist [Official](https://developers.mercadolibre.com.ar/en_us/questions)
- [updateCambiarOpinion](operations/updateCambiarOpinion.json) (PUT /feedback/{id})：Cambiar opinión [Official](https://developers.mercadolibre.com.ar/en_us/order-management)
- [updateMandatoryParameters](operations/updateMandatoryParameters.json) (PUT /moderations/pppi/case/files)：Mandatory parameters [Official](https://developers.mercadolibre.com.ar/en_us/complained-publications)
