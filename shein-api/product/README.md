---
title: "SHEIN 商品 API"
description: "SHEIN official category 1000001, with one JSON model per named operation."
---

# API List

Official category: [商品 (1000001)](https://open.sheincorp.com/documents/apidoc/1000001). 40 records. Official IDs, applicable modes, and update times remain in the [manifest](../manifest.md) and each JSON file.

- [addCustomAttributeValues](operations/addCustomAttributeValues.json) (POST /open-api/goods/add-custom-attribute-value)：Add custom attribute values（添加自定义属性值）
- [checkCertificateRequirementsAndStatus](operations/checkCertificateRequirementsAndStatus.json) (POST /open-api/goods/get-certificate-rule)：Check product certificate requirements and verification status（查询商品证书要求和审核状态）
- [checkProductAuditStatus](operations/checkProductAuditStatus.json) (POST /open-api/goods/query-document-state)：Check product audit status（查询商品审核状态）
- [commodityObtainSkcAndSizeInBatchesAccordingToBarcode](operations/commodityObtainSkcAndSizeInBatchesAccordingToBarcode.json) (POST /open-api/goods/batch-skc-size)：Commodity interface - obtain SKC and size in batches according to the barcode（商品接口-根据条码批量获取SKC与尺码）
- [comprehensiveProductQuery](operations/comprehensiveProductQuery.json) (POST /open-api/goods/searchProduct)：Comprehensive product query（商品综合查询）
- [confirmWhetherProductIsEditable](operations/confirmWhetherProductIsEditable.json) (POST /open-api/goods/product/check-edit-permission)：Confirm whether the product is editable（确认商品是否可编辑）
- [confirmWhetherStoreCanPublishProducts](operations/confirmWhetherStoreCanPublishProducts.json) (GET /open-api/goods/product/check-publish-permission)：Confirm whether the store can publish products（确认店铺是否可发品）
- [convertImageLink](operations/convertImageLink.json) (POST /open-api/goods/transform-pic)：Convert image link（图片链接转换）
- [createOrEditProductCertificatePool](operations/createOrEditProductCertificatePool.json) (POST /open-api/goods/save-or-update-certificate-pool)：Create/edit product certificate pool（商品证书池创建/编辑）
- [createOrEditShopCertificatePool](operations/createOrEditShopCertificatePool.json) (POST /open-api/goods/save-or-update-supplier-certificate)：Create/edit shop certificate pool（店铺证书池创建/编辑）
- [createProductVideoConversionTask](operations/createProductVideoConversionTask.json) (POST /open-api/goods/product/create-video-transform-task)：Create product video conversion task（创建商品视频转换任务）
- [documentsRequiredToQueryCertificateNew](operations/documentsRequiredToQueryCertificateNew.json) (POST /open-api/goods/certificate/get-all-certificate-type-list-v2)：Documents required to query the certificate (New)（查询证书所需上传资料（新））
- [getFinalCategory](operations/getFinalCategory.json) (POST /open-api/goods/query-category-tree)：Get the final category（店铺查商品末级分类）
- [getVideoConversionResult](operations/getVideoConversionResult.json) (POST /open-api/goods/product/query-video-transform-task)：Get video conversion result（获取视频转换结果）
- [imageAndTextRecognitionRecommendedCategory](operations/imageAndTextRecognitionRecommendedCategory.json) (POST /open-api/goods/image-category-suggestion)：Image and text recognition recommended category（图文识别推荐类目）
- [localImageUpload](operations/localImageUpload.json) (POST /open-api/goods/upload-pic)：Local Image Upload（本地图片上传）
- [obtainStoreListingQuota](operations/obtainStoreListingQuota.json) (POST /open-api/goods/query-shelf-quota)：Obtain store listing quota（获取店铺上架额度）
- [partialProductEditing](operations/partialProductEditing.json) (POST /open-api/goods/product/partialEdit)：Partial product editing（商品部分编辑）
- [productDeletionPreValidation](operations/productDeletionPreValidation.json) (POST /open-api/goods/check-deletable)：Product deletion pre-validation（商品删除预校验）
- [productList](operations/productList.json) (POST /open-api/openapi-business-backend/product/query)：Product list API（商品列表接口）
- [productListedAndProductPendingListed](operations/productListedAndProductPendingListed.json) (POST /open-api/goods/modify-skc-shelf)：Product listed and product pending listed（商品上下架）
- [productListingFieldSpecifications](operations/productListingFieldSpecifications.json) (POST /open-api/goods/query-publish-fill-in-standard)：Product listing field specifications（商品发布字段规范）
- [publishOrEditProduct](operations/publishOrEditProduct.json) (POST /open-api/goods/product/publishOrEdit)：Product publish or Edit（商品发布/编辑）
- [queryAssociatedAttributeFillingRules](operations/queryAssociatedAttributeFillingRules.json) (POST /open-api/goods/get-associated-attribute-rules)：Query associated attribute filling rules（查询关联属性填写规则）
- [queryAvailableBrandList](operations/queryAvailableBrandList.json) (POST /open-api/goods/query-brand-list)：Query available brand list（查询可用品牌列表）
- [queryAvailableCategoryAttributes](operations/queryAvailableCategoryAttributes.json) (POST /open-api/goods/query-attribute-template)：Query available category attributes（查询分类可用属性）
- [queryAvailableIpList](operations/queryAvailableIpList.json) (POST /open-api/goods/query-ip-list)：Query available IP list（查询可用IP列表）
- [queryMerchantPublishingQuota](operations/queryMerchantPublishingQuota.json) (POST /open-api/goods-publish-quotas/detail)：Query merchant publishing quota（查询商家发品额度）
- [queryProductDeletionReviewRecords](operations/queryProductDeletionReviewRecords.json) (POST /open-api/goods-delete-logs/search)：Query product deletion review records（查询商品删除审核记录）
- [querySkcSkuDesignModelRelations](operations/querySkcSkuDesignModelRelations.json) (GET /open-api/goods/number-list)：Commodity interface - full query SKC/SKU/design model number relationship list（商品接口-全量查询SKC/SKU/设计款号关系列表）
- [queryStoreSiteAndCurrencyInformationNew](operations/queryStoreSiteAndCurrencyInformationNew.json) (POST /open-api/goods/query-site-list)：Query store site and currency information (new)（查询店铺站点和币种信息（新））
- [queryStoreSiteAndSiteCurrenciesOld](operations/queryStoreSiteAndSiteCurrenciesOld.json) (POST /open-api/openapi-business-backend/site/query)：Query store site and site currencies (old)（查询店铺站点和站点币种（旧））
- [queryWhetherCustomAttributeValuesAreSupported](operations/queryWhetherCustomAttributeValuesAreSupported.json) (POST /open-api/goods/get-custom-attribute-permission-config)：Query whether custom attribute values are supported（查询是否支持自定义属性值）
- [queryWhetherMerchantSkuAlreadyExists](operations/queryWhetherMerchantSkuAlreadyExists.json) (POST /open-api/goods/product/check-supplierSku-repeated)：Query whether the merchant sku already exists（查询商家sku是否已存在）
- [skcBindProductCertificatePool](operations/skcBindProductCertificatePool.json) (POST /open-api/goods/save-certificate-pool-skc-bind)：SKC bind product certificate pool（SKC绑定商品证书池）
- [skuItemDetailsQuery](operations/skuItemDetailsQuery.json) (POST /open-api/openapi-business-backend/product/full-detail)：sku item details query (to be deprecated soon)（sku商品详情查询（即将作废））
- [spuProductDetailsQuery](operations/spuProductDetailsQuery.json) (POST /open-api/goods/spu-info)：SPU product details query（spu商品详情查询）
- [submitProductDeletionRequest](operations/submitProductDeletionRequest.json) (DELETE /open-api/goods/delete/{skcName})：Submit product deletion request（提交商品删除申请）
- [uploadCertificateFile](operations/uploadCertificateFile.json) (POST /open-api/goods/upload-certificate-file)：Upload certificate file（上传证书文件）
- [withdrawProductReview](operations/withdrawProductReview.json) (POST /open-api/goods/revoke-product)：Withdraw product review（撤回商品审核）
