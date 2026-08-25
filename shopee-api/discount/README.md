---
title: Shopee Discount API
description: "Discount, discount item, and SIP discount lifecycle operations."
---

# API List

- [v2.discount.add_discount_item](operations/v2-discount-add-discount-item.json) (POST /api/v2/discount/add_discount_item)：Use this api to add shop discount item.
- [v2.discount.add_discount](operations/v2-discount-add-discount.json) (POST /api/v2/discount/add_discount)：Use this api to add shop discount activity
- [v2.discount.delete_discount_item](operations/v2-discount-delete-discount-item.json) (POST /api/v2/discount/delete_discount_item)：Use this api to delete items of the discount activity
- [v2.discount.delete_discount](operations/v2-discount-delete-discount.json) (POST /api/v2/discount/delete_discount)：Use this api to delete one discount activity
- [v2.discount.delete_sip_discount](operations/v2-discount-delete-sip-discount.json) (POST /api/v2/discount/delete_sip_discount)：Delete SIP Overseas Discounts for SIP affiliate region. Please use Primary shop's Shop ID to request, and provide the region of the Affiliate shop to be deleted, the API will delete the discount from that region's Affiliate shop.
- [v2.discount.end_discount](operations/v2-discount-end-discount.json) (POST /api/v2/discount/end_discount)：Use this api to end shop discount activity
- [v2.discount.get_discount_list](operations/v2-discount-get-discount-list.json) (GET /api/v2/discount/get_discount_list)：Use this api to get shop discount activity list
- [v2.discount.get_discount](operations/v2-discount-get-discount.json) (GET /api/v2/discount/get_discount)：Use this api to get one shop discount activity detail
- [v2.discount.get_sip_discounts](operations/v2-discount-get-sip-discounts.json) (GET /api/v2/discount/get_sip_discounts)：Get SIP Overseas Discounts. Only regions that have upcoming/ongoing discounts will be returned. Please use Primary shop's Shop ID to request, the API will return the list of Affiliate shops under this Primary shop that have set discounts, along with the discount details.
- [v2.discount.set_sip_discount](operations/v2-discount-set-sip-discount.json) (POST /api/v2/discount/set_sip_discount)：Set SIP Overseas Discount for SIP affiliate region. Please use Primary shop's Shop ID to request, and provide the region and discount rate of the Affiliate shop to be set or update, the API will set or update the discount rate for that region's Affiliate shop.
- [v2.discount.update_discount_item](operations/v2-discount-update-discount-item.json) (POST /api/v2/discount/update_discount_item)：Use this api to update items of the discount promotion.
- [v2.discount.update_discount](operations/v2-discount-update-discount.json) (POST /api/v2/discount/update_discount)：Use this api to update one discount information
