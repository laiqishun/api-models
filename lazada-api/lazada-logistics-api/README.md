---
title: "Lazada Lazada Logistics API"
description: "Lazada Logistics API"
---

# API List

- [CreateCustomerAccountRelationshipByOTP](operations/create-customer-account-relationship-by-otp.json) (GET/POST /logistics/epis/customers/external_relationships_bundle) — Create customer account relationship for external by OTP
- [CreateCustomerAccountRelationshipForExternal](operations/create-customer-account-relationship-for-external.json) (POST /logistics/epis/customers/external_relationships) — External partner calls LAZADA to create account relationship
- [CreateOrUpdateCustomerWarehouse](operations/create-or-update-customer-warehouse.json) (POST /logistics/epis/customers/warehouses) — External partner calls LAZADA to create or update warehouses
- [EpisGetDeliveryOptions](operations/epis-get-delivery-options.json) (GET /logistics/epis/service/delivery_options) — External partner call EPIS to get delivery options for package
- [EpisPackageCancellation](operations/epis-package-cancellation.json) (POST /logistics/epis/packages/cancel) — External partner call EPIS to cancel package
- [EpisPackageCancellationV3](operations/epis-package-cancellation-v3.json) (POST /logistics/epis/packages/cancel/v3) — External partner call EPIS to cancel FFM + DEL package
- [EpisPackageConsignment](operations/epis-package-consignment.json) (POST /logistics/epis/packages/consign) — External partner call EPIS to consign package to get the tracking number and be able to print AWB after consign
- [EpisPackageConsignmentV2](operations/epis-package-consignment-v2.json) (POST /logistics/epis/packages/consign/v2) — External partner call EPIS to consign FFM + DEL package to get the tracking number and be able to print AWB after consign
- [EpisPackageCreation](operations/epis-package-creation.json) (POST /logistics/epis/packages) — External partner call EPIS to create package
- [EpisPackageInfoUpdate](operations/epis-package-info-update.json) (POST /logistics/epis/packages/update) — External partner call EPIS to update package info after RTS
- [EpisPackagePrintAwb](operations/epis-package-print-awb.json) (GET /logistics/epis/packages/awb) — External partner call LAZADA to print AWB
- [EpisPackageReadyToBeShipped](operations/epis-package-ready-to-be-shipped.json) (POST /logistics/epis/packages/rts) — External partner calls EPIS to mark a package as ready to be shipped
- [EpisPackageReAttempt](operations/epis-package-re-attempt.json) (POST /logistics/epis/packages/reattempt) — Send re-attempt package request
- [EpisUploadAwbFulfillment](operations/epis-upload-awb-fulfillment.json) (POST /logistics/epis/fulfillment/upload_awb) — External partner call EPIS to upload awb for fulfillment
- [EpisXspaceCreate](operations/epis-xspace-create.json) (POST /logistics/epis/xspace/create) — Create Xspace case
- [EpisXspaceGetDetail](operations/epis-xspace-get-detail.json) (POST /logistics/epis/xspace/detail) — Get Xspace case detail
- [EpisXspaceQuery](operations/epis-xspace-query.json) (GET/POST /logistics/epis/xspace/query) — Query Xspace case
- [EpisXspaceRateTicket](operations/epis-xspace-rate-ticket.json) (GET/POST /logistics/epis/xspace/rate) — Rate Xspace ticket
- [EstimateShippingFee](operations/estimate-shipping-fee.json) (GET/POST /logistics/epis/estimate_shipping_fee) — Estimate shipping fee
- [GetShippingFee](operations/get-shipping-fee.json) (GET/POST /logistics/epis/get_shipping_fee) — Estimate package shipping fee (Estimated & Actual)

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
