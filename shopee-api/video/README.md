---
title: Shopee Video API
description: "Video upload, video information, video list, and video performance operations."
---

# API List

- [v2.video.delete_video](operations/v2-video-delete-video.json) (POST /api/v2/video/delete_video)：Use this API to delete video. You can delete the video for both draft and post status.
- [v2.video.edit_video_info](operations/v2-video-edit-video-info.json) (POST /api/v2/video/edit_video_info)：You need to call v2.media.init_video_upload, v2.media.upload_video_part, and v2.media.complete_video_upload to upload the video, and call the v2.media.get_video_upload_result to get the video_upload_id of uploaded video first, then call this API to set video post information. After submit, the video is still draft status, you need to call v2.video.post_video to post the video to Shopee Video. You can only set and update post information before the video is post.
- [v2.video.get_cover_list](operations/v2-video-get-cover-list.json) (GET /api/v2/video/get_cover_list)：You need to call v2.media.init_video_upload, v2.media.upload_video_part, and v2.media.complete_video_upload to upload the video, and call the v2.media.get_video_upload_result to get the video_upload_id of uploaded video. After the video is uploaded, obtain the frame-by-frame results and select a specific frame as the video cover.
- [v2.video.get_metric_trend](operations/v2-video-get-metric-trend.json) (GET /api/v2/video/get_metric_trend)：Query video data indicator trends.
- [v2.video.get_overview_performance](operations/v2-video-get-overview-performance.json) (GET /api/v2/video/get_overview_performance)：Get overall performance data for all post Shopee Video. There is at least a one-day delay.
- [v2.video.get_prodcut_performance_list](operations/v2-video-get-prodcut-performance-list.json) (GET /api/v2/video/get_prodcut_performance_list)：Get specific performance data for products linked with Shopee Video. There is at least a one-day delay.
- [v2.video.get_user_demographics](operations/v2-video-get-user-demographics.json) (GET /api/v2/video/get_user_demographics)：Get user demographics data to better understand the types of viewers that watch your Shopee Video.
- [v2.video.get_video_detail_audience_distribution](operations/v2-video-get-video-detail-audience-distribution.json) (GET /api/v2/video/get_video_detail_audience_distribution)：Get detailed audience distribution data for individual post Shopee Video. There is at least a one-day delay.
- [v2.video.get_video_detail_metric_trend](operations/v2-video-get-video-detail-metric-trend.json) (GET /api/v2/video/get_video_detail_metric_trend)：Get detailed metric trend data for individual post Shopee Video. There is at least a one-day delay.
- [v2.video.get_video_detail_performance](operations/v2-video-get-video-detail-performance.json) (GET /api/v2/video/get_video_detail_performance)：Get detailed performance data for individual post Shopee Video. There is at least a one-day delay.
- [v2.video.get_video_detail_product_performance](operations/v2-video-get-video-detail-product-performance.json) (GET /api/v2/video/get_video_detail_product_performance)：Get performance data for products linked with individual post Shopee Video. There is at least a one-day delay.
- [v2.video.get_video_detail](operations/v2-video-get-video-detail.json) (GET /api/v2/video/get_video_detail)：Get the detail information of video.
- [v2.video.get_video_list](operations/v2-video-get-video-list.json) (GET /api/v2/video/get_video_list)：Get the list of video in draft status or video already post to Shopee Video.
- [v2.video.get_video_performance_list](operations/v2-video-get-video-performance-list.json) (GET /api/v2/video/get_video_performance_list)：Get specific performance data for individual post Shopee Video. There is at least a one-day delay.
- [v2.video.post_video](operations/v2-video-post-video.json) (POST /api/v2/video/post_video)：You need to call v2.media.init_video_upload, v2.media.upload_video_part, and v2.media.complete_video_upload to upload the video, then call the v2.video.edit_video_info API to set video post information, finally call this API to post the video to Shopee Video.
