# Size Chart API

Source groups: `尺码表API组`, `尺码表API组-PA`.

## 使用范围

尺码表创建、模板、元信息与图片识别仍在 CN；货品尺码表编辑走 Partner。调用前按 operation 的 host/`x-temu-migration` 选择对应 token。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## API List

- [bg.glo.goods.size.template.edit](operations/bg.glo.goods.size.template.edit.json) - 用于编辑货品尺码表
- [bg.goods.imagesizechart.get](operations/bg.goods.imagesizechart.get.json) - 图片提取尺码表
- [bg.goods.sizecharts.class.get](operations/bg.goods.sizecharts.class.get.json) - 用于查询尺码分组配置
- [bg.goods.sizecharts.create](operations/bg.goods.sizecharts.create.json) - 用于新增尺码表
- [bg.goods.sizecharts.get](operations/bg.goods.sizecharts.get.json) - 查询已创建的尺码表模板
- [bg.goods.sizecharts.meta.get](operations/bg.goods.sizecharts.meta.get.json) - 查询尺码表元信息
- [bg.goods.sizecharts.settings.get](operations/bg.goods.sizecharts.settings.get.json) - 查询尺码模板规则
- [bg.goods.sizecharts.template.create](operations/bg.goods.sizecharts.template.create.json) - 用于创建尺码表模板
