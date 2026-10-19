---
title: "SHEIN 价格 API"
description: "SHEIN official category 3000013, with one JSON model per named operation."
---

# API List

Official category: [价格 (3000013)](https://open.sheincorp.com/documents/apidoc/3000013). 10 records. Official IDs, applicable modes, and update times remain in the [manifest](../manifest.md) and each JSON file.

- [getCostPriceIncreaseReasonEnumValues](operations/getCostPriceIncreaseReasonEnumValues.json) (POST /open-api/goods/query-change-price-reason)：Get cost price increase reason enum values（获取成本价涨价原因枚举值）
- [getListOfDiscussPrices](operations/getListOfDiscussPrices.json) (POST /open-api/goods/discuss/query-discuss-list)：Get the list of discuss prices（获取议价单列表）
- [priceProofMaterialUpload](operations/priceProofMaterialUpload.json) (POST /open-api/goods/discuss/upload-discuss-file)：Price proof material upload（价格证明材料上传）
- [processDiscussOrder](operations/processDiscussOrder.json) (POST /open-api/goods/discuss/process-discuss)：Process discuss order（处理议价单）
- [productPriceUpdate](operations/productPriceUpdate.json) (POST /open-api/openapi-business-backend/product/price/save)：Product price update API（更新商品售价）
- [queryProductSuggestedRetailPrice](operations/queryProductSuggestedRetailPrice.json) (POST /open-api/goods-recommend-retail-price/search)：Query product suggested retail price（查询商品建议零售价）
- [querySuggestedRetailPriceEntryRules](operations/querySuggestedRetailPriceEntryRules.json) (POST /open-api/goods/query-recommend-retail-price-rule)：Query suggested retail price entry rules（查询建议零售价填写规则）
- [querySuggestedRetailPriceReviewRecords](operations/querySuggestedRetailPriceReviewRecords.json) (POST /open-api/goods-recommend-retail-price-audit/search)：Query suggested retail price review records（查询建议零售价审核记录）
- [submitSuggestedRetailPrice](operations/submitSuggestedRetailPrice.json) (POST /open-api/goods-recommend-retail-price/batch-save)：Submit suggested retail price（提交建议零售价）
- [updateCostPrice](operations/updateCostPrice.json) (POST /open-api/goods/update-cost)：Update cost price（更新成本价）
