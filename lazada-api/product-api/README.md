---
title: "Lazada Product API"
description: "Product Management"
---

# API List

- [AdjustSellableQuantity](operations/adjust-sellable-quantity.json) (POST /product/stock/sellable/adjust) — Use this API to increase or decrease sellable quantity of one or more existing products. The maximum number of products that can be updated is 50, but 20 is recommended.
- [BatchUpdateSizeChart](operations/batch-update-size-chart.json) (POST /size/chart/batch/update) — 批量更新尺码表
- [CreateProduct](operations/create-product.json) (POST /product/create) — Use this API to create a single new product.

Find more details below: https://open.lazada.com/apps/doc/doc?nodeId=30720&docId=120949
- [DeactivateProduct](operations/deactivate-product.json) (POST /product/deactivate) — Use this API to deactivate Product or SKUs corresponding to the product
- [GetBrandByPages](operations/get-brand-by-pages.json) (GET/POST /category/brands/query) — Use this API to retrieve all product brands by page index in the system.
- [GetCategoryAttributes](operations/get-category-attributes.json) (GET /category/attributes/get) — Use this API to get a list of attributes for a specified product category.
- [GetCategorySuggestion](operations/get-category-suggestion.json) (GET /product/category/suggestion/get) — Get product's category suggestion by product title
- [GetCategoryTree](operations/get-category-tree.json) (GET /category/tree/get) — Use this API to retrieve the list of all product categories in the system.
- [GetNextCascadeProp](operations/get-next-cascade-prop.json) (GET/POST /category/cascade/getNextCascadeProp) — Use this API to query next cascade prop.
- [GetPreQcRules](operations/get-pre-qc-rules.json) (GET/POST /product/seller/item/getPreQcRules) — query pre qc rules
- [GetProductContentScore](operations/get-product-content-score.json) (GET/POST /product/content/score/get) — get product content score
- [GetProductItem](operations/get-product-item.json) (GET /product/item/get) — Get single product by ItemId or SellerSku.
- [GetProducts](operations/get-products.json) (GET /products/get) — Use this API to get detailed information of the specified products.
- [GetQCAlertProducts](operations/get-qc-alert-products.json) (GET /product/qc/alert/list) — Getting seller's products that have been alerted by quality control.
- [GetResponse](operations/get-response.json) (GET /image/response/get) — Use this API to get the returned information from the system for the MigrateImages API.
- [GetSellerItemLimit](operations/get-seller-item-limit.json) (GET /product/seller/item/limit) — The platform will provide the product quantity limit information by this interface. The qps will be limited by seller, 10 qps per seller.
- [GetSizeChartTemplate](operations/get-size-chart-template.json) (GET /size/chart/template/get) — 获取尺码模板列表
- [GetUnfilledAttributeItem](operations/get-unfilled-attribute-item.json) (GET/POST /product/unfilled/attribute/get) — Get products without key attributes. (For cross boarder sellers Only)
- [MigrateImage](operations/migrate-image.json) (POST /image/migrate) — Use this API to migrate a single image from an external site to Lazada site. Allowed image formats are JPG and PNG. The maximum size of an image file is 1MB.
- [MigrateImages](operations/migrate-images.json) (POST /images/migrate) — Use this API to migrate multiple images from an external site to Lazada site. Allowed image formats are JPG and PNG. The maximum size of an image file is 1MB. A single call can migrate 8 images at most.
- [ProductCheck](operations/product-check.json) (GET/POST /product/pre/check) — Use this API to check CB seller quantity limit of adding product .
- [RemoveProduct](operations/remove-product.json) (POST /product/remove) — Use this API to remove an existing product, some SKUs in one product, or all SKUs in one product. System supports a maximum number of 50 SellerSkus in one request.
- [RemoveSku](operations/remove-sku.json) (POST /product/sku/remove) — Use this API to delete SKUs and sales attributes of corresponding products.
- [SetImages](operations/set-images.json) (POST /images/set) — Use this API to set the images for an existing product by associating one or more image URLs with it.
- [UpdatePriceQuantity](operations/update-price-quantity.json) (POST /product/price_quantity/update) — Use this API to update the price and quantity of one or more existing products. The maximum number of products that can be updated is 50, but 20 is recommended.
- [UpdateProduct](operations/update-product.json) (POST /product/update) — Use this API to update attributes or SKUs of an existing product. if need update inventory, offline, price, not recommended to use this API.
The iteration 25/6/2020 Updated for DBS changes. Refer to Input Parameters Payl
- [UpdateSellableQuantity](operations/update-sellable-quantity.json) (GET/POST /product/stock/sellable/update) — Use this API to update sellable quantity of one or more existing products. The maximum number of products that can be updated is 50, but 20 is recommended.
- [UploadImage](operations/upload-image.json) (POST /image/upload) — Use this API to upload a single image file to Lazada site. Allowed image formats are JPG and PNG. The maximum size of an image file is 1MB.

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
