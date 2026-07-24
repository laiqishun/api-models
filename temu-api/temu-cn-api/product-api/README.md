# Product API

Source group: `货品API组`.

## 使用范围

仍在 CN 网关的商品补充查询与清关校验（product lookup, customs validation）。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## API List

- [bg.goods.brand.get](operations/bg.goods.brand.get.json) - 大卖家，对应货品发布的时候，设置自己品牌
- [bg.goods.customs.property.check](operations/bg.goods.customs.property.check.json) - 新增货品清关属性校验接口
- [bg.goods.file.upload](operations/bg.goods.file.upload.json) - 货品文件上传接口
- [bg.goods.suggest.supplyprice.get](operations/bg.goods.suggest.supplyprice.get.json) - 查询脱敏后建议申报参考价
- [bg.product.search](operations/bg.product.search.json) - 外部erp系统，查询货品生命周期状态
