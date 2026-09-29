-- =============================================================================
-- t_platform_module_api 初始化数据：shopee-ads-api
-- 来源: shopee-api/README.md 应用归属与各 operation Swagger 2.0 JSON
-- 生成接口数: 31（ID 1431-1461）；public 6 条为 ERP/Ads 共用接口
-- Ads 的 2 条 coming offline soon 接口仍有可调用路由，按源文件保留。
-- api_desc: operation description；api_desc_cn: 根据接口用途生成的简明中文说明
-- sub_module / sub_module_cn: NULL
-- path: Swagger 原始路径（不含 /proxy/{site} 前缀）
-- =============================================================================

DELETE FROM `t_platform_module_api` WHERE `module` = 'shopee-ads-api';

INSERT INTO `t_platform_module_api` (
  `id`, `module`, `module_cn`, `sub_module`, `sub_module_cn`,
  `module_group`, `module_group_cn`,
  `api_name`, `api_name_cn`, `api_desc`, `api_desc_cn`,
  `method`, `path`, `is_enabled`, `is_deleted`
) VALUES
(1431, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'public', '公共授权', 'v2_public_get_access_token', '获取访问令牌', 'Use the code from the authorization step to call this API to obtain the authorized shop_id, merchant_id, supplier_id, or user_id, and its corresponding access_token and refresh_token.', '获取访问令牌。', 'POST', '/api/v2/auth/token/get', 1, 0),
(1432, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'public', '公共授权', 'v2_public_get_merchants_by_partner', '查询合作伙伴已授权商家', 'Use this API to get basic info of merchants which have authorized to the partner.', '查询合作伙伴已授权商家。', 'GET', '/api/v2/public/get_merchants_by_partner', 1, 0),
(1433, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'public', '公共授权', 'v2_public_get_shopee_ip_ranges', '查询 Shopee IP 地址段', 'You can get shopee ip address ranges through this open api.', '查询 Shopee IP 地址段。', 'GET', '/api/v2/public/get_shopee_ip_ranges', 1, 0),
(1434, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'public', '公共授权', 'v2_public_get_shops_by_partner', '查询合作伙伴已授权店铺', 'get basic info of shops which have authorized to the partner.', '查询合作伙伴已授权店铺。', 'GET', '/api/v2/public/get_shops_by_partner', 1, 0),
(1435, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'public', '公共授权', 'v2_public_get_token_by_resend_code', '使用重发授权码获取令牌', 'Use the resend code to get access token and refresh token. When you lost your access token or refresh token, you can go to authorization management page to resend code by yourselves. You can only use this endpoint in live environment, we don''t support in test-stable environment.', '使用重发授权码获取令牌。', 'POST', '/api/v2/public/get_token_by_resend_code', 1, 0),
(1436, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'public', '公共授权', 'v2_public_refresh_access_token', '刷新访问令牌', 'Use this API to refresh the access_token after it expires. Refresh_token can be used once only, this API will also return a new refresh_token. Please use the new refresh_token for the next RefreshAccessToken call', '刷新访问令牌。', 'POST', '/api/v2/auth/access_token/get', 1, 0),
(1437, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'coming_offline_soon_v2_ads_create_auto_product_ads', '创建自动商品广告', 'Use this API to create Auto Product Ads', '创建自动商品广告。', 'POST', '/api/v2/ads/create_auto_product_ads', 1, 0),
(1438, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'coming_offline_soon_v2_ads_edit_auto_product_ads', '编辑自动商品广告', 'Use this API to edit Auto Product Ads', '编辑自动商品广告。', 'POST', '/api/v2/ads/edit_auto_product_ads', 1, 0),
(1439, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_check_create_gms_product_campaign_eligibility', '查询创建GMS商品广告活动资格', 'Check the seller''s eligibility in creating a GMS campaign', '查询创建GMS商品广告活动资格。', 'GET', '/api/v2/ads/check_create_gms_product_campaign_eligibility', 1, 0),
(1440, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_create_gms_product_campaign', '创建GMS商品广告活动', 'Create a GMS campaign', '创建GMS商品广告活动。', 'POST', '/api/v2/ads/create_gms_product_campaign', 1, 0),
(1441, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_create_manual_product_ads', '创建手动选品商品广告', 'Use this API to create Manual Selection Product Ads', '创建手动选品商品广告。', 'POST', '/api/v2/ads/create_manual_product_ads', 1, 0),
(1442, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_edit_gms_item_product_campaign', '编辑GMS广告活动商品', 'Add/remove items to/from the GMS Campaign', '编辑GMS广告活动商品。', 'POST', '/api/v2/ads/edit_gms_item_product_campaign', 1, 0),
(1443, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_edit_gms_product_campaign', '编辑GMS商品广告活动', 'Edit a GMS campaign', '编辑GMS商品广告活动。', 'POST', '/api/v2/ads/edit_gms_product_campaign', 1, 0),
(1444, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_edit_manual_product_ad_keywords', '编辑手动选品商品广告关键词', 'Use this API to edit Manual Selection Product Ad Keywords', '编辑手动选品商品广告关键词。', 'POST', '/api/v2/ads/edit_manual_product_ad_keywords', 1, 0),
(1445, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_edit_manual_product_ads', '编辑手动选品商品广告', 'Use this API to edit Manual Selection Product Ads', '编辑手动选品商品广告。', 'POST', '/api/v2/ads/edit_manual_product_ads', 1, 0),
(1446, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_get_ads_f_cil_shop_rate', '查询Ads Fácil计划店铺费率', 'Get shop rate for Ads Facil Program', '查询Ads Fácil计划店铺费率。', 'GET', '/api/v2/ads/get_ads_facil_shop_rate', 1, 0),
(1447, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_get_all_cpc_ads_daily_performance', '查询店铺CPC广告每日表现', 'Use this API to get Shop level CPC ads multiple-days daily performance.', '查询店铺CPC广告每日表现。', 'GET', '/api/v2/ads/get_all_cpc_ads_daily_performance', 1, 0),
(1448, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_get_all_cpc_ads_hourly_performance', '查询店铺CPC广告每小时表现', 'Use this API to get Shop level CPC ads single-date hourly performance.', '查询店铺CPC广告每小时表现。', 'GET', '/api/v2/ads/get_all_cpc_ads_hourly_performance', 1, 0),
(1449, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_get_create_product_ad_budget_suggestion', '查询商品广告创建预算建议', 'Call this API to get budget suggestion for product ads creation', '查询商品广告创建预算建议。', 'GET', '/api/v2/ads/get_create_product_ad_budget_suggestion', 1, 0),
(1450, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_get_gms_campaign_performance', '查询GMS广告活动表现', 'Get GMS Campaign performance', '查询GMS广告活动表现。', 'POST', '/api/v2/ads/get_gms_campaign_performance', 1, 0),
(1451, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_get_gms_item_performance', '查询GMS商品广告表现', 'Get GMS Item performance 1. The response returned is sorted by item_id 2. Only items with performance will be returned', '查询GMS商品广告表现。', 'POST', '/api/v2/ads/get_gms_item_performance', 1, 0),
(1452, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_get_product_campaign_daily_performance', '查询商品广告活动每日表现', 'Use this API to get Product level ads multiple-days daily performance.', '查询商品广告活动每日表现。', 'GET', '/api/v2/ads/get_product_campaign_daily_performance', 1, 0),
(1453, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_get_product_campaign_hourly_performance', '查询商品广告活动每小时表现', 'Use this API to get Product level ads single-day hourly performance.', '查询商品广告活动每小时表现。', 'GET', '/api/v2/ads/get_product_campaign_hourly_performance', 1, 0),
(1454, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_get_product_level_campaign_id_list', '查询商品广告活动ID列表', 'Call this API to fetch all the product campaign ids displayed on advertiser platform under a specific Shop', '查询商品广告活动ID列表。', 'GET', '/api/v2/ads/get_product_level_campaign_id_list', 1, 0),
(1455, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_get_product_level_campaign_setting_info', '查询商品广告活动配置', 'Call this API to fetch all the campaign setting info under this Shop.', '查询商品广告活动配置。', 'GET', '/api/v2/ads/get_product_level_campaign_setting_info', 1, 0),
(1456, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_get_product_recommended_roi_target', '查询商品广告推荐ROI目标', 'Get Product Recommended ROI Target', '查询商品广告推荐ROI目标。', 'GET', '/api/v2/ads/get_product_recommended_roi_target', 1, 0),
(1457, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_get_recommended_item_list', '查询推荐投放商品列表', 'Use this API to get the list of recommended SKU (Shop level) with the corresponding tag, i.e top search/best selling/best ROI tag.', '查询推荐投放商品列表。', 'GET', '/api/v2/ads/get_recommended_item_list', 1, 0),
(1458, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_get_recommended_keyword_list', '查询推荐关键词列表', 'Use this API to get the list of Recommended keywords by item and optionally a search keyword', '查询推荐关键词列表。', 'GET', '/api/v2/ads/get_recommended_keyword_list', 1, 0),
(1459, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_get_shop_toggle_info', '查询店铺广告开关状态', 'Use this API to get Shop level info - i.e. seller''s toggle status is on/off', '查询店铺广告开关状态。', 'GET', '/api/v2/ads/get_shop_toggle_info', 1, 0),
(1460, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_get_total_balance', '查询广告账户总余额', 'Use this API to return the seller''s Real-time total balance of their ads credit including the paid credits and free credits.', '查询广告账户总余额。', 'GET', '/api/v2/ads/get_total_balance', 1, 0),
(1461, 'shopee-ads-api', 'Shopee广告API', NULL, NULL, 'ads', '广告', 'v2_ads_list_gms_user_deleted_item', '查询GMS活动已移除商品列表', 'List GMS items that have been removed from the Campaign by seller', '查询GMS活动已移除商品列表。', 'POST', '/api/v2/ads/list_gms_user_deleted_item', 1, 0);
