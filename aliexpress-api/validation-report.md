# AliExpress source validation

Snapshot: 2026-11-03. Sources: the official public category and detail responses at `open.aliexpress.com`, and the official SDK download linked by those detail responses.

| Check | Result |
|---|---:|
| Public catalog categories / records | 42 / 528 |
| Included AliExpress and shared categories / records | 36 / 496 |
| Excluded separate MIRAVIA categories / records | 6 / 32 |
| Unique included API names / detail document IDs | 496 / 496 |
| Retrieved included detail records | 496 / 496 |
| Integration solutions checked in Chinese and English | 4 / 4 |
| Additional guide-referenced APIs with readable details | 4 |
| Guide-referenced API with empty public detail | 1 |
| Named operation models, including supplements | 500 |
| Documented HTTP operations, including supplements | 920 |
| Official SDK request classes matched by exact API name, including supplements | 500 / 500 |
| Business request/response tree nodes compared, including supplements | 12,898 |
| Non-empty contract default values preserved | 59 |
| Binary fields represented with original byte[] type metadata | 9 |
| Missing or extra included catalog API names | 0 |

The recursive comparison checks field names, types, array elements, and requiredness. Original request, response, common-parameter, error and example metadata is retained under `x-aliexpress-reference`; sensitive sample values and SDK sample code values are redacted. Complex business schemas are definitions, not an assertion that object fields are transmitted as a JSON HTTP body. Response definitions describe business fields; the official sample envelope is kept separately as a redacted shape.

## Review corrections

The review found and corrected two conversion problems: 59 non-empty `defaultValue` entries had been unnecessarily replaced as sample values, and nine binary `byte[]` fields had been expressed as arrays of strings. Defaults are now preserved as source metadata. Binary business fields now use a string/binary schema with the original source type and an explicit wire-encoding note. The original 496 catalog records remain present; their names, methods, and source paths were not removed.

The live category response was fetched again and compared as category ID + API name/path + method sets: no additions, removals or method changes were found. Its four `solutionDocs` entries were missing from navigation and are now linked in [integration solutions](integration-solutions.md). The Chinese and English guide content and API hyperlinks were checked together; [guide-reference coverage](guide-reference-manifest.md) records every API reference and its outcome.

Four references absent from the main category list had readable detail records and matching official SDK request classes, and were added as supplemental models:

- `aliexpress.solution.batch.product.price.update`
- `aliexpress.solution.product.edit`
- `aliexpress.solution.product.post`
- `aliexpress.category.redefining.getchildrenpostcategorybyid`

One reference, `aliexpress.offer.redefining.getcanusedproductbysizetemplateid`, returned `success=true` with an empty `apiList`. Its contract, lifecycle and availability cannot be established from that response. It is retained as a source gap rather than a generated model. The supplemental modules do not imply current app permissions or working production access.

## Upstream field contradictions

Three source nodes declare `String` while also supplying nested child fields. The generated schema preserves the child structure as an object and records both the original type and the unresolved contradiction in `x-aliexpress-original-type` and `x-aliexpress-source-type-conflict`. This is not a correction to the official contract.

| API | Business response field |
|---|---|
| `aliexpress.product.customize.font.query` | `result.model` |
| `aliexpress.local.service.seller.self.hscode.query` | `result.seller_search_tax_rate_value_dtolist.cur_country_tax_rate_level` |
| `aliexpress.local.service.seller.self.hscode.query` | `result.seller_search_tax_rate_value_dtolist.tax_rate_level_dolist` |

## Validation boundary

JSON/Swagger validity, naming, unique operationIds, module and manifest links are local structural checks. They do not prove current application permissions, merchant authorization, live request serialization, production response envelopes or successful API calls. The newer `openservice.aliexpress.com` directory request timed out in this session; its availability and differences from the accessible official catalog are not established. The frozen source snapshot remains the collection boundary.
