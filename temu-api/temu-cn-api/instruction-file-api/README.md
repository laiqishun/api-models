# Instruction File API

Source groups: `说明书API组`, `说明书API组-PA`.

## 使用范围

货品说明书上传、语种、翻译与结果查询仍在 CN；说明书编辑走 Partner。调用前按 operation 的 host/`x-temu-migration` 选择对应 token。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## API List

- [bg.glo.goods.edit.guide.file](operations/bg.glo.goods.edit.guide.file.json) - 编辑货品说明书
- [bg.goods.instructions.upload](operations/bg.goods.instructions.upload.json) - 文件上传接口
- [bg.goods.instructionslanguages.get](operations/bg.goods.instructionslanguages.get.json) - 说明书语种查询信息
- [bg.goods.instructionstranslation.get](operations/bg.goods.instructionstranslation.get.json) - 说明书翻译接口
- [bg.goods.translationresult.get](operations/bg.goods.translationresult.get.json) - 查询说明书翻译结果
