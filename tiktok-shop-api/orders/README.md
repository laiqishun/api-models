---
title: TikTok Shop Orders API
description: "Order lists, details, prices, external references, and order-specific operations."
---

# API List

- [Add External Order References](operations/add-external-order-references-202406.json) (POST /order/202406/orders/external_orders)：If you are using your own external OMS (order management system) to manage TikTok Shop orders, the corresponding order IDs between your OMS and TikTok Shop may be different. Use this endpoint to attach the information in your OMS to the correct order(s) in TikTok Shop for further reference.
- [Get External Order References](operations/get-external-order-references-202406.json) (GET /order/202406/orders/{order_id}/external_orders)：If you have used the `Add External Order References` API to sync order information between your external order management system (OMS) and TikTok Shop, you may call this API to get information on the synced orders.
- [Get Order Detail](operations/get-order-detail-202507.json) (GET /order/202507/orders)：Get the detailed order information of an order, including important attributes such as order status, shipping addresses, payment details, price and tax info, and package information.
- [Get Order List](operations/get-order-list-202309.json) (POST /order/202309/orders/search)：Returns a list of orders created or updated during the timeframe indicated by the specified parameters. You can also apply a range of filtering criteria to narrow the list of orders returned, such as order status, delivery option type, and buyer user ID.
- [Get Price Detail](operations/get-price-detail-202407.json) (GET /order/202407/orders/{order_id}/price_detail)：Get the detailed pricing calculation information of an order or a line item, including vouchers, tax, etc.
- [Pod Details](operations/pod-details-202606.json) (POST /order/202606/pod_details/search)：Description of [POST]/order/:version/pod_details/search
- [Search Order By External Order Reference](operations/search-order-by-external-order-reference-202406.json) (POST /order/202406/orders/external_order_search)：If you have used the `Add External Order References` API to sync information from your external order management system (OMS) to corresponding orders in TikTok Shop, you may call this API to search for order information in TikTok Shop based on information in your OMS.
- [Update The Blind Box Opening Results](operations/update-the-blind-box-opening-results-202605.json) (POST /order/202605/orders/blind_box_result/callback)：After the merchant completes blind box opening in a live room, use this callback to send blind box and batch box opening results for an order back to the platform. Buyers can then view the unboxing results in the order details.
