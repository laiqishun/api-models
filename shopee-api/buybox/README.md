---
title: "Shopee Buybox API"
description: "Buybox model enrollment and model or shop performance APIs."
---

# API List

- [v2.buybox.get_buybox_model_performance](operations/v2-buybox-get-buybox-model-performance.json) (POST /api/v2/buybox/get_buybox_model_performance)：Get Buybox model performance by model IDs for the authorized shop.
- [v2.buybox.get_buybox_models_by_model_id](operations/v2-buybox-get-buybox-models-by-model-id.json) (POST /api/v2/buybox/get_buybox_models_by_model_id)：Get Buybox model information by model IDs for the authorized shop.
- [v2.buybox.get_buybox_models_by_shop_id](operations/v2-buybox-get-buybox-models-by-shop-id.json) (POST /api/v2/buybox/get_buybox_models_by_shop_id)：Get the paginated Buybox model list for the authorized shop.
- [v2.buybox.get_buybox_shop_performance](operations/v2-buybox-get-buybox-shop-performance.json) (POST /api/v2/buybox/get_buybox_shop_performance)：Get Buybox shop performance for the authorized shop.
- [v2.buybox.update_buybox_model_enrollment](operations/v2-buybox-update-buybox-model-enrollment.json) (POST /api/v2/buybox/update_buybox_model_enrollment)：Update Buybox model enrollment status for the authorized shop.

## Modeling notes

The operation JSON retains request and response parameter trees, API-specific and common errors, examples, permissions, API tools, and update logs in `x-shopee-*` fields. Check each operation's `x-shopee-permissions` before treating it as callable.
