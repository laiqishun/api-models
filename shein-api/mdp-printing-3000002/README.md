# MDP印染 (3000002)

Official API category: [SHEIN developer reference](https://open.sheincorp.com/documents/apidoc/3000002).

22 records in the 2026-10-15 18:50 CST public catalog snapshot. Mode labels are copied per operation from official details; actual application access requires subscription and approval.

| Method | Name | Path / event | Official ID | Modes | Updated | Model |
|---|---|---|---:|---|---|---|
| POST | 获取大货订单信息 | `/open-api/mdp/get-order-info-list` | 3001429 | Not listed | 2025-10-15 15:14:48 | [JSON](./operations/3001429.json) |
| POST | 提供更新MDP打印任务开始 | `/open-api/mdp/product/print-task/begin` | 3001421 | Not listed | 2025-10-15 15:00:36 | [JSON](./operations/3001421.json) |
| POST | 提供更新MDP打印任务完成 | `/open-api/mdp/product/print-task/finish` | 3001422 | Not listed | 2025-10-15 15:02:22 | [JSON](./operations/3001422.json) |
| POST | 提供扫码排产创建波次 | `/open-api/mdp/product/schedule/allocation-confirm` | 3001420 | Not listed | 2025-10-15 14:59:24 | [JSON](./operations/3001420.json) |
| POST | 提供更新MDP转印任务开始 | `/open-api/mdp/product/transfer-print-task/begin` | 3001419 | Not listed | 2025-10-15 14:54:17 | [JSON](./operations/3001419.json) |
| POST | 提供更新MDP转印任务结束 | `/open-api/mdp/product/transfer-print-task/finish` | 3001418 | Not listed | 2025-10-15 14:53:00 | [JSON](./operations/3001418.json) |
| POST | 创建待补全审核的客户需求 | `/open-api/mdp/order/customer-requirement/create-customer-requirement` | 3001427 | Not listed | 2025-10-15 15:09:37 | [JSON](./operations/3001427.json) |
| POST | 根据印花厂code获取客户信息 | `/open-api/mdp/order/customer-requirement/get-factory-customer-list` | 3001426 | Not listed | 2025-10-15 15:08:32 | [JSON](./operations/3001426.json) |
| POST | 根据名称获取可用的印花厂 | `/open-api/mdp/order/customer-requirement/get-factory-list` | 3001425 | Not listed | 2025-10-15 15:05:40 | [JSON](./operations/3001425.json) |
| POST | 给外部供应商调用- 重录订单米数和裁片 | `/open-api/mdp/order/goods/reenter-order-info` | 3001424 | Not listed | 2025-10-15 15:04:38 | [JSON](./operations/3001424.json) |
| POST | 给外部供应商调用- 同步订单信息（状态，发货） | `/open-api/mdp/order/goods/sync-order-info` | 3001467 | Not listed | 2025-12-03 15:45:28 | [JSON](./operations/3001467.json) |
| POST | 微信小程序登陆 | `/open-api/mdp/wx-mini-program/login` | 3001417 | Not listed | 2025-10-15 14:50:57 | [JSON](./operations/3001417.json) |
| POST | 挂卡聚合操作（上架or出库or移位） | `/open-api/mdp/hangcard/operate` | 3001430 | Not listed | 2025-10-15 16:18:40 | [JSON](./operations/3001430.json) |
| POST | 新增或更新挂卡信息 | `/open-api/mdp/hang-card/add-or-update` | 3001431 | Not listed | 2025-10-15 16:18:49 | [JSON](./operations/3001431.json) |
| POST | 获取打印设备列表 | `/open-api/mdp/basic-configure/production-equipment/get-print-equipmentList` | 3001432 | Not listed | 2025-10-15 16:19:42 | [JSON](./operations/3001432.json) |
| POST | 添加或取消设备异常 | `/open-api/mdp/basic-configure/production-equipment/add-or-cancel-equipment-exception` | 3001433 | Not listed | 2025-10-15 16:19:51 | [JSON](./operations/3001433.json) |
| POST | 接收外部ERP完结订单 | `/open-api/mdp/order/goods/external/receive-external-erp-complete-order` | 3001434 | Not listed | 2025-10-15 16:20:00 | [JSON](./operations/3001434.json) |
| POST | 提供外部ERP版料任务查询接口 | `/open-api/mdp/process/get-process-develop-info-list` | 3001469 | Not listed | 2025-12-03 17:00:08 | [JSON](./operations/3001469.json) |
| POST | 外部查询操作日志（供小程序调用） | `/open-api/mdp/order/external/get-order-log-list` | 3001470 | Not listed | 2025-12-03 17:00:57 | [JSON](./operations/3001470.json) |
| POST | 提供外部ERP花型开发分页查询接口 | `/open-api/mdp/flower/get-pattern-dev-page-list` | 3001474 | Not listed | 2025-12-09 11:42:15 | [JSON](./operations/3001474.json) |
| POST | 推送版料文件URL | `/open-api/mdp/process/pushProcessFileUrl` | 3001950 | Not listed | 2026-08-07 10:36:12 | [JSON](./operations/3001950.json) |
| POST | 获取文件上传sts | `/open-api/mdp/process/getPushProcessSts` | 3001953 | Not listed | 2026-08-07 16:41:07 | [JSON](./operations/3001953.json) |
