# Report Type Values

Use a report type value to request, schedule, or filter Reports API reports.

Common fields:

- `createReport.body.reportType`
- `createReportSchedule.body.reportType`
- `getReports.query.reportTypes`
- `getReportSchedules.query.reportTypes`
- response fields named `reportType`

Always pass the exact uppercase string. Report availability depends on account type, selling partner role, marketplace, report type, and date range.

## High-value choices

| Need | Report type values to try first |
| --- | --- |
| Orders by order date / last update | `GET_FLAT_FILE_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL`, `GET_FLAT_FILE_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL`, `GET_XML_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL`, `GET_XML_ALL_ORDERS_DATA_BY_LAST_UPDATE_GENERAL` |
| Order invoicing / shipping / tax | `GET_ORDER_REPORT_DATA_INVOICING`, `GET_ORDER_REPORT_DATA_SHIPPING`, `GET_ORDER_REPORT_DATA_TAX`, `GET_FLAT_FILE_ORDER_REPORT_DATA_INVOICING`, `GET_FLAT_FILE_ORDER_REPORT_DATA_SHIPPING`, `GET_FLAT_FILE_ORDER_REPORT_DATA_TAX` |
| Pending orders | `GET_FLAT_FILE_PENDING_ORDERS_DATA`, `GET_PENDING_ORDERS_DATA`, `GET_CONVERGED_FLAT_FILE_PENDING_ORDERS_DATA` |
| Listings and inventory | `GET_MERCHANT_LISTINGS_ALL_DATA`, `GET_MERCHANT_LISTINGS_DATA`, `GET_MERCHANT_LISTINGS_INACTIVE_DATA`, `GET_MERCHANT_CANCELLED_LISTINGS_DATA`, `GET_MERCHANTS_LISTINGS_FYP_REPORT`, `GET_REFERRAL_FEE_PREVIEW_REPORT` |
| FBA shipments and sales | `GET_AMAZON_FULFILLED_SHIPMENTS_DATA_GENERAL`, `GET_AMAZON_FULFILLED_SHIPMENTS_DATA_INVOICING`, `GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_SALES_DATA`, `GET_FBA_FULFILLMENT_CUSTOMER_SHIPMENT_PROMOTION_DATA`, `GET_FBA_FULFILLMENT_CUSTOMER_TAXES_DATA` |
| FBA inventory | `GET_AFN_INVENTORY_DATA`, `GET_AFN_INVENTORY_DATA_BY_COUNTRY`, `GET_FBA_MYI_UNSUPPRESSED_INVENTORY_DATA`, `GET_FBA_MYI_ALL_INVENTORY_DATA`, `GET_FBA_INVENTORY_PLANNING_DATA`, `GET_RESERVED_INVENTORY_DATA` |
| FBA fees, storage, reimbursements, removals | `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA`, `GET_FBA_STORAGE_FEE_CHARGES_DATA`, `GET_FBA_OVERAGE_FEE_CHARGES_DATA`, `GET_FBA_REIMBURSEMENTS_DATA`, `GET_FBA_RECOMMENDED_REMOVAL_DATA`, `GET_FBA_FULFILLMENT_REMOVAL_ORDER_DETAIL_DATA`, `GET_FBA_FULFILLMENT_REMOVAL_SHIPMENT_DETAIL_DATA` |
| Returns | `GET_XML_RETURNS_DATA_BY_RETURN_DATE`, `GET_FLAT_FILE_RETURNS_DATA_BY_RETURN_DATE`, `GET_FBA_FULFILLMENT_CUSTOMER_RETURNS_DATA` |
| Settlement / actual payments and fees | `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE`, `GET_V2_SETTLEMENT_REPORT_DATA_XML`, `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE_V2` |
| Sales and traffic analytics | `GET_SALES_AND_TRAFFIC_REPORT` |
| Brand analytics | `GET_BRAND_ANALYTICS_SEARCH_CATALOG_PERFORMANCE_REPORT`, `GET_BRAND_ANALYTICS_SEARCH_QUERY_PERFORMANCE_REPORT`, `GET_BRAND_ANALYTICS_MARKET_BASKET_REPORT`, `GET_BRAND_ANALYTICS_SEARCH_TERMS_REPORT`, `GET_BRAND_ANALYTICS_REPEAT_PURCHASE_REPORT` |
| Vendor analytics | `GET_VENDOR_SALES_REPORT`, `GET_VENDOR_TRAFFIC_REPORT`, `GET_VENDOR_INVENTORY_REPORT`, `GET_VENDOR_FORECASTING_REPORT`, `GET_VENDOR_REAL_TIME_SALES_REPORT`, `GET_VENDOR_REAL_TIME_TRAFFIC_REPORT`, `GET_VENDOR_REAL_TIME_INVENTORY_REPORT` |
| Performance / promotions | `GET_SELLER_FEEDBACK_DATA`, `GET_V1_SELLER_PERFORMANCE_REPORT`, `GET_V2_SELLER_PERFORMANCE_REPORT`, `GET_PROMOTION_PERFORMANCE_REPORT`, `GET_COUPON_PERFORMANCE_REPORT` |
| Tax / VAT / GST | `GET_FLAT_FILE_SALES_TAX_DATA`, `GET_VAT_TRANSACTION_DATA`, `SC_VAT_TAX_REPORT`, `GST_MTR_B2B`, `GST_MTR_B2C`, `GST_MTR_STOCK_TRANSFER_REPORT`, `GET_GST_MTR_B2B_CUSTOM`, `GET_GST_MTR_B2C_CUSTOM`, `GET_GST_STR_ADHOC` |
| Easy Ship | `GET_EASYSHIP_DOCUMENTS`, `GET_EASYSHIP_PICKEDUP`, `GET_EASYSHIP_WAITING_FOR_PICKUP` |

## How to fill Reports API requests

1. Pick one `reportType` from this file.
2. Pass `marketplaceIds` when the report type uses marketplace-scoped data.
3. Pass `dataStartTime` and `dataEndTime` only when the report type uses a date range.
4. Pass `reportOptions` only when the selected report type explicitly requires options.
5. For `getReports` or `getReportSchedules`, pass `reportTypes` as an array, for example `["GET_FLAT_FILE_ALL_ORDERS_DATA_BY_ORDER_DATE_GENERAL"]`.

## Notes for fees and SKU sales

- For actual charged commissions, FBA fees, refunds, reimbursements, and settlement-level money movement, start with settlement reports such as `GET_V2_SETTLEMENT_REPORT_DATA_FLAT_FILE`.
- For estimated FBA fees by SKU/ASIN, use `GET_FBA_ESTIMATED_FBA_FEES_TXT_DATA`.
- For order and item sales lines, use the order/FBA shipment reports that match the fulfillment channel and date basis you need.

Source checked: Amazon SP-API Report Type Values online documentation, 2026-07-14.

Online source URLs:

- https://developer-docs.amazon/sp-api/docs/report-type-values
