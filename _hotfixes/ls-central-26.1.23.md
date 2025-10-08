---
title: "LS Central hotfixes - 26.1.23, Release date September 2, 2025 - Hotfixes"
product: LS Central
version: "26.1.23"
subproduct: 
minor_version: "26.1"
date: 2025-09-02 00:00:00+00:00
order: 10
guid: e98bcd8db1abba8567c230ecbd9f3289433e6a1f
---

<strong>70634 New Events in Mix & Match Registration #560</strong>
<ul><li>New event <b>OnBeforeRegisterMixMatch</b> and <b>OnAfterCalcDiscountPr</b> added to <b>LSC POS Price Utility</b> codeunit.</li></ul>
<strong>70606 New Event Parameter in OnSuspendNotConfirmedBeforeConfirm #558</strong>
<ul><li>New parameter: <b>Returnvalue</b> in event <b>OnSuspendNotConfirmedBeforeConfirm</b> in POS Transactions Functions codeunit.</li></ul>
<strong>70604 feat(SC-2704): New Event request for creating Dedicated Tender removal line for foreign currency #559</strong>
<ul><li>New event <b>OnBeforeRemoveAdd</b> added to <b>LSC POS Post Utility</b> codeunit.</li></ul>
<strong>70561 LSC Process Inv. Adjmt. Entr - HF</strong>
<ul><li>Details not available.</li></ul>
<strong>70544 Shopify - Negative inventory</strong>
<ul><li>There was an error with Shopify Location setup. It was not correct and could cause CopyStr Error when updating inventory. This was fixed. </li></ul>
<strong>66971 SC-1535-TR UAT-Suspended transaction count is zero in the X report</strong>
<ul><li>The count and amount of suspended transactions was incorrect. This was fixed.</li></ul>
<strong>64793 If a Line Discount Reset occurs, no new Line discount can be awarded</strong>
<ul><li>It is now allowed to add <b>Line Discounts</b> to lines where a reset discount was previously applied.</li></ul>
