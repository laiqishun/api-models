---
title: Shopee Media Space API
description: "Media Space image and video upload workflow operations."
---

# API List

- [v2.media_space.cancel_video_upload](operations/v2-media-space-cancel-video-upload.json) (POST /api/v2/media_space/cancel_video_upload)：Cancel a video upload session
- [v2.media_space.complete_video_upload](operations/v2-media-space-complete-video-upload.json) (POST /api/v2/media_space/complete_video_upload)：Complete the video upload and starts the transcoding process when all parts are uploaded successfully.
- [v2.media_space.get_video_upload_result](operations/v2-media-space-get-video-upload-result.json) (GET /api/v2/media_space/get_video_upload_result)：Query the upload status and result of video upload.
- [v2.media_space.init_video_upload](operations/v2-media-space-init-video-upload.json) (POST /api/v2/media_space/init_video_upload)：Initiate video upload session. Video duration should be between 10s and 60s (inclusive).
- [v2.media_space.upload_image](operations/v2-media-space-upload-image.json) (POST /api/v2/media_space/upload_image)：Use this API to upload multiple image files (less than 9 images).
- [v2.media_space.upload_video_part](operations/v2-media-space-upload-video-part.json) (POST /api/v2/media_space/upload_video_part)：Upload video file by part using the upload_id in initiate_video_upload. The request Content-Type of this API should be of multipart/form-data
