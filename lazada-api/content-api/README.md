---
title: "Lazada Content API"
description: "The Content APIs are content-related APIs that are only available to specific users. Make sure that communication has been completed prior to applying permission to visit them."
---

# API List

- [cancelTask](operations/cancel-task.json) (POST /content/ai/cancelTask) — cancel tasks
- [changeFace](operations/change-face.json) (POST /content/ai/changeFace) — change face using lazada AI algorithm
- [changeProductBackground](operations/change-product-background.json) (POST /content/ai/changeProductBackground) — change product background using lazada AI algorithm
- [fixHand](operations/fix-hand.json) (POST /content/ai/fixHand) — fixHand using lazada AI algorithm
- [getTaskStatus](operations/get-task-status.json) (GET /content/ai/getTaskStatus) — get task status
- [productImageMatch](operations/product-image-match.json) (GET/POST /content/ai/productImageMatch) — match product image
- [tryOnCloth](operations/try-on-cloth.json) (POST /content/ai/tryOnCloth) — try on cloth using lazada AI algorithm

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
