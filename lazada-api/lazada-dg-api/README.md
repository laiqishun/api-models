---
title: "Lazada Lazada DG API"
description: "lazada digital good  API"
---

# API List

- [digitalServiceCdkCodeReceived](operations/digital-service-cdk-code-received.json) (POST /digital/service/cdkCodeReceived) — 接受码商发码请求，给用户发送码。
- [InstallServiceCallBack](operations/install-service-call-back.json) (GET/POST /digital/install/servicecallback) — Install the service callback interface
- [InstallServiceCallBack](operations/install-service-call-back-246457.json) (GET/POST /digital/test/install/servicecallback) — Install the service callback interface
- [InstallServiceCallBackForTest](operations/install-service-call-back-for-test.json) (GET/POST /digital/install/test/servicecallback) — Install the service callback interface
- [InuranceNotication](operations/inurance-notication.json) (GET/POST /digital/insurance/notification) — Third party insurance company callback interface
- [InuranceNotication](operations/inurance-notication-246460.json) (GET/POST /digital/insurance/test/notificationcopy) — Third party insurance company callback interface
- [InuranceNotifyLapse](operations/inurance-notify-lapse.json) (GET/POST /digital/insurance/notificationlapse) — Insurance company push the callback notification to partners once the policy has been cancelled successfully

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
