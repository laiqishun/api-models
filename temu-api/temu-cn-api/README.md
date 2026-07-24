# Temu CN API

China cross-border Temu APIs, including current CN gateway operations and PA gateway replacements.

## How To Call

All operation files are Swagger 2.0 documents. Temu router APIs are called with `POST` and a `type` parameter. Put common auth/signature fields together with the operation request fields in the JSON body unless your runtime wraps common parameters separately.

Default gateway: `/openapi/router`

Note: CN source tables state /openapi/router. Use the CN host configured for the seller application.

For fields whose values come from the CN data dictionary, use [offline-docs/data-dictionary.md](offline-docs/data-dictionary.md).

## API Groups

- [Authorization](./authorization-api/README.md) - 1 operations
- [Authorization PA](./authorization-api-pa/README.md) - 1 operations
- [Category Attribute](./category-attribute-api/README.md) - 11 operations
- [Category Attribute PA](./category-attribute-api-pa/README.md) - 4 operations
- [Image Processing](./image-processing-api/README.md) - 10 operations
- [Instruction File](./instruction-file-api/README.md) - 4 operations
- [Instruction File PA](./instruction-file-api-pa/README.md) - 1 operations
- [Inventory PA](./inventory-api-pa/README.md) - 4 operations
- [JIT](./jit-api/README.md) - 4 operations
- [JIT PA](./jit-api-pa/README.md) - 1 operations
- [Marketing Activity PA](./marketing-activity-api-pa/README.md) - 6 operations
- [Model Fitting](./model-fitting-api/README.md) - 4 operations
- [PA Gateway](./partner-gateway-api/README.md) - 1 operations
- [Price Review](./price-review-api/README.md) - 5 operations
- [Price Review PA](./price-review-api-pa/README.md) - 6 operations
- [Product](./product-api/README.md) - 5 operations
- [Product PA](./product-api-pa/README.md) - 5 operations
- [Product Barcode PA](./product-barcode-api-pa/README.md) - 2 operations
- [Product Edit](./product-edit-api/README.md) - 1 operations
- [Product Edit PA](./product-edit-api-pa/README.md) - 7 operations
- [Sales](./sales-api/README.md) - 1 operations
- [Sample Quality Return](./sample-quality-return-api/README.md) - 7 operations
- [Size Chart](./size-chart-api/README.md) - 7 operations
- [Size Chart PA](./size-chart-api-pa/README.md) - 1 operations
- [Stock And Shipping](./stock-shipping-api/README.md) - 21 operations
- [Video Upload](./video-upload-api/README.md) - 2 operations
- [Waybill And Box Label](./waybill-box-label-api/README.md) - 2 operations

## Build Notes

- Excluded 31 migrated legacy CN types when a PA replacement was available or synthesized.
- Synthesized 12 PA operation files from legacy schemas because the migration table listed a PA type without a detailed PA section.

## Source Checked

- `C:\Users\Administrator\Downloads\Temu CN API文档.md`
