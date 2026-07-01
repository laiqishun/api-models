---
title: Selling Partner API for A+ Content Management
description: "Use the A+ Content API to build applications that help selling partners add rich marketing content to their Amazon product detail pages. Selling partners can use A+ content to share their brand and product story, which helps buyers make informed purchasing decisions. Selling partners use content modules to add images and text."
---

# API List
- [searchContentDocuments](operations/searchContentDocuments.json) (GET /aplus/2020-11-01/contentDocuments)：Returns a list of all A+ Content documents, including metadata, that are assigned to a selling partner. To get the actual contents of the A+ Content documents, call the `getContentDocument` operation.
- [createContentDocument](operations/createContentDocument.json) (POST /aplus/2020-11-01/contentDocuments)：Creates a new A+ Content document.
- [getContentDocument](operations/getContentDocument.json) (GET /aplus/2020-11-01/contentDocuments/{contentReferenceKey})：Returns an A+ Content document, if available.
- [updateContentDocument](operations/updateContentDocument.json) (POST /aplus/2020-11-01/contentDocuments/{contentReferenceKey})：Updates an existing A+ Content document.
- [listContentDocumentAsinRelations](operations/listContentDocumentAsinRelations.json) (GET /aplus/2020-11-01/contentDocuments/{contentReferenceKey}/asins)：Returns a list of ASINs that are related to the specified A+ Content document, if available. If you don't include the `asinSet` parameter, this operation returns all ASINs related to the content document.
- [postContentDocumentAsinRelations](operations/postContentDocumentAsinRelations.json) (POST /aplus/2020-11-01/contentDocuments/{contentReferenceKey}/asins)：Replaces all ASINs related to the specified A+ Content document, if available. This operation can add or remove ASINs, depending on the current set of related ASINs. Removing an ASIN will suspend the content document from that ASIN.
- [validateContentDocumentAsinRelations](operations/validateContentDocumentAsinRelations.json) (POST /aplus/2020-11-01/contentAsinValidations)：Checks if the A+ Content document is valid for use on a set of ASINs.
- [searchContentPublishRecords](operations/searchContentPublishRecords.json) (GET /aplus/2020-11-01/contentPublishRecords)：Searches for A+ Content publishing records, if available.
- [postContentDocumentApprovalSubmission](operations/postContentDocumentApprovalSubmission.json) (POST /aplus/2020-11-01/contentDocuments/{contentReferenceKey}/approvalSubmissions)：Submits an A+ Content document for review, approval, and publishing.
- [postContentDocumentSuspendSubmission](operations/postContentDocumentSuspendSubmission.json) (POST /aplus/2020-11-01/contentDocuments/{contentReferenceKey}/suspendSubmissions)：Submits a request to suspend visible A+ Content. This doesn't delete the content document or the ASIN relations.
