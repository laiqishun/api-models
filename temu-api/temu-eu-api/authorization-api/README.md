# Authorization API

Source group: `1、Authorization`.

## 使用范围

区域授权、token 创建与权限查询（authorization, token scope）。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## API List

- [bg.local.mall.info.get](operations/bg.local.mall.info.get.json) - Get the list of all stores associated with the same entity.
- [bg.open.accesstoken.info.get](operations/bg.open.accesstoken.info.get.json) - This interface allows merchants to view the API permissions associated with their currently authorized token, providing a list of authorized API endpoints.
- [temu.local.mall.tags.get](operations/temu.local.mall.tags.get.json) - This API allows sellers to retrieve the list of store tags currently assigned to their store.
