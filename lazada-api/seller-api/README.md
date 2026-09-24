---
title: "Lazada Seller API"
description: "Seller Profile"
---

# API List

- [BatchQueryFollowStatus](operations/batch-query-follow-status.json) (GET/POST /shop/follow/status/batch/query) — Query whether these customers follow this seller.
- [getCountryInfo](operations/get-country-info.json) (GET/POST /seller/cb/country/get) — getCountryInfo
- [GetPickUpStoreList](operations/get-pick-up-store-list.json) (GET/POST /rc/store/list/get) — return the list of pick up store infomation for requested Seller
- [GetSeller](operations/get-seller.json) (GET /seller/get) — Get seller information by current seller ID.
- [GetSellerMetricsById](operations/get-seller-metrics-by-id.json) (GET /seller/metrics/get) — Provide seller metrics data of the specific seller, like positive seller rating, ship on time rate and etc.
- [GetSellerPerformance](operations/get-seller-performance.json) (GET/POST /seller/performance/get) — Provide the performance metrics of the current seller, such as positive seller rating, ship on time, etc.
- [getSellerRegisterInfo ](operations/get-seller-register-info.json) (GET/POST /seller/cb/register/info) — getSellerRegisterInfo
- [getSubAddress](operations/get-sub-address.json) (GET/POST /seller/cb/country/location/get) — get location info
- [GetWarehouseBySellerId](operations/get-warehouse-by-seller-id.json) (GET/POST /rc/warehouse/get) — get warehouse by seller id
- [paymentBinding](operations/payment-binding.json) (GET/POST /seller/cb/payment/config) — paymentBinding
- [queryBuyboxHuntingInfo](operations/query-buybox-hunting-info.json) (GET/POST /hunting/buybox/get) — SPU竞价接口
- [QueryWarehouseDetailInfoBySellerId](operations/query-warehouse-detail-info-by-seller-id.json) (GET/POST /rc/warehouse/detail/get) — query warehouse detail info by seller id
- [saveSellerWarehouseInfo](operations/save-seller-warehouse-info.json) (GET/POST /rc/sellerWarehouse/saveWarehouseInfo) — Api to create or edit the seller warehouse info except the "default"
dropshipping warehouse and the return warehouse.
- [SellerCenterMsgList](operations/seller-center-msg-list.json) (GET/POST /sellercenter/msg/list) — seller center msg box
- [sellerFieldVerify](operations/seller-field-verify.json) (GET/POST /seller/cb/register/fieldcheck) — verify seller info field
- [SellerPolicyFetch](operations/seller-policy-fetch.json) (GET /seller/policy/fetch) — Fetch seller policy information
- [SynchronizeSellerItemArConfig](operations/synchronize-seller-item-ar-config.json) (GET/POST /seller/ar/config/syn) — synchronize seller item ar config

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
