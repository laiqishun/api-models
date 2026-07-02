---
title: Selling Partner API for Product Fees
description: "The Selling Partner API for Product Fees lets you programmatically retrieve estimated fees for a product. You can then account for those fees in your pricing."
---

# API List
- [getMyFeesEstimateForSKU](operations/getMyFeesEstimateForSKU.json) (POST /products/fees/v0/listings/{SellerSKU}/feesEstimate)：Returns the estimated fees for the item indicated by the specified seller SKU in the marketplace specified in the request body.
- [getMyFeesEstimateForASIN](operations/getMyFeesEstimateForASIN.json) (POST /products/fees/v0/items/{Asin}/feesEstimate)：Returns the estimated fees for the item indicated by the specified ASIN in the marketplace specified in the request body.
- [getMyFeesEstimates](operations/getMyFeesEstimates.json) (POST /products/fees/v0/feesEstimate)：Returns the estimated fees for a list of products.
