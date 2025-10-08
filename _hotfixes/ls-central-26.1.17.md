---
title: "LS Central hotfixes - 26.1.17, Release date August 19, 2025 - Hotfixes"
product: LS Central
version: "26.1.17"
subproduct: 
minor_version: "26.1"
date: 2025-08-19 00:00:00+00:00
order: 16
guid: dcbb88335fb35e7c5dbc20ee3819fe2fc5939da4
---

<strong>70158 Upgrade failed from LS 25.3 to 26.1</strong>
<ul><li>When upgrading WKS tables: Check, <b>put in on new tables</b> being empty - upgrade only done if they are. </li></ul>
<strong>70067 Referenced refund payments - format the amount</strong>
<ul><li>When displaying referenced refund payment list, in a region where the decimal point is a comma, the list displaying the cards payments for refund was not being formatted correctly. This was fixed. When voiding a card payment within the same day, the POS does not try to retrieve token storage information for the voided payment.</li></ul>
<strong>70026 Fix coupon discount in Customer Order</strong>
<ul><li>Coupon discount % calculation is not taking into account quantity when processing collect from web Customer Order.</li></ul>
<strong>70004 Need to be able to filter inactive variants</strong>
<ul><li>Event <b>OnBeforeFindItemVariants</b> was added to <b>Popup Variant Handler</b> and <b>Pop-up POS Commands</b> to enable the user to filter on item variants shown in the pop-up.</li></ul>
<strong>69992 Focus does not go to POS after completing a purchase in a SaaS environment</strong>
<ul><li>Details not available.</li></ul>
<strong>69963 LSTS-39665: Delete price check records #554</strong>
<ul><li>New event <b>OnBeforeInsertNewTrans</b> added to <b>LSC Price Check Card</b> page.</li></ul>
