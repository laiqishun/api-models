---
title: "SHEIN 物流 API"
description: "SHEIN official category 1000006, with one JSON model per named operation."
---

# API List

Official category: [物流 (1000006)](https://open.sheincorp.com/documents/apidoc/1000006). 11 records. Official IDs, applicable modes, and update times remain in the [manifest](../manifest.md) and each JSON file.

- [licensePlateInformationCallback](operations/licensePlateInformationCallback.json) (POST /open-api/cargo/platenum-callback)：License plate information callback（车牌信息回调）
- [logisticProviderLogisticProviderWaybillCallback](operations/logisticProviderLogisticProviderWaybillCallback.json) (POST /open-api/cargo/express-notify)：Logistic provider interface - Logistic provider waybill callback（物流商接口-物流商运单回调）
- [logisticProviderNetworkCallback](operations/logisticProviderNetworkCallback.json) (POST /open-api/cargo/express-website-message)：Logistic provider network callback interface（物流商网点回调接口）
- [logisticsGetCourierCompanyInformation](operations/logisticsGetCourierCompanyInformation.json) (GET /open-api/order/express-infos)：Logistics interface - get courier company information（物流接口-获取快递公司信息）
- [logisticsProvidersPushTrajectoryDataTrackingmore](operations/logisticsProvidersPushTrajectoryDataTrackingmore.json) (POST /open-api/cargo/track-notify-trackingmore)：Logistics providers push trajectory data-trackingmore（物流商推送轨迹数据-trackingmore）
- [logisticsProvidersPushTrajectoryDataUnified](operations/logisticsProvidersPushTrajectoryDataUnified.json) (POST /open-api/cargo/track-notify)：Logistics providers push trajectory data-unified interface（物流商推送轨迹数据-统一接口）
- [logisticsTrackCallback](operations/logisticsTrackCallback.json) (POST /open-api/cargo/logistics-trajectory-callback)：[New] Logistics track callback（【新】物流轨迹回调）
- [newLogisticWeightCallback](operations/newLogisticWeightCallback.json) (POST /open-api/cargo/weight-callback)：【New】Logistic weight callback（【新】物流重量回调）
- [pickUpTimeoutOrCancelShipmentReasonsFeedback](operations/pickUpTimeoutOrCancelShipmentReasonsFeedback.json) (POST /open-api/cargo/timeout-cancel-reason-return)：Pick-up timeout/cancel shipment reasons feedback（揽收超时/取消运单原因回传）
- [sfWaybillUncollectedPackageDetailsCallback](operations/sfWaybillUncollectedPackageDetailsCallback.json) (POST /open-api/cargo/qc-outside-cancel-sf-express)：SF Waybill Uncollected Package Details Callback Interface（顺丰运单未揽收包裹明细回调接口）
- [uploadEvidenceOfSettlementAbnormalities](operations/uploadEvidenceOfSettlementAbnormalities.json) (POST /open-api/cargo/quote-return)：Upload evidence of settlement abnormalities（上传结算异常举证）
