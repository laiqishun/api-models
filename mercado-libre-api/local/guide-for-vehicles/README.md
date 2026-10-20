# Guide for vehicles

Local seller official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Introduction](https://developers.mercadolibre.com.ar/en_us/introduction-vehicles) | 0 | 0 | guide-only |
| [Official: Manage users](https://developers.mercadolibre.com.ar/en_us/vehicles-manage-users) | 6 | 0 | modeled |
| [Official: Manage packages vehicles](https://developers.mercadolibre.com.ar/en_us/vehicles-manage-packages) | 4 | 1 | partial |
| [Official: Categories & attributes](https://developers.mercadolibre.com.ar/en_us/categories-attributes) | 8 | 0 | modeled |
| [Official: List vehicles](https://developers.mercadolibre.com.ar/en_us/list-vehicles) | 3 | 0 | modeled |
| [Official: Sync listings](https://developers.mercadolibre.com.ar/en_us/vehicles-sync-listings) | 1 | 0 | modeled |
| [Official: Manage questions & contacts](https://developers.mercadolibre.com.ar/en_us/vehicles-manage-contacts) | 13 | 1 | partial |
| [Official: Subscribe to our feeds](https://developers.mercadolibre.com.ar/en_us/vehicles-subscribe-to-our-feeds) | 6 | 0 | modeled |
| [Official: Interested persons](https://developers.mercadolibre.com.ar/en_us/interested-persons) | 3 | 0 | modeled |
| [Official: Credits pre-approved](https://developers.mercadolibre.com.ar/en_us/credits-pre-approved-vehicles) | 3 | 0 | modeled |

## API List

- [checkInterestedUsersInSeller](operations/checkInterestedUsersInSeller.json) (GET /vis/users/{user_id}/leads/buyers)：Check interested users in the seller’s [Official](https://developers.mercadolibre.com.ar/en_us/interested-persons)
- [deleteImmediatePaymentByUser](operations/deleteImmediatePaymentByUser.json) (DELETE /users/{user_id}/immediate_payment/by_user)：User Seller S = P (Sell Equal Pay) [Official](https://developers.mercadolibre.com.ar/en_us/vehicles-manage-users)
- [getDetailsLead](operations/getDetailsLead.json) (GET /vis/leads/3f2dedf2-dfbd-4981-a726-40b13aa172ff)：Get details of a Lead [Official](https://developers.mercadolibre.com.ar/en_us/interested-persons)
- [getDumpCategories](operations/getDumpCategories.json) (GET /sites/{site_id}/all)：Dump categories [Official](https://developers.mercadolibre.com.ar/en_us/categories-attributes)
- [getLeadsByLeadId](operations/getLeadsByLeadId.json) (GET /vis/leads/{lead_id})：Get details of a Lead [Official](https://developers.mercadolibre.com.ar/en_us/interested-persons)
- [postByUserIdImmediatePayment](operations/postByUserIdImmediatePayment.json) (POST /users/{user_id}/immediate_payment)：User Seller S = P (Sell Equal Pay) [Official](https://developers.mercadolibre.com.ar/en_us/vehicles-manage-users)
