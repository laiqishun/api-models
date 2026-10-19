---
title: "SHEIN Feed API"
description: "SHEIN official category 3000003, with one JSON model per named operation."
---

# API List

Official category: [Feed (3000003)](https://open.sheincorp.com/documents/apidoc/3000003). 6 records. Official IDs, applicable modes, and update times remain in the [manifest](../manifest.md) and each JSON file.

- [cancelFeed](operations/cancelFeed.json) (POST /open-api/sem/feed/cancelFeed)：Cancel Feed（取消Feed任务）
- [createFeed](operations/createFeed.json) (POST /open-api/sem/feed/createFeed)：Create Feed（创建Feed任务）
- [createFeedFile](operations/createFeedFile.json) (POST /open-api/sem/feed/createFeedDocument)：Create Feed file（创建Feed文件）
- [getFeedResult](operations/getFeedResult.json) (GET /open-api/sem/feed/getFeed)：Get Feed Result（查看Feed任务）
- [queryFeedFile](operations/queryFeedFile.json) (GET /open-api/sem/feed/getFeedDocument)：Query Feed file（查询Feed文件）
- [uploadFeedFile](operations/uploadFeedFile.json) (POST /open-api/sem/feed/uploadDocumentContent)：Upload Feed file（上传Feed文件）
