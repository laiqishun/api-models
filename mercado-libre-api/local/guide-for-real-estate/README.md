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

## Operation models

| Host | Method | Path | Source pages | JSON |
|---|---|---|---:|---|
| `api.mercadolibre.com` | DELETE | `/users/{your_cust_id}/order_blacklist/{seller_id}` | 1 | [JSON](./operations/delete-a0f317117568.json) |
| `api.mercadolibre.com` | GET | `/classified_locations/cities/TUxBQ0NBUGZlZG1sYQ` | 2 | [JSON](./operations/get-7e6b4ef09d6e.json) |
| `api.mercadolibre.com` | GET | `/classified_locations/cities/{city_id}` | 2 | [JSON](./operations/get-2744f9b0c2e5.json) |
| `api.mercadolibre.com` | GET | `/classified_locations/countries/AR` | 2 | [JSON](./operations/get-156bd56b0d11.json) |
| `api.mercadolibre.com` | GET | `/classified_locations/countries/{country_id}` | 2 | [JSON](./operations/get-ebf40503adfb.json) |
| `api.mercadolibre.com` | GET | `/classified_locations/neighborhoods/TUxBQkNBQjM4MDda` | 2 | [JSON](./operations/get-4688aa8b1a16.json) |
| `api.mercadolibre.com` | GET | `/classified_locations/neighborhoods/{neighborhood_id}` | 1 | [JSON](./operations/get-d16541d65ba3.json) |
| `api.mercadolibre.com` | GET | `/classified_locations/neighborhoods/{neighborhoods_id}` | 1 | [JSON](./operations/get-7add2fcab8a1.json) |
| `api.mercadolibre.com` | GET | `/classified_locations/states/TUxBUENBUGw3M2E1` | 2 | [JSON](./operations/get-249f70ff977e.json) |
| `api.mercadolibre.com` | GET | `/classified_locations/states/{state_id}` | 2 | [JSON](./operations/get-62d41e563204.json) |
| `api.mercadolibre.com` | GET | `/collections/{payment_id}` | 3 | [JSON](./operations/get-e67a9e0db9a6.json) |
| `api.mercadolibre.com` | GET | `/items/contacts/whatsapp/time_window` | 2 | [JSON](./operations/get-1700a4fc49ad.json) |
| `api.mercadolibre.com` | GET | `/items/{item_id}/contacts/phone_views` | 2 | [JSON](./operations/get-c31b1aeb322a.json) |
| `api.mercadolibre.com` | GET | `/items/{item_id}/contacts/phone_views/time_window` | 2 | [JSON](./operations/get-b9b7657acdd9.json) |
| `api.mercadolibre.com` | GET | `/items/{item_id}/contacts/whatsapp` | 2 | [JSON](./operations/get-98618cef40a5.json) |
| `api.mercadolibre.com` | GET | `/items/{item_id}/contacts/whatsapp/time_window` | 2 | [JSON](./operations/get-312f197c1414.json) |
| `api.mercadolibre.com` | GET | `/myfeeds` | 3 | [JSON](./operations/get-55bb281c8fa6.json) |
| `api.mercadolibre.com` | GET | `/oauth/token` | 1 | [JSON](./operations/get-987fbb7a34b3.json) |
| `api.mercadolibre.com` | GET | `/quotations/items_ids` | 1 | [JSON](./operations/get-c84701d20f2e.json) |
| `api.mercadolibre.com` | GET | `/quotations/report` | 1 | [JSON](./operations/get-75846e520c27.json) |
| `api.mercadolibre.com` | GET | `/quotations/{id}` | 1 | [JSON](./operations/get-a5833c3f87e0.json) |
| `api.mercadolibre.com` | GET | `/quotations/{quotationid}` | 1 | [JSON](./operations/get-fed0f97d26ba.json) |
| `api.mercadolibre.com` | GET | `/sites/Site_id/categories` | 1 | [JSON](./operations/get-61b4243c9776.json) |
| `api.mercadolibre.com` | GET | `/sites/{site_id}/categories/all` | 1 | [JSON](./operations/get-99682e43d765.json) |
| `api.mercadolibre.com` | GET | `/users/{cuyour_cust_idst_id}/order_blacklist` | 1 | [JSON](./operations/get-5daae64f31ae.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/classifieds_promotion_packs/{listing_type}` | 2 | [JSON](./operations/get-dcd89f9b9812.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/contacts/phone_views/time_window` | 2 | [JSON](./operations/get-af08dd7a5618.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/contacts/questions` | 2 | [JSON](./operations/get-c1af6b985829.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/contacts/questions/time_window` | 2 | [JSON](./operations/get-e0ce12909ca1.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/contacts/whatsapp/time_window` | 2 | [JSON](./operations/get-c4f3442266ca.json) |
| `api.mercadolibre.com` | GET | `/vis-transactions-hub/configurations/provider/{providerid}` | 1 | [JSON](./operations/get-06be64a4868c.json) |
| `api.mercadolibre.com` | GET | `/vis-transactions-hub/configurations/seller/{sellerid}` | 1 | [JSON](./operations/get-656b55d09460.json) |
| `api.mercadolibre.com` | GET | `/vis-transactions-hub/{providerid}/entities/item-candidates/seller/{sellerid}` | 1 | [JSON](./operations/get-d6b32f80581b.json) |
| `api.mercadolibre.com` | GET | `/vis-transactions-hub/{providerid}/entities/schedules/{scheduleid}` | 1 | [JSON](./operations/get-bf05db5180fb.json) |
| `api.mercadolibre.com` | GET | `/vis/loans/14b52fd8-85dc-11eb-8436-2753cb1f9665` | 2 | [JSON](./operations/get-90611f2ea44f.json) |
| `api.mercadolibre.com` | GET | `/vis/loans/search` | 2 | [JSON](./operations/get-16db72131ada.json) |
| `api.mercadolibre.com` | PATCH | `/vis-transactions-hub/configurations/provider/{providerid}` | 1 | [JSON](./operations/patch-7f37d70f859d.json) |
| `api.mercadolibre.com` | POST | `/vis-transactions-hub/configurations/provider` | 1 | [JSON](./operations/post-30e8e860f177.json) |
| `api.mercadolibre.com` | POST | `/vis-transactions-hub/{providerid}/entities/item-candidates` | 1 | [JSON](./operations/post-e89fd4633ad9.json) |
| `api.mercadolibre.com` | PUT | `/items/ITEM` | 1 | [JSON](./operations/put-fdc98acc8e89.json) |
| `api.mercadolibre.com` | PUT | `/quotations/{quotationid}` | 1 | [JSON](./operations/put-04ab9e23682d.json) |
| `api.mercadolibre.com` | PUT | `/vis-transactions-hub/{providerid}/entities/items` | 1 | [JSON](./operations/put-41377ad3c586.json) |
| `api.mercadolibre.com` | PUT | `/vis-transactions-hub/{providerid}/entities/schedules` | 1 | [JSON](./operations/put-d28ed6e17a56.json) |
