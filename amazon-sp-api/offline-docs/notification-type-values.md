# Notification Type Values

Use a notification type value when creating, reading, deleting, or testing Notifications API subscriptions.

Common fields:

- path parameter `notificationType`
- `eventFilter.eventFilterType`
- `processingDirective.eventFilter`
- `processingDirective.filterExpression`

Always pass the exact uppercase string.

## Current notificationType values

| notificationType | Use when you need |
| --- | --- |
| `ACCOUNT_STATUS_CHANGED` | Account status changes for subscribed selling partner / store pairs. |
| `ANY_OFFER_CHANGED` | Top offer, external price, Buy Box winner, or Buy Box price changes for active seller offers. |
| `B2B_ANY_OFFER_CHANGED` | Amazon Business B2B offer changes for active seller offers. |
| `BRANDED_ITEM_CONTENT_CHANGE` | Brand-owned ASIN content changes such as title, description, bullets, or images. |
| `DETAIL_PAGE_TRAFFIC_EVENT` | Hourly detail page traffic event data. |
| `FBA_INVENTORY_AVAILABILITY_CHANGES` | FBA inventory quantity changes. |
| `EXTERNAL_FULFILLMENT_SHIPMENT_STATUS_CHANGE` | Warehouse integration shipment status changes. |
| `FBA_OUTBOUND_SHIPMENT_STATUS` | FBA outbound shipment creation or cancellation. |
| `FEE_PROMOTION` | Available fee promotions. |
| `FEED_PROCESSING_FINISHED` | A submitted feed reaches `DONE`, `CANCELLED`, or `FATAL`. |
| `FULFILLMENT_ORDER_STATUS` | Multi-Channel Fulfillment order status changes. |
| `ITEM_INVENTORY_EVENT_CHANGE` | Hourly item inventory event data. |
| `ITEM_SALES_EVENT_CHANGE` | Hourly item sales event data. |
| `ITEM_PRODUCT_TYPE_CHANGE` | Product type changes for brand-related items. |
| `LISTINGS_ITEM_STATUS_CHANGE` | Listing item create/delete/buyability status changes. |
| `LISTINGS_ITEM_ISSUES_CHANGE` | Listing issue changes. Prefer payload version `2023-12-13` when available. |
| `LISTINGS_ITEM_MFN_QUANTITY_CHANGE` | Seller-fulfilled listing quantity changes. |
| `ORDER_CHANGE` | Important order changes, including order status changes and buyer requested cancellations. |
| `PRICING_HEALTH` | Offer is ineligible for Featured Offer / Buy Box because of uncompetitive price. |
| `PRODUCT_TYPE_DEFINITIONS_CHANGE` | New product type or product type version. |
| `REPORT_PROCESSING_FINISHED` | A requested report reaches `DONE`, `CANCELLED`, or `FATAL`. |
| `TRANSACTION_UPDATE` | A new transaction is posted to the seller account. |

## Event filters and filter expressions

`eventFilter` and `filterExpression` are mutually exclusive. Use only one in a subscription.

| notificationType | eventFilter support | filterExpression support |
| --- | --- | --- |
| `ANY_OFFER_CHANGED` | Supports `aggregationSettings` and `marketplaceIds`; set `eventFilterType` to `ANY_OFFER_CHANGED`. | Supported, but without aggregation capability. |
| `ORDER_CHANGE` | Supports `orderChangeTypes`; set `eventFilterType` to `ORDER_CHANGE`. | Supported. |
| Most other current types | No local eventFilter details captured here. | Many current types support CEL-based `filterExpression`; check this file first, then validate against current Amazon docs if adding a new filter expression. |

When using `filterExpression`, write a CEL expression against the notification payload. Do not also send `eventFilter`.

## Minimal createSubscription shape

```json
{
  "destinationId": "destination-id",
  "payloadVersion": "1.0",
  "processingDirective": {
    "eventFilter": {
      "eventFilterType": "ORDER_CHANGE",
      "orderChangeTypes": ["OrderStatusChange"]
    }
  }
}
```

For notifications that support CEL filtering, use this shape instead:

```json
{
  "destinationId": "destination-id",
  "payloadVersion": "1.0",
  "processingDirective": {
    "filterExpression": "OrderNotification.OrderChangeType == 'OrderStatusChange'"
  }
}
```

Source checked: Amazon SP-API Notification Type Values online documentation, 2026-07-14.

Online source URLs:

- https://developer-docs.amazon/sp-api/docs/notification-type-values
