---
title: TikTok Shop Logistics API
description: "Warehouses, shipping providers, delivery options, templates, and logistics tracking."
---

# API List

- [Get Available Shipping Template](operations/get-available-shipping-template-202510.json) (GET /logistics/202510/seller_templates)：get seller's available shipping template and return the reason why the template is not available，this api is now only available for JP and UK market
- [Get Global Seller Warehouse](operations/get-global-seller-warehouse-202309.json) (GET /logistics/202309/global_warehouses)：This API retrieves all global warehouse information associated with the seller. Warehouse information includes global warehouse ID, warehouse name, and warehouse ownership.
- [Get Logistics Tracking](operations/get-logistics-tracking-202604.json) (GET /logistics/202604/orders/{order_id}/tracking)：This API can use the order number to obtain the corresponding logistics tracking information, it can obtain more comprehensive logistics tracking information, which is more detailed than the Get tracking API, but only for CBT orders now. Refer: action_code/action_code_name mapping details https://partner.tiktokshop.com/docv2/page/37tihrdq
- [Get Shipping Providers](operations/get-shipping-providers-202309.json) (GET /logistics/202309/delivery_options/{delivery_option_id}/shipping_providers)：This API is used to obtain the shipping provider corresponding to the specified delivery option
- [Get Warehouse Delivery Options](operations/get-warehouse-delivery-options-202309.json) (GET /logistics/202309/warehouses/{warehouse_id}/delivery_options)：This API is used to obtain a list of delivery options available through the seller's designated warehouse.
- [Get Warehouse List](operations/get-warehouse-list-202309.json) (GET /logistics/202309/warehouses)：This API retrieves all warehouse information associated with the seller. Warehouse information includes name, status, address, and other details.
- [Shipping Template Exist V2](operations/shipping-template-exist-v2-202606.json) (GET /logistics/202606/seller_template/template_exist)：Shipping Template Exist
