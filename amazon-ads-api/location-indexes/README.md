---
title: Location Indexes
description: "Amazon Ads API group for Location Indexes operations."
---

# API List
- [CreateLocationIndex](operations/CreateLocationIndex.json) (POST /adsApi/v1/create/locationIndexes)：Create a Smart Location Index. A Smart Location Index is a named dataset that maps postal codes to index values representing relative audience quality or sales potential for a given advertiser. Index data is processed asynchronously; the index status will transition from PENDING to ENABLED once processing is complete.
- [ListLocationIndex](operations/ListLocationIndex.json) (GET /adsApi/v1/locationIndexes)：List all Smart Location Indexes for the authenticated advertiser. Returns a paginated collection of indexes including their current processing status. Use the nextToken from the response to retrieve subsequent pages.
- [RetrieveLocationIndex](operations/RetrieveLocationIndex.json) (POST /adsApi/v1/retrieve/locationIndexes)：Retrieve one or more Smart Location Indexes by ID. Returns the current metadata and processing status for each requested index. An index with status PENDING is still being processed and is not yet available for use in smart location targeting.
- [UpdateLocationIndex](operations/UpdateLocationIndex.json) (POST /adsApi/v1/update/locationIndexes)：Update the data for an existing Smart Location Index. Replaces the index's postal code values with the provided dataset. The update is processed asynchronously; the index status will return to PENDING until the new data has been fully processed.
