# Waybill And Box Label API

Source group: `运单标签&箱唛`.

## 使用范围

全托运单面单、箱唛与打印数据（waybill, box label）。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## API List

- [bg.logistics.boxmarkinfo.get](operations/bg.logistics.boxmarkinfo.get.json) - 更新OPEN API箱唛返回格式，新增发货状态和灰度key命中情況2个字段，用于控制不同的箱唛打印样式使用。
- [bg.shiporder.express.note.get](operations/bg.shiporder.express.note.get.json) - 物流运单标签获取
