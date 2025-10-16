---
title: "LS Central hotfixes - 26.1.15,  Release date August 12, 2025 - Hotfixes"
product: LS Central
version: "26.1.15"
subproduct: 
minor_version: "26.1"
date: 2025-08-12 00:00:00+00:00
order: 19
guid: 1c2473e41fc0e3163165c69944aef1f30defc769
---

<strong>69978 Published Offer not showing</strong><ul><li>Redundant local variable removed, to get access to the results from the <b>GetDirectMarketingInfo WS</b>.</li></ul>
<strong>69953 Problem with cancelling orders on Shopify - BC</strong><ul><li>Posting Customer Order non refundable shipping cost was wrongly done to fixed account. Now it follows normal Sales account.</li></ul>
<strong>69882 Customer Orders are not posted at the end of transaction</strong><ul><li>Added parameter <b>ReturnValue</b> to publisher event <b>OnBeforeApplyFilterToStatusCOReadyForPosting</b>.</li></ul>
<strong>69873 Codeunit 99001486 LSC Delete Logs</strong><ul><li>Bugfix to avoid overflow error on <b>EntryFilter</b> value in <b>Delete Logs</b> codeunit.</li></ul>
<strong>69853 SumAmountInclVATByCustomerOrderID calculates in LCY causing error creating Customer Orders</strong><ul><li>Customer Orders and Sales Orders are now in the same currency when creating SO and CO values.</li></ul>
<strong>69827 Skip Validating Pos Data Entry Number Series #553</strong><ul><li>Event <b>OnBeforeValidateNumberSeries</b> was added in <b>Backoffice Ext</b>.codeunit.</li></ul>
<strong>69809 Enable SumIndexFields on key 5 on Transaction Header</strong><ul><li>Details not available.</li></ul>
<strong>69790 Event Request: LS Omni Inventory Endpoint XmlPort Insert Lines</strong><ul><li>Event <b>OnBeforeInsertPOSTransInvLinesTemp</b> was added to <b>GetDocumentXML</b></li></ul>
<strong>69670 Clear IsHandled on FindPromotion loop #552</strong><ul><li>Details not available.</li></ul>
<strong>69668 Make procedure Push accessible in LSC POS Control Event #550</strong><ul><li>Event <b>OnBeforeAssignActivePanelID</b>was added in <b>Safe Denom. Panel Commands</b>.</li></ul>
<strong>69605 Extra Print Eventsubscribtion</strong><ul><li>Parameters <b>DataEntryTypeCode</b> and <b>InfoNumber</b> were added to event <b>OnBeforeAddFieldValueToTmpStr</b>.</li></ul>
<strong>69597 Commit changes for "To Skip UOMPopUp" #549</strong><ul><li>New event <b>OnBeforeIsUOMPopUp</b> was added to <b>LSC POS Transaction Impl</b> codeunit.</li></ul>
<strong>69595 Issue new coupon entry fix, fill "Value Type" based on "Calculation Type" #548</strong><ul><li>Respect Coupon Header Calculation type field, when creating the coupon entries using web services.</li></ul>
<strong>69532 OnBeforeExistEachTransaction Event #546</strong><ul><li>Event <b>OnBeforeExistEachTransaction</b> was added in <b>POS Transaction</b> codeunit.</li></ul>
<strong>69487 This PR adds a public wrapper procedure GetResourceAvailabilityText #541</strong><ul><li>Access was added to function <b>ShowResourceAvailability</b> in <b>LS Activities functions CU</b>.  The access point is in the hotel integration codeunit.</li></ul>
<strong>68667 Incorrect VAT calculation on Sales Order created by Customer Order</strong><ul><li>Fixed VAT calculation on Sales Order, created by Customer Order.</li></ul>
<strong>62087 Flexible bag should start with start amount 0</strong><ul><li>When you use <b>POS Start Amount Method = Flexible Bag</b>  it should always open the start of day float with amount 0 (as the online help). But it behaved exactly the same as the fixed bag. This was fixed. </li></ul>
