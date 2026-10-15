---
title: "Mercado Libre API Models"
description: "Global Selling and local seller official developer documentation with evidence-bounded API models."
---

# Mercado Libre developer documentation

Snapshot: **2026-10-15 19:13 CST**. The two official article directories contain **117 Global Selling / CBT** and **173 local-seller** articles. All 290 were retrieved from the official sites. The [document manifest](./document-manifest.md) records every article and its extraction status. The [operation manifest](./manifest.md) lists **910 distinct family + host + method + path models** derived from explicit request examples. [Review gaps](./review-gaps.md) identifies cURL examples that could not be modeled conservatively.

- [Global Selling / CBT](./global-selling/README.md): Global user authorization and marketplace user resources. [Official developer directory](https://global-selling.mercadolibre.com/devsite/api-docs).
- [Local sellers](./local/README.md): local site seller resources and guides. [Official developer directory](https://developers.mercadolibre.com.ar/en_us/api-docs).

## Evidence and limits

Mercado Libre's article directories do not provide a unified official Swagger/OpenAPI download. These JSON files are derived models, not official specifications. A modeled operation has an explicit `curl` method or an unambiguous curl default plus a supported official article API URL. Numeric or site identifiers in example paths are normalized into named variables and flagged in `x-meli-inferred-path-parameters`. Sample request/response data is retained only as redacted structural shapes under `x-meli-*`, never as a complete or required-field schema. Articles without a supported request example remain linked and marked `guide-only` or `needs-review`; this does not mean they have no API or that the entire platform API surface is covered.

Global Selling, ordinary local sellers, and Fully Managed may require different authorization subjects, resources, site rules, and write semantics. Some documented examples use `cbt-shipping-op-api.melisystems.com` or `user-products.melioffice.com` instead of the common API host; the models preserve the documented host but do not prove access to it. Check the linked official article, app permission configuration, and live authorized account before using an operation. The document models do not establish current Ziniao app permissions or successful calls.
