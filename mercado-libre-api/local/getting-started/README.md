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

## Operation models

| Host | Method | Path | Source pages | JSON |
|---|---|---|---:|---|
| `api.mercadolibre.com` | DELETE | `/users/{user_id}/applications/{app_id}` | 1 | [JSON](./operations/delete-89be15c1c293.json) |
| `api.mercadolibre.com` | GET | `/applications/v1/{app_id}/consumed-applications` | 1 | [JSON](./operations/get-20a99e1cc42e.json) |
| `api.mercadolibre.com` | GET | `/applications/{app_id}` | 3 | [JSON](./operations/get-e2b5f28b5a2a.json) |
| `api.mercadolibre.com` | GET | `/applications/{app_id}/grants` | 1 | [JSON](./operations/get-6ba6a9d0c625.json) |
| `api.mercadolibre.com` | GET | `/currencies` | 3 | [JSON](./operations/get-13584bf4ae56.json) |
| `api.mercadolibre.com` | GET | `/currencies/ARS` | 1 | [JSON](./operations/get-16f6d5631022.json) |
| `api.mercadolibre.com` | GET | `/sites/{site_id}/search` | 15 | [JSON](./operations/get-4d9f01f7e4b1.json) |
| `api.mercadolibre.com` | GET | `/users/me` | 7 | [JSON](./operations/get-9f2a0ee5948c.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}` | 14 | [JSON](./operations/get-8dc1057dfee6.json) |
| `api.mercadolibre.com` | GET | `/users/{user_id}/applications` | 1 | [JSON](./operations/get-9de9a21417d5.json) |
| `api.mercadolibre.com` | POST | `/items/validate` | 4 | [JSON](./operations/post-c39968a77888.json) |
| `api.mercadolibre.com` | POST | `/oauth/token` | 3 | [JSON](./operations/post-bce0abb3d5a4.json) |
| `api.mercadolibre.com` | POST | `/users/test_user` | 1 | [JSON](./operations/post-fe55ad4d27f1.json) |
