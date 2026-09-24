---
title: "Lazada Logistics API"
description: "Logistics"
---

# API List

- [AddOrUpdatePickupStop](operations/add-or-update-pickup-stop.json) (POST /logistics/tps/runsheets/stops) — 3PL call TPS to update pickup stops
- [Create3PLStation](operations/create3-pl-station.json) (POST /logistics/tps/stations/create) — TPS_CREATE_STATION_API
External partner call TPS to create station
- [createConsolidationService](operations/create-consolidation-service.json) (POST /logistics/ldp/createConsolidationService) — create Consolidation Service
- [GetOrderTrace](operations/get-order-trace.json) (GET/POST /logistic/order/trace) — Query logistic detail for seller erp with seller id, order id and locale info. This api is only available in the state after ready to ship.
- [ScanParcel](operations/scan-parcel.json) (GET/POST /dop/scan) — DOP Scan Parcel
- [StationDopScan](operations/station-dop-scan.json) (GET/POST /stations/dop/scan) — StationDopScan
- [Update3PLStation](operations/update3-pl-station.json) (POST /logistics/tps/stations/update) — TPS_UPDATE_STATION_API
External partner call TPS to update station
- [updateLastMile](operations/update-last-mile.json) (POST /logistics/ldp/updateLastmile) — 跨境场景，物流末端预报信息
- [UpdatePickupTimeSlot](operations/update-pickup-time-slot.json) (POST /logistics/tps/sellers/pickup_timeslot) — 3PL call TPS to update pickup timeslot

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
