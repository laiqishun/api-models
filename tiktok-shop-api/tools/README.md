---
title: TikTok Shop Tools API
description: "Shared file and developer tool operations."
---

# API List

- [Upload File Init](operations/upload-file-init-202512.json) (POST /open/202512/file/init)：To upload a large file to TikTok Shop, such as a video, first use this API to initialize the upload session. Then upload the file to the returned upload URL; files smaller than 5 MB must be uploaded as a single, non-chunked request. After the upload step returns a ResourceId, pass that ResourceId to the API for the target path. For more details, see https://partner.tiktokshop.com/docv2/page/wfi3nz36.
