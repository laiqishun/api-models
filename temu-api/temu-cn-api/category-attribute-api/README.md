# Category Attribute API

Source groups: `类目属性API组`, `类目属性API组-PA`.

## 使用范围

中国跨境类目、属性、规格与整改相关能力。部分查询仍在 CN；类目必填项、运费模板与类目整改走 Partner。调用前按 operation 的 host/`x-temu-migration` 选择对应 token。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## API List

- [bg.glo.goods.catsmandatory.get](operations/bg.glo.goods.catsmandatory.get.json) - 类目必填信息查询接口
- [bg.glo.goods.photorecommendationcategory.get](operations/bg.glo.goods.photorecommendationcategory.get.json) - 外部商品图片映射temu类目
- [bg.glo.logistics.template.get](operations/bg.glo.logistics.template.get.json) - 查询运费模板，用于半托管发品API发布时填写运费模板ID
- [bg.goods.accessories.get](operations/bg.goods.accessories.get.json) - 发品时分页查询包装清单支持的配件信息
- [bg.goods.attribute.mapping](operations/bg.goods.attribute.mapping.json) - 内外属性映射
- [bg.goods.attrs.get](operations/bg.goods.attrs.get.json) - 用于查询发布时的类目属性模板
- [bg.goods.category.mapping](operations/bg.goods.category.mapping.json) - 查询中文类目映射接口
- [bg.goods.category.match](operations/bg.goods.category.match.json) - 对接方可以根据类目名称查找到适合的类目进行发品挂靠
- [bg.goods.cats.get](operations/bg.goods.cats.get.json) - 查询类目层级接口
- [bg.goods.parentspec.get](operations/bg.goods.parentspec.get.json) - 用于发品时查询父规格列表
- [bg.goods.redress.correctrecord.query](operations/bg.goods.redress.correctrecord.query.json) - 提供给商家端，用于查询当前店铺的类目整改记录
- [bg.goods.redress.optionalcategory.correct](operations/bg.goods.redress.optionalcategory.correct.json) - 提供给商家端，用于确认可选发品推荐类目
- [bg.goods.spec.create](operations/bg.goods.spec.create.json) - 用于货品发布时创建自定义规格
- [bg.vehicle.library.prop.dependency.query](operations/bg.vehicle.library.prop.dependency.query.json) - 商家填写车型库时查询模板信息
- [bg.vehicle.library.query](operations/bg.vehicle.library.query.json) - 商家发品时查询车型库模板
