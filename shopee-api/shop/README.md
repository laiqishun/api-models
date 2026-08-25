---
title: Shopee Shop API
description: "Shop information, profile, warehouse, notification, brand, and holiday mode operations."
---

# API List

- [v2.shop.get_authorised_reseller_brand](operations/v2-shop-get-authorised-reseller-brand.json) (GET /api/v2/shop/get_authorised_reseller_brand)：Get the authorised reseller brand list for the shop.
- [v2.shop.get_br_shop_onboarding_info](operations/v2-shop-get-br-shop-onboarding-info.json) (GET /api/v2/shop/get_br_shop_onboarding_info)：[For BR Shop Only] Use this API to get shop KYC registration and qualification information.
- [v2.shop.get_profile](operations/v2-shop-get-profile.json) (GET /api/v2/shop/get_profile)：This API support to get information of shop.
- [v2.shop.get_shop_holiday_mode](operations/v2-shop-get-shop-holiday-mode.json) (GET /api/v2/shop/get_shop_holiday_mode)：Use this API to check whether a shop has enabled holiday mode and its ongoing and upcoming holiday mode period.
- [v2.shop.get_shop_info](operations/v2-shop-get-shop-info.json) (GET /api/v2/shop/get_shop_info)：Use this call to get information of shop
- [v2.shop.get_shop_notification](operations/v2-shop-get-shop-notification.json) (GET /api/v2/shop/get_shop_notification)：get Seller Center notification, the permission is controlled by App type
- [v2.shop.get_warehouse_detail](operations/v2-shop-get-warehouse-detail.json) (GET /api/v2/shop/get_warehouse_detail)：For given shop id and region, return warehouse info including warehouse id, address id and location id, return all warehouse with once call.
- [v2.shop.set_shop_holiday_mode](operations/v2-shop-set-shop-holiday-mode.json) (POST /api/v2/shop/set_shop_holiday_mode)：Use this API to set holiday periods in advance for automatic on/off of holiday mode and there are two holiday modes allowing sellers to choose whether to accept new orders during holiday.
- [v2.shop.update_profile](operations/v2-shop-update-profile.json) (POST /api/v2/shop/update_profile)：This API support to let sellers to update the shop name, shop logo, and shop description.
