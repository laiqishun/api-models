---
title: "Lazada Early Bird Price API"
description: "Set early bird price for new products and get more sales."
---

# API List

- [CreateEarlyBirdActivityV2](operations/create-early-bird-activity-v2.json) (POST /activity/early/bird/create/v2) — early bird price activity create
- [EarlyBirdActivityAddSkusV2](operations/early-bird-activity-add-skus-v2.json) (POST /activity/early/bird/addSkus/v2) — add skus for early bird activity
- [EarlyBirdActivityDeactivateSkusV2](operations/early-bird-activity-deactivate-skus-v2.json) (POST /activity/early/bird/deactivateSkus/v2) — deactivate Skus for early bird acivity
- [EarlyBirdActivityIsWhitelistSeller](operations/early-bird-activity-is-whitelist-seller.json) (POST /activity/early/bird/isWhitelistSeller) — is whitelist seller for early bird acivity

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
