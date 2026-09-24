---
title: "Lazada LazLike API"
description: "LazLike Content API"
---

# API List

- [McnContentCancelSchedulePublish](operations/mcn-content-cancel-schedule-publish.json) (POST /content/mcn/content/cancelScheduled) — McnContentCancelSchedulePublish
- [McnContentCompleteCreateVideo](operations/mcn-content-complete-create-video.json) (POST /content/mcn/video/block/commit) — After uploading all blocks of the video file, call McnContentCompleteCreateVideo to complete the video uploading process.
- [McnContentCreate](operations/mcn-content-create.json) (POST /content/mcn/content/create) — create content
- [McnContentInitCreateVideo](operations/mcn-content-init-create-video.json) (GET/POST /content/mcn/video/block/create) — Initial an upload video process, this API will return the corresponding UploadID
- [McnContentListCategory](operations/mcn-content-list-category.json) (GET /content/mcn/category/list) — list mcn content categories
- [McnContentPropertyTagList](operations/mcn-content-property-tag-list.json) (GET/POST /content/mcn/property/list) — list mcn content property tags
- [McnContentReplySchedulePublish](operations/mcn-content-reply-schedule-publish.json) (POST /content/mcn/content/replySchedulePublish) — McnContentReplySchedulePublish
- [McnContentUploadImage](operations/mcn-content-upload-image.json) (POST /content/mcn/image/upload) — upload image
- [McnContentUploadVideoBlock](operations/mcn-content-upload-video-block.json) (POST /content/mcn/video/block/upload) — upload one block of video file
- [McnProductValidator](operations/mcn-product-validator.json) (GET /content/mcn/product/validate) — Identify high risk products
- [MCNQueryTagInfoByName](operations/mcn-query-tag-info-by-name.json) (GET/POST /content/mcn/content/queryTagInfosByName) — MCNQueryTagInfoByName
- [McnSimilarProductSearch](operations/mcn-similar-product-search.json) (GET/POST /content/mcn/similar/product/search) — 相似商品搜索接口
- [queryContentReviewRecords](operations/query-content-review-records.json) (GET/POST /content/mcn/content/queryReviewRecords) — Query content audit records. Currently, querying records with audit results of low (block) is supported.The number of query contents is limited to 500 (adjustable).

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
