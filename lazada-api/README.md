---
title: "Lazada Open Platform API Models"
description: "Lazada Open Platform API references organized by official business category and operation."
---

# Module List

Choose an official API category, then open an API JSON file. The model contains Swagger 2.0 paths and response schemas where supported by the official reference, with Lazada-specific source fields preserved in `x-lazada-*` extensions.

Official catalog snapshot: 2026-09-24. The catalog listed 378 API records across 35 categories. Combined `GET/POST` methods remain one catalog record and are represented as both methods in the operation JSON.

Lazada pages list six regional service endpoints. The regional mapping is retained at the platform and operation level; choose the endpoint for the authorized seller's country. API category listing does not prove that a given application has permission to call the API. Check app category, seller authorization, and API permissions in Lazada Open Platform.

## Modules

- [Lazada System API](./system-api/README.md) — System API (4 APIs)
- [Lazada Seller API](./seller-api/README.md) — Seller Profile (17 APIs)
- [Lazada Product API](./product-api/README.md) — Product Management (28 APIs)
- [Lazada Cross Boarder Product API](./cross-boarder-product-api/README.md) — API group for crossborder APIs (Cross Boarder Sellers Only) (11 APIs)
- [Lazada Product Review API](./product-review-api/README.md) — For product review record and reply API (3 APIs)
- [Lazada Store Decoration API](./store-decoration-api/README.md) — Store Decoration API (1 APIs)
- [Lazada Media Center API](./media-center-api/README.md) — For video upload/delete/create API (6 APIs)
- [Lazada Flexicombo API](./flexicombo-api/README.md) — The APIs for Flexicombo Tools (9 APIs)
- [Lazada Seller Voucher API](./seller-voucher-api/README.md) — for Seller Voucher API (9 APIs)
- [Lazada Free Shipping API](./free-shipping-api/README.md) — for Free Shipping API (11 APIs)
- [Lazada Early Bird Price API](./early-bird-price-api/README.md) — Set early bird price for new products and get more sales. (4 APIs)
- [Lazada Order API](./order-api/README.md) — Order Information (8 APIs)
- [Lazada Return and Refund API](./return-and-refund-api/README.md) — The APIs to manage return orders (8 APIs)
- [Lazada Fulfillment API](./fulfillment-api/README.md) — Fulfillment API (10 APIs)
- [Lazada Logistics API](./logistics-api/README.md) — Logistics (9 APIs)
- [Lazada FirstMile Bigbag(only for CN)](./first-mile-bigbag-only-for-cn/README.md) — 大包接口 (9 APIs)
- [Lazada Finance API](./finance-api/README.md) — Finance (4 APIs)
- [Lazada Membership API](./membership-api/README.md) — Membership APIs for Loyalty and User Account related services (10 APIs)
- [Lazada FBL API](./fbl-api/README.md) — FBL API group (51 APIs)
- [Lazada Instant Messaging API](./instant-messaging-api/README.md) — Instant Messaging APIs (7 APIs)
- [Lazada Lazada Logistics API](./lazada-logistics-api/README.md) — Lazada Logistics API (20 APIs)
- [Lazada E-Tickets API](./e-tickets-api/README.md) — E-Tickets API for digital voucher and e-ticketing service (8 APIs)
- [Lazada LazPay API](./laz-pay-api/README.md) — Payment information (24 APIs)
- [Lazada Lazada Wallet Corporate Top-up API](./lazada-wallet-corporate-top-up-api/README.md) — Lazada Wallet Corporate Top-up (5 APIs)
- [Lazada RedMart API](./red-mart-api/README.md) — API for RedMart (8 APIs)
- [Lazada Lazada DG API](./lazada-dg-api/README.md) — lazada digital good  API (7 APIs)
- [Lazada Sponsored Solutions API](./sponsored-solutions-api/README.md) — The API to createCampaign,updateCampaign. (28 APIs)
- [Lazada Service Market API](./service-market-api/README.md) — Lazada Service Market API (2 APIs)
- [Lazada Choice Customized API](./choice-customized-api/README.md) — Choice Customized API (12 APIs)
- [Lazada LazLike API](./laz-like-api/README.md) — LazLike Content API (13 APIs)
- [Lazada LazLive API](./laz-live-api/README.md) — The API to highlight product in live room (1 APIs)
- [Lazada Logistics Station API](./logistics-station-api/README.md) — API to integrate with Lazada logistics station including Drop-off point and Collection point (18 APIs)
- [Lazada LazCredit Risk API](./laz-credit-risk-api/README.md) — lazada credit risk (0 APIs)
- [Lazada Content API](./content-api/README.md) — The Content APIs are content-related APIs that are only available to specific users. Make sure that communication has been completed prior to applying permission to visit them. (7 APIs)
- [Lazada Store Flash Sale API](./store-flash-sale-api/README.md) — 店铺闪购API (6 APIs)

## Source and field mapping

Lazada's official API reference is dynamically rendered and does not provide an official Swagger download. Request and response trees, common parameters, regional endpoints, errors, examples, and SDK snippets are retained in `x-lazada-*` fields. Standard request parameter locations are added only where the GET method or an official cURL example provides evidence. Example credentials and sample personal contact data are redacted.

The [manifest](./manifest.md) lists each catalog record, source page, detail status, and generated JSON file.
