---
title: "Lazada Membership API"
description: "Membership APIs for Loyalty and User Account related services"
---

# API List

- [GetLinkMember](operations/get-link-member.json) (GET/POST /membership/linkmember/get) — Query the linkmember relationship between buyers and sellers.
- [GetLinkMember](operations/get-link-member-1591.json) (GET/POST /partner/get) — Query the linkmember relationship between buyers and sellers.
- [GetLinkMemberList](operations/get-link-member-list.json) (GET/POST /membership/linkmember/list) — Query all linkmembers of the seller
- [GetLinkMemberList](operations/get-link-member-list-1592.json) (GET/POST /partner/list) — Query all linkmembers of the seller
- [LinkMembership](operations/link-membership.json) (POST /membership/link) — Used to push a new membership to Lazada for proactively linking memberships.
- [PartnerLink](operations/partner-link.json) (GET/POST /partner/link) — Used to push a new membership to Lazada for proactively linking memberships.
- [PartnerTransaction](operations/partner-transaction.json) (GET/POST /partner/transaction) — Using this interface, you can obtain the seller's transaction order based on the conditions, and also contain the membership information
- [PartnerUnlink](operations/partner-unlink.json) (GET/POST /partner/unlink) — Used to remove a linked membership from Lazada. Please note that the link will not physically be removed, but deactivated.
- [PartnerUpdate](operations/partner-update.json) (GET/POST /partner/update) — Used to push membership bulk status updates to Lazada. Please note that this is not an incremental update, thus information left out that haven been in our system before, will be removed on our end.
- [UpdatePartnerUserId](operations/update-partner-user-id.json) (GET/POST /partner/updatePartnerUserId) — Used to update the partner user id to new partner user id

## Modeling notes

Each JSON file is built from the official Lazada API reference page. The complete parameter trees, endpoint list, error table, examples, and code samples are retained in `x-lazada-*` fields. Lazada does not provide these pages as downloadable Swagger files.

For GET operations, documented request fields are represented as query parameters. POST body placement is represented in standard Swagger only when shown by the official cURL example; otherwise the original request field tree remains available under `x-lazada-request-parameters`.
