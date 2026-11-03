# AliExpress source validation

Snapshot: 2026-11-03. Sources: the official public category and detail responses at `open.aliexpress.com`, and the official SDK download linked by those detail responses.

| Check | Result |
|---|---:|
| Public catalog categories / records | 42 / 528 |
| Included AliExpress and shared categories / records | 36 / 496 |
| Excluded separate MIRAVIA categories / records | 6 / 32 |
| Unique included API names / detail document IDs | 496 / 496 |
| Retrieved included detail records | 496 / 496 |
| Named operation models | 496 |
| Documented HTTP operations (combined GET/POST retained) | 912 |
| Official SDK request classes matched by exact API name | 496 / 496 |
| Business request/response tree nodes compared | 12,685 |
| Missing or extra included catalog API names | 0 |

The recursive comparison checks field names, types, array elements, and requiredness. Original request, response, common-parameter, error and example metadata is retained under `x-aliexpress-reference`; sensitive sample values and SDK sample code values are redacted. Complex business schemas are definitions, not an assertion that object fields are transmitted as a JSON HTTP body. Response definitions describe business fields; the official sample envelope is kept separately as a redacted shape.

## Upstream field contradictions

Three source nodes declare `String` while also supplying nested child fields. The generated schema preserves the child structure as an object and records both the original type and the unresolved contradiction in `x-aliexpress-original-type` and `x-aliexpress-source-type-conflict`. This is not a correction to the official contract.

| API | Business response field |
|---|---|
| `aliexpress.product.customize.font.query` | `result.model` |
| `aliexpress.local.service.seller.self.hscode.query` | `result.seller_search_tax_rate_value_dtolist.cur_country_tax_rate_level` |
| `aliexpress.local.service.seller.self.hscode.query` | `result.seller_search_tax_rate_value_dtolist.tax_rate_level_dolist` |

## Validation boundary

JSON/Swagger validity, naming, unique operationIds, module and manifest links are local structural checks. They do not prove current application permissions, merchant authorization, live request serialization, production response envelopes or successful API calls. The newer `openservice.aliexpress.com` directory request timed out in this session; its availability and differences from the accessible official catalog are not established. The frozen source snapshot remains the collection boundary.
