---
title: Selling Partner API for Easy Ship
description: "Use the Selling Partner API for Easy Ship to build applications for sellers to manage and ship Amazon Easy Ship orders. With this API, you can get available time slots, schedule and reschedule Easy Ship orders, and print shipping labels, invoices, and warranties. To review the differences in Easy Ship operations by marketplace, refer to [Marketplace support](https://developer-docs.amazon.com/sp-api/docs/easyship-api-v2022-03-23-use-case-guide#marketplace-support)."
---

# API List
- [listHandoverSlots](operations/listHandoverSlots.json) (POST /easyShip/2022-03-23/timeSlot)：Returns time slots available for Easy Ship orders to be scheduled based on the package weight and dimensions that the seller specifies.
- [getScheduledPackage](operations/getScheduledPackage.json) (GET /easyShip/2022-03-23/package)：Returns information about a package, including dimensions, weight, time slot information for handover, invoice and item information, and status.
- [createScheduledPackage](operations/createScheduledPackage.json) (POST /easyShip/2022-03-23/package)：Schedules an Easy Ship order and returns the scheduled package information.
- [updateScheduledPackages](operations/updateScheduledPackages.json) (PATCH /easyShip/2022-03-23/package)：Updates the time slot for handing over the package indicated by the specified `scheduledPackageId`. You can get the new `slotId` value for the time slot by calling the `listHandoverSlots` operation before making another `patch` call.
- [createScheduledPackageBulk](operations/createScheduledPackageBulk.json) (POST /easyShip/2022-03-23/packages/bulk)：This operation automatically schedules a time slot for all the `amazonOrderId`s given as input, generating the associated shipping labels, along with other compliance documents according to the marketplace (refer to the [marketplace document support table](doc:easyship-api-v2022-03-23-use-case-guide#marketplace-support-table)).
