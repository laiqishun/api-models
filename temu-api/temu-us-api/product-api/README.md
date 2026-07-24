# Product API

Source group: `1、Product`.

## 使用范围

区域本土商品发布、编辑、上下架、库存与合规（local product, listing, compliance）。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## API List

- [bg.freight.template.list.query](operations/bg.freight.template.list.query.json) - query freight template list by Temu seller, use for claim that goods logistics fee rules when listing items
- [bg.local.compliance.goods.list.query](operations/bg.local.compliance.goods.list.query.json) - Product management attribute list query
- [bg.local.goods.add](operations/bg.local.goods.add.json) - Add New Items On Temu
- [bg.local.goods.category.check](operations/bg.local.goods.category.check.json) - precheck category misplacement
- [bg.local.goods.category.recommend](operations/bg.local.goods.category.recommend.json) - query recommended category by product name
- [bg.local.goods.cats.get](operations/bg.local.goods.cats.get.json) - Get Temu Categories
- [bg.local.goods.compliance.edit](operations/bg.local.goods.compliance.edit.json) - Edit product qualification information
- [bg.local.goods.compliance.extra.template.get](operations/bg.local.goods.compliance.extra.template.get.json) - Inquire Required Compliance Information
- [bg.local.goods.compliance.property.check](operations/bg.local.goods.compliance.property.check.json) - Verify Product Attribute Settings
- [bg.local.goods.compliance.rules.get](operations/bg.local.goods.compliance.rules.get.json) - Query Mandatory Qualification Information
- [bg.local.goods.detail.query](operations/bg.local.goods.detail.query.json) - Query local goods detail
- [bg.local.goods.gallery.signature.get](operations/bg.local.goods.gallery.signature.get.json) - Get gallery Signature
- [bg.local.goods.image.upload](operations/bg.local.goods.image.upload.json) - Image material processing
- [bg.local.goods.list.query](operations/bg.local.goods.list.query.json) - Get product list
- [bg.local.goods.out.sn.check](operations/bg.local.goods.out.sn.check.json) - Check if contribution ID for goods is repeated
- [bg.local.goods.out.sn.set](operations/bg.local.goods.out.sn.set.json) - Set contribution ID for goods
- [bg.local.goods.partial.update](operations/bg.local.goods.partial.update.json) - Edit a subset of the product properties (e.g. description, brand, images, attributes).
- [bg.local.goods.property.get](operations/bg.local.goods.property.get.json) - Get Temu goods attributes
- [bg.local.goods.property.relations](operations/bg.local.goods.property.relations.json) - Query the relational database data associated with goods, such as vehicle library.
- [bg.local.goods.property.relations.level.template](operations/bg.local.goods.property.relations.level.template.json) - Obtaining the hierarchical attribute value and hierarchical id of vehicle type library data.
- [bg.local.goods.property.relations.template](operations/bg.local.goods.property.relations.template.json) - Query the full quantum attribute by the dependency id of the parent attribute value and the hierarchical id.
- [bg.local.goods.publish.status.get](operations/bg.local.goods.publish.status.get.json) - Batch Query Product Publication Status
- [bg.local.goods.sale.status.set](operations/bg.local.goods.sale.status.set.json) - Support goods/SKU dimension for listing and delisting operations
- [bg.local.goods.size.element.get](operations/bg.local.goods.size.element.get.json) - Query Size Chart Element Information
- [bg.local.goods.sku.list.query](operations/bg.local.goods.sku.list.query.json) - Get sku list, as well as get Variants
- [bg.local.goods.sku.out.sn.check](operations/bg.local.goods.sku.out.sn.check.json) - Check if contribution ID for SKU is duplicate
- [bg.local.goods.sku.out.sn.set](operations/bg.local.goods.sku.out.sn.set.json) - Set contribution ID for SKU
- [bg.local.goods.spec.id.get](operations/bg.local.goods.spec.id.get.json) - Search And Generate Merchant-Customized Specifications
- [bg.local.goods.stock.edit](operations/bg.local.goods.stock.edit.json) - Edit product stock with full-update and diff-update
- [bg.local.goods.tax.code.get](operations/bg.local.goods.tax.code.get.json) - local-local goods B
- [bg.local.goods.template.get](operations/bg.local.goods.template.get.json) - query product attributes template
- [bg.local.goods.update](operations/bg.local.goods.update.json) - Edit all properties (e.g. description, brand, images, attributes) of a product.
- [bg.local.goods.videocoverimage.get](operations/bg.local.goods.videocoverimage.get.json) - Used to obtain the cover image of the video screen
- [temu.local.goods.baseprice.recommend](operations/temu.local.goods.baseprice.recommend.json) - recommend baseprice
- [temu.local.goods.brand.trademark.V2.get](operations/temu.local.goods.brand.trademark.V2.get.json) - Query trademarks and properties
- [temu.local.goods.delete](operations/temu.local.goods.delete.json) - Product deletion
- [temu.local.goods.illegal.vocabulary.check](operations/temu.local.goods.illegal.vocabulary.check.json) - check illegal vocabulary
- [temu.local.goods.list.retrieve](operations/temu.local.goods.list.retrieve.json) - local goods list search
- [temu.local.goods.sku.net.content.unit.query](operations/temu.local.goods.sku.net.content.unit.query.json) - Query multi-language information of sku transfer type net content unit
- [temu.local.goods.spec.info.get](operations/temu.local.goods.spec.info.get.json) - Used to query the specification value information in different languages corresponding to the platform's specification ID
- [temu.local.sku.list.retrieve](operations/temu.local.sku.list.retrieve.json) - local sku list search
