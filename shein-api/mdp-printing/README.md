---
title: "SHEIN MDP印染 API"
description: "SHEIN official category 3000002, with one JSON model per named operation."
---

# API List

Official category: [MDP印染 (3000002)](https://open.sheincorp.com/documents/apidoc/3000002). 22 records. Official IDs, applicable modes, and update times remain in the [manifest](../manifest.md) and each JSON file.

- [addOrCancelDeviceException](operations/addOrCancelDeviceException.json) (POST /open-api/mdp/basic-configure/production-equipment/add-or-cancel-equipment-exception)：Add or cancel device exception（添加或取消设备异常）
- [addOrUpdateCardHangingInformation](operations/addOrUpdateCardHangingInformation.json) (POST /open-api/mdp/hang-card/add-or-update)：Add or update card hanging information（新增或更新挂卡信息）
- [createCustomerRequirementsPendingCompletionReview](operations/createCustomerRequirementsPendingCompletionReview.json) (POST /open-api/mdp/order/customer-requirement/create-customer-requirement)：Create customer requirements pending completion review（创建待补全审核的客户需求）
- [externalQueryOperationLogForAppletCall](operations/externalQueryOperationLogForAppletCall.json) (POST /open-api/mdp/order/external/get-order-log-list)：External query operation log (for applet call)（外部查询操作日志（供小程序调用））
- [getAvailablePrintingFactoriesBasedOnName](operations/getAvailablePrintingFactoriesBasedOnName.json) (POST /open-api/mdp/order/customer-requirement/get-factory-list)：Get available printing factories based on name（根据名称获取可用的印花厂）
- [getBulkOrder](operations/getBulkOrder.json) (POST /open-api/mdp/get-order-info-list)：Get bulk order（获取大货订单信息）
- [getCustomerInformationBasedOnPrintingFactoryCode](operations/getCustomerInformationBasedOnPrintingFactoryCode.json) (POST /open-api/mdp/order/customer-requirement/get-factory-customer-list)：Get customer information based on printing factory code（根据印花厂code获取客户信息）
- [getPrintEquipmentList](operations/getPrintEquipmentList.json) (POST /open-api/mdp/basic-configure/production-equipment/get-print-equipmentList)：获取打印设备列表
- [getPushProcessSts](operations/getPushProcessSts.json) (POST /open-api/mdp/process/getPushProcessSts)：获取文件上传sts
- [operateHangtag](operations/operateHangtag.json) (POST /open-api/mdp/hangcard/operate)：Hangtag aggregation operation（put on shelf or outbound or relocation）（挂卡聚合操作（上架or出库or移位））
- [provideExternalErpMaterialTaskQuery](operations/provideExternalErpMaterialTaskQuery.json) (POST /open-api/mdp/process/get-process-develop-info-list)：Provide external ERP material task query interface（提供外部ERP版料任务查询接口）
- [provideScanningForProductionSchedulingToCreateWaves](operations/provideScanningForProductionSchedulingToCreateWaves.json) (POST /open-api/mdp/product/schedule/allocation-confirm)：Provide scanning for production scheduling to create waves（提供扫码排产创建波次）
- [providesUpdatedMdpPrintJobStart](operations/providesUpdatedMdpPrintJobStart.json) (POST /open-api/mdp/product/print-task/begin)：Provides updated MDP print job start（提供更新MDP打印任务开始）
- [provideUpdatedMdpPrintTaskCompletion](operations/provideUpdatedMdpPrintTaskCompletion.json) (POST /open-api/mdp/product/print-task/finish)：Provide updated MDP print task completion（提供更新MDP打印任务完成）
- [provideUpdateForMdpTransferTaskEnd](operations/provideUpdateForMdpTransferTaskEnd.json) (POST /open-api/mdp/product/transfer-print-task/finish)：Provide update for MDP transfer task end（提供更新MDP转印任务结束）
- [provideUpdateForMdpTransferTaskStart](operations/provideUpdateForMdpTransferTaskStart.json) (POST /open-api/mdp/product/transfer-print-task/begin)：Provide update for MDP transfer task start（提供更新MDP转印任务开始）
- [pushProcessFileUrl](operations/pushProcessFileUrl.json) (POST /open-api/mdp/process/pushProcessFileUrl)：推送版料文件URL
- [queryFlowerPatternDevelopmentPages](operations/queryFlowerPatternDevelopmentPages.json) (POST /open-api/mdp/flower/get-pattern-dev-page-list)：Provide external ERP flower pattern development pagination query interface（提供外部ERP花型开发分页查询接口）
- [receiveExternalErpCompletedOrders](operations/receiveExternalErpCompletedOrders.json) (POST /open-api/mdp/order/goods/external/receive-external-erp-complete-order)：Receive external ERP completed orders（接收外部ERP完结订单）
- [rerecordOrderMetersAndCutPieces](operations/rerecordOrderMetersAndCutPieces.json) (POST /open-api/mdp/order/goods/reenter-order-info)：Call for external suppliers - Re-record order meters and cut pieces（给外部供应商调用- 重录订单米数和裁片）
- [syncExternalSupplierShipmentStatus](operations/syncExternalSupplierShipmentStatus.json) (POST /open-api/mdp/order/goods/sync-order-info)：Call for external suppliers - Synchronize order information (status, shipment)（给外部供应商调用- 同步订单信息（状态，发货））
- [weChatMiniProgramLogin](operations/weChatMiniProgramLogin.json) (POST /open-api/mdp/wx-mini-program/login)：WeChat Mini Program login（微信小程序登陆）
