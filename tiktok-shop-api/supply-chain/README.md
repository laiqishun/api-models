---
title: TikTok Shop Supply Chain API
description: "Supply chain package shipment confirmation operations."
---

The [official API page](https://partner.tiktokshop.com/docv2/page/confirm-package-shipment) lists ERP among the app categories for China registration and Vietnam target market. Calling this endpoint additionally requires TikTok certification as a warehouse service provider and a TikTok-issued `warehouse_provider_id` matching the app key.

# API List

- [Confirm Package Shipment](operations/confirm-package-shipment-202309.json) (POST /supply_chain/202309/packages/sync)：This API enables a warehouse service provider to send package shipment information for an order. Only warehouse service providers who have been certified by the platform have permission to access this interface.
