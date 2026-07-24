# Temu EU Local API

Temu local seller API for European local stores. Includes the 0416 logistics scanform additions.

## How To Call

All operation files are Swagger 2.0 documents. Temu router APIs are called with `POST` and a `type` parameter. Put common auth/signature fields together with the operation request fields in the JSON body unless your runtime wraps common parameters separately.

Default gateway: `https://openapi-b-eu.temu.com/openapi/router`

## API Groups

- [Authorization](./authorization-api/README.md) - 3 operations
- [Fulfillment](./fulfillment-api/README.md) - 18 operations
- [Logistics](./logistics-api/README.md) - 8 operations
- [Order](./order-api/README.md) - 10 operations
- [Price](./price-api/README.md) - 12 operations
- [Product](./product-api/README.md) - 41 operations
- [Promotion](./promotion-api/README.md) - 6 operations
- [Return And Refund](./return-refund-api/README.md) - 9 operations
- [Tax](./tax-api/README.md) - 2 operations

## Source Checked

- `C:\Users\Administrator\Downloads\Temu欧洲本土API文档.md`
- `C:\Users\Administrator\Downloads\Temu欧洲API文档新增接口-0416.md`
