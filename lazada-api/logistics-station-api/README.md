---
title: "Lazada Logistics Station API"
description: "API to integrate with Lazada logistics station including Drop-off point and Collection point"
---

# API List

- [CageValidation](operations/cage-validation.json) (POST /logistics/station/cages/validate) — Validate if a cage is valid
- [ConfirmInbound](operations/confirm-inbound.json) (POST /logistics/station/v1/confirm-inbound) — Confirm inbound. Call this API to inbound the scanned parcel and finish the inbound process
- [ConfirmParcelCollection](operations/confirm-parcel-collection.json) (POST /logistics/station/v1/cp/confirm-parcel-collection) — Confirm customer collects or rejects parcel. This API is used after ValidateOTP success.
- [CreateScannedParcel](operations/create-scanned-parcel.json) (POST /logistics/station/v1/scanned-parcels/create) — Create a scanned parcel. Call this API when scanning the tracking number on the parcel.
- [DeleteScannedParcel](operations/delete-scanned-parcel.json) (POST /logistics/station/v1/scanned-parcels/delete) — Delete scanned parcels by tracking number. This API is required when user deletes the scanned parcels
- [DopConfirmInbound](operations/dop-confirm-inbound.json) (POST /logistics/station/dop/confirm-inbound) — DOP confirm inbound
- [DopCreateScannedParcel](operations/dop-create-scanned-parcel.json) (POST /logistics/station/dop/scanned-parcels) — DOP create scanned parcel
- [DopDeleteScannedParcel](operations/dop-delete-scanned-parcel.json) (POST /logistics/station/dop/scanned-parcels/delete) — DOP delete scanned parcel
- [DopGetInboundedParcel](operations/dop-get-inbounded-parcel.json) (GET /logistics/station/dop/inbounded-parcels/list) — DOP get list scanned parcel
- [DopGetScannedParcel](operations/dop-get-scanned-parcel.json) (GET /logistics/station/dop/scanned-parcels/list) — DOP get list scanned parcel
- [GetCpScheduledPuParcel](operations/get-cp-scheduled-pu-parcel.json) (GET /logistics/station/v1/cp/scheduled-pu-parcels/list) — Get a list of parcels that are scheduled to be picked up for return to seller. These parcels are expired (no collection from customer), SLA breached or customer rejected. This API is used to help the agent prepare parcel
- [GetInboundedParcel](operations/get-inbounded-parcel.json) (GET /logistics/station/v1/inbounded-parcels/list) — Get a list of inbounded parcels by a list of tracking numbers. This API is used for checking the status of inbounded parcels such as parcels picked up by LEX, picked up by 3PL, or collected by a customer.
- [GetListAccessStation](operations/get-list-access-station.json) (GET /logistics/station/list) — Get list access station by APP
- [GetMetaData](operations/get-meta-data.json) (GET /logistics/station/v1/metadata) — Get metadata such as reject reasons, etc
- [GetScannedParcel](operations/get-scanned-parcel.json) (GET /logistics/station/v1/scanned-parcels/list) — Get a list of scanned parcels for parcel synchronization.
- [SearchCustomerReturnParcel](operations/search-customer-return-parcel.json) (GET /logistics/station/v1/dop/cr-parcels/search) — Search customer return parcel by at least 4 letters text. This API is to improve user experience, user can search for the tracking number instead of typing the full tracking number.
- [ValidateCage](operations/validate-cage.json) (POST /logistics/station/v1/cages/validate) — Validate if a cage is valid. This API is often called before starting inbound but it's not required.
- [ValidateOTP](operations/validate-otp.json) (POST /logistics/station/v1/cp/validate-otp) — Validate if OTP of parcel is valid or not. This API is used for checking OTP before confirming collection.

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
