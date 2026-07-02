---
title: Selling Partner API for Reports
description: "The Selling Partner API for Reports lets you retrieve and manage a variety of reports that can help selling partners manage their businesses."
---

# API List
- [getReports](operations/getReports.json) (GET /reports/2021-06-30/reports)：Returns report details for the reports that match the filters that you specify.
- [createReport](operations/createReport.json) (POST /reports/2021-06-30/reports)：Creates a report.
- [cancelReport](operations/cancelReport.json) (DELETE /reports/2021-06-30/reports/{reportId})：Cancels the report that you specify. Only reports with `processingStatus=IN_QUEUE` can be cancelled. Cancelled reports are returned in subsequent calls to the `getReport` and `getReports` operations.
- [getReport](operations/getReport.json) (GET /reports/2021-06-30/reports/{reportId})：Returns report details (including the `reportDocumentId`, if available) for the report that you specify.
- [getReportSchedules](operations/getReportSchedules.json) (GET /reports/2021-06-30/schedules)：Returns report schedule details that match the filters that you specify.
- [createReportSchedule](operations/createReportSchedule.json) (POST /reports/2021-06-30/schedules)：Creates a report schedule. If a report schedule with the same report type and marketplace IDs already exists, it will be cancelled and replaced with this one.
- [cancelReportSchedule](operations/cancelReportSchedule.json) (DELETE /reports/2021-06-30/schedules/{reportScheduleId})：Cancels the report schedule that you specify.
- [getReportSchedule](operations/getReportSchedule.json) (GET /reports/2021-06-30/schedules/{reportScheduleId})：Returns report schedule details for the report schedule that you specify.
- [getReportDocument](operations/getReportDocument.json) (GET /reports/2021-06-30/documents/{reportDocumentId})：Returns the information required for retrieving a report document's contents.
