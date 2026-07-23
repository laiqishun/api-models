---
title: Reporting
description: "Amazon Ads API group for asynchronous reporting operations."
---

# API List
- [createAsyncReport](operations/createAsyncReport.json) (POST /reporting/reports)：Creates a report request.
- [getAsyncReport](operations/getAsyncReport.json) (GET /reporting/reports/{reportId})：Gets a generation status of report by id. When `status` is `COMPLETED`, download the report from the returned `url`.
- [deleteAsyncReport](operations/deleteAsyncReport.json) (DELETE /reporting/reports/{reportId})：Deletes a report by id. Use this operation to cancel a report in a `PENDING` status.
