# Getting started

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Authorization and Token Best Practices](https://global-selling.mercadolibre.com/devsite/authorization-and-token-best-practices) | 1 | 1 | partial |
| [Official: CyberSecurity Best Practices](https://global-selling.mercadolibre.com/devsite/cybersecurity-best-practices) | 0 | 0 | guide-only |
| [Official: Security requirements and validations](https://global-selling.mercadolibre.com/devsite/security-requirements-and-validations) | 0 | 0 | guide-only |
| [Official: Create application](https://global-selling.mercadolibre.com/devsite/create-application) | 0 | 0 | guide-only |
| [Official: Authentication and Authorization](https://global-selling.mercadolibre.com/devsite/authentication-and-authorization-global-selling) | 2 | 1 | partial |
| [Official: Users](https://global-selling.mercadolibre.com/devsite/manage-users-global-selling) | 10 | 0 | modeled |
| [Official: Test users](https://global-selling.mercadolibre.com/devsite/start-testing-global-selling) | 3 | 0 | modeled |
| [Official: Application and permissions](https://global-selling.mercadolibre.com/devsite/application-manager-gs) | 5 | 0 | modeled |
| [Official: Design considerations](https://global-selling.mercadolibre.com/devsite/design-considerations-global-selling) | 3 | 0 | modeled |
| [Official: Support for Integrators](https://global-selling.mercadolibre.com/devsite/support-for-integrators) | 0 | 0 | guide-only |

## API List

- [createGlobalTestUser](operations/createGlobalTestUser.json) (POST /users/global_selling_test_user)：Create a global test user [Official](https://global-selling.mercadolibre.com/devsite/start-testing-global-selling)
- [createMarketplaceTestUser](operations/createMarketplaceTestUser.json) (POST /users/test_user)：Create a marketplace test user [Official](https://global-selling.mercadolibre.com/devsite/start-testing-global-selling)
- [deleteRevokePermissionsApplication](operations/deleteRevokePermissionsApplication.json) (DELETE /users/{cust_id}/applications/{app_id})：Revoke permissions to an application. [Official](https://global-selling.mercadolibre.com/devsite/manage-users-global-selling)
- [deleteRevokeUserAuthorization](operations/deleteRevokeUserAuthorization.json) (DELETE /users/{user_id}/applications/{app_id})：Revoke user authorization [Official](https://global-selling.mercadolibre.com/devsite/application-manager-gs)
- [getAcceptedPaymentMethodsByUser](operations/getAcceptedPaymentMethodsByUser.json) (GET /users/{user_id}/accepted_payment_methods)：Get accepted payment methods by user. [Official](https://global-selling.mercadolibre.com/devsite/manage-users-global-selling)
- [getApplicationConsumptionMetrics](operations/getApplicationConsumptionMetrics.json) (GET /applications/v1/{app_id}/consumed-applications)：Application Consumption Metrics [Official](https://global-selling.mercadolibre.com/devsite/application-manager-gs)
- [getApplicationDetails](operations/getApplicationDetails.json) (GET /applications/{app_id})：Get application details. [Official](https://global-selling.mercadolibre.com/devsite/manage-users-global-selling)
- [getApplicationsAuthorizedByUser](operations/getApplicationsAuthorizedByUser.json) (GET /users/{user_id}/applications)：Applications authorized by user [Official](https://global-selling.mercadolibre.com/devsite/application-manager-gs)
- [getBrandsByUser](operations/getBrandsByUser.json) (GET /users/{user_id}/brands)：Get brands by user. [Official](https://global-selling.mercadolibre.com/devsite/manage-users-global-selling)
- [getDefaultValues](operations/getDefaultValues.json) (GET /sites/MLM/search)：Default values [Official](https://global-selling.mercadolibre.com/devsite/design-considerations-global-selling)
- [getHistoricNotificationsByApp](operations/getHistoricNotificationsByApp.json) (GET /missed_feeds)：Get historic of notifications by app [Official](https://global-selling.mercadolibre.com/devsite/manage-users-global-selling)
- [getJsonFormat](operations/getJsonFormat.json) (GET /currencies/MXN)：JSON format [Official](https://global-selling.mercadolibre.com/devsite/design-considerations-global-selling)
- [getMappingUserAndItsCorrespondingMarketplace](operations/getMappingUserAndItsCorrespondingMarketplace.json) (GET /marketplace/users/{user_id})：Get the mapping of a user and its corresponding marketplace: [Official](https://global-selling.mercadolibre.com/devsite/manage-users-global-selling)
- [getReduceResponses](operations/getReduceResponses.json) (GET /currencies)：Reduce responses [Official](https://global-selling.mercadolibre.com/devsite/design-considerations-global-selling)
- [getUserAddresses](operations/getUserAddresses.json) (GET /users/{user_id}/addresses)：Get user addresses. [Official](https://global-selling.mercadolibre.com/devsite/manage-users-global-selling)
- [getUserInformation](operations/getUserInformation.json) (GET /users/{user_id})：Get user information. [Official](https://global-selling.mercadolibre.com/devsite/manage-users-global-selling)
- [getUsersGrantedPermissionsApp](operations/getUsersGrantedPermissionsApp.json) (GET /applications/{app_id}/grants)：Users granted permissions to app [Official](https://global-selling.mercadolibre.com/devsite/application-manager-gs)
- [obtainAccessTokenBySendingBodyParameters](operations/obtainAccessTokenBySendingBodyParameters.json) (POST /oauth/token)：Obtain access token by sending body parameters [Official](https://global-selling.mercadolibre.com/devsite/authorization-and-token-best-practices)
- [sendAccessTokenByHeader](operations/sendAccessTokenByHeader.json) (GET /users/me)：Send access token by header [Official](https://global-selling.mercadolibre.com/devsite/authentication-and-authorization-global-selling)
- [updateUserInformation](operations/updateUserInformation.json) (PUT /users/{user_id})：Update user information. [Official](https://global-selling.mercadolibre.com/devsite/manage-users-global-selling)
