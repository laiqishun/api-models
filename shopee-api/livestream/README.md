---
title: Shopee Livestream API
description: "Livestream sessions, items, comments, metrics, and audience operations."
---

# API List

- [v2.livestream.add_item_list](operations/v2-livestream-add-item-list.json) (POST /api/v2/livestream/add_item_list)：Add items to item bag. (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.apply_item_set](operations/v2-livestream-apply-item-set.json) (POST /api/v2/livestream/apply_item_set)：Add product set to item bag. (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.ban_user_comment](operations/v2-livestream-ban-user-comment.json) (POST /api/v2/livestream/ban_user_comment)：Ban the user from posting comments. (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.create_session](operations/v2-livestream-create-session.json) (POST /api/v2/livestream/create_session)：Create a new live stream, include basic information, like cover, title, description, type (test live or normal live). (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.delete_item_list](operations/v2-livestream-delete-item-list.json) (POST /api/v2/livestream/delete_item_list)：Delete items from item bag. (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.delete_show_item](operations/v2-livestream-delete-show-item.json) (POST /api/v2/livestream/delete_show_item)：Unshow showing item. (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.end_session](operations/v2-livestream-end-session.json) (POST /api/v2/livestream/end_session)：End Live. (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.get_item_count](operations/v2-livestream-get-item-count.json) (GET /api/v2/livestream/get_item_count)：Get the number of items in the shopping bag, including the current number of items in the shopping bag, the upper limit of the number, etc. (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.get_item_list](operations/v2-livestream-get-item-list.json) (GET /api/v2/livestream/get_item_list)：Get the detail information of item in item bag, including item id, item serial number, etc.(For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.get_item_set_item_list](operations/v2-livestream-get-item-set-item-list.json) (GET /api/v2/livestream/get_item_set_item_list)：Get the item list of the product set, including item name, id, etc. (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.get_item_set_list](operations/v2-livestream-get-item-set-list.json) (GET /api/v2/livestream/get_item_set_list)：Get the product set of the live stream, including the product set name, id, and item number. (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.get_latest_comment_list](operations/v2-livestream-get-latest-comment-list.json) (GET /api/v2/livestream/get_latest_comment_list)：Get live stream room comments in the last 10 seconds, including user id, user name, comment id, comment content, and comment time. (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.get_like_item_list](operations/v2-livestream-get-like-item-list.json) (GET /api/v2/livestream/get_like_item_list)：Get the item list of My Likes tab.(For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.get_recent_item_list](operations/v2-livestream-get-recent-item-list.json) (GET /api/v2/livestream/get_recent_item_list)：Get the item list of the Recently tab. (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.get_session_detail](operations/v2-livestream-get-session-detail.json) (GET /api/v2/livestream/get_session_detail)：Get basic information about the live streaming room, including cover, title, description, type (test live or normal live), create time, update time, stream url, etc. (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.get_session_item_metric](operations/v2-livestream-get-session-item-metric.json) (GET /api/v2/livestream/get_session_item_metric)：Get real-time indicator data of live stream products, including product clicks, add-to-cart, etc. (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.get_session_metric](operations/v2-livestream-get-session-metric.json) (GET /api/v2/livestream/get_session_metric)：Get real-time indicator data of the live stream room, including the number of likes, comments, shares, views, etc.(For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.get_show_item](operations/v2-livestream-get-show-item.json) (GET /api/v2/livestream/get_show_item)：Get the showing item. (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.post_comment](operations/v2-livestream-post-comment.json) (POST /api/v2/livestream/post_comment)：Post comment in the live stream as streamer. (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.start_session](operations/v2-livestream-start-session.json) (POST /api/v2/livestream/start_session)：Start Live. (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.unban_user_comment](operations/v2-livestream-unban-user-comment.json) (POST /api/v2/livestream/unban_user_comment)：Unban a user from posting comments. (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.update_item_list](operations/v2-livestream-update-item-list.json) (POST /api/v2/livestream/update_item_list)：Update the order of items in item bag. (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.update_session](operations/v2-livestream-update-session.json) (POST /api/v2/livestream/update_session)：Update live stream information, including cover, title, description, and type (test live or normal live). (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.update_show_item](operations/v2-livestream-update-show-item.json) (POST /api/v2/livestream/update_show_item)：Set the showing item. (For TW, ID, TH, PH, MY, SG, VN)
- [v2.livestream.upload_image](operations/v2-livestream-upload-image.json) (POST /api/v2/livestream/upload_image)：Upload an image as the live stream cover.(For TW, ID, TH, PH, MY, SG, VN)
