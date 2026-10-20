# Post-sale messages

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Post-sale Messages](https://global-selling.mercadolibre.com/devsite/messaging-after-sale-global-selling) | 7 | 0 | modeled |
| [Official: Pending messages](https://global-selling.mercadolibre.com/devsite/pending-messages-gs) | 2 | 0 | modeled |
| [Official: Blocked messages](https://global-selling.mercadolibre.com/devsite/blocked-messages-gs) | 1 | 0 | modeled |

## API List

- [createMessage](operations/createMessage.json) (POST /marketplace/messages/packs/{pack_id})：Create message [Official](https://global-selling.mercadolibre.com/devsite/messaging-after-sale-global-selling)
- [getAttachment](operations/getAttachment.json) (GET /marketplace/messages/attachments/{attachment_id})：Get attachment [Official](https://global-selling.mercadolibre.com/devsite/messaging-after-sale-global-selling)
- [getAttachmentsByAttachmentId](operations/getAttachmentsByAttachmentId.json) (GET /marketplace/messages/attachments/76601286_5946e4c4-168a-45fd-945e-b8f0c306c58d.png)：Get attachment [Official](https://global-selling.mercadolibre.com/devsite/messaging-after-sale-global-selling)
- [getMessageById](operations/getMessageById.json) (GET /marketplace/messages/{message_id})：Get message by ID [Official](https://global-selling.mercadolibre.com/devsite/messaging-after-sale-global-selling)
- [getMessagesByMessageId](operations/getMessagesByMessageId.json) (GET /marketplace/messages/2d45a5ad186041659e9a608f0c109dff)：Get message by ID [Official](https://global-selling.mercadolibre.com/devsite/messaging-after-sale-global-selling)
- [getMessagesByPack](operations/getMessagesByPack.json) (GET /marketplace/messages/packs/{pack_id})：Get messages by pack [Official](https://global-selling.mercadolibre.com/devsite/messaging-after-sale-global-selling)
- [getMessagesUnread](operations/getMessagesUnread.json) (GET /marketplace/messages/unread)：Parameters [Official](https://global-selling.mercadolibre.com/devsite/pending-messages-gs)
- [markMessagesAsRead](operations/markMessagesAsRead.json) (GET /messages/packs/{pack_id}/sellers/{seller_id})：Mark messages as read [Official](https://global-selling.mercadolibre.com/devsite/pending-messages-gs)
- [uploadAttachment](operations/uploadAttachment.json) (POST /marketplace/messages/attachments)：Upload attachment [Official](https://global-selling.mercadolibre.com/devsite/messaging-after-sale-global-selling)
