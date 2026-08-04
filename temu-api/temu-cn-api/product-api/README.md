# Product API

Source groups: `货品API组`, `货品API组-PA`.

## 使用范围

中国跨境货品能力。发品、详情、列表、搬运与爆款售罄走 Partner；品牌、清关校验、文件上传、建议供货价、生命周期查询仍在 CN。调用前按 operation 的 host/`x-temu-migration` 选择对应 token。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## 选择规则

- 发品、商品详情、SKC 列表、货品搬运、爆款售罄：使用 `bg.glo.goods.*`（Partner）
- 品牌、清关属性校验、货品文件上传、建议申报价、生命周期查询：使用仍在 CN 的 `bg.goods.*` / `bg.product.search`

## API List

- [bg.glo.goods.add](operations/bg.glo.goods.add.json) - 用于发布货品
- [bg.glo.goods.detail.get](operations/bg.glo.goods.detail.get.json) - 查询商品详情信息
- [bg.glo.goods.list.get](operations/bg.glo.goods.list.get.json) - 货品skc列表查询
- [bg.glo.goods.migrate](operations/bg.glo.goods.migrate.json) - 半托管店铺搬运同主体下全托管店铺的货品
- [bg.glo.goods.topselling.soldout.get](operations/bg.glo.goods.topselling.soldout.get.json) - 批量查询爆款售罄商品
- [bg.goods.brand.get](operations/bg.goods.brand.get.json) - 大卖家，对应货品发布的时候，设置自己品牌
- [bg.goods.customs.property.check](operations/bg.goods.customs.property.check.json) - 新增货品清关属性校验接口
- [bg.goods.file.upload](operations/bg.goods.file.upload.json) - 货品文件上传接口
- [bg.goods.suggest.supplyprice.get](operations/bg.goods.suggest.supplyprice.get.json) - 查询脱敏后建议申报参考价
- [bg.product.search](operations/bg.product.search.json) - 外部erp系统，查询货品生命周期状态
