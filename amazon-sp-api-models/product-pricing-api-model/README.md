---
title: Selling Partner API for Pricing
description: "The Selling Partner API for Pricing helps you programmatically retrieve product pricing and offer pricing information for Amazon Marketplace products. For more information, refer to the [Product Pricing v2022-05-01 Use Case Guide](https://developer-docs.amazon.com/sp-api/docs/product-pricing-api-v2022-05-01-use-case-guide)."
---

# API List
- [getFeaturedOfferExpectedPriceBatch](operations/getFeaturedOfferExpectedPriceBatch.json) (POST /batches/products/pricing/2022-05-01/offer/featuredOfferExpectedPrice)：Returns the set of responses that correspond to the batched list of up to 40 requests defined in the request body. The response for each successful (HTTP status code 200) request in the set includes the computed listing price at or below which a seller can expect to become the featured offer (before applicable promotions). This is called the featured offer expected price (FOEP). Featured offer is not guaranteed because competing offers might change. Other offers might be featured based on factors such as fulfillment capabilities to a specific customer. The response to an unsuccessful request includes the available error text.
- [getCompetitiveSummary](operations/getCompetitiveSummary.json) (POST /batches/products/pricing/2022-05-01/items/competitiveSummary)：Returns the competitive summary response, including featured buying options for the ASIN and `marketplaceId` combination.
