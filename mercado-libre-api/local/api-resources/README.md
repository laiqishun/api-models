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

## Operation models

| Host | Method | Path | Source pages | JSON |
|---|---|---|---:|---|
| `api.mercadolibre.com` | DELETE | `/users/me/bookmarks/{id}` | 1 | [JSON](./operations/delete-eb0ce3809240.json) |
| `api.mercadolibre.com` | DELETE | `/users/{cust_id}/applications/{app_id}` | 1 | [JSON](./operations/delete-6a4274337ffb.json) |
| `api.mercadolibre.com` | DELETE | `/users/{seller_id}/questions_blacklist/{user_id}` | 2 | [JSON](./operations/delete-e899ad6593f2.json) |
| `api.mercadolibre.com` | DELETE | `/users/{user_id}/order_blacklist/{id}` | 1 | [JSON](./operations/delete-d60f1bf0cd8c.json) |
| `api.mercadolibre.com` | GET | `/catalog_suggestions/{suggestion_id}` | 2 | [JSON](./operations/get-db13ab1e0b09.json) |
| `api.mercadolibre.com` | GET | `/categories/{category_id}` | 10 | [JSON](./operations/get-be0b111d1b70.json) |
| `api.mercadolibre.com` | GET | `/categories/{category_id}/attributes` | 8 | [JSON](./operations/get-867f16b8fd70.json) |
| `api.mercadolibre.com` | GET | `/categories/{category_id}/classifieds_promotion_packs` | 4 | [JSON](./operations/get-e2ee7fba1255.json) |
| `api.mercadolibre.com` | GET | `/categories/{category_id}/technical_specs/input` | 1 | [JSON](./operations/get-31805565d2bd.json) |
| `api.mercadolibre.com` | GET | `/classified_locations/cities/TUxVQ0NBQjY1MmQ1` | 1 | [JSON](./operations/get-a823bb660e50.json) |
| `api.mercadolibre.com` | GET | `/classified_locations/countries` | 3 | [JSON](./operations/get-3c8b607466f8.json) |
| `api.mercadolibre.com` | GET | `/classified_locations/countries/UY` | 1 | [JSON](./operations/get-273ee1c8ea3e.json) |
| `api.mercadolibre.com` | GET | `/classified_locations/states/UY-RO` | 1 | [JSON](./operations/get-fe34bc119fac.json) |
| `api.mercadolibre.com` | GET | `/communications/notices` | 1 | [JSON](./operations/get-ff355f2cca25.json) |
| `api.mercadolibre.com` | GET | `/countries/AR/zip_codes/{id}` | 1 | [JSON](./operations/get-ebee521b83dd.json) |
| `api.mercadolibre.com` | GET | `/country/AR/zip_codes/search_between` | 1 | [JSON](./operations/get-e2137cbc4c9d.json) |
| `api.mercadolibre.com` | GET | `/currencies/CLP` | 1 | [JSON](./operations/get-45459e0540d6.json) |
| `api.mercadolibre.com` | GET | `/currency_conversions/search` | 2 | [JSON](./operations/get-74ee54c572b8.json) |
| `api.mercadolibre.com` | GET | `/domains/MLA-JACKETS_AND_COATS/technical_specs` | 1 | [JSON](./operations/get-b236472572ce.json) |
| `api.mercadolibre.com` | GET | `/flex/sites/{site_id}/shipments/{shipment_id}/assignment/v1` | 3 | [JSON](./operations/get-0c9cf7aee331.json) |
| `api.mercadolibre.com` | GET | `/items` | 2 | [JSON](./operations/get-3fb41a0ed2bf.json) |
| `api.mercadolibre.com` | GET | `/items/contacts/phone_views/time_window` | 6 | [JSON](./operations/get-45c2c6fe9817.json) |
| `api.mercadolibre.com` | GET | `/items/visits` | 2 | [JSON](./operations/get-3924f48217ab.json) |
| `api.mercadolibre.com` | GET | `/items/visits/time_window` | 1 | [JSON](./operations/get-3ee421c13447.json) |
| `api.mercadolibre.com` | GET | `/items/{item_id}` | 25 | [JSON](./operations/get-c5f5b64ad91f.json) |
| `api.mercadolibre.com` | GET | `/items/{item_id}/contacts/questions` | 5 | [JSON](./operations/get-4cdc034ba5c6.json) |
| `api.mercadolibre.com` | GET | `/items/{item_id}/contacts/questions/time_window` | 6 | [JSON](./operations/get-d6e62f3e508a.json) |
| `api.mercadolibre.com` | GET | `/items/{item_id}/price_to_win` | 2 | [JSON](./operations/get-7609e41eb1db.json) |
| `api.mercadolibre.com` | GET | `/items/{item_id}/prices` | 2 | [JSON](./operations/get-d6693bc56e88.json) |
| `api.mercadolibre.com` | GET | `/items/{item_id}/shipping_options` | 3 | [JSON](./operations/get-9202115d022d.json) |
| `api.mercadolibre.com` | GET | `/items/{item_id}/visits/time_window` | 2 | [JSON](./operations/get-3b9db157ba12.json) |
| `api.mercadolibre.com` | GET | `/messages/{resource}` | 1 | [JSON](./operations/get-c33b0555ca44.json) |
| `api.mercadolibre.com` | GET | `/missed_feeds` | 3 | [JSON](./operations/get-0cb382621c60.json) |
| `api.mercadolibre.com` | GET | `/moderations/infractions/{id}` | 2 | [JSON](./operations/get-8d37ea7b4ce5.json) |
| `api.mercadolibre.com` | GET | `/moderations/infractions/{user_id}` | 2 | [JSON](./operations/get-436bc4ce42e6.json) |
| `api.mercadolibre.com` | GET | `/moderations/last_moderation/MLA123444123-ITM` | 1 | [JSON](./operations/get-82e94f39df24.json) |
| `api.mercadolibre.com` | GET | `/moderations/last_moderation/MLA926647862-ITM` | 1 | [JSON](./operations/get-7c76b19772e7.json) |
| `api.mercadolibre.com` | GET | `/moderations/last_moderation/{moderation_reference_id}` | 3 | [JSON](./operations/get-39b059d7ecbc.json) |
| `api.mercadolibre.com` | GET | `/moderations/pppi/case/123` | 1 | [JSON](./operations/get-e0f989add0a8.json) |
| `api.mercadolibre.com` | GET | `/moderations/pppi/case/{case_id}` | 1 | [JSON](./operations/get-ba3123d7c4a6.json) |
| `api.mercadolibre.com` | GET | `/moderations/pppi/case/{denounce_id}` | 1 | [JSON](./operations/get-30a4902f29c3.json) |
| `api.mercadolibre.com` | GET | `/moderations/pppi/case/{id}` | 1 | [JSON](./operations/get-2474bf46a78b.json) |
| `api.mercadolibre.com` | GET | `/moderations/pppi/cases` | 1 | [JSON](./operations/get-c51adae12dea.json) |
| `api.mercadolibre.com` | GET | `/moderations/pppi/denounces/MLA/ITM/options` | 1 | [JSON](./operations/get-5552c6c86ad2.json) |
| `api.mercadolibre.com` | GET | `/moderations/pppi/denounces/{site_id}/ITM/options` | 1 | [JSON](./operations/get-402c8d2b23b1.json) |
| `api.mercadolibre.com` | GET | `/my/received_questions/search` | 1 | [JSON](./operations/get-5b103a6679fe.json) |
| `api.mercadolibre.com` | GET | `/orders/search` | 6 | [JSON](./operations/get-3a89145f6dae.json) |
| `api.mercadolibre.com` | GET | `/orders/{order_id}` | 12 | [JSON](./operations/get-948dd86947c5.json) |
| `api.mercadolibre.com` | GET | `/orders/{order_id}/feedback` | 2 | [JSON](./operations/get-e6fae400ec7d.json) |
| `api.mercadolibre.com` | GET | `/orders/{order_id}/product` | 2 | [JSON](./operations/get-8c71d0a6bc0a.json) |
| `api.mercadolibre.com` | GET | `/orders/{order_id}/shipments` | 3 | [JSON](./operations/get-c4e3ca8c4b85.json) |
| `api.mercadolibre.com` | GET | `/questions/search` | 7 | [JSON](./operations/get-ea91150225ec.json) |
| `api.mercadolibre.com` | GET | `/questions/{question_id}` | 6 | [JSON](./operations/get-abc35ee5fa49.json) |
| `api.mercadolibre.com` | GET | `/quotations/{quotation_id}` | 1 | [JSON](./operations/get-72f0b10796dc.json) |
| `api.mercadolibre.com` | GET | `/seller-promotions/candidates/{candidate_id}` | 2 | [JSON](./operations/get-60348d660283.json) |
| `api.mercadolibre.com` | GET | `/shipment_labels` | 4 | [JSON](./operations/get-e0030f676294.json) |
| `api.mercadolibre.com` | GET | `/shipments/{shipment_id}` | 5 | [JSON](./operations/get-b4bf0b5ceccd.json) |
| `api.mercadolibre.com` | GET | `/sites` | 1 | [JSON](./operations/get-d96ba0e2a6e7.json) |
| `api.mercadolibre.com` | GET | `/sites/{site_id}/categories` | 6 | [JSON](./operations/get-8f50424f36c5.json) |
| `api.mercadolibre.com` | GET | `/sites/{site_id}/domain_discovery/search` | 3 | [JSON](./operations/get-c97b021bb4f3.json) |
| `api.mercadolibre.com` | GET | `/sites/{site_id}/listing_exposures` | 2 | [JSON](./operations/get-18d37b13c670.json) |
| `api.mercadolibre.com` | GET | `/sites/{site_id}/listing_prices` | 10 | [JSON](./operations/get-7d127ae572d3.json) |
| `api.mercadolibre.com` | GET | `/sites/{site_id}/payment_methods` | 1 | [JSON](./operations/get-ba66f24ce327.json) |
| `api.mercadolibre.com` | GET | `/sites/{site_id}/payment_methods/amex` | 1 | [JSON](./operations/get-c7b1761e3e36.json) |
| `api.mercadolibre.com` | GET | `/sites/{site_id}/shipping_methods` | 2 | [JSON](./operations/get-f9b5b1d6e2ec.json) |
| `api.mercadolibre.com` | GET | `/sites/{site_id}/user-products-families/{family_id}` | 2 | [JSON](./operations/get-3e08bc51735b.json) |
| `api.mercadolibre.com` | GET | `/user-products/{user_product_id}/stock` | 5 | [JSON](./operations/get-82089946f540.json) |
| `api.mercadolibre.com` | GET | `/users` | 1 | [JSON](./operations/get-25655e62c49d.json) |
| `api.mercadolibre.com` | GET | `/users/${seller_id}/questions_blacklist` | 1 | [JSON](./operations/get-0338d99e1644.json) |
| `api.mercadolibre.com` | GET | `/users/:userID/order_blacklist` | 1 | [JSON](./operations/get-1b2d05835338.json) |
| `api.mercadolibre.com` | GET | `/users/me/bookmarks` | 1 | [JSON](./operations/get-1e03f80ee034.json) |
| `api.mercadolibre.com` | GET | `/users/{seller_id}/items/search` | 7 | [JSON](./operations/get-bb7e7adf95b1.json) |
| `api.mercadolibre.com` | GET | `/users/{seller_id}/questions_blacklist` | 2 | [JSON](./operations/get-960138a2f45e.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/accepted_payment_methods` | 1 | [JSON](./operations/get-c6f70a819e16.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/addresses` | 2 | [JSON](./operations/get-c3f71e019851.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/available_listing_type/gold_special` | 1 | [JSON](./operations/get-7b0fd85fb01f.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/available_listing_types` | 2 | [JSON](./operations/get-8cf86414f27d.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/brands` | 2 | [JSON](./operations/get-66ac6a09fb9f.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/classifieds_promotion_packs` | 3 | [JSON](./operations/get-f09c3aac5576.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/classifieds_promotion_packs/silver` | 2 | [JSON](./operations/get-c5d6b7caf11e.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/contacts/phone_views` | 3 | [JSON](./operations/get-022d83a4f856.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/items/search` | 17 | [JSON](./operations/get-8c4d1a783a29.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/items_visits` | 2 | [JSON](./operations/get-3b8f52c4c8a8.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/items_visits/time_window` | 2 | [JSON](./operations/get-101ac3e69da2.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/order_blacklist` | 1 | [JSON](./operations/get-460fe3cea94f.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/shipping_preferences` | 3 | [JSON](./operations/get-4e35ef3fe675.json) |
| `api.mercadolibre.com` | GET | `/vis/loans/{credit_id}` | 3 | [JSON](./operations/get-b8c8e38e3042.json) |
| `api.mercadolibre.com` | GET | `/{resource}` | 4 | [JSON](./operations/get-5b1d53874ce4.json) |
| `api.mercadolibre.com` | POST | `/answers` | 2 | [JSON](./operations/post-9c6c763c6617.json) |
| `api.mercadolibre.com` | POST | `/catalog_domains/MLA-CELLPHONES/attributes/BRAND/top_values` | 1 | [JSON](./operations/post-650e4357d571.json) |
| `api.mercadolibre.com` | POST | `/catalog_domains/MLA-CELLPHONES/attributes/MODEL/top_value` | 1 | [JSON](./operations/post-59b43afc3c44.json) |
| `api.mercadolibre.com` | POST | `/catalog_domains/{doamain_id}/attributes/{attribute_id}/top_value` | 1 | [JSON](./operations/post-a9b96aee4e96.json) |
| `api.mercadolibre.com` | POST | `/catalog_domains/{domain_id}/attributes/{attribute_id}/top_values` | 3 | [JSON](./operations/post-444b5e67722b.json) |
| `api.mercadolibre.com` | POST | `/categories/{category_id}/attributes/conditional` | 1 | [JSON](./operations/post-8ea6eb073615.json) |
| `api.mercadolibre.com` | POST | `/feedback/{id}/reply` | 1 | [JSON](./operations/post-13a4d0b6b217.json) |
| `api.mercadolibre.com` | POST | `/items` | 19 | [JSON](./operations/post-6eeb0889e5f5.json) |
| `api.mercadolibre.com` | POST | `/moderations/pictures/diagnostic` | 1 | [JSON](./operations/post-0b30b5f446dc.json) |
| `api.mercadolibre.com` | POST | `/moderations/pppi/case/{case_id}` | 1 | [JSON](./operations/post-ab8d1cff95e2.json) |
| `api.mercadolibre.com` | POST | `/moderations/pppi/case/{denounce_id}` | 1 | [JSON](./operations/post-2a0cf37fb435.json) |
| `api.mercadolibre.com` | POST | `/moderations/pppi/case/{id}` | 1 | [JSON](./operations/post-ec47e30c69af.json) |
| `api.mercadolibre.com` | POST | `/moderations/pppi/denounces/items/MLA123` | 2 | [JSON](./operations/post-98ea1d040e6e.json) |
| `api.mercadolibre.com` | POST | `/moderations/pppi/denounces/items/{item_id}` | 1 | [JSON](./operations/post-4a8b196447f2.json) |
| `api.mercadolibre.com` | POST | `/orders/{order_id}/feedback` | 2 | [JSON](./operations/post-b4ff700031db.json) |
| `api.mercadolibre.com` | POST | `/questions` | 2 | [JSON](./operations/post-cd57ce50c2d0.json) |
| `api.mercadolibre.com` | POST | `/users/me/bookmarks` | 1 | [JSON](./operations/post-12e5b4e9f35f.json) |
| `api.mercadolibre.com` | POST | `/users/{seller_id}/questions_blacklist` | 2 | [JSON](./operations/post-a23520af4b2d.json) |
| `api.mercadolibre.com` | POST | `/users/{user_id}/classifieds_promotion_packs` | 1 | [JSON](./operations/post-fa43086b1a89.json) |
| `api.mercadolibre.com` | POST | `/users/{user_id}/order_blacklist` | 1 | [JSON](./operations/post-aa18ab021906.json) |
| `api.mercadolibre.com` | PUT | `/feedback/{id}` | 1 | [JSON](./operations/put-2a35af407c5e.json) |
| `api.mercadolibre.com` | PUT | `/items/{item_id}` | 37 | [JSON](./operations/put-e8a2d3fe2796.json) |
| `api.mercadolibre.com` | PUT | `/moderations/pppi/case/files` | 1 | [JSON](./operations/put-91872c60cf92.json) |
| `api.mercadolibre.com` | PUT | `/users/{user_id}` | 5 | [JSON](./operations/put-21453870cfd7.json) |
