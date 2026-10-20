# Promotions

Global Selling / CBT official documentation category. The operation models below are derived from documented request examples; article links are authoritative for the full rules and context.

## Official articles

| Article | Extracted operations | Unparsed cURL | Status |
|---|---:|---:|---|
| [Official: Manage promotions](https://global-selling.mercadolibre.com/devsite/manage-promotions-gs) | 16 | 0 | modeled |
| [Official: Deals](https://global-selling.mercadolibre.com/devsite/deals-gs) | 11 | 0 | modeled |
| [Official: Co-funded campaigns](https://global-selling.mercadolibre.com/devsite/cofunded-campaigns) | 6 | 0 | modeled |
| [Official: Pre-negotiated discount per item](https://global-selling.mercadolibre.com/devsite/pre-negotiated-discount-per-item-gs) | 6 | 0 | modeled |
| [Official: Unhealthy Stock Campaign](https://global-selling.mercadolibre.com/devsite/unhealthy-stock-campaign) | 6 | 0 | modeled |
| [Official: Price discount](https://global-selling.mercadolibre.com/devsite/price-discount) | 5 | 0 | modeled |
| [Official: Volume discount campaigns](https://global-selling.mercadolibre.com/devsite/volume-discount-campaigns-gs) | 10 | 0 | modeled |
| [Official: Deal of the day](https://global-selling.mercadolibre.com/devsite/deal-of-day-gs) | 8 | 0 | modeled |
| [Official: Lightning Deal](https://global-selling.mercadolibre.com/devsite/lightning-deal-gs) | 7 | 0 | modeled |
| [Official: Seller Campaign](https://global-selling.mercadolibre.com/devsite/seller-campaign) | 16 | 0 | modeled |
| [Official: Automated co-participation and competitive pricing campaign](https://global-selling.mercadolibre.com/devsite/automated-co-participation-and-competitive-pricing-campaign) | 7 | 0 | modeled |
| [Official: Clearance](https://global-selling.mercadolibre.com/devsite/clearance) | 5 | 0 | modeled |

## API List

- [checkCampaignDetails](operations/checkCampaignDetails.json) (GET /marketplace/seller-promotions/promotions/P-MLM1806015)：Check campaign details [Official](https://global-selling.mercadolibre.com/devsite/cofunded-campaigns)
- [checkCampaignItems](operations/checkCampaignItems.json) (GET /marketplace/seller-promotions/promotions/P-MLC13457036/items)：Check campaign items [Official](https://global-selling.mercadolibre.com/devsite/unhealthy-stock-campaign)
- [checkDetailsAboutPreNegotiatedCampaign](operations/checkDetailsAboutPreNegotiatedCampaign.json) (GET /marketplace/seller-promotions/promotions/P-MLM13773008)：Check details about a pre-negotiated campaign [Official](https://global-selling.mercadolibre.com/devsite/pre-negotiated-discount-per-item-gs)
- [checkItemPromotions](operations/checkItemPromotions.json) (GET /marketplace/seller-promotions/items/{item_id})：Check Item Promotions [Official](https://global-selling.mercadolibre.com/devsite/manage-promotions-gs)
- [checkItemsInDealDay](operations/checkItemsInDealDay.json) (GET /marketplace/seller-promotions/promotions/{dodid}/items)：Check items in a deal of the day [Official](https://global-selling.mercadolibre.com/devsite/deal-of-day-gs)
- [checkItemsInLightningDeal](operations/checkItemsInLightningDeal.json) (GET /marketplace/seller-promotions/promotions/LGH-MLM1000/items)：Check items in a lightning deal [Official](https://global-selling.mercadolibre.com/devsite/lightning-deal-gs)
- [checkOffers](operations/checkOffers.json) (GET /marketplace/seller-promotions/promotions/offer/OFFER-MLM1873971357-10078845289/{id})：Check offers [Official](https://global-selling.mercadolibre.com/devsite/manage-promotions-gs)
- [checkPromotionItems](operations/checkPromotionItems.json) (GET /marketplace/seller-promotions/promotions/C-MLM201059/items)：Check Promotion Items [Official](https://global-selling.mercadolibre.com/devsite/manage-promotions-gs)
- [checkPromotionItemsGetItems](operations/checkPromotionItemsGetItems.json) (GET /marketplace/seller-promotions/promotions/{promotionid}/items)：Check Promotion Items [Official](https://global-selling.mercadolibre.com/devsite/manage-promotions-gs)
- [checkSellerPricingModel](operations/checkSellerPricingModel.json) (GET /marketplace/seller-promotions/users/{user_id}/pricing-model)：Check seller pricing model [Official](https://global-selling.mercadolibre.com/devsite/manage-promotions-gs)
- [deleteCampaign](operations/deleteCampaign.json) (DELETE /marketplace/seller-promotions/seller-campaign/C-MLM360923)：Delete campaign [Official](https://global-selling.mercadolibre.com/devsite/volume-discount-campaigns-gs)
- [deleteDealFromCampaign](operations/deleteDealFromCampaign.json) (DELETE /marketplace/seller-promotions/items/{itemid})：Delete a Deal from a campaign [Official](https://global-selling.mercadolibre.com/devsite/deals-gs)
- [deleteItemsByItemId](operations/deleteItemsByItemId.json) (DELETE /marketplace/seller-promotions/items/{item_id})：Delete a Deal from a campaign [Official](https://global-selling.mercadolibre.com/devsite/deals-gs)
- [deleteMassiveById](operations/deleteMassiveById.json) (DELETE /marketplace/seller-promotions/items/massive/{id})：Massive delete of offers [Official](https://global-selling.mercadolibre.com/devsite/manage-promotions-gs)
- [deleteMassiveDeleteOffers](operations/deleteMassiveDeleteOffers.json) (DELETE /marketplace/seller-promotions/items/massive/{itemid})：Massive delete of offers [Official](https://global-selling.mercadolibre.com/devsite/manage-promotions-gs)
- [deleteSellerCampaignByCampaignid](operations/deleteSellerCampaignByCampaignid.json) (DELETE /marketplace/seller-promotions/seller-campaign/{campaignid})：Delete a campaign [Official](https://global-selling.mercadolibre.com/devsite/seller-campaign)
- [deleteSellerCampaignByPromotionId](operations/deleteSellerCampaignByPromotionId.json) (DELETE /marketplace/seller-promotions/seller-campaign/{promotion_id})：Delete campaign [Official](https://global-selling.mercadolibre.com/devsite/volume-discount-campaigns-gs)
- [deleteSellerCampaign](operations/deleteSellerCampaign.json) (DELETE /marketplace/seller-promotions/seller-campaign/C-MLM703970)：Delete a campaign [Official](https://global-selling.mercadolibre.com/devsite/seller-campaign)
- [getByOfferidByUserId](operations/getByOfferidByUserId.json) (GET /marketplace/seller-promotions/promotions/offer/{offerid}/{user_id})：Check offers [Official](https://global-selling.mercadolibre.com/devsite/manage-promotions-gs)
- [getByPromotionIdItems](operations/getByPromotionIdItems.json) (GET /marketplace/seller-promotions/promotions/{promotion_id}/items)：Check campaign Items [Official](https://global-selling.mercadolibre.com/devsite/cofunded-campaigns)
- [getByResourceIdById](operations/getByResourceIdById.json) (GET /marketplace/seller-promotions/promotions/candidate/CANDIDATE-MLM2199514002-70027957276/{id})：Consult candidate items [Official](https://global-selling.mercadolibre.com/devsite/manage-promotions-gs)
- [getByResourceIdItems](operations/getByResourceIdItems.json) (GET /marketplace/seller-promotions/promotions/P-MLM13773008/items)：Filters [Official](https://global-selling.mercadolibre.com/devsite/manage-promotions-gs)
- [getCampaignDetails](operations/getCampaignDetails.json) (GET /marketplace/seller-promotions/promotions/P-MLM13757022)：Get campaign details [Official](https://global-selling.mercadolibre.com/devsite/deals-gs)
- [getCampaignItems](operations/getCampaignItems.json) (GET /marketplace/seller-promotions/promotions/C-MLM614177)：Get campaign items [Official](https://global-selling.mercadolibre.com/devsite/volume-discount-campaigns-gs)
- [listPromotionItemsPage](operations/listPromotionItemsPage.json) (GET /marketplace/seller-promotions/promotions/C-MLM199082/items)：Pagination [Official](https://global-selling.mercadolibre.com/devsite/manage-promotions-gs)
- [getConsultCandidateItems](operations/getConsultCandidateItems.json) (GET /marketplace/seller-promotions/promotions/candidates/{candidate_id})：Consult candidate items [Official](https://global-selling.mercadolibre.com/devsite/manage-promotions-gs)
- [getDealOfDayItems](operations/getDealOfDayItems.json) (GET /marketplace/seller-promotions/promotions/DOD-MLM1000/items)：Check items in a deal of the day [Official](https://global-selling.mercadolibre.com/devsite/deal-of-day-gs)
- [getMarketplaceSellerPromotionsPromotionsByPromotionid](operations/getMarketplaceSellerPromotionsPromotionsByPromotionid.json) (GET /marketplace/seller-promotions/promotions/{promotionid})：Promotion Details [Official](https://global-selling.mercadolibre.com/devsite/manage-promotions-gs)
- [getMarketplaceSellerPromotionsPromotionsByPromotionIdItems](operations/getMarketplaceSellerPromotionsPromotionsByPromotionIdItems.json) (GET /marketplace/seller-promotions/promotions/P-MLM13757022/items)：Check campaign items [Official](https://global-selling.mercadolibre.com/devsite/deals-gs)
- [getPromotionDetails](operations/getPromotionDetails.json) (GET /marketplace/seller-promotions/promotions/C-MLM201059)：Promotion Details [Official](https://global-selling.mercadolibre.com/devsite/manage-promotions-gs)
- [getPromotionsByPromotionId](operations/getPromotionsByPromotionId.json) (GET /marketplace/seller-promotions/promotions/P-MLC13457036)：Check campaign details [Official](https://global-selling.mercadolibre.com/devsite/unhealthy-stock-campaign)
- [getPromotionsByPromotionIdItems](operations/getPromotionsByPromotionIdItems.json) (GET /marketplace/seller-promotions/promotions/P-MLM13765128/items)：View campaign items [Official](https://global-selling.mercadolibre.com/devsite/automated-co-participation-and-competitive-pricing-campaign)
- [getSellerCampaignDetails](operations/getSellerCampaignDetails.json) (GET /marketplace/seller-promotions/promotions/C-MLM703970)：View campaign details [Official](https://global-selling.mercadolibre.com/devsite/seller-campaign)
- [getSalesPromotionsSeller](operations/getSalesPromotionsSeller.json) (GET /marketplace/seller-promotions/users/{user_id})：Sales promotions for the seller [Official](https://global-selling.mercadolibre.com/devsite/manage-promotions-gs)
- [getSellerPromotionsItemsByItemid](operations/getSellerPromotionsItemsByItemid.json) (GET /marketplace/seller-promotions/items/{itemid})：Check Item Promotions [Official](https://global-selling.mercadolibre.com/devsite/manage-promotions-gs)
- [getSellerPromotionsPromotionsByPromotionId](operations/getSellerPromotionsPromotionsByPromotionId.json) (GET /marketplace/seller-promotions/promotions/{promotion_id})：Check campaign details [Official](https://global-selling.mercadolibre.com/devsite/cofunded-campaigns)
- [getSellerPromotionsPromotionsByPromotionIdItems](operations/getSellerPromotionsPromotionsByPromotionIdItems.json) (GET /marketplace/seller-promotions/promotions/P-MLM1806015/items)：Check campaign Items [Official](https://global-selling.mercadolibre.com/devsite/cofunded-campaigns)
- [postItemsByItemId](operations/postItemsByItemId.json) (POST /marketplace/seller-promotions/items/{item_id})：A Listing price flow [Official](https://global-selling.mercadolibre.com/devsite/deals-gs)
- [postSellerCampaignById](operations/postSellerCampaignById.json) (POST /marketplace/seller-promotions/seller-campaign/{id})：Create campaign [Official](https://global-selling.mercadolibre.com/devsite/volume-discount-campaigns-gs)
- [postSellerCampaignByUserId](operations/postSellerCampaignByUserId.json) (POST /marketplace/seller-promotions/seller-campaign/{user_id})：Create campaign [Official](https://global-selling.mercadolibre.com/devsite/volume-discount-campaigns-gs)
- [postSellerPromotionsItemsByItemid](operations/postSellerPromotionsItemsByItemid.json) (POST /marketplace/seller-promotions/items/{itemid})：A Listing price flow [Official](https://global-selling.mercadolibre.com/devsite/deals-gs)
- [putMarketplaceSellerPromotionsItemsByItemId](operations/putMarketplaceSellerPromotionsItemsByItemId.json) (PUT /marketplace/seller-promotions/items/{item_id})：Listing price flow [Official](https://global-selling.mercadolibre.com/devsite/deals-gs)
- [putSellerCampaignByPromotionId](operations/putSellerCampaignByPromotionId.json) (PUT /marketplace/seller-promotions/seller-campaign/{promotion_id})：Update campaign [Official](https://global-selling.mercadolibre.com/devsite/volume-discount-campaigns-gs)
- [updateVolumeDiscountCampaign](operations/updateVolumeDiscountCampaign.json) (PUT /marketplace/seller-promotions/seller-campaign/C-MLM5689)：Update campaign [Official](https://global-selling.mercadolibre.com/devsite/volume-discount-campaigns-gs)
- [updateSellerCampaign](operations/updateSellerCampaign.json) (PUT /marketplace/seller-promotions/seller-campaign/C-MLM703970)：Update a campaign [Official](https://global-selling.mercadolibre.com/devsite/seller-campaign)
- [putSellerPromotionsItemsByItemid](operations/putSellerPromotionsItemsByItemid.json) (PUT /marketplace/seller-promotions/items/{itemid})：Listing price flow [Official](https://global-selling.mercadolibre.com/devsite/deals-gs)
- [queryCampaignDetails](operations/queryCampaignDetails.json) (GET /marketplace/seller-promotions/promotions/P-MLM6276082)：Query Campaign Details [Official](https://global-selling.mercadolibre.com/devsite/clearance)
- [updateCampaign](operations/updateCampaign.json) (PUT /marketplace/seller-promotions/seller-campaign/{campaignid})：Update a campaign [Official](https://global-selling.mercadolibre.com/devsite/seller-campaign)
- [viewCampaignDetails](operations/viewCampaignDetails.json) (GET /marketplace/seller-promotions/promotions/P-MLM13637333)：View campaign details [Official](https://global-selling.mercadolibre.com/devsite/automated-co-participation-and-competitive-pricing-campaign)
- [viewCampaignDetailsGetByResourceId](operations/viewCampaignDetailsGetByResourceId.json) (GET /marketplace/seller-promotions/promotions/P-MLM13765128)：View campaign details [Official](https://global-selling.mercadolibre.com/devsite/automated-co-participation-and-competitive-pricing-campaign)
- [viewCampaignItems](operations/viewCampaignItems.json) (GET /seller-promotions/P-MLB2087012/items)：View campaign items [Official](https://global-selling.mercadolibre.com/devsite/automated-co-participation-and-competitive-pricing-campaign)
- [viewItemsInCampaign](operations/viewItemsInCampaign.json) (GET /marketplace/seller-promotions/promotions/C-MLM703970/items)：View items in a campaign [Official](https://global-selling.mercadolibre.com/devsite/seller-campaign)
