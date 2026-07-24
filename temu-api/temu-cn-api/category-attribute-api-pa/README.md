# Category Attribute PA API

Source group: `类目属性API组-PA`.

## 使用范围

Partner 网关类目必填项、运费模板与商品纠错查询（category requirements, freight template）。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## API List

- [bg.glo.goods.catsmandatory.get](operations/bg.glo.goods.catsmandatory.get.json) - 类目必填信息查询接口
- [bg.glo.logistics.template.get](operations/bg.glo.logistics.template.get.json) - 查询运费模版，用于半托管商品的API发布时关联运费模版ID
- [bg.goods.redress.correctrecord.query](operations/bg.goods.redress.correctrecord.query.json) - 提供给商家端，用于查询当前店铺的类目整改记录
- [bg.goods.redress.optionalcategory.correct](operations/bg.goods.redress.optionalcategory.correct.json) - 提供给商家端，用于主动选择商品的推荐类目
