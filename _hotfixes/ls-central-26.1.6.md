---
title: "LS Central hotfixes - 26.1.6,  Release date July 15, 2025 - Hotfixes"
product: LS Central
version: "26.1.6"
subproduct: 
minor_version: "26.1"
date: 2025-07-15 00:00:00+00:00
order: 26
guid: 1ef372822bfcc26fa85f83d76d6d0e8df8503c99
---

<strong>69222 Some cleanup for LSC-69172</strong>
<ul><li>Details not available.</li></ul>
<strong>69161 AL: Fix Variant using Desc as name</strong>
<ul><li>Fixed Error: OPTION_DOES_NOT_EXIST, when <b>Use Variant Description</b> option is checked under Shopify Administration page.</li>
<li>
<p>Fixed fulfillment handling from Shopify that caused invalid order ID error and wrong qtr of items were shipped.</p>
</li></ul>
<strong>69032 Requested event to clear uncompressed discount voucher lines #535</strong>
<ul><li>New event <b>OnBeforeClearDiscountEntryTmp</b> was added to  <b>LSC POS Post Utility</b> codeunit.</li></ul>
<strong>68961 An event to have an option to change or skip the prompt message when using the Print_Z Command</strong>
<ul><li>New event <b>OnBeforeZReportConfirm</b> was added to <b>LSC POS Transaction Impl</b> codeunit.</li></ul>
<strong>67746 Discounts not recalculated and added to modifiers when added after the discount is triggered</strong>
<ul><li>Periodic discounts are now applied to linked modifier lines when they are inserted into the transaction. Previously, a discount offer on modifier lines were applied to modifier lines if the discount offer was activated, after selecting modifiers (for example, if member scanned after selecting the modifiers then that action, activated a discount offer).</li></ul>
