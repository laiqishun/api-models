---
title: The Selling Partner API for CustomerFeedback
description: "The Selling Partner API for Customer Feedback (Customer Feedback API) provides information about customer reviews and returns at both the item and browse node level."
---

# API List
- [getItemReviewTopics](operations/getItemReviewTopics.json) (GET /customerFeedback/2024-06-01/items/{asin}/reviews/topics)：Retrieve an item's ten most positive and ten most negative review topics.
- [getItemBrowseNode](operations/getItemBrowseNode.json) (GET /customerFeedback/2024-06-01/items/{asin}/browseNode)：This API returns the associated browse node of the requested ASIN. A browse node is a location in a browse tree that is used for navigation, product classification, and website content on the Amazon retail website.
- [getBrowseNodeReviewTopics](operations/getBrowseNodeReviewTopics.json) (GET /customerFeedback/2024-06-01/browseNodes/{browseNodeId}/reviews/topics)：Retrieve a browse node's ten most positive and ten most negative review topics.
- [getItemReviewTrends](operations/getItemReviewTrends.json) (GET /customerFeedback/2024-06-01/items/{asin}/reviews/trends)：Retrieve an item's positive and negative review trends for the past six months.
- [getBrowseNodeReviewTrends](operations/getBrowseNodeReviewTrends.json) (GET /customerFeedback/2024-06-01/browseNodes/{browseNodeId}/reviews/trends)：Retrieve the positive and negative review trends of items in a browse node for the past six months.
- [getBrowseNodeReturnTopics](operations/getBrowseNodeReturnTopics.json) (GET /customerFeedback/2024-06-01/browseNodes/{browseNodeId}/returns/topics)：Retrieve the topics that customers mention when they return items in a browse node.
- [getBrowseNodeReturnTrends](operations/getBrowseNodeReturnTrends.json) (GET /customerFeedback/2024-06-01/browseNodes/{browseNodeId}/returns/trends)：Retrieve the trends of topics that customers mention when they return items in a browse node.
