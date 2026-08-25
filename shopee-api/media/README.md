---
title: Shopee Media API
description: "Media image and video upload operations."
---

# API List

- [v2.media.cancel_video_upload](operations/v2-media-cancel-video-upload.json) (POST /api/v2/media/cancel_video_upload)：Use this API to cancel an ongoing video upload task. If the upload has already succeeded, failed, or been cancelled, this operation will fail and return error.
- [v2.media.complete_video_upload](operations/v2-media-complete-video-upload.json) (POST /api/v2/media/complete_video_upload)：Use this API to finalize a video upload task. Once called, the system will transcode all uploaded video parts and prepare the video for use. All parts must be fully uploaded before calling this API.
- [v2.media.get_video_upload_result](operations/v2-media-get-video-upload-result.json) (GET /api/v2/media/get_video_upload_result)：Use this API to retrieve the current status and result of a video upload task. You can also use video_upload_result_push to get notified immediately when a video upload reaches a final status (SUCCEEDED, FAILED, or CANCELLED).
- [v2.media.init_video_upload](operations/v2-media-init-video-upload.json) (POST /api/v2/media/init_video_upload)：Use this API to initialize a new video upload task and obtain a unique upload session ID.
- [v2.media.upload_image](operations/v2-media-upload-image.json) (POST /api/v2/media/upload_image)：Use this API to upload images and support different business scenarios through business and scene parameters.
- [v2.media.upload_video_part](operations/v2-media-upload-video-part.json) (POST /api/v2/media/upload_video_part)：Use this API to upload a video file in parts.
