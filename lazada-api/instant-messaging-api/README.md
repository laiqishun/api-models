---
title: "Lazada Instant Messaging API"
description: "Instant Messaging APIs"
---

# API List

- [GetMessages](operations/get-messages.json) (GET /im/message/list) — Get message list
- [GetSessionDetail](operations/get-session-detail.json) (GET /im/session/get) — get session detail by sessionid
- [GetSessionList](operations/get-session-list.json) (GET /im/session/list) — query seller session list
- [MessageRecall](operations/message-recall.json) (GET/POST /im/message/recall) — message recall
- [OpenSession](operations/open-session.json) (GET/POST /im/session/open) — open a new conversation
- [ReadSession](operations/read-session.json) (POST /im/session/read) — session read
- [SendMessage](operations/send-message.json) (POST /im/message/send) — send message

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
