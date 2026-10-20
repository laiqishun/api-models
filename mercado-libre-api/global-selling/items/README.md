# Items

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Introduction](https://global-selling.mercadolibre.com/devsite/introduction-globalselling) | 0 | 0 | guide-only |
| [Official: Appropriate category](https://global-selling.mercadolibre.com/devsite/appropriate-category-gs) | 0 | 0 | guide-only |
| [Official: Category prediction](https://global-selling.mercadolibre.com/devsite/category-predictor) | 8 | 0 | modeled |
| [Official: Publish items](https://global-selling.mercadolibre.com/devsite/global-listing) | 9 | 0 | modeled |
| [Official: Restricted brands](https://global-selling.mercadolibre.com/devsite/restricted-brands) | 0 | 0 | guide-only |
| [Official: Pricing Reference](https://global-selling.mercadolibre.com/devsite/pricing-reference) | 3 | 0 | modeled |
| [Official: Pricing Automation](https://global-selling.mercadolibre.com/devsite/manage-automations) | 11 | 0 | modeled |
| [Official: Product identifiers](https://global-selling.mercadolibre.com/devsite/product-identifiers-gs) | 3 | 0 | modeled |
| [Official: Listing types and exposures](https://global-selling.mercadolibre.com/devsite/listing-types-and-exposures) | 17 | 0 | modeled |
| [Official: Attributes](https://global-selling.mercadolibre.com/devsite/atributtes-global-selling) | 5 | 1 | partial |
| [Official: Variations](https://global-selling.mercadolibre.com/devsite/variations-global-selling) | 5 | 0 | modeled |
| [Official: Pictures](https://global-selling.mercadolibre.com/devsite/pictures) | 5 | 3 | partial |
| [Official: Item description](https://global-selling.mercadolibre.com/devsite/item-description) | 2 | 0 | modeled |
| [Official: Specific Regulations](https://global-selling.mercadolibre.com/devsite/specific-regulations) | 2 | 0 | modeled |
| [Official: Working with Clips](https://global-selling.mercadolibre.com/devsite/working-with-clips) | 5 | 0 | modeled |
| [Official: Prohibited & regulated products](https://global-selling.mercadolibre.com/devsite/prohibited-and-regulated-products) | 0 | 0 | guide-only |
| [Official: First steps](https://global-selling.mercadolibre.com/devsite/first-steps) | 8 | 0 | modeled |
| [Official: Manage size chart](https://global-selling.mercadolibre.com/devsite/manage-size-chart) | 10 | 0 | modeled |
| [Official: Create an item with size chart](https://global-selling.mercadolibre.com/devsite/create-an-item-with-size-chart) | 2 | 0 | modeled |
| [Official: Size Chart Validations](https://global-selling.mercadolibre.com/devsite/size-chart-validation) | 0 | 0 | guide-only |
| [Official: User Products with a size chart](https://global-selling.mercadolibre.com/devsite/user-products-with-a-size-chart) | 2 | 0 | modeled |
| [Official: What is catalog?](https://global-selling.mercadolibre.com/devsite/what-is-catalog) | 0 | 0 | guide-only |
| [Official: Catalog eligibility](https://global-selling.mercadolibre.com/devsite/catalog-eligibility-gs) | 3 | 0 | modeled |
| [Official: Products search](https://global-selling.mercadolibre.com/devsite/products-search-gs) | 2 | 0 | modeled |
| [Official: Catalog listing](https://global-selling.mercadolibre.com/devsite/catalog-listing-gs) | 2 | 1 | partial |
| [Official: Listing Required](https://global-selling.mercadolibre.com/devsite/listing-required) | 1 | 0 | modeled |
| [Official: Catalog competition](https://global-selling.mercadolibre.com/devsite/catalog-competition-gs) | 3 | 0 | modeled |
| [Official: Multi-marketplace tool](https://global-selling.mercadolibre.com/devsite/multi-marketplace-tool) | 7 | 0 | modeled |

## API List

- [activateAndDeactivateAutomaticMultiMarketplaceTool](operations/activateAndDeactivateAutomaticMultiMarketplaceTool.json) (PUT /multi-marketplace-tool/config/automatic)：Activate and deactivate automatic multi-marketplace tool [Official](https://global-selling.mercadolibre.com/devsite/multi-marketplace-tool)
- [activateInAnotherMarketplace](operations/activateInAnotherMarketplace.json) (POST /global/items/{item_id})：Activate in another marketplace [Official](https://global-selling.mercadolibre.com/devsite/global-listing)
- [addRowsSizeChart](operations/addRowsSizeChart.json) (POST /catalog/charts/{id}/rows)：Add rows to size chart [Official](https://global-selling.mercadolibre.com/devsite/manage-size-chart)
- [checkPossibleErrors](operations/checkPossibleErrors.json) (GET /pictures/{picture_id}/errors)：Check possible errors [Official](https://global-selling.mercadolibre.com/devsite/pictures)
- [checkProductSpecificationSheetDomain](operations/checkProductSpecificationSheetDomain.json) (GET /domains/CBT-SNEAKERS/technical_specs)：Check product specification sheet of domain [Official](https://global-selling.mercadolibre.com/devsite/first-steps)
- [checkProductSpecificationSheetSizeChart](operations/checkProductSpecificationSheetSizeChart.json) (POST /domains/{domain_id}/technical_specs)：Check the product specification sheet of the size chart [Official](https://global-selling.mercadolibre.com/devsite/first-steps)
- [createConsultingSizeChartsDataSheet](operations/createConsultingSizeChartsDataSheet.json) (POST /catalog/charts/search)：Consulting a size charts data sheet [Official](https://global-selling.mercadolibre.com/devsite/first-steps)
- [createFamilyUserProductsWithSizeChart](operations/createFamilyUserProductsWithSizeChart.json) (POST /global/user-products/families)：Create a family of User Products with a size chart [Official](https://global-selling.mercadolibre.com/devsite/user-products-with-a-size-chart)
- [createItemWithAtributeN](operations/createItemWithAtributeN.json) (PUT /global/items/{item_id})：Create ítem with atribute N/A [Official](https://global-selling.mercadolibre.com/devsite/atributtes-global-selling)
- [createItemWithAttributes](operations/createItemWithAttributes.json) (POST /items)：Create an item with attributes [Official](https://global-selling.mercadolibre.com/devsite/atributtes-global-selling)
- [createMandatoryAttributes](operations/createMandatoryAttributes.json) (POST /global/items)：Mandatory attributes [Official](https://global-selling.mercadolibre.com/devsite/global-listing)
- [createPreconditionsAssignAutomation](operations/createPreconditionsAssignAutomation.json) (POST /marketplace/items/{item_id}/prices/automate)：Preconditions to assign an automation [Official](https://global-selling.mercadolibre.com/devsite/manage-automations)
- [createSuggestedItems](operations/createSuggestedItems.json) (POST /multi-marketplace-tool/suggestions)：Create suggested items [Official](https://global-selling.mercadolibre.com/devsite/multi-marketplace-tool)
- [deleteChartsByChartId](operations/deleteChartsByChartId.json) (DELETE /catalog/charts/{chart_id})：Delete size chart [Official](https://global-selling.mercadolibre.com/devsite/manage-size-chart)
- [deleteClip](operations/deleteClip.json) (DELETE /marketplace/items/{cbt_item_id}/clips/{clip_relation_id})：Delete a Clip [Official](https://global-selling.mercadolibre.com/devsite/working-with-clips)
- [deleteClipsByClipId](operations/deleteClipsByClipId.json) (DELETE /marketplace/items/{item_id}/clips/c69658ac-f1f8-4860-b56b-be9f285a9edf)：Delete a Clip [Official](https://global-selling.mercadolibre.com/devsite/working-with-clips)
- [deleteSizeChart](operations/deleteSizeChart.json) (DELETE /catalog/charts/{id})：Delete size chart [Official](https://global-selling.mercadolibre.com/devsite/manage-size-chart)
- [deleteVariations](operations/deleteVariations.json) (DELETE /marketplace/items/{item_id}/variations/{id})：Delete variations [Official](https://global-selling.mercadolibre.com/devsite/variations-global-selling)
- [getAllSites](operations/getAllSites.json) (GET /sites)：Get all sites. [Official](https://global-selling.mercadolibre.com/devsite/category-predictor)
- [getAutomateRules](operations/getAutomateRules.json) (GET /marketplace/products/{product_id}/prices/automate/rules)：Prerequisites to get the available rules for an item [Official](https://global-selling.mercadolibre.com/devsite/manage-automations)
- [getAutomaticListing](operations/getAutomaticListing.json) (GET /multi-marketplace-tool/config/automatic)：Automatic listing [Official](https://global-selling.mercadolibre.com/devsite/multi-marketplace-tool)
- [getAvailableDomainsSizeChart](operations/getAvailableDomainsSizeChart.json) (GET /catalog/charts/CBT/configurations/active_domains)：Available domains for size chart [Official](https://global-selling.mercadolibre.com/devsite/first-steps)
- [getAvailableDowngradesListing](operations/getAvailableDowngradesListing.json) (GET /items/{item_id}/available_downgrades)：Available Downgrades for a Listing [Official](https://global-selling.mercadolibre.com/devsite/listing-types-and-exposures)
- [getAvailableListingTypes](operations/getAvailableListingTypes.json) (GET /users/{user_id}/available_listing_type/free)：Available Listing Types [Official](https://global-selling.mercadolibre.com/devsite/listing-types-and-exposures)
- [getAvailableTransactionsListing](operations/getAvailableTransactionsListing.json) (GET /items/{item_id}/available_listing_types)：Available Transactions for a Listing [Official](https://global-selling.mercadolibre.com/devsite/listing-types-and-exposures)
- [getAvailableUpgradesListing](operations/getAvailableUpgradesListing.json) (GET /items/{item_id}/available_upgrades)：Available Upgrades for a Listing [Official](https://global-selling.mercadolibre.com/devsite/listing-types-and-exposures)
- [getByCbtItemIdClips](operations/getByCbtItemIdClips.json) (GET /marketplace/items/{cbt_item_id}/clips)：Get Clips info of an item [Official](https://global-selling.mercadolibre.com/devsite/working-with-clips)
- [getByDomainIdTechnicalSpecs](operations/getByDomainIdTechnicalSpecs.json) (GET /domains/{domain_id}/technical_specs)：Check product specification sheet of domain [Official](https://global-selling.mercadolibre.com/devsite/first-steps)
- [getByIdItems](operations/getByIdItems.json) (GET /marketplace/benchmarks/user/{id}/items)：Preconditions for getting price references by seller [Official](https://global-selling.mercadolibre.com/devsite/pricing-reference)
- [getByItemIdDescription](operations/getByItemIdDescription.json) (GET /marketplace/items/{item_id}/description)：Parameters [Official](https://global-selling.mercadolibre.com/devsite/item-description)
- [getByItemIdPriceToWin](operations/getByItemIdPriceToWin.json) (GET /marketplace/items/{item_id}/price_to_win)：Conditions and price of the    winning item [Official](https://global-selling.mercadolibre.com/devsite/catalog-competition-gs)
- [getByResourceIdErrors](operations/getByResourceIdErrors.json) (GET /pictures/622077-CBT42350860502_062020/errors)：Check possible errors [Official](https://global-selling.mercadolibre.com/devsite/pictures)
- [getBySiteIdListingTypes](operations/getBySiteIdListingTypes.json) (GET /sites/{site_id}/listing_types)：Listing Types by Site [Official](https://global-selling.mercadolibre.com/devsite/listing-types-and-exposures)
- [getByUserIdAvailableListingTypes](operations/getByUserIdAvailableListingTypes.json) (GET /users/{user_id}/available_listing_types)：Available Listing Types [Official](https://global-selling.mercadolibre.com/devsite/listing-types-and-exposures)
- [getCategoryAttributes](operations/getCategoryAttributes.json) (GET /categories/{category_id}/attributes)：Get category attributes. [Official](https://global-selling.mercadolibre.com/devsite/category-predictor)
- [getCategoryDetails](operations/getCategoryDetails.json) (GET /categories/{category_id})：Get category details. [Official](https://global-selling.mercadolibre.com/devsite/category-predictor)
- [getCategoryTreeBySite](operations/getCategoryTreeBySite.json) (GET /sites/CBT/categories)：Get the category tree by site. [Official](https://global-selling.mercadolibre.com/devsite/category-predictor)
- [getCbtTShirtsTechnicalSpecs](operations/getCbtTShirtsTechnicalSpecs.json) (GET /domains/CBT-T_SHIRTS/technical_specs)：Parameters [Official](https://global-selling.mercadolibre.com/devsite/first-steps)
- [getChartsByChartId](operations/getChartsByChartId.json) (GET /catalog/charts/{chart_id})：Get size chart by ID [Official](https://global-selling.mercadolibre.com/devsite/manage-size-chart)
- [getClipsInfoItem](operations/getClipsInfoItem.json) (GET /marketplace/items/{item_id}/clips)：Get Clips info of an item [Official](https://global-selling.mercadolibre.com/devsite/working-with-clips)
- [getConditionsAndPriceWinningItem](operations/getConditionsAndPriceWinningItem.json) (GET /items/MLA12)：Conditions and price of the    winning item [Official](https://global-selling.mercadolibre.com/devsite/catalog-competition-gs)
- [getFilterItems](operations/getFilterItems.json) (GET /users/{user_id}/items/search)：Filter items [Official](https://global-selling.mercadolibre.com/devsite/catalog-eligibility-gs)
- [getItemsByItem](operations/getItemsByItem.json) (GET /items/{item})：Conditions and price of the    winning item [Official](https://global-selling.mercadolibre.com/devsite/catalog-competition-gs)
- [getItemsCatalogForewarning](operations/getItemsCatalogForewarning.json) (GET /marketplace/items/catalog-forewarning)：Parameters [Official](https://global-selling.mercadolibre.com/devsite/listing-required)
- [getListingExposures](operations/getListingExposures.json) (GET /sites/{site_id}/listing_exposures)：Listing Exposures [Official](https://global-selling.mercadolibre.com/devsite/listing-types-and-exposures)
- [getListingExposuresByExposureLevel](operations/getListingExposuresByExposureLevel.json) (GET /sites/{site_id}/listing_exposures/{exposure_level})：Listing Exposures [Official](https://global-selling.mercadolibre.com/devsite/listing-types-and-exposures)
- [getListingExposuresBySite](operations/getListingExposuresBySite.json) (GET /sites/CBT/listing_types)：Get listing exposures by site [Official](https://global-selling.mercadolibre.com/devsite/category-predictor)
- [getListingExposuresHigh](operations/getListingExposuresHigh.json) (GET /sites/MLA/listing_exposures/high)：Listing Exposures [Official](https://global-selling.mercadolibre.com/devsite/listing-types-and-exposures)
- [getListingLimit](operations/getListingLimit.json) (GET /marketplace/users/cap)：Get listing limit [Official](https://global-selling.mercadolibre.com/devsite/global-listing)
- [getListingProcessStatus](operations/getListingProcessStatus.json) (GET /multi-marketplace-tool/suggestions/status)：Listing process status [Official](https://global-selling.mercadolibre.com/devsite/multi-marketplace-tool)
- [getListingProcessStatusDetail](operations/getListingProcessStatusDetail.json) (GET /multi-marketplace-tool/suggestions/status/{processid})：Listing process status detail [Official](https://global-selling.mercadolibre.com/devsite/multi-marketplace-tool)
- [getListingTypeDetails](operations/getListingTypeDetails.json) (GET /sites/CBT/listing_types/gold_pro)：Get listing type details. [Official](https://global-selling.mercadolibre.com/devsite/category-predictor)
- [getListingTypesByListingTypeId](operations/getListingTypesByListingTypeId.json) (GET /sites/{site_id}/listing_types/{listing_type_id})：Listing Type Specification [Official](https://global-selling.mercadolibre.com/devsite/listing-types-and-exposures)
- [getListingTypesBySite](operations/getListingTypesBySite.json) (GET /sites/MLA/listing_types)：Listing Types by Site [Official](https://global-selling.mercadolibre.com/devsite/listing-types-and-exposures)
- [getListingTypeSpecification](operations/getListingTypeSpecification.json) (GET /sites/MLA/listing_types/gold_special)：Listing Type Specification [Official](https://global-selling.mercadolibre.com/devsite/listing-types-and-exposures)
- [getMandatoryAttributes](operations/getMandatoryAttributes.json) (GET /categories/{category_id}/technical_specs/input)：Mandatory attributes [Official](https://global-selling.mercadolibre.com/devsite/atributtes-global-selling)
- [getMandatoryParameter](operations/getMandatoryParameter.json) (GET /marketplace/domain_discovery/search)：Mandatory parameter [Official](https://global-selling.mercadolibre.com/devsite/category-predictor)
- [getMarketplaceItemsByItemId](operations/getMarketplaceItemsByItemId.json) (GET /marketplace/items/MCO2996325000)：Configuration by Sites to Sell - item with variations [Official](https://global-selling.mercadolibre.com/devsite/global-listing)
- [getMlaListingExposures](operations/getMlaListingExposures.json) (GET /sites/MLA/listing_exposures)：Listing Exposures [Official](https://global-selling.mercadolibre.com/devsite/listing-types-and-exposures)
- [getMluListingTypes](operations/getMluListingTypes.json) (GET /sites/MLU/listing_types)：Listing Types by Site [Official](https://global-selling.mercadolibre.com/devsite/listing-types-and-exposures)
- [getMultiMarketplaceToolSuggestions](operations/getMultiMarketplaceToolSuggestions.json) (GET /multi-marketplace-tool/suggestions)：Optional parameters [Official](https://global-selling.mercadolibre.com/devsite/multi-marketplace-tool)
- [getMultiplePublications](operations/getMultiplePublications.json) (GET /multiget/catalog_listing_eligibility)：Multiple publications [Official](https://global-selling.mercadolibre.com/devsite/catalog-eligibility-gs)
- [getObtainsInformationDomain](operations/getObtainsInformationDomain.json) (GET /domains/CBT-JACKETS_AND_COATS/technical_specs)：Obtains information of the domain. [Official](https://global-selling.mercadolibre.com/devsite/category-predictor)
- [getPreconditionsDeleteAutomation](operations/getPreconditionsDeleteAutomation.json) (GET /marketplace/items/{itemid}/prices/automate)：Preconditions to delete an automation [Official](https://global-selling.mercadolibre.com/devsite/manage-automations)
- [getPreconditionsGettingPriceReferencesBySeller](operations/getPreconditionsGettingPriceReferencesBySeller.json) (GET /marketplace/benchmarks/user/{user_id}/items)：Preconditions for getting price references by seller [Official](https://global-selling.mercadolibre.com/devsite/pricing-reference)
- [getPreconditionsObtainAutomation](operations/getPreconditionsObtainAutomation.json) (GET /marketplace/items/{item_id}/prices/automate)：Preconditions to obtain an automation [Official](https://global-selling.mercadolibre.com/devsite/manage-automations)
- [getPreconditionsObtainAvailableRulesItem](operations/getPreconditionsObtainAvailableRulesItem.json) (GET /marketplace/items/{item_id}/prices/automate/rules)：Preconditions to obtain the available rules for an item [Official](https://global-selling.mercadolibre.com/devsite/manage-automations)
- [getPrerequisitesGetAvailableRulesItem](operations/getPrerequisitesGetAvailableRulesItem.json) (GET /marketplace/products/{catalog_product_id}/prices/automate/rules)：Prerequisites to get the available rules for an item [Official](https://global-selling.mercadolibre.com/devsite/manage-automations)
- [getPrerequisitesGetPriceHistoryItem](operations/getPrerequisitesGetPriceHistoryItem.json) (GET /marketplace/items/{item_id}/prices/history)：Prerequisites to get the price history for an item [Official](https://global-selling.mercadolibre.com/devsite/manage-automations)
- [getProductById](operations/getProductById.json) (GET /products/{product_id})：Product by ID [Official](https://global-selling.mercadolibre.com/devsite/products-search-gs)
- [getProductsSearch](operations/getProductsSearch.json) (GET /marketplace/products/search)：Parameters [Official](https://global-selling.mercadolibre.com/devsite/products-search-gs)
- [getSizeChartById](operations/getSizeChartById.json) (GET /catalog/charts/{id})：Get size chart by ID [Official](https://global-selling.mercadolibre.com/devsite/manage-size-chart)
- [getSizechartEquivalences](operations/getSizechartEquivalences.json) (GET /marketplace/sizechart/equivalences)：Parameters [Official](https://global-selling.mercadolibre.com/devsite/manage-size-chart)
- [getStep0GetMarketplaceChildren](operations/getStep0GetMarketplaceChildren.json) (GET /items/{cbt_item_id}/marketplace_items)：Step 0: Get marketplace children [Official](https://global-selling.mercadolibre.com/devsite/global-listing)
- [linkPictureYourItem](operations/linkPictureYourItem.json) (POST /items/{item_id}/pictures)：Link a picture to your Item [Official](https://global-selling.mercadolibre.com/devsite/pictures)
- [postByChartIdRows](operations/postByChartIdRows.json) (POST /catalog/charts/{chart_id}/rows)：Add rows to size chart [Official](https://global-selling.mercadolibre.com/devsite/manage-size-chart)
- [postByProductByCatalogProductId](operations/postByProductByCatalogProductId.json) (POST /marketplace/items/{item_id}/prices/automate/by-product/{catalog_product_id})：Parameters [Official](https://global-selling.mercadolibre.com/devsite/manage-automations)
- [postByProductById](operations/postByProductById.json) (POST /marketplace/items/{item_id}/prices/automate/by-product/{id})：Parameters [Official](https://global-selling.mercadolibre.com/devsite/manage-automations)
- [postCatalogCharts](operations/postCatalogCharts.json) (POST /catalog/charts)：Example of creating size chart in footwear [Official](https://global-selling.mercadolibre.com/devsite/manage-size-chart)
- [postCbtSneakersTechnicalSpecs](operations/postCbtSneakersTechnicalSpecs.json) (POST /domains/CBT-SNEAKERS/technical_specs)：Check the product specification sheet of the size chart [Official](https://global-selling.mercadolibre.com/devsite/first-steps)
- [postItemsCatalogListings](operations/postItemsCatalogListings.json) (POST /items/catalog_listings)：Variations [Official](https://global-selling.mercadolibre.com/devsite/catalog-listing-gs)
- [putByItemIdListingType](operations/putByItemIdListingType.json) (PUT /global/items/{item_id}/listing_type)：Update Listing Type [Official](https://global-selling.mercadolibre.com/devsite/listing-types-and-exposures)
- [putChartsByChartId](operations/putChartsByChartId.json) (PUT /catalog/charts/{chart_id})：Update size chart rows [Official](https://global-selling.mercadolibre.com/devsite/manage-size-chart)
- [putItemsByItemId](operations/putItemsByItemId.json) (PUT /items/{item_id})：Example of item variation: [Official](https://global-selling.mercadolibre.com/devsite/product-identifiers-gs)
- [putPricesAutomate](operations/putPricesAutomate.json) (PUT /marketplace/items/{item_id}/prices/automate)：Preconditions to update an automation [Official](https://global-selling.mercadolibre.com/devsite/manage-automations)
- [updateListingType](operations/updateListingType.json) (PUT /items/{item_id}/listing_type)：Update Listing Type [Official](https://global-selling.mercadolibre.com/devsite/listing-types-and-exposures)
- [updatePreconditionsUpdateAutomation](operations/updatePreconditionsUpdateAutomation.json) (PUT /marketplace/items/{itemid}/prices/automate)：Preconditions to update an automation [Official](https://global-selling.mercadolibre.com/devsite/manage-automations)
- [updateSizeChartRows](operations/updateSizeChartRows.json) (PUT /catalog/charts/{id})：Update size chart rows [Official](https://global-selling.mercadolibre.com/devsite/manage-size-chart)
- [updateStep1PauseEachChildItem](operations/updateStep1PauseEachChildItem.json) (PUT /global/items/{SITE_ITEM_ID}-d)：Step 1: Pause each child item [Official](https://global-selling.mercadolibre.com/devsite/global-listing)
- [updateStep2PauseParentCbtItem](operations/updateStep2PauseParentCbtItem.json) (PUT /global/items/{CBT_ITEM_ID}-d)：Step 2: Pause the parent CBT item [Official](https://global-selling.mercadolibre.com/devsite/global-listing)
- [uploadClip](operations/uploadClip.json) (POST /marketplace/items/{cbt_item_id}/clips/upload)：Upload a Clip [Official](https://global-selling.mercadolibre.com/devsite/working-with-clips)
- [uploadStampImage](operations/uploadStampImage.json) (GET /pictures/items/upload)：Upload the stamp image [Official](https://global-selling.mercadolibre.com/devsite/specific-regulations)
- [validateAndUploadPictures](operations/validateAndUploadPictures.json) (POST /pictures/items/upload)：Validate and upload pictures [Official](https://global-selling.mercadolibre.com/devsite/pictures)
- [validateEligibilityCatalog](operations/validateEligibilityCatalog.json) (GET /items/{item_id}/catalog_listing_eligibility)：Validate eligibility to catalog [Official](https://global-selling.mercadolibre.com/devsite/catalog-eligibility-gs)
- [validateUnrealizedSuggestions](operations/validateUnrealizedSuggestions.json) (GET /multi-marketplace-tool/suggestions/validate)：Validate unrealized suggestions [Official](https://global-selling.mercadolibre.com/devsite/multi-marketplace-tool)
