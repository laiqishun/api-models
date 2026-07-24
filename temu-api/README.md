# Temu API Models

AI-friendly local Temu API documentation generated from the downloaded Markdown source files. The structure mirrors the local Amazon API docs style: regional API modules, API group READMEs, and operation-level Swagger 2.0 JSON files under `operations/`.

## Routing Rules

- Chinese cross-border stores, including full-managed and semi-managed stores, use [temu-cn-api](./temu-cn-api/README.md) for inventory.
- Chinese cross-border semi-managed stores should use the destination-region API for order-related operations.
- European local stores use [temu-eu-api](./temu-eu-api/README.md).
- US local stores use [temu-us-api](./temu-us-api/README.md).
- Americas outside the US use [temu-global-api](./temu-global-api/README.md).

## Calling Model

Temu router APIs are generally `POST` requests to an `/openapi/router` endpoint. Each operation JSON is a standalone Swagger 2.0 file with one `POST /openapi/router` operation. The API operation is selected by the `type` field, and common fields such as `app_key`, `access_token`, `timestamp`, `sign`, `data_type`, and `version` appear in the request body schema.

For CN APIs, some legacy CN gateway `type` values have migrated to the PA gateway. This local model prefers the PA replacement type when the source migration table marks the old type as migrated; old types that the source explicitly says are still used for full-managed flows are retained with migration notes.

## Modules

- [Temu CN API](./temu-cn-api/README.md) - 124 operations
- [Temu US Local API](./temu-us-api/README.md) - 104 operations
- [Temu EU Local API](./temu-eu-api/README.md) - 109 operations
- [Temu Global Local API](./temu-global-api/README.md) - 98 operations

## Offline References

- [Temu CN data dictionary](./temu-cn-api/offline-docs/data-dictionary.md) - local reference values used by CN product/inventory fields.

## Source Checked

- `C:\Users\Administrator\Downloads\Temu CN 数据字典(1).md`
- `C:\Users\Administrator\Downloads\Temu CN API文档.md`
- `C:\Users\Administrator\Downloads\Temu美国本土API文档.md`
- `C:\Users\Administrator\Downloads\Temu欧洲本土API文档.md`
- `C:\Users\Administrator\Downloads\Temu欧洲API文档新增接口-0416.md`
- `C:\Users\Administrator\Downloads\Temu全球API文档.md`
