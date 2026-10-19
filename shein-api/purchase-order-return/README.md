---
title: "SHEIN 采购单退货 API"
description: "SHEIN official category 3000011, with one JSON model per named operation."
---

# API List

Official category: [采购单退货 (3000011)](https://open.sheincorp.com/documents/apidoc/3000011). 13 records. Official IDs, applicable modes, and update times remain in the [manifest](../manifest.md) and each JSON file.

- [checkAvailableLogisticsOptionsForReturns](operations/checkAvailableLogisticsOptionsForReturns.json) (POST /open-api/purchase/return-carriers)：Check available logistics options for returns（查询退货可选择的物流）
- [checkReturnableInventoryQuantityOfProduct](operations/checkReturnableInventoryQuantityOfProduct.json) (POST /open-api/purchase/returnable-inventory)：Check the returnable inventory quantity of the product（查询商品可退库存数）
- [checkReturnApplicationItemDetails](operations/checkReturnApplicationItemDetails.json) (POST /open-api/purchase/return-application-detail)：Check Return Application Item Details（查询退货申请单商品明细）
- [checkReturnMethods](operations/checkReturnMethods.json) (POST /open-api/purchase/return-pickup-methods)：Check return methods（查询退货方式）
- [confirmReturnRequest](operations/confirmReturnRequest.json) (POST /open-api/purchase/confirm-return-application)：Confirm Return Request（确认退货申请单）
- [createReturnRequest](operations/createReturnRequest.json) (POST /open-api/purchase/create-return-application)：Create a Return Request（创建退货申请单）
- [modifyReturnMethodOfReturnOrder](operations/modifyReturnMethodOfReturnOrder.json) (POST /open-api/purchase/update-pickup-methods)：Modify the return method of the return order（修改退货单的退货方式）
- [queryAvailableHandlingMethodsForMerchants](operations/queryAvailableHandlingMethodsForMerchants.json) (GET /open-api/purchase/return-disposals)：Query the available handling methods for merchants（查询商家可选择的处理方式）
- [queryMerchantReturnAddress](operations/queryMerchantReturnAddress.json) (POST /open-api/purchase/query-return-address)：Query merchant's return address（查询商家退货地址）
- [queryReturnAndScrapOrderItemDetails](operations/queryReturnAndScrapOrderItemDetails.json) (POST /open-api/purchase/return-product-detail)：Query Return and Scrap Order Item Details（查询退货与报废单商品明细）
- [queryReturnAndScrapOrderList](operations/queryReturnAndScrapOrderList.json) (POST /open-api/purchase/return-list)：Query Return and Scrap Order List（查询退货与报废单列表）
- [queryReturnAndScrapOrderPackageDetails](operations/queryReturnAndScrapOrderPackageDetails.json) (POST /open-api/purchase/return-package-detail)：Query Return and Scrap Order Package Details（查询退货与报废单包裹明细）
- [queryReturnApplicationList](operations/queryReturnApplicationList.json) (POST /open-api/purchase/return-application-list)：Query Return Application List（查询退货申请单列表）
