# Product Edit API

Source groups: `编辑API组`, `编辑API组-PA`.

## 使用范围

中国跨境货品编辑能力。修改单申请仍在 CN；属性/图片/敏感属性/产地/运费模板等编辑走 Partner。调用前按 operation 的 host/`x-temu-migration` 选择对应 token。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## 选择规则

- 发起货品修改单：`bg.goods.edit.task.apply`（CN）
- 提交修改单、编辑属性/图片/敏感属性/产地、编辑运费模板：使用 `bg.glo.goods.*` / `bg.glo.goodslogistics.template.edit`（Partner）

## API List

- [bg.glo.goods.add.property](operations/bg.glo.goods.add.property.json) - 支持开平新增货品上的属性信息
- [bg.glo.goods.edit.pictures.submit](operations/bg.glo.goods.edit.pictures.submit.json) - 修改商品素材
- [bg.glo.goods.edit.property](operations/bg.glo.goods.edit.property.json) - 支持开平编辑货品上的属性信息
- [bg.glo.goods.edit.sensitive.attr](operations/bg.glo.goods.edit.sensitive.attr.json) - 商家编辑货品敏感品属性
- [bg.glo.goods.edit.task.submit](operations/bg.glo.goods.edit.task.submit.json) - 支持开平提交货品修改单，用于编辑货品信息
- [bg.glo.goods.update](operations/bg.glo.goods.update.json) - 这个接口作为后续的通用货品更新接口，用于“无编辑限制规则的字段”的更新编辑，本次只用于产地编辑
- [bg.glo.goodslogistics.template.edit](operations/bg.glo.goodslogistics.template.edit.json) - 编辑商品运费模板
- [bg.goods.edit.task.apply](operations/bg.goods.edit.task.apply.json) - 支持开平发起货品修改单用于编辑货品信息
