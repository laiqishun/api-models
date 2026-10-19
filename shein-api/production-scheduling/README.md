---
title: "SHEIN 排产 API"
description: "SHEIN official category 3000012, with one JSON model per named operation."
---

# API List

Official category: [排产 (3000012)](https://open.sheincorp.com/documents/apidoc/3000012). 10 records. Official IDs, applicable modes, and update times remain in the [manifest](../manifest.md) and each JSON file.

- [batchCreateFinishedProductionTasks](operations/batchCreateFinishedProductionTasks.json) (POST /open-api/sims/srp/tasks-create-by-production-nos)：Batch Create Finished Goods Production Tasks Based on Scheduling Plan（根据排单计划批量创建成品生产任务）
- [batchCreateFinishedSchedulingAndTasks](operations/batchCreateFinishedSchedulingAndTasks.json) (POST /open-api/sims/srp/tasks-create-by-products)：Batch Create Finished Product Scheduling Plans and Production Tasks Based on Product Information（根据商品信息批量创建成品排单计划和生产任务）
- [batchCreateSemiFinishedProductionTasks](operations/batchCreateSemiFinishedProductionTasks.json) (POST /open-api/sims/srp/sfp-tasks-create-by-production-nos)：Batch Create Semi-Finished Product Production Tasks Based on Scheduling Plan（根据排单计划批量创建半成品生产任务）
- [batchCreateSemiFinishedSchedulingAndTasks](operations/batchCreateSemiFinishedSchedulingAndTasks.json) (POST /open-api/sims/srp/sfp-tasks-create-by-sfps)：Batch Create Semi-Finished Product Scheduling Plans and Production Tasks Based on Product Information（根据商品信息批量创建半成品排单计划和生产任务）
- [paginatedQueryOfProductionSchedulingPlans](operations/paginatedQueryOfProductionSchedulingPlans.json) (POST /open-api/sims/srp/production-plan-query)：Paginated Query of Production Scheduling Plans（分页查询排产计划）
- [queryProductionTasksByPage](operations/queryProductionTasksByPage.json) (POST /open-api/sims/srp/task-query)：Query Production Tasks by Page（分页查询生产任务）
- [queryTaskNodeConfiguration](operations/queryTaskNodeConfiguration.json) (POST /open-api/sims/srp/progress-node-query)：Query Task Node Configuration（查询任务节点配置）
- [queryTaskProgressAndDeliveryDateConfiguration](operations/queryTaskProgressAndDeliveryDateConfiguration.json) (POST /open-api/sims/srp/timeline-query)：Query Task Progress and Delivery Date Configuration（查询任务进度交期配置）
- [queryWorkflowConfiguration](operations/queryWorkflowConfiguration.json) (POST /open-api/sims/srp/procedure-query)：Query Workflow Configuration（查询作业流程配置）
- [updateProductionTask](operations/updateProductionTask.json) (POST /open-api/sims/srp/task-update)：Update Production Task API（更新生产任务接口）
