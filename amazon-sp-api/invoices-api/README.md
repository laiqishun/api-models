---
title: The Selling Partner API for Invoices.
description: "Use the Selling Partner API for Invoices to retrieve and manage invoice-related operations, which can help selling partners manage their bookkeeping processes."
---

# API List
- [getInvoicesAttributes](operations/getInvoicesAttributes.json) (GET /tax/invoices/2024-06-19/attributes)：Returns marketplace-dependent schemas and their respective set of possible values.
- [getInvoicesDocument](operations/getInvoicesDocument.json) (GET /tax/invoices/2024-06-19/documents/{invoicesDocumentId})：Returns the invoice document's ID and URL. Use the URL to download the ZIP file, which contains the invoices from the corresponding `createInvoicesExport` request.
- [createInvoicesExport](operations/createInvoicesExport.json) (POST /tax/invoices/2024-06-19/exports)：Creates an invoice export request.
- [getInvoicesExports](operations/getInvoicesExports.json) (GET /tax/invoices/2024-06-19/exports)：Returns invoice exports details for exports that match the filters that you specify.
- [getInvoicesExport](operations/getInvoicesExport.json) (GET /tax/invoices/2024-06-19/exports/{exportId})：Returns invoice export details (including the `exportDocumentId`, if available) for the export that you specify.
- [createGovernmentInvoice](operations/createGovernmentInvoice.json) (POST /tax/invoices/2024-06-19/governmentInvoiceRequests)：Submits an asynchronous government invoice creation request.
- [getGovernmentInvoiceStatus](operations/getGovernmentInvoiceStatus.json) (GET /tax/invoices/2024-06-19/governmentInvoiceRequests)：Returns the status of an invoice generation request.
- [getGovernmentInvoiceDocument](operations/getGovernmentInvoiceDocument.json) (GET /tax/invoices/2024-06-19/governmentInvoiceRequests/{shipmentId})：Returns an invoiceDocument object containing an invoiceDocumentUrl .
- [getInvoices](operations/getInvoices.json) (GET /tax/invoices/2024-06-19/invoices)：Returns invoice details for the invoices that match the filters that you specify.
- [getInvoice](operations/getInvoice.json) (GET /tax/invoices/2024-06-19/invoices/{invoiceId})：Returns invoice data for the specified invoice. This operation returns only a subset of the invoices data; refer to the response definition to get all the possible attributes. To get the full invoice, use the `createInvoicesExport` operation to start an export request.
