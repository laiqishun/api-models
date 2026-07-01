---
title: The Selling Partner API for Transfers.
description: "The Selling Partner API for Transfers enables selling partners to retrieve payment methods and initiate payouts for their seller accounts. This API supports the following marketplaces: DE, FR, IT, ES, SE, NL, PL, and BE."
---

# API List
- [initiatePayout](initiatePayout.json) (POST /finances/transfers/2024-06-01/payouts)：Initiates an on-demand payout to the seller's default deposit method in Seller Central for the given `marketplaceId` and `accountType`, if eligible. You can only initiate one on-demand payout for each marketplace and account type within a 24-hour period.
- [getPaymentMethods](getPaymentMethods.json) (GET /finances/transfers/2024-06-01/paymentMethods)：Returns the list of payment methods for the seller, which can be filtered by method type.
