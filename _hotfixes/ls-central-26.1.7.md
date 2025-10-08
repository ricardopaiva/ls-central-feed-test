---
title: "LS Central hotfixes - 26.1.7, Release date July 22, 2025 - Hotfixes"
product: LS Central
version: "26.1.7"
subproduct: 
minor_version: "26.1"
date: 2025-07-22 00:00:00+00:00
order: 26
guid: 0af54b1095fc317f419c4cb50bc6bebd1a0575b5
---

<strong>69426 AL: fix Order Pull License error</strong>
<ul><li>Fixed Sales Header and Sales Shipping Header License errors when pulling orders from Shopify that have been fulfilled in Shopify.</li></ul>
<strong>69311 Need OnBeforeOpenPanel event urgently</strong>
<ul><li>New event <b>OnBeforeOpenPanel</b> was added to <b>LSC CO Create Panel</b> codeunit.</li></ul>
<strong>69310 Required Additional parameter in procedure- OpenAlphabeticKeyboardFromInfoCode</strong>
<ul><li>Additional parameter added to <b>OpenAlphabeticKeyboardFromInfoCode</b> procedure.</li></ul>
<strong>69289 New Event in LSC Statement - OnModify trigger #538</strong>
<ul><li>New event <b>OnBeforeCheckPostingDate</b> was added to <b>LSC Statement</b> table.</li></ul>
<strong>69288 Feature/onbeforeprocesscountingheader #540</strong>
<ul><li>New event <b>OnBeforeProcessCountingHeader</b> was added to <b>LSCGetDocumentListUtilsV2</b> codeunit.</li></ul>
<strong>69250 Expanded OnBeforeCheckUseQtyNoItemsNeeded and added another event for MixMatchPopup handling #539</strong>
<ul><li>New events <b>OnBeforeCheckUseQtyNoItemsNeededV2</b> and <b>OnBeforeCheckUseQtyNoOnTriggerMMPopUp</b> were added to <b>LSC POS Price Utility</b> codeunit.</li></ul>
<strong>69169 Event in Statement-Post codeunit</strong>
<ul><li>New event <b>OnBeforePostTenderTypeStatementLine</b> was added to  <b>LSC Statement-Post</b> codeunit.</li></ul>
<strong>69151 Error mgmt in refund #537</strong>
<ul><li>New event <b>OnBeforeCopyTransactionValues</b> was added to <b>LSC POS Refund Mgt.</b> codeunit.</li></ul>
<strong>69099 Add event OnAfterProcessInventoryHeaderRecord to CU 10012802 "LSC Web IM Functions" #536</strong>
<ul><li>New event <b>OnAfterProcessInventoryHeaderRecord</b> was added to <b>LSC Web IM Functions</b> codeunit.</li></ul>
<strong>69029 Call CheckMember in codeunit 10000823 "LSC POS Transaction Member"</strong>
<ul><li>Make <b>CheckMemberCard</b> procedure from <b>LSC POS Transaction Member</b> codeunit public.</li></ul>
<strong>69016 Add OnBeforePrintCustomerOrderShippingInfo and OnBeforePrintCustomerOrderShipmentCost #533</strong>
<ul><li>New events <b>OnBeforePrintCustomerOrderShippingInfo</b> and <b>OnBeforePrintCustomerOrderShipmentCost</b> were added to <b>LSC POS Print Utility CO</b> codeunit.</li></ul>
<strong>68999 Error while selecting Link to account</strong>
<ul><li>Details not available.</li></ul>
<strong>68857 Incorrect dimensions on transfer orders</strong>
<ul><li>Details not available.</li></ul>
<strong>68813 POS Command SEARCHCONTACT doesn't work in new version</strong>
<ul><li>Details not available.</li></ul>
<strong>68801 LSC AU - Sales Order - Invoicing issue</strong>
<ul><li>Added source code to the journal.</li></ul>
<strong>68795 Payment issue</strong>
<ul><li>Issued fixed with INCEXP as overtender which does not close the transaction.</li></ul>
<strong>68232 BarcDataEntry cuts 0 from front of Giftcard entry</strong>
<ul><li>Allow the “Keep Leading Zeroes in Barc.” field in the “POS Data Entry Type” table to be set to true for all Numbering selection.</li></ul>
