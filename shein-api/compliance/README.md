---
title: "SHEIN 合规 API"
description: "SHEIN official category 3000008, with one JSON model per named operation."
---

# API List

Official category: [合规 (3000008)](https://open.sheincorp.com/documents/apidoc/3000008). 18 records. Official IDs, applicable modes, and update times remain in the [manifest](../manifest.md) and each JSON file.

- [bindSkcAndAgencyCompany](operations/bindSkcAndAgencyCompany.json) (POST /open-api/goods-compliance/save-skc-agency)：Bind SKC and the agency company（绑定SKC和代理公司）
- [bindSkcAndRealShotImage](operations/bindSkcAndRealShotImage.json) (POST /open-api/goods-compliance/skc-save-label)：Bind SKC and real shot image（绑定SKC和实拍图）
- [createOrEditQualificationCertificate](operations/createOrEditQualificationCertificate.json) (POST /open-api/goods-certificates/save)：Create/Edit qualification certificate（创建/编辑资质证书）
- [getFullEcoFriendlyConsumablesInformation](operations/getFullEcoFriendlyConsumablesInformation.json) (GET /open-api/goods-quality/environmental-label-rule/material-quality-tree-v2)：Get full eco-friendly consumables information（获取全量环保耗材信息）
- [printComplianceLabel](operations/printComplianceLabel.json) (POST /open-api/goods-compliance/label-print)：Print compliance label（打印合规标签）
- [queryAgencyCompanyList](operations/queryAgencyCompanyList.json) (POST /open-api/goods-compliance/agency-list)：Query agency company list（查询代理公司列表）
- [queryBindingStatusOfSkcWarningLanguage](operations/queryBindingStatusOfSkcWarningLanguage.json) (POST /open-api/goods-compliance/query-skc-warning-status)：Query the binding status of SKC warning language（查询SKC的警告语绑定状态）
- [queryFillingRulesOfWarningTextCertificate](operations/queryFillingRulesOfWarningTextCertificate.json) (POST /open-api/goods-compliance/query-warning-certificate-rules)：Query the filling rules of the warning text certificate（查询警告语证书的填写规则）
- [queryQualificationCertificateFillingRules](operations/queryQualificationCertificateFillingRules.json) (POST /open-api/goods-certificate-schemas/detail)：Query qualification certificate filling rules（查询资质证书填写规则）
- [queryQualificationCertificateList](operations/queryQualificationCertificateList.json) (POST /open-api/goods-certificates/search)：Query qualification certificate list（查询资质证书列表）
- [querySkcAgencyCompanyBindingRequirements](operations/querySkcAgencyCompanyBindingRequirements.json) (POST /open-api/goods-compliance/skc-agency-detail)：Query SKC's agency company binding requirements（查询SKC的代理公司绑定要求）
- [querySkcAvailableLabelTemplates](operations/querySkcAvailableLabelTemplates.json) (POST /open-api/goods-compliance/get-label-template)：Query SKC available label templates（查询SKC可用的标签模板）
- [querySkcComplianceInformationRequirements](operations/querySkcComplianceInformationRequirements.json) (POST /open-api/goods-compliance-requirements/list)：Query SKC compliance information requirements（查询SKC的合规信息要求）
- [querySkcRealShotImageRequirements](operations/querySkcRealShotImageRequirements.json) (POST /open-api/goods-compliance/skc-label-list)：Query SKC's real shot image requirements（查询SKC的实拍图要求）
- [skcBindQualificationCertificate](operations/skcBindQualificationCertificate.json) (POST /open-api/goods-certificates/bind)：SKC bind qualification certificate（SKC绑定资质证书）
- [updateSkcWarningText](operations/updateSkcWarningText.json) (POST /open-api/goods-compliance/update-skc-warning-certificate)：Update SKC warning text（更新SKC的警告语）
- [uploadQualificationCertificateFile](operations/uploadQualificationCertificateFile.json) (POST /open-api/goods-certificate-files/upload)：Upload qualification certificate file（上传资质证书文件）
- [uploadRealShotImage](operations/uploadRealShotImage.json) (POST /open-api/goods-compliance/upload-skc-label-picture)：Upload real shot image（上传实拍图图片）
