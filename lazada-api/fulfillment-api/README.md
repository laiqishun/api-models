---
title: "Lazada Fulfillment API"
description: "Fulfillment API"
---

# API List

- [ConfirmCollectForDBS](operations/confirm-collect-for-dbs.json) (POST /order/package/sof/collect) — Use this API to mark an sof order item as being collected.
- [ConfirmDeliveryForDBS](operations/confirm-delivery-for-dbs.json) (POST /order/package/sof/delivered) — Use this API to mark an sof order item as being delivered.
- [DeliverDigital](operations/deliver-digital.json) (POST /order/digital/delivered) — Use this API to mark a digital order item as being delivered.
- [FailedDeliveryForDBS](operations/failed-delivery-for-dbs.json) (POST /order/package/sof/failed_delivery) — Use this API to mark an sof order item as being delivered failed
- [GetShipmentProvider](operations/get-shipment-provider.json) (GET/POST /order/shipment/providers/get) — Use this API to get the list of all active shipping providers, which is needed when working with the PackOrder API.
- [Pack](operations/pack.json) (POST /order/fulfill/pack) — Use this API to mark an order item as being packed.
- [PackageStatusUpdateForDBS](operations/package-status-update-for-dbs.json) (POST /order/package/sof/status/update) — DBS package status update.
This interface is only open to some stores
- [PrintAWB](operations/print-awb.json) (GET/POST /order/package/document/get) — Use this API to retrieve order-related documents, only for shipping labels.
- [ReadyToShip](operations/ready-to-ship.json) (POST /order/package/rts) — Use this API to mark an order item as being ready to ship.
- [RecreatePackage](operations/recreate-package.json) (GET/POST /order/package/repack) — Use this API to mark a package item as being repack.

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
