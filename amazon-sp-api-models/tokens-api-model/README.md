---
title: Selling Partner API for Tokens
description: "The Selling Partner API for Tokens provides a secure way to access a customer's PII (Personally Identifiable Information). You can call the Tokens API to get a Restricted Data Token (RDT) for one or more restricted resources that you specify. The RDT authorizes subsequent calls to restricted operations that correspond to the restricted resources that you specified. For more information, see the [Tokens API Use Case Guide](doc:tokens-api-use-case-guide)."
---

# API List
- [createRestrictedDataToken](operations/createRestrictedDataToken.json) (POST /tokens/2021-03-01/restrictedDataToken)：Returns a Restricted Data Token (RDT) for one or more restricted resources that you specify. A restricted resource is the HTTP method and path from a restricted operation that returns Personally Identifiable Information (PII), plus a dataElements value that indicates the type of PII requested. See the Tokens API Use Case Guide for a list of restricted operations. Use the RDT returned here as the access token in subsequent calls to the corresponding restricted operations.
