---
title: TikTok Shop Authorization API
description: "Authorized shops and authorized category asset operations."
---

# API List

- [Get Authorized Category Assets](operations/get-authorized-category-assets-202405.json) (GET /authorization/202405/category_assets)：Retrieves the list of business category assets authorized by a partner for an app. Partner authorization is required before an app can access the data of a partner, and this access is granted based on business categories. Use this API to check which business category assets are currently authorized for an app and obtain the corresponding category asset cipher for use as an input parameter in affiliate partner related APIs. For more information about partner authorization, refer to [Partner authorization guide](678e3a3978f4c20311b8b555). Target partner: All
- [Get Authorized Shops](operations/get-authorized-shops-202309.json) (GET /authorization/202309/shops)：Retrieves the list of shops that a seller has authorized for an app. Seller authorization is required before an app can access the data of a shop. Use this API to check which shops are currently authorized for an app and obtain the corresponding shop cipher for use as an input parameter in shop related APIs. For more information about seller authorization, refer to [Seller authorization guide](https://partner.tiktokshop.com/docv2/page/678e3a344ddec3030b238fa0). Target seller: All
