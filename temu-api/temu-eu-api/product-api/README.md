# Product API

Source group: `2、Product`.

## 使用范围

区域本土商品发布、编辑、上下架、库存与合规（local product, listing, compliance）。

先按上级区域 README 确定店铺模式和网关，再从下方列表选择唯一 operation。

## API List

- [bg.freight.template.list.query](operations/bg.freight.template.list.query.json) - Query Freight Template List
- [bg.local.compliance.goods.list.query](operations/bg.local.compliance.goods.list.query.json) - Product management attribute list query
- [bg.local.goods.add](operations/bg.local.goods.add.json) - Add New Items On Temu
- [bg.local.goods.category.check](operations/bg.local.goods.category.check.json) - precheck category misplacement
- [bg.local.goods.category.recommend](operations/bg.local.goods.category.recommend.json) - query recommended category by product name
- [bg.local.goods.cats.get](operations/bg.local.goods.cats.get.json) - Get Temu Categories
- [bg.local.goods.compliance.edit](operations/bg.local.goods.compliance.edit.json) - Edit product qualification information
- [bg.local.goods.compliance.extra.template.get](operations/bg.local.goods.compliance.extra.template.get.json) - Inquire Required Compliance Information
- [bg.local.goods.compliance.info.fill.list.query](operations/bg.local.goods.compliance.info.fill.list.query.json) - local-local goods B
- [bg.local.goods.compliance.property.check](operations/bg.local.goods.compliance.property.check.json) - Verify Product Attribute Settings
- [bg.local.goods.compliance.rules.get](operations/bg.local.goods.compliance.rules.get.json) - Query Mandatory Qualification Information
- [bg.local.goods.detail.query](operations/bg.local.goods.detail.query.json) - Query local goods detail
- [bg.local.goods.gallery.signature.get](operations/bg.local.goods.gallery.signature.get.json) - Get gallery Signature
- [bg.local.goods.image.upload](operations/bg.local.goods.image.upload.json) - Image material processing
- [bg.local.goods.list.query](operations/bg.local.goods.list.query.json) - Get product list
- [bg.local.goods.multi.site.submit](operations/bg.local.goods.multi.site.submit.json) - Sell in other marketplaces
- [bg.local.goods.out.sn.check](operations/bg.local.goods.out.sn.check.json) - Batch check whether the product codes are duplicated
- [bg.local.goods.out.sn.set](operations/bg.local.goods.out.sn.set.json) - Product external coding Settings
- [bg.local.goods.partial.update](operations/bg.local.goods.partial.update.json) - Edit a subset of the product properties (e.g. description, brand, images, attributes).
- [bg.local.goods.property.get](operations/bg.local.goods.property.get.json) - Get Temu goods attributes
- [bg.local.goods.sale.status.set](operations/bg.local.goods.sale.status.set.json) - Support goods/SKU dimension for listing and delisting operations
- [bg.local.goods.size.element.get](operations/bg.local.goods.size.element.get.json) - Query Size Chart Element Information
- [bg.local.goods.sku.list.query](operations/bg.local.goods.sku.list.query.json) - Get sku list, as well as get Variants
- [bg.local.goods.sku.out.sn.check](operations/bg.local.goods.sku.out.sn.check.json) - Verify whether the sku code is duplicated
- [bg.local.goods.sku.out.sn.set](operations/bg.local.goods.sku.out.sn.set.json) - sku external encoding Settings
- [bg.local.goods.spec.id.get](operations/bg.local.goods.spec.id.get.json) - Search And Generate Merchant-Customized Specifications
- [bg.local.goods.stock.edit](operations/bg.local.goods.stock.edit.json) - Edit product stock with full-update and diff-update
- [bg.local.goods.tax.code.get](operations/bg.local.goods.tax.code.get.json) - Obtain the tax code information corresponding to the product
- [bg.local.goods.template.get](operations/bg.local.goods.template.get.json) - query product attributes template
- [bg.local.goods.update](operations/bg.local.goods.update.json) - Edit all properties (e.g. description, brand, images, attributes) of a product.
- [bg.local.goods.videocoverimage.get](operations/bg.local.goods.videocoverimage.get.json) - Used to obtain the cover image of the video screen
- [temu.local.goods.baseprice.recommend](operations/temu.local.goods.baseprice.recommend.json) - recommend baseprice
- [temu.local.goods.brand.trademark.V2.get](operations/temu.local.goods.brand.trademark.V2.get.json) - Query trademarks and properties
- [temu.local.goods.delete](operations/temu.local.goods.delete.json) - Product deletion
- [temu.local.goods.illegal.vocabulary.check](operations/temu.local.goods.illegal.vocabulary.check.json) - check illegal vocabulary
- [temu.local.goods.list.retrieve](operations/temu.local.goods.list.retrieve.json) - local goods list search
- [temu.local.goods.pre.sale.status.edit](operations/temu.local.goods.pre.sale.status.edit.json) - This API allows batch enabling or disabling the pre-sale status for multiple SKUs belonging to a product item.
- [temu.local.goods.sku.net.content.unit.query](operations/temu.local.goods.sku.net.content.unit.query.json) - Query multi-language information of sku transfer type net content unit
- [temu.local.sku.list.retrieve](operations/temu.local.sku.list.retrieve.json) - local sku list search
- [temu.olaf.auth.rep.create](operations/temu.olaf.auth.rep.create.json) - Local ERP Agent Information Creation
- [temu.olaf.auth.rep.upload](operations/temu.olaf.auth.rep.upload.json) - Local ERP Agent File Upload
