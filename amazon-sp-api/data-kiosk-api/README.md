---
title: Selling Partner API for Data Kiosk
description: "The Selling Partner API for Data Kiosk lets you submit GraphQL queries from a variety of schemas to help selling partners manage their businesses."
---

# API List
- [getQueries](operations/getQueries.json) (GET /dataKiosk/2023-11-15/queries)：Returns details for the Data Kiosk queries that match the specified filters. See the `createQuery` operation for details about query retention.
- [createQuery](operations/createQuery.json) (POST /dataKiosk/2023-11-15/queries)：Creates a Data Kiosk query request.
- [cancelQuery](operations/cancelQuery.json) (DELETE /dataKiosk/2023-11-15/queries/{queryId})：Cancels the query specified by the `queryId` parameter. Only queries with a non-terminal `processingStatus` (`IN_QUEUE`, `IN_PROGRESS`) can be cancelled. Cancelling a query that already has a `processingStatus` of `CANCELLED` will no-op. Cancelled queries are returned in subsequent calls to the `getQuery` and `getQueries` operations.
- [getQuery](operations/getQuery.json) (GET /dataKiosk/2023-11-15/queries/{queryId})：Returns query details for the query specified by the `queryId` parameter. See the `createQuery` operation for details about query retention.
- [getDocument](operations/getDocument.json) (GET /dataKiosk/2023-11-15/documents/{documentId})：Returns the information required for retrieving a Data Kiosk document's contents. See the `createQuery` operation for details about document retention.
