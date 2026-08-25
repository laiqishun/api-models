---
title: Shopee Public API
description: "Partner, merchant, access token, token refresh, and Shopee IP range operations."
---

# API List

- [v2.public.get_access_token](operations/v2-public-get-access-token.json) (POST /api/v2/auth/token/get)：Use the code from the authorization step to call this API to obtain the authorized shop_id, merchant_id, supplier_id, or user_id, and its corresponding access_token and refresh_token.
- [v2.public.get_merchants_by_partner](operations/v2-public-get-merchants-by-partner.json) (GET /api/v2/public/get_merchants_by_partner)：Use this API to get basic info of merchants which have authorized to the partner.
- [v2.public.get_shopee_ip_ranges](operations/v2-public-get-shopee-ip-ranges.json) (GET /api/v2/public/get_shopee_ip_ranges)：You can get shopee ip address ranges through this open api.
- [v2.public.get_shops_by_partner](operations/v2-public-get-shops-by-partner.json) (GET /api/v2/public/get_shops_by_partner)：get basic info of shops which have authorized to the partner.
- [v2.public.get_token_by_resend_code](operations/v2-public-get-token-by-resend-code.json) (POST /api/v2/public/get_token_by_resend_code)：Use the resend code to get access token and refresh token. When you lost your access token or refresh token, you can go to authorization management page to resend code by yourselves. You can only use this endpoint in live environment, we don't support in test-stable environment.
- [v2.public.refresh_access_token](operations/v2-public-refresh-access-token.json) (POST /api/v2/auth/access_token/get)：Use this API to refresh the access_token after it expires. Refresh_token can be used once only, this API will also return a new refresh_token. Please use the new refresh_token for the next RefreshAccessToken call
