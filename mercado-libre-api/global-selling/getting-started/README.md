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

## Operation models

| Host | Method | Path | Source pages | JSON |
|---|---|---|---:|---|
| `api.mercadolibre.com` | DELETE | `/users/{cust_id}/applications/{app_id}` | 1 | [JSON](./operations/delete-c9886bd03c25.json) |
| `api.mercadolibre.com` | DELETE | `/users/{user_id}/applications/{app_id}` | 1 | [JSON](./operations/delete-7f7ca89c7d8b.json) |
| `api.mercadolibre.com` | GET | `/applications/v1/{app_id}/consumed-applications` | 1 | [JSON](./operations/get-d88ae6b35ce8.json) |
| `api.mercadolibre.com` | GET | `/applications/{app_id}` | 2 | [JSON](./operations/get-9a5f9cfab3d7.json) |
| `api.mercadolibre.com` | GET | `/applications/{app_id}/grants` | 1 | [JSON](./operations/get-4a49f4b6bde7.json) |
| `api.mercadolibre.com` | GET | `/currencies` | 1 | [JSON](./operations/get-7caac35d0f4b.json) |
| `api.mercadolibre.com` | GET | `/currencies/MXN` | 1 | [JSON](./operations/get-11b5603c85ee.json) |
| `api.mercadolibre.com` | GET | `/marketplace/users/{user_id}` | 5 | [JSON](./operations/get-866d31b2cdb2.json) |
| `api.mercadolibre.com` | GET | `/missed_feeds` | 3 | [JSON](./operations/get-6330ea269bbc.json) |
| `api.mercadolibre.com` | GET | `/sites/MLM/search` | 8 | [JSON](./operations/get-342b6243cfec.json) |
| `api.mercadolibre.com` | GET | `/users/me` | 4 | [JSON](./operations/get-645e997b76b2.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}` | 5 | [JSON](./operations/get-0812f822fbf9.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/accepted_payment_methods` | 1 | [JSON](./operations/get-2a81ac60d9a6.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/addresses` | 1 | [JSON](./operations/get-8c23bd74830c.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/applications` | 1 | [JSON](./operations/get-ad26439033d9.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/brands` | 2 | [JSON](./operations/get-b497d8ebdcb7.json) |
| `api.mercadolibre.com` | POST | `/oauth/token` | 3 | [JSON](./operations/post-dc1166301156.json) |
| `api.mercadolibre.com` | POST | `/users/global_selling_test_user` | 1 | [JSON](./operations/post-1e57c6214b2f.json) |
| `api.mercadolibre.com` | POST | `/users/test_user` | 1 | [JSON](./operations/post-d0487c868577.json) |
| `api.mercadolibre.com` | PUT | `/users/{user_id}` | 4 | [JSON](./operations/put-2b528584c79e.json) |
