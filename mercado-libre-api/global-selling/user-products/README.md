# User Products

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Introduction](https://global-selling.mercadolibre.com/devsite/user-products-cbt) | 1 | 0 | modeled |
| [Official: Price per Variation](https://global-selling.mercadolibre.com/devsite/price-per-variation-cbt) | 14 | 0 | modeled |
| [Official: UPTIN Migration](https://global-selling.mercadolibre.com/devsite/uptin-migration) | 2 | 0 | modeled |

## API List

- [addVariantsExistingFamily](operations/addVariantsExistingFamily.json) (POST /global/user-products/families/{siteless_family_id})：Add variants to an existing family [Official](https://global-selling.mercadolibre.com/devsite/price-per-variation-cbt)
- [createAddingNewMarketplaces](operations/createAddingNewMarketplaces.json) (POST /global/user-products/{siteless_user_product_id})：Adding new marketplaces [Official](https://global-selling.mercadolibre.com/devsite/price-per-variation-cbt)
- [getIdentifyingProductsFromSameFamily](operations/getIdentifyingProductsFromSameFamily.json) (GET /sites/{site_id}/user-products-families/{family_id})：Identifying products from the same family [Official](https://global-selling.mercadolibre.com/devsite/price-per-variation-cbt)
- [getItemsByCbtItemId](operations/getItemsByCbtItemId.json) (GET /marketplace/items/{cbt_item_id})：Step 2: GET the CBT item to retrieve the UP Siteless ID [Official](https://global-selling.mercadolibre.com/devsite/price-per-variation-cbt)
- [getMigrationStatus](operations/getMigrationStatus.json) (GET /marketplace/items/{item_id}/migration_live_listing)：Get migration status [Official](https://global-selling.mercadolibre.com/devsite/uptin-migration)
- [getQueryingStatusTask](operations/getQueryingStatusTask.json) (GET /user-products-families/tasks/{task_id})：Querying the status of a task [Official](https://global-selling.mercadolibre.com/devsite/price-per-variation-cbt)
- [getUpMapping](operations/getUpMapping.json) (GET /marketplace/user-products/{siteless_user_product_id}/mapping)：UP Mapping [Official](https://global-selling.mercadolibre.com/devsite/price-per-variation-cbt)
- [getUpSitelessInformation](operations/getUpSitelessInformation.json) (GET /user-products/{siteless_user_product_id})：Get UP Siteless information [Official](https://global-selling.mercadolibre.com/devsite/price-per-variation-cbt)
- [updateUpdatingPrices](operations/updateUpdatingPrices.json) (PUT /global/user-products/{siteless_user_product_id})：Updating prices [Official](https://global-selling.mercadolibre.com/devsite/price-per-variation-cbt)
- [updateUpdatingUserProduct](operations/updateUpdatingUserProduct.json) (PUT /global/user-products/{user_product_id})：Updating a user product [Official](https://global-selling.mercadolibre.com/devsite/price-per-variation-cbt)
- [updateUpdatingUserProductFamily](operations/updateUpdatingUserProductFamily.json) (PUT /global/user-products/families/{family_id})：Updating a user product family [Official](https://global-selling.mercadolibre.com/devsite/price-per-variation-cbt)
