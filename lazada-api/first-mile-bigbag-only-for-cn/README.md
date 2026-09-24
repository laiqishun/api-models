---
title: "Lazada FirstMile Bigbag(only for CN)"
description: "大包接口"
---

# API List

- [GetChannelcodeByFirstMileNo](operations/get-channelcode-by-first-mile-no.json) (GET/POST /logistics/cngfc/fulfill/getchannelcode) — get channelcode by first mile No
- [GetLazadaBigbagPDFLable](operations/get-lazada-bigbag-pdf-lable.json) (GET/POST /logistics/cnpms/bigbag/lable/getPdf) — Get Lazada Bigbag PDF Lable
- [LazadaBigbagCancel](operations/lazada-bigbag-cancel.json) (GET/POST /logistics/cnpms/bigbag/cancel) — Lazada Bigbag cancel
- [LazadaBigbagCollectionPoints](operations/lazada-bigbag-collection-points.json) (GET/POST /logistics/cnpms/bigbag/querycollection) — Lazada bigbag query collection points
- [LazadaBigbagCommit](operations/lazada-bigbag-commit.json) (GET/POST /logistics/cnpms/bigbag/commit) — Lazada bigbag commit
- [LazadaBigbagUpdate](operations/lazada-bigbag-update.json) (GET/POST /logistics/cnpms/bigbag/update) — Lazada bigbag update
- [LazadaSellerAccountBind](operations/lazada-seller-account-bind.json) (GET/POST /logistics/cnpms/account/bind) — Lazada seller account bind for big bag pick up
- [QueryAddressInformaiton](operations/query-address-informaiton.json) (GET/POST /logistics/cnpms/address/query) — Query Address Informaiton
- [QueryLazadaBigbagInfo](operations/query-lazada-bigbag-info.json) (GET/POST /logistics/cnpms/bigbag/query) — Query Lazada Bigbag Info

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
