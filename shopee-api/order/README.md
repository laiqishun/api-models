---
title: Shopee Order API
description: "Order, shipment, package, cancellation, invoice, booking, and buyer request operations."
---

# API List

- [v2.order.cancel_order](operations/v2-order-cancel-order.json) (POST /api/v2/order/cancel_order)：Use this api to cancel an order. This action can only be performed before the order has been shipped.
- [v2.order.download_fbs_invoices](operations/v2-order-download-fbs-invoices.json) (POST /api/v2/order/download_fbs_invoices)：This API allows you to download FBS invoices. To use this API, the client must first call v2.order.generate_fbs_invoices to create a new shipping document task, followed by calling v2.order.get_fbs_invoices_result to check the task status. The document can only be downloaded once the task status is "READY."
- [v2.order.download_invoice_doc](operations/v2-order-download-invoice-doc.json) (GET /api/v2/order/download_invoice_doc)：This endpoint only for PH and BR local seller. Seller can download the invoice uploaded before through this endpoint.
- [v2.order.generate_fbs_invoices](operations/v2-order-generate-fbs-invoices.json) (POST /api/v2/order/generate_fbs_invoices)：This API creates a task to download a specific tax document (e.g., sales invoice, remessa invoice) for the seller's account, available only after the document is issued by the system as part of the Fulfilled by Shopee (FBS) process. The workflow is as follows: (1) v2.order.generate_fbs_invoices; (2) v2.order.get_fbs_invoices_result; (3) v2.order.download_fbs_invoices. Please note: The download link for the document will expire 30 minutes after being generated.
- [v2.order.get_booking_detail](operations/v2-order-get-booking-detail.json) (GET /api/v2/order/get_booking_detail)：Use this api to get booking detail.
- [v2.order.get_booking_list](operations/v2-order-get-booking-list.json) (GET /api/v2/order/get_booking_list)：Use this api to search bookings. You may also filter them by status, if needed.
- [v2.order.get_buyer_invoice_info](operations/v2-order-get-buyer-invoice-info.json) (POST /api/v2/order/get_buyer_invoice_info)：API to obtain buyer submitted invoice info for VN, TH and PH local sellers only.
- [v2.order.get_estimate_cancel_value](operations/v2-order-get-estimate-cancel-value.json) (POST /api/v2/order/get_estimate_cancel_value)：Returns the estimated refund value for a partial order cancellation given the specified items to cancel.
- [v2.order.get_fbs_invoices_result](operations/v2-order-get-fbs-invoices-result.json) (POST /api/v2/order/get_fbs_invoices_result)：This API allows you to consult the status of a previously requested batch download for FBS tax documents.
- [v2.order.get_order_detail](operations/v2-order-get-order-detail.json) (GET /api/v2/order/get_order_detail)：Use this api to get order detail.
- [v2.order.get_order_list](operations/v2-order-get-order-list.json) (GET /api/v2/order/get_order_list)：Use this api to search orders. You may also filter them by status, if needed.
- [v2.order.get_package_detail](operations/v2-order-get-package-detail.json) (GET /api/v2/order/get_package_detail)：Use this api to get package detail.
- [v2.order.get_pending_buyer_invoice_order_list](operations/v2-order-get-pending-buyer-invoice-order-list.json) (GET /api/v2/order/get_pending_buyer_invoice_order_list)：This endpoint only for PH and BR local sellers only. This API is used for seller to retrieve a list of order IDs that are pending invoice upload.
- [v2.order.get_shipment_list](operations/v2-order-get-shipment-list.json) (GET /api/v2/order/get_shipment_list)：Use this api to get order list which order_status is READY_TO_SHIP or RETRY_SHIP to start process the whole shipping progress.
- [v2.order.get_warehouse_filter_config](operations/v2-order-get-warehouse-filter-config.json) (GET /api/v2/order/get_warehouse_filter_config)：For multi-warehouse shops, return all warehouses with packages that have not been SHIPPED including product_location_id and address_id. Compared to v2.shop.get_warehouse_detail, it covers some edge cases like warehouse that have been unlinked but still retain packages that have not been SHIPPED, and does not cover some cases like single warehouse with default product_location_id and FBS shop.
- [v2.order.handle_buyer_cancellation](operations/v2-order-handle-buyer-cancellation.json) (POST /api/v2/order/handle_buyer_cancellation)：Use this api to handle buyer's cancellation application.
- [v2.order.handle_prescription_check](operations/v2-order-handle-prescription-check.json) (POST /api/v2/order/handle_prescription_check)：Use this API to approve or reject a prescription
- [v2.order.search_package_list](operations/v2-order-search-package-list.json) (POST /api/v2/order/search_package_list)：Use this API to search the list of packages that have not been SHIPPED to proceed arranging shipment, and it supports various filters and sort fields.
- [v2.order.set_note](operations/v2-order-set-note.json) (POST /api/v2/order/set_note)：Use this api to set note for an order.
- [v2.order.split_order](operations/v2-order-split-order.json) (POST /api/v2/order/split_order)：Use this api to split an order into multiple packages. Orders that include installation services cannot be split by quantity.
- [v2.order.unsplit_order](operations/v2-order-unsplit-order.json) (POST /api/v2/order/unsplit_order)：Use this ai to undo split of order. After undo split, the order will have only one package. It can only be used when order status still at READY_TO_SHIP.
- [v2.order.upload_invoice_doc](operations/v2-order-upload-invoice-doc.json) (POST /api/v2/order/upload_invoice_doc)：This endpoint is for PH and BR local seller. Upload the invoice document
