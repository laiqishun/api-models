---
title: Selling Partner API for Messaging
description: "With the Messaging API you can build applications that send messages to buyers. You can get a list of message types that are available for an order that you specify, then call an operation that sends a message to the buyer for that order. The Messaging API returns responses that are formed according to the <a href=https://tools.ietf.org/html/draft-kelly-json-hal-08>JSON Hypertext Application Language</a> (HAL) standard."
---

# API List
- [getMessagingActionsForOrder](operations/getMessagingActionsForOrder.json) (GET /messaging/v1/orders/{amazonOrderId})：Returns a list of message types that are available for an order that you specify. A message type is represented by an actions object, which contains a path and query parameter(s). You can use the path and parameter(s) to call an operation that sends a message.
- [confirmCustomizationDetails](operations/confirmCustomizationDetails.json) (POST /messaging/v1/orders/{amazonOrderId}/messages/confirmCustomizationDetails)：Sends a message asking a buyer to provide or verify customization details such as name spelling, images, initials, etc.
- [createConfirmDeliveryDetails](operations/createConfirmDeliveryDetails.json) (POST /messaging/v1/orders/{amazonOrderId}/messages/confirmDeliveryDetails)：Sends a message to a buyer to arrange a delivery or to confirm contact information for making a delivery.
- [createLegalDisclosure](operations/createLegalDisclosure.json) (POST /messaging/v1/orders/{amazonOrderId}/messages/legalDisclosure)：Sends a critical message that contains documents that a seller is legally obligated to provide to the buyer. This message should only be used to deliver documents that are required by law.
- [createConfirmOrderDetails](operations/createConfirmOrderDetails.json) (POST /messaging/v1/orders/{amazonOrderId}/messages/confirmOrderDetails)：Sends a message to ask a buyer an order-related question prior to shipping their order.
- [createConfirmServiceDetails](operations/createConfirmServiceDetails.json) (POST /messaging/v1/orders/{amazonOrderId}/messages/confirmServiceDetails)：Sends a message to contact a Home Service customer to arrange a service call or to gather information prior to a service call.
- [CreateWarranty](operations/CreateWarranty.json) (POST /messaging/v1/orders/{amazonOrderId}/messages/warranty)：Sends a message to a buyer to provide details about warranty information on a purchase in their order.
- [GetAttributes](operations/GetAttributes.json) (GET /messaging/v1/orders/{amazonOrderId}/attributes)：Returns a response containing attributes related to an order. This includes buyer preferences.
- [createDigitalAccessKey](operations/createDigitalAccessKey.json) (POST /messaging/v1/orders/{amazonOrderId}/messages/digitalAccessKey)：Sends a buyer a message to share a digital access key that is required to utilize digital content in their order.
- [createUnexpectedProblem](operations/createUnexpectedProblem.json) (POST /messaging/v1/orders/{amazonOrderId}/messages/unexpectedProblem)：Sends a critical message to a buyer that an unexpected problem was encountered affecting the completion of the order.
- [sendInvoice](operations/sendInvoice.json) (POST /messaging/v1/orders/{amazonOrderId}/messages/invoice)：Sends a message providing the buyer an invoice
