---
title: "LS Central hotfixes - 26.1.27, Release date September 16, 2025 - Hotfixes"
product: LS Central
version: "26.1.27"
subproduct: 
minor_version: "26.1"
date: 2025-09-16 00:00:00+00:00
order: 5
guid: a38f6dd6d275664affee6bb6aee6b99e8fe9717f
---

<strong>71686 Incorrect posting when partially returning Customer Order</strong>
<ul><li>Customer Order Edit: duplicate payment line was created when <b>Sales Order</b> was posted and a line had been voided and refunded on POS.</li></ul>
<strong>71470 Decimal places issue in Inc/Exp Entries.</strong>
<ul><li>Rounding of Net Amount was fixed on returns when canceling prepayments and returning with cash.</li></ul>
<strong>71276 Event to skip ItemBaseUnitOfMeasureOnAfterValidateEvent - codeunit 10036991 "LSC Product Ext." implements "LSC IProductExt"</strong>
<ul><li>New event, <b>OnBeforeItemBaseUnitOfMeasureOnAfterValidateEvent</b> was added to <b>LSC Product Ext.</b> codeunit.</li></ul>
<strong>70972 Changes in Subform Objects for Variant Frameworks</strong>
<ul><li>Allowed global variables <b>gIsLSCentralPage</b> and <b>gIsShowLinesPage</b> to be changed outside the page extension, setting it as protected.</li></ul>
