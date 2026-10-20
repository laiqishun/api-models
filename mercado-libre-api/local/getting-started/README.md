# Getting started

Local seller official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Create an application on Mercado Libre](https://developers.mercadolibre.com.ar/en_us/register-your-application) | 0 | 0 | guide-only |
| [Official: Validations and security requirements](https://developers.mercadolibre.com.ar/en_us/validations-and-security-requirements) | 0 | 0 | guide-only |
| [Official: CyberSecurity Practices](https://developers.mercadolibre.com.ar/en_us/cybersecurity-practices) | 0 | 0 | guide-only |
| [Official: Authorization and Token Recommendations](https://developers.mercadolibre.com.ar/en_us/authorization-and-token-recommendations) | 2 | 1 | partial |
| [Official: Manage your applications](https://developers.mercadolibre.com.ar/en_us/manage-your-applications) | 5 | 0 | modeled |
| [Official: Authentication and Authorization](https://developers.mercadolibre.com.ar/en_us/authentication-and-authorization) | 2 | 1 | partial |
| [Official: Start testing](https://developers.mercadolibre.com.ar/en_us/start-testing) | 1 | 0 | modeled |
| [Official: Listing validator](https://developers.mercadolibre.com.ar/en_us/listing-validator) | 1 | 0 | modeled |
| [Official: Validate seller's information](https://developers.mercadolibre.com.ar/en_us/validate-sellers) | 1 | 0 | modeled |
| [Official: Design considerations](https://developers.mercadolibre.com.ar/en_us/design-considerations) | 3 | 0 | modeled |
| [Official: Manage an application IPs](https://developers.mercadolibre.com.ar/en_us/manage-an-application-ips) | 0 | 0 | guide-only |
| [Official: Support for Integrators](https://developers.mercadolibre.com.ar/en_us/integrator-support) | 0 | 0 | guide-only |

## API List

- [createTestUser](operations/createTestUser.json) (POST /users/test_user)：Create a test user [Official](https://developers.mercadolibre.com.ar/en_us/start-testing)
- [createValidationExamples](operations/createValidationExamples.json) (POST /items/validate)：Validation examples [Official](https://developers.mercadolibre.com.ar/en_us/listing-validator)
- [deleteByUserIdApplicationsByAppId](operations/deleteByUserIdApplicationsByAppId.json) (DELETE /users/{user_id}/applications/{app_id})：Revoke user authorization [Official](https://developers.mercadolibre.com.ar/en_us/manage-your-applications)
- [getApplicationsByAppId](operations/getApplicationsByAppId.json) (GET /applications/{app_id})：Application details [Official](https://developers.mercadolibre.com.ar/en_us/manage-your-applications)
- [getAuthorizedApplicationsByUser](operations/getAuthorizedApplicationsByUser.json) (GET /users/{user_id}/applications)：Authorized applications by user [Official](https://developers.mercadolibre.com.ar/en_us/manage-your-applications)
- [getBySiteIdSearch](operations/getBySiteIdSearch.json) (GET /sites/{site_id}/search)：Default values [Official](https://developers.mercadolibre.com.ar/en_us/design-considerations)
- [getJsonpUsage](operations/getJsonpUsage.json) (GET /currencies/ARS)：JSONP Usage [Official](https://developers.mercadolibre.com.ar/en_us/design-considerations)
- [getReducingResponses](operations/getReducingResponses.json) (GET /currencies)：Reducing responses [Official](https://developers.mercadolibre.com.ar/en_us/design-considerations)
- [getUsersMe](operations/getUsersMe.json) (GET /users/me)：Send access token by header [Official](https://developers.mercadolibre.com.ar/en_us/authorization-and-token-recommendations)
- [getUsersWhoGavePermissionsYourApplication](operations/getUsersWhoGavePermissionsYourApplication.json) (GET /applications/{app_id}/grants)：Users who gave permissions to your application [Official](https://developers.mercadolibre.com.ar/en_us/manage-your-applications)
- [getYourApplicationConsumptionMetrics](operations/getYourApplicationConsumptionMetrics.json) (GET /applications/v1/{app_id}/consumed-applications)：Your application's consumption metrics [Official](https://developers.mercadolibre.com.ar/en_us/manage-your-applications)
- [postOauthToken](operations/postOauthToken.json) (POST /oauth/token)：Obtain access token by sending body parameters [Official](https://developers.mercadolibre.com.ar/en_us/authorization-and-token-recommendations)
- [validateSellerInformation](operations/validateSellerInformation.json) (GET /users/{user_id})：Validate seller's information [Official](https://developers.mercadolibre.com.ar/en_us/validate-sellers)
