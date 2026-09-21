---
title: TikTok Shop Analytics API
description: "Shop, product, SKU, video, LIVE, bestselling, and shop performance analytics."
---

# API List

- [Get Bestselling Creators](operations/get-bestselling-creators-202511.json) (GET /analytics/202511/creators/bestselling)：Get the top 100 performing creators of the target date range
- [Get Bestselling LIVE Sessions](operations/get-bestselling-live-sessions-202511.json) (GET /analytics/202511/lives/bestselling)：Get the top 100 performing lives of the target date range
- [Get Bestselling Products](operations/get-bestselling-products-202511.json) (GET /analytics/202511/products/bestselling)：Get the top 100 performing products of the target date range
- [Get Bestselling Videos](operations/get-bestselling-videos-202511.json) (GET /analytics/202511/videos/bestselling)：Get the top 100 performing videos of the target date range
- [Get Shop LIVE Minute Performance](operations/get-shop-live-minute-performance-202510.json) (GET /analytics/202510/shop_lives/{live_id}/performance_per_minutes)：Returns minute-level performance for a LIVE session after the session is finished. This API only returns data for live streams hosted by the shop official account or marketing account.
- [Get Shop LIVE Performance List](operations/get-shop-live-performance-list-202509.json) (GET /analytics/202509/shop_lives/performance)：Returns a list of LIVE stream sessions and associated metrics for a shop. Sellers can only query room ID data for their own official creator accounts.
- [Get Shop LIVE Performance Overview](operations/get-shop-live-performance-overview-202509.json) (GET /analytics/202509/shop_lives/overview_performance)：Returns overall performance metrics for all LIVE stream sessions under a certain shop.
- [Get Shop LIVE Products Performance List](operations/get-shop-live-products-performance-list-202512.json) (GET /analytics/202512/shop/{live_id}/products_performance)：Returns sale performance for each product in a shop-related LIVE session from the official account or marketing accounts.
- [Get Shop Performance](operations/get-shop-performance-202509.json) (GET /analytics/202509/shop/performance)：Returns performance metrics at shop/seller level.
- [Get Shop Performance Per Hour](operations/get-shop-performance-per-hour-202510.json) (GET /analytics/202510/shop/performance/{date}/performance_per_hour)：Returns hourly shop performance details for the requested date. The date can be within the last 30 days, including today.
- [Get Shop Product Performance Detail](operations/get-shop-product-performance-detail-202509.json) (GET /analytics/202509/shop_products/{product_id}/performance)：Returns detailed performance metrics for the specified product.
- [Get Shop Product Performance List](operations/get-shop-product-performance-list-202605.json) (GET /analytics/202605/shop_products/performance)：Returns a list of product performance overview metrics.
- [Get Shop SKU Performance Detail](operations/get-shop-sku-performance-detail-202509.json) (GET /analytics/202509/shop_skus/{sku_id}/performance)：Returns performance metrics for the specified SKU.
- [Get Shop SKU Performance List](operations/get-shop-sku-performance-list-202509.json) (GET /analytics/202509/shop_skus/performance)：Returns a list of SKU performance metrics.
- [Get Shop Video Performance Details](operations/get-shop-video-performance-details-202509.json) (GET /analytics/202509/shop_videos/{video_id}/performance)：Returns detailed performance metrics for a (requested) video.
- [Get Shop Video Performance List](operations/get-shop-video-performance-list-202605.json) (GET /analytics/202605/shop_videos/performance)：Returns a list of videos and associated metrics for a shop.
- [Get Shop Video Performance Overview](operations/get-shop-video-performance-overview-202509.json) (GET /analytics/202509/shop_videos/overview_performance)：Returns overall performance metrics for all videos under a shop.
- [Get Shop Video Product Performance List](operations/get-shop-video-product-performance-list-202509.json) (GET /analytics/202509/shop_videos/{video_id}/products/performance)：Returns performance metrics for a list of products promoted in a given video.
- [Get SPS Metric Diagnosis](operations/get-sps-metric-diagnosis-202606.json) (GET /analytics/202606/shop_performances/metrics/{metric_code}/diagnosis)：Returns diagnosis details for a single SPS metric, including benchmark thresholds, trends, calculation details, and distribution details. Supported only for US-region shops.
- [Get SPS Metric Problem Details](operations/get-sps-metric-problem-details-202606.json) (GET /analytics/202606/shop_performances/metrics/{metric_code}/problem_details)：Returns problem order or chat details for a selected SPS metric. Supported only for US-region shops.
- [Get SPS Metric Top Items](operations/get-sps-metric-top-items-202606.json) (GET /analytics/202606/shop_performances/metrics/{metric_code}/top_items)：Returns top products, logistics providers, or aftersales types for a selected SPS metric. Supported only for US-region shops.
- [Get SPS Metrics](operations/get-sps-metrics-202606.json) (GET /analytics/202606/shop_performances/metrics)：Returns SPS metric details and benchmark thresholds for the authorized shop. Supported only for US-region shops.
- [Get SPS Overview](operations/get-sps-overview-202606.json) (GET /analytics/202606/shop_performances/overview)：Returns the SPS overview for the authorized shop, including the score, tier, dimensions, benefits, and top issues. Supported only for US-region shops.
