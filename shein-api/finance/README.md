---
title: "SHEIN 财务 API"
description: "SHEIN official category 3000005, with one JSON model per named operation."
---

# API List

Official category: [财务 (3000005)](https://open.sheincorp.com/documents/apidoc/3000005). 6 records. Official IDs, applicable modes, and update times remain in the [manifest](../manifest.md) and each JSON file.

- [billingList](operations/billingList.json) (POST /open-api/finance/report-list)：Billing list（报账单列表）
- [debitAndReplenishmentDetailsOfBill](operations/debitAndReplenishmentDetailsOfBill.json) (POST /open-api/finance/report-adjustment-detail)：Debit and  replenishment details of the bill（报账单补扣款收支明细）
- [queryListOfInvoices](operations/queryListOfInvoices.json) (POST /open-api/finance/report-order-list)：Query the list of invoices（查询报账单列表）
- [queryStatementDetails](operations/queryStatementDetails.json) (GET /open-api/finance/get-check-order-detail)：Query statement details（查询对账单详情）
- [queryStatementList](operations/queryStatementList.json) (POST /open-api/finance/get-check-order-list)：Query statement list（查询对账单列表）
- [salesDetailsOfBill](operations/salesDetailsOfBill.json) (POST /open-api/finance/report-sales-detail)：Sales details of the bill（报账单销售款收支明细）
