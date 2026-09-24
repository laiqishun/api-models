---
title: "Lazada Seller Voucher API"
description: "for Seller Voucher API"
---

# API List

- [SellerVoucheDeleteSelectedProductSKU](operations/seller-vouche-delete-selected-product-sku.json) (POST /promotion/voucher/product/sku/remove) — delete seller voucher promotion product sku
- [SellerVoucherActivate](operations/seller-voucher-activate.json) (POST /promotion/voucher/activate) — activate seller voucher promotion
- [SellerVoucherAddSelectedProductSKU](operations/seller-voucher-add-selected-product-sku.json) (POST /promotion/voucher/product/sku/add) — add seller voucher promotion product sku
- [SellerVoucherCreate](operations/seller-voucher-create.json) (POST /promotion/voucher/create) — create a new seller voucher promotion
- [SellerVoucherDeactivate](operations/seller-voucher-deactivate.json) (POST /promotion/voucher/deactivate) — deactivate seller voucher promotion
- [SellerVoucherDetailQuery](operations/seller-voucher-detail-query.json) (GET /promotion/voucher/get) — get a seller voucher promotion detail
- [SellerVoucherList](operations/seller-voucher-list.json) (GET /promotion/vouchers/get) — query seller voucher promotion list
- [SellerVoucherSelectedProductList](operations/seller-voucher-selected-product-list.json) (GET /promotion/voucher/products/get) — query seller voucher selected products list
- [SellerVoucherUpdate](operations/seller-voucher-update.json) (POST /promotion/voucher/update) — update a existing seller voucher promotion

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
