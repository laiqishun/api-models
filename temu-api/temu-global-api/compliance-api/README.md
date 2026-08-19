# Compliance API

Source group: `Compliance`.

## 使用范围

商品合规规则、合规属性、合规标签、合规资料及认证证书（product compliance, certification, compliance label）。

Compliance（商品合规）目录主要用于处理商品在目标市场销售时涉及的合规规则、合规属性、合规标签、合规资料及认证证书等能力：通过规则类接口查询商品需要满足哪些合规要求，通过属性校验类接口检查商品填写的信息是否符合要求，通过 `bg.goods.compliancelabel.get` 查询商品对应的合规标签，通过合规信息接口查询/填写商品所需的合规信息，并通过证书相关接口查询需要上传的认证材料、查询商品已有证书以及上传商品合规证书。

简单来说，Compliance 目录解决的是“这个商品能不能合规销售、需要满足什么要求、需要提供什么资料以及当前有哪些合规标签”这一整套商品合规管理问题，而不是订单、库存或物流等业务。

本土店铺发品过程中的 `bg.local.goods.compliance.*` 仍在 [Product](../product-api/README.md)。本目录收录跨境/Global 网关的商品合规与证书接口。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## API List

- [bg.goods.compliancelabel.get](operations/bg.goods.compliancelabel.get.json) - page query goods compliance labels
- [bg.compliance.edit](operations/bg.compliance.edit.json) - edit compliance info
- [bg.compliance.metadata.get](operations/bg.compliance.metadata.get.json) - query compliance metadata
- [bg.arbok.open.product.cert.query](operations/bg.arbok.open.product.cert.query.json) - Some large stores with R&D capabilities, after using the Kaiping interface to upload qualifications in batches, need to query the reasons for the rejection of product qualifications in batches
- [bg.flash.open.upload.recognize](operations/bg.flash.open.upload.recognize.json) - For large merchants (10,000+ products), the cost of uploading pictures one by one is too high. We provide API and allow merchants to connect with their own ERP systems.
- [bg.flash.open.upload.real.image](operations/bg.flash.open.upload.real.image.json) - For large merchants (10,000+ products), the cost of uploading pictures one by one is too high. We provide API and allow merchants to connect with their own ERP systems.
- [bg.arbok.open.cert.uploadProductCert](operations/bg.arbok.open.cert.uploadProductCert.json) - External key customers have their own development capabilities and can call APIs to submit qualifications
- [bg.arbok.open.upload.uploadFile](operations/bg.arbok.open.upload.uploadFile.json) - Large external customers have their own development capabilities and can call APIs to upload files
- [bg.arbok.open.cert.queryNeedUploadItems](operations/bg.arbok.open.cert.queryNeedUploadItems.json) - External key customers have their own development capabilities and can call APIs to query the content to be uploaded
