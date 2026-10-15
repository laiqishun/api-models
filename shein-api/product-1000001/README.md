# 商品 (1000001)

Official API category: [SHEIN developer reference](https://open.sheincorp.com/documents/apidoc/1000001).

40 records in the 2026-10-15 18:50 CST public catalog snapshot. Mode labels are copied per operation from official details; actual application access requires subscription and approval.

| Method | Name | Path / event | Official ID | Modes | Updated | Model |
|---|---|---|---:|---|---|---|
| POST | 商品发布/编辑 | `/open-api/goods/product/publishOrEdit` | 3002018 | 自运营, 全托管, 半托管 | 2026-09-02 10:14:04 | [JSON](./operations/3002018.json) |
| POST | 商品部分编辑 | `/open-api/goods/product/partialEdit` | 3002047 | 自运营, 全托管, 半托管 | 2026-10-09 19:39:27 | [JSON](./operations/3002047.json) |
| GET | 确认店铺是否可发品 | `/open-api/goods/product/check-publish-permission` | 3001589 | 自运营, 全托管, 半托管 | 2026-02-06 18:06:06 | [JSON](./operations/3001589.json) |
| POST | 确认商品是否可编辑 | `/open-api/goods/product/check-edit-permission` | 3001380 | 自运营, 全托管, 半托管 | 2025-08-28 14:46:52 | [JSON](./operations/3001380.json) |
| POST | 查询商品审核状态 | `/open-api/goods/query-document-state` | 3001368 | 自运营, 全托管, 半托管, POP | 2025-08-15 14:49:04 | [JSON](./operations/3001368.json) |
| POST | 撤回商品审核 | `/open-api/goods/revoke-product` | 3001896 | 自运营, 全托管, 半托管 | 2026-07-02 21:00:01 | [JSON](./operations/3001896.json) |
| POST | 商品综合查询 | `/open-api/goods/searchProduct` | 3001938 | 自运营, 全托管, 半托管, POP | 2026-08-03 10:41:33 | [JSON](./operations/3001938.json) |
| POST | 商品列表接口 | `/open-api/openapi-business-backend/product/query` | 3001239 | 自运营, 全托管, 半托管, POP | 2025-07-17 11:56:50 | [JSON](./operations/3001239.json) |
| POST | 商品上下架 | `/open-api/goods/modify-skc-shelf` | 3001939 | 自运营, 半托管, POP | 2026-08-03 11:02:08 | [JSON](./operations/3001939.json) |
| POST | spu商品详情查询 | `/open-api/goods/spu-info` | 3002017 | 自运营, 全托管, 半托管, POP | 2026-09-02 10:12:51 | [JSON](./operations/3002017.json) |
| POST | sku商品详情查询（即将作废） | `/open-api/openapi-business-backend/product/full-detail` | 3001085 | 自运营, 全托管, 半托管, POP | 2025-05-06 16:08:52 | [JSON](./operations/3001085.json) |
| POST | 商品发布字段规范 | `/open-api/goods/query-publish-fill-in-standard` | 3002044 | 自运营, 全托管, 半托管 | 2026-09-24 11:47:20 | [JSON](./operations/3002044.json) |
| POST | 店铺查商品末级分类 | `/open-api/goods/query-category-tree` | 3001594 | 自运营, 全托管, 半托管, POP | 2026-02-20 11:00:30 | [JSON](./operations/3001594.json) |
| POST | 图文识别推荐类目 | `/open-api/goods/image-category-suggestion` | 3001363 | 自运营, 全托管, 半托管 | 2025-08-12 17:29:45 | [JSON](./operations/3001363.json) |
| POST | 查询分类可用属性 | `/open-api/goods/query-attribute-template` | 3002046 | 自运营, 全托管, 半托管 | 2026-10-09 11:18:49 | [JSON](./operations/3002046.json) |
| POST | 查询是否支持自定义属性值 | `/open-api/goods/get-custom-attribute-permission-config` | 3001369 | 自运营, 全托管, SHEIN自营, 半托管 | 2025-08-15 14:57:20 | [JSON](./operations/3001369.json) |
| POST | 添加自定义属性值 | `/open-api/goods/add-custom-attribute-value` | 3001483 | Not listed | 2025-12-18 10:31:29 | [JSON](./operations/3001483.json) |
| POST | 查询关联属性填写规则 | `/open-api/goods/get-associated-attribute-rules` | 3001680 | 自运营, 全托管, 半托管 | 2026-04-21 17:39:13 | [JSON](./operations/3001680.json) |
| POST | 查询店铺站点和币种信息（新） | `/open-api/goods/query-site-list` | 3001249 | 自运营, 全托管, 半托管, POP | 2025-07-17 14:45:31 | [JSON](./operations/3001249.json) |
| POST | 查询店铺站点和站点币种（旧） | `/open-api/openapi-business-backend/site/query` | 3001254 | 自运营, 全托管, 半托管, POP | 2025-07-17 14:54:50 | [JSON](./operations/3001254.json) |
| POST | 查询可用品牌列表 | `/open-api/goods/query-brand-list` | 3001900 | 自运营, 全托管, 半托管 | 2026-07-02 21:01:07 | [JSON](./operations/3001900.json) |
| POST | 查询可用IP列表 | `/open-api/goods/query-ip-list` | 3001901 | 自运营, 全托管, 半托管 | 2026-07-02 21:01:10 | [JSON](./operations/3001901.json) |
| POST | 图片链接转换 | `/open-api/goods/transform-pic` | 3001360 | 自运营, 全托管, 半托管 | 2025-08-12 11:32:52 | [JSON](./operations/3001360.json) |
| POST | 本地图片上传 | `/open-api/goods/upload-pic` | 3001359 | 自运营, 全托管, 半托管 | 2025-08-12 11:32:25 | [JSON](./operations/3001359.json) |
| POST | 创建商品视频转换任务 | `/open-api/goods/product/create-video-transform-task` | 3002020 | 自运营, 全托管, 半托管 | 2026-09-02 10:21:29 | [JSON](./operations/3002020.json) |
| POST | 获取视频转换结果 | `/open-api/goods/product/query-video-transform-task` | 3002021 | 自运营, 全托管, 半托管 | 2026-09-02 10:21:45 | [JSON](./operations/3002021.json) |
| POST | 查询商家发品额度 | `/open-api/goods-publish-quotas/detail` | 3002025 | 自运营, 全托管, 半托管 | 2026-09-04 10:21:42 | [JSON](./operations/3002025.json) |
| POST | 获取店铺上架额度 | `/open-api/goods/query-shelf-quota` | 3001931 | 自运营, 半托管, POP | 2026-07-23 11:04:59 | [JSON](./operations/3001931.json) |
| POST | 查询商家sku是否已存在 | `/open-api/goods/product/check-supplierSku-repeated` | 3001437 | 自运营, 全托管, 半托管 | 2025-10-22 20:45:14 | [JSON](./operations/3001437.json) |
| POST | 商品删除预校验 | `/open-api/goods/check-deletable` | 3001904 | 自运营, 全托管, 半托管 | 2026-07-03 13:41:11 | [JSON](./operations/3001904.json) |
| DELETE | 提交商品删除申请 | `/open-api/goods/delete/{skcName}` | 3001905 | Not listed | 2026-07-03 13:41:20 | [JSON](./operations/3001905.json) |
| POST | 查询商品删除审核记录 | `/open-api/goods-delete-logs/search` | 3001906 | 自运营, 全托管, 半托管 | 2026-07-03 13:41:30 | [JSON](./operations/3001906.json) |
| POST | 查询商品证书要求和审核状态 | `/open-api/goods/get-certificate-rule` | 3001859 | 自运营, 全托管, 半托管, POP | 2026-06-29 19:52:41 | [JSON](./operations/3001859.json) |
| POST | 查询证书所需上传资料（新） | `/open-api/goods/certificate/get-all-certificate-type-list-v2` | 3001860 | 自运营, 全托管, 半托管, POP | 2026-06-29 19:52:48 | [JSON](./operations/3001860.json) |
| POST | 上传证书文件 | `/open-api/goods/upload-certificate-file` | 3001861 | 自运营, 全托管, 半托管, POP | 2026-06-29 19:52:53 | [JSON](./operations/3001861.json) |
| POST | 商品证书池创建/编辑 | `/open-api/goods/save-or-update-certificate-pool` | 3001862 | 自运营, 全托管, 半托管, POP | 2026-06-29 19:52:58 | [JSON](./operations/3001862.json) |
| POST | 店铺证书池创建/编辑 | `/open-api/goods/save-or-update-supplier-certificate` | 3001863 | 自运营, 全托管, 半托管, POP | 2026-06-29 19:53:39 | [JSON](./operations/3001863.json) |
| POST | SKC绑定商品证书池 | `/open-api/goods/save-certificate-pool-skc-bind` | 3001864 | 自运营, 全托管, 半托管, POP | 2026-06-29 19:53:44 | [JSON](./operations/3001864.json) |
| POST | 商品接口-根据条码批量获取SKC与尺码 | `/open-api/goods/batch-skc-size` | 3001485 | 全托管, SHEIN自营 | 2025-12-18 10:31:55 | [JSON](./operations/3001485.json) |
| GET | 商品接口-全量查询SKC/SKU/设计款号关系列表 | `/open-api/goods/number-list` | 3001486 | 全托管, SHEIN自营 | 2025-12-18 10:32:02 | [JSON](./operations/3001486.json) |
