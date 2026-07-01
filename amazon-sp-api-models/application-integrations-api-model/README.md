---
title: The Selling Partner API for third party application integrations.
description: "With the AppIntegrations API v2024-04-01, you can send notifications to Amazon Selling Partners and display the notifications in Seller Central."
---

# API List
- [createNotification](operations/createNotification.json) (POST /appIntegrations/2024-04-01/notifications)：Create a notification for sellers in Seller Central.
- [deleteNotifications](operations/deleteNotifications.json) (POST /appIntegrations/2024-04-01/notifications/deletion)：Remove your application's notifications from the Appstore notifications dashboard.
- [recordActionFeedback](operations/recordActionFeedback.json) (POST /appIntegrations/2024-04-01/notifications/{notificationId}/feedback)：Records the seller's response to a notification.
