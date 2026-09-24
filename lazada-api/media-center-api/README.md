---
title: "Lazada Media Center API"
description: "For video upload/delete/create API"
---

# API List

- [CompleteCreateVideo](operations/complete-create-video.json) (POST /media/video/block/commit) — After uploading all blocks of the video file,  call CompleteCreateVideo to complete the video uploading process.
- [GetVideo](operations/get-video.json) (GET /media/video/get) — You call this action to get video info after uploading.
- [GetVideoQuota](operations/get-video-quota.json) (GET /media/video/quota/get) — You call this api to get the capacity quota of seller.
- [InitCreateVideo](operations/init-create-video.json) (POST /media/video/block/create) — A seller starts to upload a video file
- [RemoveVideo](operations/remove-video.json) (POST /media/video/remove) — You can this api to delete a video file permanently.
- [UploadVideoBlock](operations/upload-video-block.json) (POST /media/video/block/upload) — The API is used to upload one block of origin video file. The video file can split into multiple files. For example, a 8MB video file can be split into three blocks. 3MB, 3MB and 2MB. These three blocks can be uploaded b

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
