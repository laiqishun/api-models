# Authorization API

Source groups: `基础API组`, `基础API组-PA`.

## 使用范围

CN 与 Partner 授权查询入口。按 token 所属网关选择对应 operation，不要混用 CN token 与 PA type。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## 选择规则

- 查当前 CN token 对应店铺类型（是否半托/二手店）：`bg.mall.info.get`（CN 网关）
- 查当前 PA token 的 `mallId`、过期时间与 API 权限列表：`bg.open.accesstoken.info.get.global`（Partner 网关）

## API List

- [bg.mall.info.get](operations/bg.mall.info.get.json) - 查询当前token对应店铺类型信息
- [bg.open.accesstoken.info.get.global](operations/bg.open.accesstoken.info.get.global.json) - 按token查询授权信息接口
