---
title: Selling Partner API for Feeds
description: "The Selling Partner API for Feeds lets you upload data to Amazon on behalf of a selling partner."
---

# API List
- [getFeeds](operations/getFeeds.json) (GET /feeds/2021-06-30/feeds)：Returns feed details for the feeds that match the filters that you specify.
- [createFeed](operations/createFeed.json) (POST /feeds/2021-06-30/feeds)：Creates a feed. Upload the contents of the feed document before calling this operation.
- [cancelFeed](operations/cancelFeed.json) (DELETE /feeds/2021-06-30/feeds/{feedId})：Cancels the feed that you specify. Only feeds with `processingStatus=IN_QUEUE` can be cancelled. Cancelled feeds are returned in subsequent calls to the [`getFeed`](https://developer-docs.amazon.com/sp-api/reference/getfeed) and [`getFeeds`](https://developer-docs.amazon.com/sp-api/reference/getfeeds) operations.
- [getFeed](operations/getFeed.json) (GET /feeds/2021-06-30/feeds/{feedId})：Returns feed details (including the `resultDocumentId`, if available) for the feed that you specify.
- [createFeedDocument](operations/createFeedDocument.json) (POST /feeds/2021-06-30/documents)：Creates a feed document for the feed type that you specify. This operation returns a presigned URL for uploading the feed document contents. It also returns a `feedDocumentId` value that you can pass in with a subsequent call to the [`createFeed`](https://developer-docs.amazon.com/sp-api/reference/createfeed) operation.
- [getFeedDocument](operations/getFeedDocument.json) (GET /feeds/2021-06-30/documents/{feedDocumentId})：Returns the information required for retrieving a feed document's contents.
