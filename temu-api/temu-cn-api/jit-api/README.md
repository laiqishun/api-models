# JIT API

Source groups: `JIT组`, `JIT组-PA`.

## 使用范围

全托 JIT 虚拟库存查询/编辑/规则签约仍在 CN；JIT 开通/关闭走 Partner。调用前按 operation 的 host/`x-temu-migration` 选择对应 token。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## API List

- [bg.glo.jitmode.activate](operations/bg.glo.jitmode.activate.json) - 开放平台JIT开通/关闭接口
- [bg.virtualinventoryjit.edit](operations/bg.virtualinventoryjit.edit.json) - 用于更新jit货品的库存
- [bg.virtualinventoryjit.get](operations/bg.virtualinventoryjit.get.json) - 用于jit货品的库存查询
- [bg.virtualinventoryjit.rule.get](operations/bg.virtualinventoryjit.rule.get.json) - jit预售规则查询接口
- [bg.virtualinventoryjit.rule.sign](operations/bg.virtualinventoryjit.rule.sign.json) - jit预售规则签约接口
