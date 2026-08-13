-- =============================================================================
-- t_platform_module_api 初始化数据：amazon-ads-api
-- 来源: external-skill-docs/amazon-ads-api 下 operation Swagger/OpenAPI
-- 生成接口数: 58
-- api_desc_cn: 由 api_desc 翻译得到（中文源文则原样保留）
-- sub_module / sub_module_cn: NULL
-- path: swagger 原始路径（不含 /proxy/{site} 前缀）
-- =============================================================================

DELETE FROM `t_platform_module_api` WHERE `module` = 'amazon-ads-api';

INSERT INTO `t_platform_module_api` (
  `id`, `module`, `module_cn`, `sub_module`, `sub_module_cn`,
  `module_group`, `module_group_cn`,
  `api_name`, `api_name_cn`, `api_desc`, `api_desc_cn`,
  `method`, `path`, `is_enabled`, `is_deleted`
) VALUES
(284, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'ad-associations', '广告关联', 'CreateAdAssociation', '创建广告关联', 'Create Ad Association', '创建广告关联', 'POST', '/adsApi/v1/create/adAssociations', 1, 0),
(285, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'ad-associations', '广告关联', 'DeleteAdAssociation', '删除广告关联', 'Delete Ad Association', '删除广告关联', 'POST', '/adsApi/v1/delete/adAssociations', 1, 0),
(286, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'ad-associations', '广告关联', 'QueryAdAssociation', '查询广告关联', 'Query Ad Association', '查询广告关联', 'POST', '/adsApi/v1/query/adAssociations', 1, 0),
(287, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'ad-associations', '广告关联', 'UpdateAdAssociation', '更新广告关联', 'Update Ad Association', '更新广告关联', 'POST', '/adsApi/v1/update/adAssociations', 1, 0),
(288, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'ad-extensions', '广告扩展', 'CreateAdExtension', '创建广告扩展', 'Create ad extensions - API is in open beta', '创建广告附加信息 - API 处于公开测试阶段', 'POST', '/adsApi/v1/create/adExtensions', 1, 0),
(289, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'ad-extensions', '广告扩展', 'QueryAdExtension', '查询广告扩展', 'Query ad_extension - API is in open beta', '查询广告附加信息 - API 处于公开测试阶段', 'POST', '/adsApi/v1/query/adExtensions', 1, 0),
(290, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'ad-extensions', '广告扩展', 'UpdateAdExtension', '更新广告扩展', 'Update ad_extension - API is in open beta', '更新广告附加信息 - API 处于公开测试阶段', 'POST', '/adsApi/v1/update/adExtensions', 1, 0),
(291, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'ad-groups', '广告组', 'CreateAdGroup', '创建广告组', 'Create ad groups', '创建广告组', 'POST', '/adsApi/v1/create/adGroups', 1, 0),
(292, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'ad-groups', '广告组', 'DeleteAdGroup', '删除广告组', 'Delete ad groups', '删除广告组', 'POST', '/adsApi/v1/delete/adGroups', 1, 0),
(293, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'ad-groups', '广告组', 'QueryAdGroup', '查询广告组', 'List ad groups', '列出广告组', 'POST', '/adsApi/v1/query/adGroups', 1, 0),
(294, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'ad-groups', '广告组', 'UpdateAdGroup', '更新广告组', 'Update ad groups', '更新广告组', 'POST', '/adsApi/v1/update/adGroups', 1, 0),
(295, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'ads', '广告', 'CreateAd', '创建广告', 'Create ads', '创建广告', 'POST', '/adsApi/v1/create/ads', 1, 0),
(296, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'ads', '广告', 'DeleteAd', '删除广告', 'Delete ads', '删除广告', 'POST', '/adsApi/v1/delete/ads', 1, 0),
(297, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'ads', '广告', 'QueryAd', '查询广告', 'List ads', '列出广告', 'POST', '/adsApi/v1/query/ads', 1, 0),
(298, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'ads', '广告', 'UpdateAd', '更新广告', 'Update ads', '更新广告', 'POST', '/adsApi/v1/update/ads', 1, 0),
(299, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'advertising-deals', '广告交易', 'SBCreateAdvertisingDeal', 'SB 创建广告交易', 'Create advertisingDeal', '创建广告交易', 'POST', '/adsApi/v1/create/advertisingDeals/sb', 1, 0),
(300, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'advertising-deals', '广告交易', 'SBCreateAdvertisingDealTarget', 'SB 创建广告交易目标', 'Create advertisingDealTarget', '创建广告交易投放目标', 'POST', '/adsApi/v1/create/advertisingDealTargets/sb', 1, 0),
(301, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'advertising-deals', '广告交易', 'SBDeleteAdvertisingDeal', 'SB 删除广告交易', 'Delete advertisingDeal', '删除广告交易', 'POST', '/adsApi/v1/delete/advertisingDeals/sb', 1, 0),
(302, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'advertising-deals', '广告交易', 'SBDeleteAdvertisingDealTarget', 'SB 删除广告交易目标', 'Delete advertisingDealTarget', '删除广告交易投放目标', 'POST', '/adsApi/v1/delete/advertisingDealTargets/sb', 1, 0),
(303, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'advertising-deals', '广告交易', 'SBQueryAdvertisingDeal', 'SB查询广告交易', 'Query advertisingDeal', '查询广告交易', 'POST', '/adsApi/v1/query/advertisingDeals/sb', 1, 0),
(304, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'advertising-deals', '广告交易', 'SBQueryAdvertisingDealTarget', 'SB查询广告交易目标', 'Query advertisingDealTarget', '查询广告交易投放目标', 'POST', '/adsApi/v1/query/advertisingDealTargets/sb', 1, 0),
(305, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'advertising-deals', '广告交易', 'SBUpdateAdvertisingDeal', 'SB 更新广告交易', 'Update advertisingDeal', '更新广告交易', 'POST', '/adsApi/v1/update/advertisingDeals/sb', 1, 0),
(306, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'brand-stores', '品牌旗舰店', 'ListBrandStoreEdition', '列出品牌旗舰店版本', 'List brand store editions', '列出品牌旗舰店版本。', 'GET', '/adsApi/v1/brandStoreEditions', 1, 0),
(307, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'brand-stores', '品牌旗舰店', 'QueryBrandStore', '查询品牌店铺', 'Query brand store content', '查询品牌店铺内容', 'POST', '/adsApi/v1/query/brandStores', 1, 0),
(308, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'brand-stores', '品牌旗舰店', 'QueryBrandStoreEditionPublishVersion', '查询品牌旗舰店版本发布记录', 'Query store edition publish versions', '查询旗舰店版本发布记录', 'POST', '/adsApi/v1/query/brandStoreEditionPublishVersions', 1, 0),
(309, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'brand-stores', '品牌旗舰店', 'QueryBrandStorePage', '查询品牌旗舰店页面', 'Retrieve brand store page content', '检索品牌旗舰店页面内容', 'POST', '/adsApi/v1/query/brandStorePages', 1, 0),
(310, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'brand-stores', '品牌旗舰店', 'UpdateBrandStoreEditionPublishVersion', '更新品牌旗舰店版本发布记录', 'Update store edition publish versions', '更新旗舰店版本发布记录', 'POST', '/adsApi/v1/update/brandStoreEditionPublishVersions', 1, 0),
(311, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'campaign-forecasts', '广告活动预测', 'DSPRetrieveCampaignForecast', 'DSP检索广告活动预测', 'Retrieve campaign forecast', '检索广告活动预测', 'POST', '/adsApi/v1/retrieve/campaignForecasts/dsp', 1, 0),
(312, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'campaigns', '广告活动', 'CreateCampaign', '创建广告活动', 'Create campaigns', '创建广告活动', 'POST', '/adsApi/v1/create/campaigns', 1, 0),
(313, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'campaigns', '广告活动', 'DeleteCampaign', '删除广告活动', 'Delete campaigns', '删除广告活动', 'POST', '/adsApi/v1/delete/campaigns', 1, 0),
(314, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'campaigns', '广告活动', 'QueryCampaign', '查询广告活动', 'Query campaign', '查询广告活动', 'POST', '/adsApi/v1/query/campaigns', 1, 0),
(315, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'campaigns', '广告活动', 'UpdateCampaign', '更新广告活动', 'Update campaign', '更新广告活动', 'POST', '/adsApi/v1/update/campaigns', 1, 0),
(316, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'commitments', '承诺/预算承诺', 'DSPCreateCommitment', 'DSP创建承诺', 'Create commitments', '创建预算承诺', 'POST', '/adsApi/v1/create/commitments/dsp', 1, 0),
(317, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'commitments', '承诺/预算承诺', 'DSPListCommitment', 'DSP列出承诺', 'List commitments', '列出承诺', 'GET', '/adsApi/v1/commitments/dsp', 1, 0),
(318, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'commitments', '承诺/预算承诺', 'DSPQueryCommitment', 'DSP查询承诺', 'Query commitments with filters', '使用过滤器查询承诺', 'POST', '/adsApi/v1/query/commitments/dsp', 1, 0),
(319, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'commitments', '承诺/预算承诺', 'DSPRetrieveCommitment', 'DSP检索承诺', 'Get Commitments', '获取预算承诺', 'POST', '/adsApi/v1/retrieve/commitments/dsp', 1, 0),
(320, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'commitments', '承诺/预算承诺', 'DSPRetrieveCommitmentSpend', 'DSP 检索承诺支出', 'Retrieve commitment spend', '检索承诺支出', 'POST', '/adsApi/v1/retrieve/commitmentSpends/dsp', 1, 0),
(321, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'commitments', '承诺/预算承诺', 'DSPUpdateCommitment', 'DSP更新承诺', 'Update commitments', '更新承诺', 'POST', '/adsApi/v1/update/commitments/dsp', 1, 0),
(322, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'geo-locations', '地理位置', 'CreateGeoLocation', '创建地理位置', 'Create geo location targeting definitions.', '创建地理位置定位定义。', 'POST', '/adsApi/v1/create/geoLocations', 1, 0),
(323, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'location-indexes', '位置索引', 'CreateLocationIndex', '创建位置索引', 'Create a Smart Location Index.', '创建智能位置索引。', 'POST', '/adsApi/v1/create/locationIndexes', 1, 0),
(324, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'location-indexes', '位置索引', 'ListLocationIndex', '列出位置索引', 'List all Smart Location Indexes for the authenticated advertiser.', '列出经过身份验证的广告商的所有智能位置索引。', 'GET', '/adsApi/v1/locationIndexes', 1, 0),
(325, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'location-indexes', '位置索引', 'RetrieveLocationIndex', '检索位置索引', 'Retrieve one or more Smart Location Indexes by ID.', '按 ID 检索一个或多个智能位置索引。', 'POST', '/adsApi/v1/retrieve/locationIndexes', 1, 0),
(326, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'location-indexes', '位置索引', 'UpdateLocationIndex', '更新位置索引', 'Update the data for an existing Smart Location Index.', '更新现有智能位置索引的数据。', 'POST', '/adsApi/v1/update/locationIndexes', 1, 0),
(327, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'profiles', '广告档案', 'getProfileById', '按ID获取广告档案', 'Gets a profile specified by identifier.', '按标识符获取广告档案。', 'GET', '/v2/profiles/{profileId}', 1, 0),
(328, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'profiles', '广告档案', 'listProfiles', '列出广告档案', 'Gets a list of profiles.', '获取广告档案列表。', 'GET', '/v2/profiles', 1, 0),
(329, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'profiles', '广告档案', 'updateProfiles', '更新广告档案', 'Update the daily budget for one or more profiles.', '更新一个或多个广告档案的每日预算。', 'PUT', '/v2/profiles', 1, 0),
(330, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'recommendations', '推荐', 'SBCreateRecommendation', 'SB 创建推荐', 'Create recommendations', '创建推荐', 'POST', '/adsApi/v1/create/recommendations/sb', 1, 0),
(331, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'recommendations', '推荐', 'SBQueryRecommendationType', 'SB查询推荐类型', 'Query RecommendationTypes', '查询推荐类型', 'POST', '/adsApi/v1/query/recommendationTypes/sb', 1, 0),
(332, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'reporting', '报表', 'createAsyncReport', '创建异步报告', 'Creates a report request.', '创建报告请求。', 'POST', '/reporting/reports', 1, 0),
(333, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'reporting', '报表', 'deleteAsyncReport', '删除异步报告', 'Deletes a report by id.', '按 ID 删除报告。', 'DELETE', '/reporting/reports/{reportId}', 1, 0),
(334, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'reporting', '报表', 'getAsyncReport', '获取异步报告', 'Gets a generation status of a report by id.', '通过id获取报表的生成状态。', 'GET', '/reporting/reports/{reportId}', 1, 0),
(335, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'sb-keyword-pricing', 'Sponsored Brands关键词定价', 'SBAdsApiv1CreateReservedTargetPricing', 'SB 创建预留目标定价', 'Create reservedTarget pricing', '创建预留目标定价', 'POST', '/adsApi/v1/create/reservedTargetPricings/sb', 1, 0),
(336, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'sb-keyword-pricing', 'Sponsored Brands关键词定价', 'SBCreateBrandedKeywordsPricing', 'SB 创建品牌关键词定价', 'Create brandedKeywords pricing', '创建品牌关键词定价', 'POST', '/adsApi/v1/create/brandedKeywordsPricings/sb', 1, 0),
(337, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'sb-keyword-pricing', 'Sponsored Brands关键词定价', 'SBCreateKeywordReservationValidation', 'SB 创建关键字预订验证', 'Validate keyword reservation', '验证关键字预留', 'POST', '/adsApi/v1/create/keywordReservationValidations/sb', 1, 0),
(338, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'targets', '投放目标', 'CreateTarget', '创建投放目标', 'Create target', '创建投放目标', 'POST', '/adsApi/v1/create/targets', 1, 0),
(339, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'targets', '投放目标', 'DeleteTarget', '删除投放目标', 'Delete target', '删除投放目标', 'POST', '/adsApi/v1/delete/targets', 1, 0),
(340, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'targets', '投放目标', 'QueryTarget', '查询投放目标', 'List target', '列出投放目标', 'POST', '/adsApi/v1/query/targets', 1, 0),
(341, 'amazon-ads-api', '亚马逊广告API', NULL, NULL, 'targets', '投放目标', 'UpdateTarget', '更新投放目标', 'Update target', '更新投放目标', 'POST', '/adsApi/v1/update/targets', 1, 0);
