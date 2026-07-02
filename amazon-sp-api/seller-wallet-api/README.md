---
title: The Selling Partner API for Amazon Seller Wallet Open Banking API
description: "The Selling Partner API for Seller Wallet (Seller Wallet API) provides financial information that is relevant to a seller's Seller Wallet account. You can obtain financial events, balances, and transfer schedules for Seller Wallet accounts. You can also schedule and initiate transactions."
---

# API List
- [listAccounts](operations/listAccounts.json) (GET /finances/transfers/wallet/2024-03-01/accounts)：Get Seller Wallet accounts for a seller.
- [getAccount](operations/getAccount.json) (GET /finances/transfers/wallet/2024-03-01/accounts/{accountId})：Retrieve a Seller Wallet bank account by Amazon account identifier.
- [listAccountBalances](operations/listAccountBalances.json) (GET /finances/transfers/wallet/2024-03-01/accounts/{accountId}/balance)：Retrieve the balance in a given Seller Wallet bank account.
- [getTransferPreview](operations/getTransferPreview.json) (GET /finances/transfers/wallet/2024-03-01/transferPreview)：Retrieve a list of potential fees on a transaction.
- [listAccountTransactions](operations/listAccountTransactions.json) (GET /finances/transfers/wallet/2024-03-01/transactions)：Retrieve a list of transactions for a given Seller Wallet bank account.
- [createTransaction](operations/createTransaction.json) (POST /finances/transfers/wallet/2024-03-01/transactions)：Create a transaction request from a Seller Wallet account to another customer-provided account.
- [getTransaction](operations/getTransaction.json) (GET /finances/transfers/wallet/2024-03-01/transactions/{transactionId})：Find a transaction by the Amazon transaction identifier.
- [listTransferSchedules](operations/listTransferSchedules.json) (GET /finances/transfers/wallet/2024-03-01/transferSchedules)：Retrieve transfer schedules of a Seller Wallet bank account.
- [createTransferSchedule](operations/createTransferSchedule.json) (POST /finances/transfers/wallet/2024-03-01/transferSchedules)：Create a transfer schedule request from a Seller Wallet account to another customer-provided account.
- [updateTransferSchedule](operations/updateTransferSchedule.json) (PUT /finances/transfers/wallet/2024-03-01/transferSchedules)：Update transfer schedule information. Returns a transfer belonging to the updated scheduled transfer request.
- [getTransferSchedule](operations/getTransferSchedule.json) (GET /finances/transfers/wallet/2024-03-01/transferSchedules/{transferScheduleId})：Find a particular Amazon Seller Wallet account transfer schedule.
- [deleteScheduleTransaction](operations/deleteScheduleTransaction.json) (DELETE /finances/transfers/wallet/2024-03-01/transferSchedules/{transferScheduleId})：Delete a transaction request that is scheduled from Amazon Seller Wallet account to another customer-provided account.
