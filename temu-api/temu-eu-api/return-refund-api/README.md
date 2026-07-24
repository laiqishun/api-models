# Return And Refund API

Source group: `8、Return and Rufund`.

## 使用范围

区域退货、退款、退货地址与售后处理（return, refund, aftersales）。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## API List

- [bg.aftersales.aftersales.list.get](operations/bg.aftersales.aftersales.list.get.json) - This interface is designed for use in an e-commerce platform, specifically for handling after-sales service requests related to product returns and refunds. The interface allows...
- [bg.aftersales.parentaftersales.list.get](operations/bg.aftersales.parentaftersales.list.get.json) - This interface is designed to provide real-time updates on the current after-sales status of an order within an e-commerce platform. It allows merchants and buyers to retrieve d...
- [bg.aftersales.parentreturnorder.get](operations/bg.aftersales.parentreturnorder.get.json) - This interface is designed to provide merchants or administrators within an e-commerce platform with detailed return logistics information for a set of after-sales service reque...
- [temu.aftersales.parentaftersales.detail.get](operations/temu.aftersales.parentaftersales.detail.get.json) - This interface is designed to provide detailed information on after-sales orders in real time
- [temu.aftersales.refund.issue](operations/temu.aftersales.refund.issue.json) - This interface is designed to enable merchants to efficiently process refund requests within the e-commerce platform.
- [temu.aftersales.returnaddress.get](operations/temu.aftersales.returnaddress.get.json) - temu.aftersales.returnaddress.get interface is designed to retrieve sensitive shipping address information for a specific return order.
- [temu.aftersales.returnlabel.prepare.get](operations/temu.aftersales.returnlabel.prepare.get.json) - This interface is designed to query return label preparation information.
- [temu.aftersales.signature.get](operations/temu.aftersales.signature.get.json) - This interface is designed to query signature information.
- [temu.aftersales.upload.returnlabel](operations/temu.aftersales.upload.returnlabel.json) - This interface is designed to upload return label.
