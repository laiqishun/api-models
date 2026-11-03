---
title: AliExpress API Models
---

# AliExpress API Models

Official public catalog snapshot: **2026-11-03T03:36:17.754545+00:00**. **496 records across 36 categories**, representing **912 documented HTTP operations**. All detail records were retrieved and matched to the catalog by API name/path and methods. [Operation manifest](manifest.md) · [Complete catalog scope](catalog-manifest.md) · [Validation and known source conflicts](validation-report.md).

## Modules

- [系统工具](system-tools/README.md) — 4 APIs. 系统工具
- [AE-服务市场](service-market/README.md) — 4 APIs. AE-服务市场
- [AE-支付](payments/README.md) — 2 APIs. AE支付
- [AE-Logistics](logistics-services/README.md) — 16 APIs. 本对本物流API类目
- [AE-POP-商品](pop-products/README.md) — 83 APIs. AE-POP-商品
- [AE-全托管-商品](fully-managed-products/README.md) — 8 APIs. Aliexpress全托管店铺-商品管理
- [AE-半托管-商品](semi-managed-products/README.md) — 12 APIs. AE-半托管-商品相关API
- [AE-海外托管-商品](overseas-managed-products/README.md) — 16 APIs. AE-海外托管-商品API
- [AE-本地跨境-商品](local-cross-border-products/README.md) — 7 APIs. AE本地跨境(如韩国跨境店铺)商品接口
- [AE-交易](orders/README.md) — 21 APIs. AE-交易
- [AE-结算](settlements/README.md) — 12 APIs. AliExpress资金结算
- [AE-定制](customization/README.md) — 4 APIs. AE-定制
- [菜鸟国际出口](cainiao-export/README.md) — 25 APIs. 菜鸟国际出口相关业务的TOP接口
- [AE-供应链](supply-chain/README.md) — 76 APIs. 维护AE供应链相关API
- [AE-Dropshipper](dropshipping/README.md) — 16 APIs. AE Dropshipper专用接口
- [AE-税务](tax/README.md) — 1 APIs. AE-税务
- [AE-营销](marketing/README.md) — 10 APIs. AE-营销
- [AE-物流](logistics/README.md) — 29 APIs. AE-物流
- [AE-数据](analytics/README.md) — 6 APIs. AE-数据
- [AE-图片银行](image-bank/README.md) — 10 APIs. AE-图片银行
- [AE-商家](sellers/README.md) — 26 APIs. AE-商家
- [AE-评价](reviews/README.md) — 4 APIs. AE-评价
- [AE-类目](categories/README.md) — 11 APIs. AE-类目
- [AE-纠纷](disputes/README.md) — 5 APIs. AE-纠纷
- [AE-运费](shipping-fees/README.md) — 7 APIs. AE-运费
- [AE-会员](membership/README.md) — 5 APIs. AE-会员
- [AE-海外托管-发货](overseas-managed-fulfillment/README.md) — 9 APIs. 海外托管发货相关
- [AIDC供应链-业财](supply-chain-finance/README.md) — 1 APIs. 国际供应链-业财
- [AE金融商服](financial-services/README.md) — 1 APIs. AE金融商服
- [AE-商品任务](product-tasks/README.md) — 10 APIs. AE-商品任务
- [AE-EAN Code](ean-codes/README.md) — 1 APIs. AE-EAN Code
- [AI能力](ai-capabilities/README.md) — 26 APIs.  Aidge AI 能力开放
- [统一跨境商家工作台-商家](shared-workbench-sellers/README.md) — 1 APIs. 统一跨境商家工作台-商家
- [统一跨境商家工作台-类目](shared-workbench-categories/README.md) — 3 APIs. 统一跨境商家工作台-类目
- [统一跨境商家工作台-商品](shared-workbench-products/README.md) — 12 APIs. 统一跨境商家工作台-商品
- [统一跨境商家工作台-媒体中心](shared-workbench-media/README.md) — 12 APIs. 统一跨境商家工作台-媒体中心

## Source and interpretation

- [Official API reference](https://open.aliexpress.com/doc/api.htm) and its public category/detail responses are the source. The official SDK linked from each detail supplies readable request class names and confirms TOP `/sync?method=...` versus GOP `/rest/...` routing. [Overseas endpoint guide](https://developer.alibaba.com/docs/doc.htm?articleId=120689&docType=1&treeId=727).
- Each file represents one catalog record. A GET/POST record has two unique method operationIds in the same named file. Business request and response schemas are retained as definitions; they do not assert the complete HTTP envelope or serialization of complex parameters. All original field trees and constraints remain under `x-aliexpress-reference`. Source demo values are redacted; parseable response samples preserve structural shapes. SDK code sample values are omitted, with the official detail linked.
- POP, fully managed, semi-managed, overseas-managed and local cross-border product categories remain distinct. Shared merchant-workbench APIs, dropshipping, AI, supply-chain and system tools are included as shown in the public AliExpress catalog. Catalog inclusion is not evidence of a current app permission, seller authorization or live call.
- The catalog also exposes 32 MIRAVIA records in six categories. They are recorded as excluded in the scope manifest because MIRAVIA is a separate marketplace. The newer `openservice.aliexpress.com` entry was reachable, but its directory request timed out in this session; collection used the accessible official `open.aliexpress.com` reference. No claim is made that app-private interfaces are covered.
