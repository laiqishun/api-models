# Image Processing API

Source group: `图片处理API组`.

## 使用范围

商品图片上传、翻译、压缩与图像处理（image upload, translate, compress）。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## API List

- [bg.algo.dimension.image.check](operations/bg.algo.dimension.image.check.json) - 部分类目要求在商品轮播图必须上传尺寸图，尺寸图要求必须使用公制和英制单位，需要提供对应的尺寸图校验接口给外部商家
- [bg.algo.dimension.image.check.result](operations/bg.algo.dimension.image.check.result.json) - 部分类目要求在商品轮播图必须上传尺寸图，尺寸图要求必须使用公制和英制单位，需要提供对应的尺寸图校验接口给外部商家
- [bg.algo.image.translate](operations/bg.algo.image.translate.json) - ERP商家的搬品，需要翻译商品图片到对应的语言
- [bg.algo.image.translate.result](operations/bg.algo.image.translate.result.json) - erp商家搬品，需要提供商品图片翻译能力
- [bg.compliancepicture.get](operations/bg.compliancepicture.get.json) - 批量识别牛皮癣图片
- [bg.glo.colorimageurl.get](operations/bg.glo.colorimageurl.get.json) - 色块图获取
- [bg.glo.fancy.image.cm2in](operations/bg.glo.fancy.image.cm2in.json) - 接口可以把公制单位的图片，自动转换成英制单位的图片，适配销售国
- [bg.glo.picturecompression.get](operations/bg.glo.picturecompression.get.json) - 高清图片压缩处理
- [bg.goods.image.upload.global](operations/bg.goods.image.upload.global.json) - 图片上传接口
- [bg.goods.texttopicture.add.global](operations/bg.goods.texttopicture.add.global.json) - 文字转图片
