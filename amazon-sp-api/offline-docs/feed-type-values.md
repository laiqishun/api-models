# Feed Type Values

Use a feed type value to submit or filter Feeds API feeds.

Common fields:

- `createFeed.body.feedType`
- `getFeeds.query.feedTypes`
- response fields named `feedType`

Always pass the exact uppercase string.

## Current Feeds API values

| Category | feedType values | Availability |
| --- | --- | --- |
| Listings | `JSON_LISTINGS_FEED` | Seller and vendor |
| Order | `POST_FLAT_FILE_ORDER_ACKNOWLEDGEMENT_DATA`, `POST_FLAT_FILE_PAYMENT_ADJUSTMENT_DATA`, `POST_FLAT_FILE_FULFILLMENT_DATA`, `POST_FLAT_FILE_IL_SNAPSHOT_FEED`, `POST_FLAT_FILE_IL_ALLOCATION_REQUESTS_CONFIRMATION_FEED`, `POST_EXPECTED_SHIP_DATE_SOD_FLAT_FILE`, `POST_INVOICE_CONFIRMATION_DATA`, `POST_ORDER_ACKNOWLEDGEMENT_DATA`, `POST_PAYMENT_ADJUSTMENT_DATA`, `POST_ORDER_FULFILLMENT_DATA`, `POST_EXPECTED_SHIP_DATE_SOD` | Seller only |
| Fulfillment by Amazon | `POST_FULFILLMENT_ORDER_REQUEST_DATA`, `POST_FULFILLMENT_ORDER_CANCELLATION_REQUEST_DATA`, `POST_FBA_INBOUND_CARTON_CONTENTS`, `POST_FLAT_FILE_FBA_CREATE_REMOVAL`, `POST_FLAT_FILE_FULFILLMENT_ORDER_REQUEST_DATA`, `POST_FLAT_FILE_FULFILLMENT_ORDER_CANCELLATION_REQUEST_DATA` | Seller only |
| Easy Ship | `POST_EASYSHIP_DOCUMENTS` | Seller only |
| Invoicing | `UPLOAD_VAT_INVOICE` | Seller only |

## How to submit a feed

1. Call `createFeedDocument` and keep the returned `feedDocumentId` and upload URL.
2. Upload the feed content to that URL using the required encryption/compression details from the document response.
3. Call `createFeed` with:
   - `feedType`: one exact value from this file.
   - `marketplaceIds`: one or more store identifiers.
   - `inputFeedDocumentId`: the document ID from step 1.
   - `feedOptions`: only when the selected feed type requires options.
4. Poll `getFeed` or `getFeeds` until `processingStatus` is `DONE`, `CANCELLED`, or `FATAL`.
5. If `resultFeedDocumentId` is returned, call `getFeedDocument` and download the processing report.

## Listings guidance

- Use `JSON_LISTINGS_FEED` for bulk listings create/update/delete workflows.
- Legacy XML and flat file product listings feeds such as `POST_PRODUCT_DATA`, `POST_INVENTORY_AVAILABILITY_DATA`, `POST_PRODUCT_PRICING_DATA`, `POST_PRODUCT_IMAGE_DATA`, `POST_PRODUCT_RELATIONSHIP_DATA`, and `POST_PRODUCT_OVERRIDES_DATA` are deprecated for Feeds API listings workflows. They can still appear in older model examples; do not choose them for new integrations unless you have a specific legacy requirement and Amazon still permits it for the account.

## Filtering existing feeds

For `getFeeds`, pass `feedTypes` as an array, for example:

```json
["JSON_LISTINGS_FEED"]
```

Source checked: Amazon SP-API Feed Type Values online documentation, 2026-07-14.

Online source URLs:

- https://developer-docs.amazon/sp-api/docs/feed-type-values
