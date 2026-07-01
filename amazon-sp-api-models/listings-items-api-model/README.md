---
title: Selling Partner API for Listings Items
description: "The Selling Partner API for Listings Items (Listings Items API) provides programmatic access to selling partner listings on Amazon. Use this API in collaboration with the Selling Partner API for Product Type Definitions, which you use to retrieve the information about Amazon product types needed to use the Listings Items API. For more information, see the [Listings Items API Use Case Guide](https://developer-docs.amazon.com/sp-api/docs/listings-items-api-v2021-08-01-use-case-guide)."
---

# API List
- [deleteListingsItem](operations/deleteListingsItem.json) (DELETE /listings/2021-08-01/items/{sellerId}/{sku})：Delete a listings item for a selling partner.
- [getListingsItem](operations/getListingsItem.json) (GET /listings/2021-08-01/items/{sellerId}/{sku})：Returns details about a listings item for a selling partner.
- [patchListingsItem](operations/patchListingsItem.json) (PATCH /listings/2021-08-01/items/{sellerId}/{sku})：Partially update (patch) a listings item for a selling partner. Only top-level listings item attributes can be patched. Patching nested attributes is not supported.
- [putListingsItem](operations/putListingsItem.json) (PUT /listings/2021-08-01/items/{sellerId}/{sku})：Creates a new or fully-updates an existing listings item for a selling partner.
- [searchListingsItems](operations/searchListingsItems.json) (GET /listings/2021-08-01/items/{sellerId})：Search for and return a list of selling partner listings items and their respective details.
