---
title: Shopee Push API
description: "Application push configuration and lost push message operations."
---

# API List

- [v2.push.confirm_consumed_lost_push_message](operations/v2-push-confirm-consumed-lost-push-message.json) (POST /api/v2/push/confirm_consumed_lost_push_message)：Confirm consumed lost push message
- [v2.push.get_app_push_config](operations/v2-push-get-app-push-config.json) (GET /api/v2/push/get_app_push_config)：you can get your app current push config setting through this api
- [v2.push.get_lost_push_message](operations/v2-push-get-lost-push-message.json) (GET /api/v2/push/get_lost_push_message)：Get the lost push messages that were lost within 3 days of the current time and not confirmed to have been consumed
- [v2.push.set_app_push_config](operations/v2-push-set-app-push-config.json) (POST /api/v2/push/set_app_push_config)：you can turn on or turn off your app push config setting through this open api
