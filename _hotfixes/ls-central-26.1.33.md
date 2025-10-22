---
title: "LS Central hotfixes - 26.1.33, Release date October 14, 2025 - Hotfixes"
product: LS Central
version: "26.1.33"
subproduct: 
minor_version: "26.1"
date: 2025-10-14 00:00:00+00:00
order: 3
guid: c1608b9df42fe596b76dfa82b4c1280626471336
---

<strong>72967 Issue with the Store Coupon linked to the Tender Type Offer</strong>
<ul><li>Hotfix for coupon Tender offer. Coupon linked to Tender Offer was rendered unvalid on Total before tender type was selected.</li></ul>
<strong>72858 Disabling CompareItemPostingBuffer in Statement-Post codeunit, in PostItem procedure</strong>
<ul><li>Event <b>OnBeforeCompressItemPostingBuffer</b> was added in codeunit Statement-Post.</li></ul>
<strong>72793 Safe Transfer</strong>
<ul><li>Details not available.</li></ul>
<strong>72763 Expose Set Procedures LSC Member Attributes Page</strong>
<ul><li>Make procedure public SetCardNo, SetContactNo, SetAccountNo and ClearParameters.</li></ul>
<strong>72697 BlockMixMatchPerDisc</strong>
<ul><li>New events were added to <b>LSC POS Offer Ext. Utility</b> and <b>LSC POS Price Utility</b> codeunit.</li></ul>
<strong>72685 Event to skip the validation Date</strong>
<ul><li>New event OnBeforeDisplayNoExpDateInPickingDocError was added to <b>LSC Picking / Receiving lines</b> table.</li></ul>
<strong>72678 Shopify item upload</strong>
<ul><li>Details not available.</li></ul>
<strong>72599 Template for pharmacy events - Event OnBeforePostTransactionAfterVoidOnProcessInfoCode in codeunit POS Transaction Events</strong>
<ul><li>Details not available.</li></ul>
<strong>72579 Make printing available</strong>
<ul><li>Details not available.</li></ul>
<strong>72578 Event OnBeforeMarkUsedCoupons in codeunit "LSC Coupon Management"</strong>
<ul><li><b>New event OnBeforeModifyPOSTransLineOnMarkUsedCoupons</b> was added to <b>LSC Coupon Management</b> codeunit.</li></ul>
<strong>72539 ADD Subscriber</strong>
<ul><li>New event <b>OnBeforeRetailProductCodeCheck</b> was added to <b>LSC Item Import Mgt</b> codeunit.</li></ul>
<strong>72538 I have two types of coupons, and each type is linked to a specific payment method</strong>
<ul><li>Parameter was added to <b>OnBeforeFindTenderTypeTable</b> event on POS Transaction.</li></ul>
<strong>72258 Azure storage queue filed validations</strong>
<ul><li>Details not available.</li></ul>
<strong>72030 Azure Storage Packet CleanUp Fix</strong>
<ul><li>Manual clean up action for fully processed Web Replication Azure Storage Packet was added.</li></ul>
<strong>71788 Discount offers linked to member accounts are not being applied when processing an exchange transaction</strong>
<ul><li>Discount offers linked to member accounts when processing an exchange transaction were fixed.</li></ul>
<strong>71768 TmpTransaction looses connection to original Deal Header in Split Bill</strong>
<ul><li>Details not available.</li></ul>
<strong>71574 New Event OnBeforePostTransactionAfterVoidOnProcessInfoCode</strong>
<ul><li>Details not available.</li></ul>
<strong>70950 Returning items by scanning receipt on POS</strong>
<ul><li>On selecting an Item to return, that has linked items, these linked items should also be selected automatically.</li></ul>
<strong>70165 Standard Activity Front Desk Extremely Slow</strong>
<ul><li>To optimize performance and concentrate on relevant transactions the #ACT-FRONTDESK POS Command uses Arrival Filter (Today + X) and Departure Filter (Today - X) Filters from Activity Setup Point of Sale Section for Transaction Filtering and Counting.</li><li>In the <b>Activity Front Desk</b> System filtering transactions based on Arrival and Departure dates is essential for managing reservations and activities efficiently. The filters are designed to provide a clear view of current and relevant transactions, ensuring that the system focuses on actionable data.</li></ul>
<strong>69852 Receipt return process in POS terminal Multi select</strong>
<ul><li>Details not available.</li></ul>
<strong>64773 Hospitality type - Combine split line action</strong>
<ul><li>There was an issue with price when <b>Combine split</b> line action is set to combine on confirmation, or always combine. This was fixed.</li></ul>
