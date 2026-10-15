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

## Operation models

| Host | Method | Path | Source pages | JSON |
|---|---|---|---:|---|
| `api.mercadolibre.com` | DELETE | `/catalog/charts/{chart_id}` | 1 | [JSON](./operations/delete-97b7063f18e1.json) |
| `api.mercadolibre.com` | DELETE | `/catalog/charts/{id}` | 1 | [JSON](./operations/delete-007d79fd971e.json) |
| `api.mercadolibre.com` | DELETE | `/marketplace/items/{cbt_item_id}/clips/{clip_relation_id}` | 1 | [JSON](./operations/delete-5039fb6b6b93.json) |
| `api.mercadolibre.com` | DELETE | `/marketplace/items/{item_id}/clips/c69658ac-f1f8-4860-b56b-be9f285a9edf` | 1 | [JSON](./operations/delete-b04fa5c717f8.json) |
| `api.mercadolibre.com` | DELETE | `/marketplace/items/{item_id}/variations/{id}` | 1 | [JSON](./operations/delete-5bae81d235a5.json) |
| `api.mercadolibre.com` | GET | `/catalog/charts/CBT/configurations/active_domains` | 1 | [JSON](./operations/get-95b857f614a3.json) |
| `api.mercadolibre.com` | GET | `/catalog/charts/{chart_id}` | 1 | [JSON](./operations/get-ef3dbe6b28c8.json) |
| `api.mercadolibre.com` | GET | `/catalog/charts/{id}` | 1 | [JSON](./operations/get-c0dd9b3848a3.json) |
| `api.mercadolibre.com` | GET | `/categories/{category_id}` | 3 | [JSON](./operations/get-c8bccf6a4cc1.json) |
| `api.mercadolibre.com` | GET | `/categories/{category_id}/attributes` | 4 | [JSON](./operations/get-933c91a03d9f.json) |
| `api.mercadolibre.com` | GET | `/categories/{category_id}/technical_specs/input` | 1 | [JSON](./operations/get-56972cff76d5.json) |
| `api.mercadolibre.com` | GET | `/domains/CBT-JACKETS_AND_COATS/technical_specs` | 1 | [JSON](./operations/get-56846d1f006d.json) |
| `api.mercadolibre.com` | GET | `/domains/CBT-SNEAKERS/technical_specs` | 1 | [JSON](./operations/get-c83fc1525324.json) |
| `api.mercadolibre.com` | GET | `/domains/CBT-T_SHIRTS/technical_specs` | 1 | [JSON](./operations/get-c8f532e1b141.json) |
| `api.mercadolibre.com` | GET | `/domains/{domain_id}/technical_specs` | 1 | [JSON](./operations/get-e827fa5c2bf7.json) |
| `api.mercadolibre.com` | GET | `/items/MLA12` | 1 | [JSON](./operations/get-29632651441a.json) |
| `api.mercadolibre.com` | GET | `/items/{cbt_item_id}/marketplace_items` | 1 | [JSON](./operations/get-ee19f3b17ea2.json) |
| `api.mercadolibre.com` | GET | `/items/{item_id}/available_downgrades` | 1 | [JSON](./operations/get-fccea083d19b.json) |
| `api.mercadolibre.com` | GET | `/items/{item_id}/available_listing_types` | 1 | [JSON](./operations/get-e938d538d051.json) |
| `api.mercadolibre.com` | GET | `/items/{item_id}/available_upgrades` | 1 | [JSON](./operations/get-5b1d66c3551b.json) |
| `api.mercadolibre.com` | GET | `/items/{item_id}/catalog_listing_eligibility` | 1 | [JSON](./operations/get-0bdcd57ee152.json) |
| `api.mercadolibre.com` | GET | `/items/{item}` | 1 | [JSON](./operations/get-fde0b8126e85.json) |
| `api.mercadolibre.com` | GET | `/marketplace/benchmarks/user/{id}/items` | 1 | [JSON](./operations/get-a70dfc141fe1.json) |
| `api.mercadolibre.com` | GET | `/marketplace/benchmarks/user/{user_id}/items` | 1 | [JSON](./operations/get-33b4a4631c87.json) |
| `api.mercadolibre.com` | GET | `/marketplace/domain_discovery/search` | 2 | [JSON](./operations/get-ff8500b96ef6.json) |
| `api.mercadolibre.com` | GET | `/marketplace/items/MCO2996325000` | 1 | [JSON](./operations/get-fa7b4f0e8430.json) |
| `api.mercadolibre.com` | GET | `/marketplace/items/catalog-forewarning` | 1 | [JSON](./operations/get-e8f2b48ce136.json) |
| `api.mercadolibre.com` | GET | `/marketplace/items/{cbt_item_id}/clips` | 1 | [JSON](./operations/get-d6fdb1e0c0ae.json) |
| `api.mercadolibre.com` | GET | `/marketplace/items/{item_id}/clips` | 1 | [JSON](./operations/get-9f1fd7a08f0d.json) |
| `api.mercadolibre.com` | GET | `/marketplace/items/{item_id}/description` | 1 | [JSON](./operations/get-913b4a7a8a57.json) |
| `api.mercadolibre.com` | GET | `/marketplace/items/{item_id}/price_to_win` | 1 | [JSON](./operations/get-8708ccd08f8f.json) |
| `api.mercadolibre.com` | GET | `/marketplace/items/{item_id}/prices/automate` | 1 | [JSON](./operations/get-d7d4e2efb8ba.json) |
| `api.mercadolibre.com` | GET | `/marketplace/items/{item_id}/prices/automate/rules` | 1 | [JSON](./operations/get-2aac57642c7d.json) |
| `api.mercadolibre.com` | GET | `/marketplace/items/{item_id}/prices/history` | 1 | [JSON](./operations/get-fa885284f729.json) |
| `api.mercadolibre.com` | GET | `/marketplace/items/{itemid}/prices/automate` | 1 | [JSON](./operations/get-b9e29cbbe83f.json) |
| `api.mercadolibre.com` | GET | `/marketplace/products/search` | 1 | [JSON](./operations/get-c1cf2bc926de.json) |
| `api.mercadolibre.com` | GET | `/marketplace/products/{catalog_product_id}/prices/automate/rules` | 1 | [JSON](./operations/get-2a8dcb647065.json) |
| `api.mercadolibre.com` | GET | `/marketplace/products/{product_id}/prices/automate/rules` | 1 | [JSON](./operations/get-c7de2c269ec3.json) |
| `api.mercadolibre.com` | GET | `/marketplace/sizechart/equivalences` | 1 | [JSON](./operations/get-f5ea85e1f7f1.json) |
| `api.mercadolibre.com` | GET | `/marketplace/users/cap` | 1 | [JSON](./operations/get-2bc55b7c8d55.json) |
| `api.mercadolibre.com` | GET | `/multi-marketplace-tool/config/automatic` | 1 | [JSON](./operations/get-220a68928268.json) |
| `api.mercadolibre.com` | GET | `/multi-marketplace-tool/suggestions` | 1 | [JSON](./operations/get-aedf2d66518e.json) |
| `api.mercadolibre.com` | GET | `/multi-marketplace-tool/suggestions/status` | 1 | [JSON](./operations/get-012ada4d4b88.json) |
| `api.mercadolibre.com` | GET | `/multi-marketplace-tool/suggestions/status/{processid}` | 1 | [JSON](./operations/get-6a6ddec24a4b.json) |
| `api.mercadolibre.com` | GET | `/multi-marketplace-tool/suggestions/validate` | 1 | [JSON](./operations/get-9ec082c68c17.json) |
| `api.mercadolibre.com` | GET | `/multiget/catalog_listing_eligibility` | 1 | [JSON](./operations/get-c7039d48732b.json) |
| `api.mercadolibre.com` | GET | `/pictures/622077-CBT42350860502_062020/errors` | 1 | [JSON](./operations/get-d9affa2e094e.json) |
| `api.mercadolibre.com` | GET | `/pictures/items/upload` | 1 | [JSON](./operations/get-adf6466fe442.json) |
| `api.mercadolibre.com` | GET | `/pictures/{picture_id}/errors` | 1 | [JSON](./operations/get-55e9cc2c3169.json) |
| `api.mercadolibre.com` | GET | `/products/{product_id}` | 2 | [JSON](./operations/get-7a27745f5bf7.json) |
| `api.mercadolibre.com` | GET | `/sites` | 1 | [JSON](./operations/get-aabb67de001d.json) |
| `api.mercadolibre.com` | GET | `/sites/CBT/categories` | 2 | [JSON](./operations/get-08f17aec4607.json) |
| `api.mercadolibre.com` | GET | `/sites/CBT/listing_types` | 1 | [JSON](./operations/get-e6133546da0b.json) |
| `api.mercadolibre.com` | GET | `/sites/CBT/listing_types/gold_pro` | 1 | [JSON](./operations/get-a2f3fd431aea.json) |
| `api.mercadolibre.com` | GET | `/sites/MLA/listing_exposures` | 1 | [JSON](./operations/get-a7fee499a387.json) |
| `api.mercadolibre.com` | GET | `/sites/MLA/listing_exposures/high` | 1 | [JSON](./operations/get-9cf05dc98076.json) |
| `api.mercadolibre.com` | GET | `/sites/MLA/listing_types` | 1 | [JSON](./operations/get-73b7d3bae1e9.json) |
| `api.mercadolibre.com` | GET | `/sites/MLA/listing_types/gold_special` | 1 | [JSON](./operations/get-139cf79ed7f9.json) |
| `api.mercadolibre.com` | GET | `/sites/MLU/listing_types` | 1 | [JSON](./operations/get-daeeeda6b657.json) |
| `api.mercadolibre.com` | GET | `/sites/{site_id}/listing_exposures` | 1 | [JSON](./operations/get-855106152c1a.json) |
| `api.mercadolibre.com` | GET | `/sites/{site_id}/listing_exposures/{exposure_level}` | 1 | [JSON](./operations/get-af40aa5017c9.json) |
| `api.mercadolibre.com` | GET | `/sites/{site_id}/listing_types` | 1 | [JSON](./operations/get-ae7f82a44f3f.json) |
| `api.mercadolibre.com` | GET | `/sites/{site_id}/listing_types/{listing_type_id}` | 1 | [JSON](./operations/get-3be8f953cb08.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/available_listing_type/free` | 1 | [JSON](./operations/get-806977ae81e6.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/available_listing_types` | 1 | [JSON](./operations/get-fdfbc7eb9f67.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/items/search` | 2 | [JSON](./operations/get-9c1540040ead.json) |
| `api.mercadolibre.com` | POST | `/catalog/charts` | 5 | [JSON](./operations/post-7ef751e3d8e6.json) |
| `api.mercadolibre.com` | POST | `/catalog/charts/search` | 1 | [JSON](./operations/post-46110f64f65f.json) |
| `api.mercadolibre.com` | POST | `/catalog/charts/{chart_id}/rows` | 1 | [JSON](./operations/post-d894e4bb94f8.json) |
| `api.mercadolibre.com` | POST | `/catalog/charts/{id}/rows` | 1 | [JSON](./operations/post-32505aeab4c3.json) |
| `api.mercadolibre.com` | POST | `/domains/CBT-SNEAKERS/technical_specs` | 1 | [JSON](./operations/post-78211ff8c3df.json) |
| `api.mercadolibre.com` | POST | `/domains/{domain_id}/technical_specs` | 1 | [JSON](./operations/post-4926cff359cb.json) |
| `api.mercadolibre.com` | POST | `/global/items` | 11 | [JSON](./operations/post-4e255add7183.json) |
| `api.mercadolibre.com` | POST | `/global/items/{item_id}` | 1 | [JSON](./operations/post-1e388f5c84a4.json) |
| `api.mercadolibre.com` | POST | `/global/user-products/families` | 1 | [JSON](./operations/post-e91a5333dd68.json) |
| `api.mercadolibre.com` | POST | `/items` | 2 | [JSON](./operations/post-6c17161f946b.json) |
| `api.mercadolibre.com` | POST | `/items/catalog_listings` | 1 | [JSON](./operations/post-c8698f97a4e3.json) |
| `api.mercadolibre.com` | POST | `/items/{item_id}/pictures` | 1 | [JSON](./operations/post-98697827847a.json) |
| `api.mercadolibre.com` | POST | `/marketplace/items/{cbt_item_id}/clips/upload` | 1 | [JSON](./operations/post-1733c68c7c7c.json) |
| `api.mercadolibre.com` | POST | `/marketplace/items/{item_id}/prices/automate` | 1 | [JSON](./operations/post-de550b637e9e.json) |
| `api.mercadolibre.com` | POST | `/marketplace/items/{item_id}/prices/automate/by-product/{catalog_product_id}` | 1 | [JSON](./operations/post-24e30443416b.json) |
| `api.mercadolibre.com` | POST | `/marketplace/items/{item_id}/prices/automate/by-product/{id}` | 1 | [JSON](./operations/post-b65f47e50840.json) |
| `api.mercadolibre.com` | POST | `/multi-marketplace-tool/suggestions` | 1 | [JSON](./operations/post-b51125bf863a.json) |
| `api.mercadolibre.com` | POST | `/pictures/items/upload` | 3 | [JSON](./operations/post-f72c92c76bab.json) |
| `api.mercadolibre.com` | PUT | `/catalog/charts/{chart_id}` | 2 | [JSON](./operations/put-98dcce7c015e.json) |
| `api.mercadolibre.com` | PUT | `/catalog/charts/{id}` | 2 | [JSON](./operations/put-1033b68bff09.json) |
| `api.mercadolibre.com` | PUT | `/global/items/{CBT_ITEM_ID}-d` | 2 | [JSON](./operations/put-ba8501a287ec.json) |
| `api.mercadolibre.com` | PUT | `/global/items/{SITE_ITEM_ID}-d` | 2 | [JSON](./operations/put-31e6a5baad8f.json) |
| `api.mercadolibre.com` | PUT | `/global/items/{item_id}` | 13 | [JSON](./operations/put-6262fc969b60.json) |
| `api.mercadolibre.com` | PUT | `/global/items/{item_id}/listing_type` | 1 | [JSON](./operations/put-4b2d4ba0f215.json) |
| `api.mercadolibre.com` | PUT | `/items/{item_id}` | 2 | [JSON](./operations/put-d822eca785a8.json) |
| `api.mercadolibre.com` | PUT | `/items/{item_id}/listing_type` | 1 | [JSON](./operations/put-3b89dc3f1e99.json) |
| `api.mercadolibre.com` | PUT | `/marketplace/items/{item_id}/prices/automate` | 1 | [JSON](./operations/put-adc461d2f74b.json) |
| `api.mercadolibre.com` | PUT | `/marketplace/items/{itemid}/prices/automate` | 1 | [JSON](./operations/put-137ef16889f7.json) |
| `api.mercadolibre.com` | PUT | `/multi-marketplace-tool/config/automatic` | 1 | [JSON](./operations/put-29b7cafb610b.json) |
