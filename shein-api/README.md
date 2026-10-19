---
title: "SHEIN Open Platform API Models"
description: "Public SHEIN API and Webhook reference organized by official category and record."
---

# SHEIN Open Platform

Snapshot: **2026-10-15 18:50 CST**. The official public catalog had **232 API records in 20 categories** and **24 Webhook records in 1 category**. Each catalog ID maps to one JSON model and one [manifest](./manifest.md) row. Module directories use business names, and each operation JSON filename matches its semantic `operationId`, based on the official English interface title when available; official numeric IDs remain in the manifest and JSON metadata. These models are derived from SHEIN's public reference responses; SHEIN did not publish these files as Swagger.

## Before using an operation

- Each operation records the applicable seller cooperation modes shown on its official detail page. A category or mode label is not proof that a specific ISV app has subscribed to, been approved for, or can call that operation.
- SHEIN uses separate applications for seller cooperation modes. Select the relevant application, authorization, permissions, signing method, and production domain using the official [Developer Guide](https://open.sheincorp.com/documents/system/dad0d1c7-be76-4b03-a735-4e23f012bdd9) and [Signature Rules](https://open.sheincorp.com/documents/system/passwdrule). The `get-by-token` authorization call signs with app credentials before seller keys are available.
- Webhook JSON files describe **inbound events**, not callable SHEIN API endpoints. Their `x-shein-decrypted-event-payload-schema` describes the decrypted business message. The actual callback uses encrypted `eventData`; use the official [Webhook Instruction](https://open.sheincorp.com/documents/system/3b13b1c5-525a-4758-a2b1-056bde083e2c) for transport, verification, decryption, and acknowledgment.
- Operation examples are retained as redacted JSON shapes where parseable. Exact sample values, including credentials and possible seller/customer data, are omitted. Official field trees, per-path error tables, and available update logs remain in `x-shein-*` extensions; source field `multiple=1` is mapped to an array. GET request bodies and complex header/query nodes are retained in extensions when their transport cannot be represented without guessing. `source-revision-*` is the portal record revision, not a semantic API version.

## Official modules

| Kind | Category | Official ID | Records | Open |
|---|---|---:|---:|---|
| API | 密钥 | 1000012 | 1 | [Module](./credentials/README.md) |
| API | 商品 | 1000001 | 40 | [Module](./product/README.md) |
| API | 价格 | 3000013 | 10 | [Module](./price/README.md) |
| API | 合规 | 3000008 | 18 | [Module](./compliance/README.md) |
| API | Feed | 3000003 | 6 | [Module](./feed/README.md) |
| API | 客单 | 2000001 | 17 | [Module](./order/README.md) |
| API | 退货退款 | 2000004 | 3 | [Module](./return-refund/README.md) |
| API | 采购单 | 1000002 | 20 | [Module](./purchase-order/README.md) |
| API | 采购单退货 | 3000011 | 13 | [Module](./purchase-order-return/README.md) |
| API | 库存和销量 | 1000003 | 6 | [Module](./inventory-sales/README.md) |
| API | 营销活动报名 | 3000009 | 6 | [Module](./campaign-registration/README.md) |
| API | 财务 | 3000005 | 6 | [Module](./finance/README.md) |
| API | 店铺 | 3000007 | 3 | [Module](./shop/README.md) |
| API | 定制商品 | 3000010 | 5 | [Module](./custom-product/README.md) |
| API | 认证仓 | 3000001 | 4 | [Module](./certified-warehouse/README.md) |
| API | 物流 | 1000006 | 11 | [Module](./logistics/README.md) |
| API | MES | 1000015 | 25 | [Module](./mes/README.md) |
| API | 排产 | 3000012 | 10 | [Module](./production-scheduling/README.md) |
| API | 面料 | 1000005 | 6 | [Module](./fabric/README.md) |
| API | MDP印染 | 3000002 | 22 | [Module](./mdp-printing/README.md) |
| Webhook | Webhook | 2000003 | 24 | [Module](./webhook/README.md) |

## Source and validation boundary

The [official API directory](https://open.sheincorp.com/documents/apidoc/1000001) and [Webhook directory](https://open.sheincorp.com/documents/msgdoc/2000003) were read through their public directory/detail data endpoints. The global directory matched each of the 21 category listings by official ID. All 256 detail records matched their catalog ID, method, path/event, and category. All 256 per-path error tables and update-log queries were retrieved, including paginated tables: 58 operations have listed errors and 47 have update logs (74 log rows). The 256 source records contain 8,053 request/response field-tree nodes. The model files are a structural conversion with source trees and redacted examples, not proof of seller authorization, approved app permissions, test-environment success, or production calls.
