---
title: "LS Central hotfixes - 26.1.1, Release date June 24, 2025 - Hotfixes"
product: LS Central
version: "26.1.1"
subproduct: 
minor_version: "26.1"
date: 2025-06-24 00:00:00+00:00
order: 35
guid: a18a32e5187635145376c023b914a01022097708
---

<strong>68530 Print Slip Subscriber on Card/Account No. Tender Payment print</strong>
<ul><li>New Event <b>OnBeforePrintCardAccountNo</b> in POS Print Utility.</li></ul>
<strong>68503 Activity Matrix – Activity List from availability slots</strong>
<ul><li>Integration Event Added <b>OnBeforeFIlterResourceReservationTimeFrom</b> in codeunit 10015912 <b>LSC ACT Matrix Filter Mgt.</b></li></ul>
<strong>68489 Add OnAfterPopulateTransactionStoreTerminal #528</strong>
<ul><li>New Event <b>OnAfterPopulateTransactionStoreTerminal</b> in CO eCommerce Mgt codeunit.</li></ul>
<strong>68469 SELLMEMDEPOSIT data table gets stuck</strong>
<ul><li>Fixed an issue where POS search panel was frozen for the command SELLMEMDEPOSIT.</li></ul>
<strong>68383 Add SetNoPrint procedure to control printing behavior #526</strong>
<ul><li>Procedure <b>SetNoPrint</b> made public in POS Print Utility.</li></ul>
<strong>68382 OnBeforeSendAtEndOfTransaction #525</strong>
<ul><li>Changed event <b>OnBeforeSendAtEndOfTransaction</b> on POS transaction Server utility codeunit.</li></ul>
<strong>68381 New Event OnAfterInitReversTransLineDiscRec in LSC POS Price Utility #524</strong>
<ul><li>Added <b>OnAfterInitReversTransLineDiscRec</b> event on codeunit POS Price Utility.</li></ul>
<strong>68327 Bookings - Activity not linked to POS Transaction after getting added to the POS to be paid</strong>
<ul><li>An issue was fixed, that could cause mismatch in payment status on an activity, and the related reservation. When an activity is pulled into POS journal line, the insert process and the assignment of receipt/line towards the activity is now within same commit and  should eliminate any issues related to errors during the payment process on POS.</li></ul>
<strong>68287 Wrong ILE for NEG_ADJ on BOM Components when Posting Statement</strong>
<ul><li>Quantity was wrong when using NEG_ADJ on BOM Items on the POS. This was fixed. </li></ul>
<strong>68268 Customer order process breaks if order is posted as customer invoice</strong>
<ul><li>When a Customer Order is collected and finalized on POS with the <b>Post + Print Customer Invoice</b> (POSTINVOICE) the Customer Order is posted if fully collected and paid.</li></ul>
<strong>68264 When statements are created the number series leaves gap</strong>
<ul><li>Fixed number series gap when creating statements.</li></ul>
<strong>68263 Add PurchaseOffline option to EFT in version 24, 25 and 26 versions</strong>
<ul><li>Details not available.</li></ul>
<strong>68224 Customer ledger entries not being created AGAIN when there is a rounding difference between the customer account tender and payment tender being used</strong>
<ul><li>When payment Info Account from POS was made and posted through <b>Statement Post</b>, it resulted in abnormal rounding. This was fixed.</li></ul>
<strong>68189 SendTransaction web service is always run even tough "TS Void Transactions" is not turned on</strong>
<ul><li>TS Void Transaction on refund transaction avoids using send transaction WS when it is not turned on. This was fixed.</li></ul>
<strong>68169 After Expire Member points #523</strong>
<ul><li>New event <b>OnAfterExpireMemberPoints</b> was added to <b>LSC Exp. Member Point Entries</b> codeunit.</li></ul>
<strong>68168 OnAfterAddMemberPointEntryOnUpdateMemberFromPOS in "LSC Member Posting Utils" #522</strong>
<ul><li>New event <b>OnAfterAddMemberPointEntryOnUpdateMemberFromPOS</b> was added to <b>"LSC Member Posting Utils</b> codeunit.</li></ul>
<strong>68154 Mix & Match (Least Expensive) - Splits the discount over multiple lines when you are selling items with different VAT Codes</strong>
<ul><li>Details not available.</li></ul>
<strong>68144 Void and Copy is missing card information on voided card payment line</strong>
<ul><li>When doing Void and Copy in the POS the voided payment line was not being updated with the card information. This was fixed.</li></ul>
<strong>68100 OnBeforeSendMemberProcessEntry in LSC POS Trans. Server Utility #521</strong>
<ul><li>Event <b>OnBeforeSendMemberProcessEntry</b> added in <b>LSC POS Trans. Server</b> Utility.</li></ul>
<strong>67862 OnBeforePickUpWarning Event #511</strong>
<ul><li>Added event <b>OnBeforePickUpWarning</b> on POS Transaction.</li></ul>
<strong>67288 New event to override the values showed in DisplayTotals() Function in POS Transaction Codeunit.</strong>
<ul><li>Details not available.</li></ul>
<strong>66736 feat(SC-1209): Added VAT Amount field on Transaction Register #492</strong>
<ul><li>Details not available.</li></ul>
