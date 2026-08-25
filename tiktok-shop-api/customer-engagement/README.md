---
title: TikTok Shop Customer Engagement API
description: "Message templates, engagement tasks, messages, and engagement permissions."
---

# API List

- [Create Custom Engagement Task](operations/create-custom-engagement-task-202502.json) (POST /customer_engagement/202502/engagement_tasks/custom)：Create an engagement task that uses a self-defined custom message instead of predefined message templates from TikTok Shop. The task acts as a container for grouping messages with similar content and rules, allowing sellers to track and compare task performance across different types of content. Note that each task has a mandatory end time, and once expired, it cannot be used to send additional messages.
- [Create Engagement Task](operations/create-engagement-task-202412.json) (POST /customer_engagement/202412/engagement_tasks)：Create an engagement task that acts as a container for grouping messages with similar content and rules, allowing sellers to track and compare task performance across different types of content. Note that each task has a mandatory end time, and once expired, it cannot be used to send additional messages.
- [Get Engagement Feature Permissions](operations/get-engagement-feature-permissions-202502.json) (GET /customer_engagement/202502/permissions)：Retrieve information about customer engagement features that the shop has permission to use.
- [Get Engagement Task Performances](operations/get-engagement-task-performances-202412.json) (POST /customer_engagement/202412/performances)：Retrieve detailed performance metrics for a customer engagement task, including message reads, order conversions, and other key engagement statistics.
- [Get Message Templates](operations/get-message-templates-202412.json) (GET /customer_engagement/202412/message_templates)：Get a library of customer engagement message templates predefined by TikTok Shop, which you can use directly in your customer engagement communications.
- [Send Engagement Message](operations/send-engagement-message-202412.json) (POST /customer_engagement/202412/messages)：Send messages to specific customers for a particular engagement task.
