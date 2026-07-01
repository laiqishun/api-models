---
title: Selling Partner API for Application Management
description: "The Selling Partner API for Application Management lets you programmatically update the client secret on registered applications."
---

# API List
- [rotateApplicationClientSecret](operations/rotateApplicationClientSecret.json) (POST /applications/2023-11-30/clientSecret)：Rotates application client secrets for a developer application. Developers must register a destination queue in the developer console before calling this operation. When this operation is called a new client secret is generated and sent to the developer-registered queue. For more information, refer to [Rotate your application client secret](https://developer-docs.amazon.com/sp-api/v0/docs/application-management-api-v2023-11-30-use-case-guide#tutorial-rotate-your-applications-client-secret).
