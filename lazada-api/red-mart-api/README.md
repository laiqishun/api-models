---
title: "Lazada RedMart API"
description: "API for RedMart"
---

# API List

- [RssGetOnePickupJob](operations/rss-get-one-pickup-job.json) (GET/POST /rss/pickup-job/get) — Get details of a pickup job
- [RssGetPickupJobs](operations/rss-get-pickup-jobs.json) (GET/POST /rss/pickup-jobs/get) — Retrieve RSS pickup jobs based on time range and status filter.
- [RssGetPickupLocations](operations/rss-get-pickup-locations.json) (GET /rss/pickupLocations/get) — rss get pickupLocations by storeId
- [RssGetProduct](operations/rss-get-product.json) (GET /rss/product/get) — get rss product by storeId and productId
- [RssGetProducts](operations/rss-get-products.json) (GET /rss/products/get) — rss get products paged by storeId and pickupLocationId
- [RssGetStockLot](operations/rss-get-stock-lot.json) (GET /rss/stockLot/get) — rss get stockLot
- [RssGetStockLots](operations/rss-get-stock-lots.json) (GET /rss/stockLots/get) — rss get stockLots
- [RssUpdateStockLot](operations/rss-update-stock-lot.json) (GET/POST /rss/stockLot/update) — rss update stockLot

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
