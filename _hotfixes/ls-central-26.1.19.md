---
title: "LS Central hotfixes - 26.1.19, Release date August 26, 2025 - Hotfixes"
product: LS Central
version: "26.1.19"
subproduct: 
minor_version: "26.1"
date: 2025-08-26 00:00:00+00:00
order: 12
guid: 8a448f3c3e6d928da87aec1d9e94f979a90c466b
---

<strong>70369 Request user to enter search criteria on Member Contact panel</strong>
<ul><li>Details not available.</li></ul>
<strong>70353 Mix Match filtering #557</strong>
<ul><li>New event OnAfterFilterPosTransLine2 added in <b>POS Price Utility</b> codeunit.</li></ul>
<strong>70308 Parameter in codeunit 10000921 "LSC Hierar. Link Mgt" to short</strong>
<ul><li>Extend parameter RightNode_p in procedure SetInheritedFields, codeunit <b>LSC Hierar. Link Mgt</b> from code[20] to code[30].</li></ul>
<strong>70260 Added Event OnVoucherRemainingAmountZeroErrorText #556</strong>
<ul><li>New Event <b>OnVoucherRemainingAmountZeroErrorText</b> in <b>LSC POS Infocode Utility</b> Codeunit.</li></ul>
<strong>70151 POS error when reading an serial no. for the item</strong>
<ul><li>Fixed an issue with reading serial numbers that start with 21 and are longer than 16 characters.</li></ul>
<strong>69968 Add isHandled and exit option to LSCCalcCurrentPrice procedure in LSC Price Line Worksheet table extension</strong>
<ul><li>New parameters in event <b>LSCOnCalcCurrentPriceOnAfterSetFilters</b> in table extension <b>LSC Price Line Worksheet</b>.</li></ul>
<strong>69944 Error when using an item flagged LSC Assign SerialNo/LotNo in CO Picking</strong>
<ul><li>New POS Command ASSIGNSERIALNO_LOTNO that can be assigned to button that is  able to assign or change Serial/Lot No for items, while in POS transaction.</li></ul>
<strong>69511 Proposed PR: Add Integration Event to ChangeInternalStatusEvents #544</strong>
<ul><li>Before and after event status change published events were added. </li></ul>
<strong>65635 Unexpected behavior with REORDQTY POS Command</strong>
<ul><li>REORDERQTY and REORDERMENUTYPE commands were refactored to fix problems with quantity, line numbers and transaction entries of linked lines.</li></ul>
