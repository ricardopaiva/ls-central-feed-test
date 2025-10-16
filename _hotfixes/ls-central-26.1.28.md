---
title: "LS Central hotfixes - 26.1.28, Release date September 23, 2025 - Hotfixes"
product: LS Central
version: "26.1.28"
subproduct: 
minor_version: "26.1"
date: 2025-09-23 00:00:00+00:00
order: 6
guid: dd827f313eb8c234b06bc11bd4156f8349427145
---

<strong>71997 Added VAR</strong><ul><li>Var was added to parameter in event <b>OnInit_OnBeforeTransDiscLoad</b> in LSC POS Transaction Events.</li></ul>
<strong>71846 Skip filtering of the record on find record - Sales Return Order Lines</strong><ul><li><b>Event OnAfterSetFilter</b> was added in page 10001344 <b>LSC Retail SRO Subform.</b></li></ul>
<strong>71828 Skip filtering of the record on find record</strong><ul><li>New event <b>OnFindRecordTrigger</b> in retail Subpages.</li></ul>
<strong>71823 Activity Matrix blank in AppShell</strong><ul><li>An issue was fixed, where the matrix could be empty when loaded.</li></ul>
<strong>71821 ADD EVENT</strong><ul><li>New events on Coupon Management <b>OnAfterGetNextNoSeriesCoupon and OnBeforeApplyCpnsThatCanBeUsedToPOSLines</b>.</li></ul>
<strong>71665 LSC NA CA - CO Details Factbox shows incorrect values when NA Tax</strong><ul><li>Details not available.</li></ul>
<strong>71581 Issue with the Store Coupon linked to the Tender Type Offer</strong><ul><li>Hotfix for coupon Tender offer. Coupon linked to Tender Offer was rendered unvalid on Total before tender type was selected.</li></ul>
<strong>71552 Data Distribution Log Fix</strong><ul><li><b>Previous Last Timestamp</b> is <b>Scheduler Log Lines</b> was corrected.</li></ul>
<strong>70807 Data Distribution Buffer Fix</strong><ul><li>Replication using timestamp was fixed to contain all data to be replicated.</li></ul>
<strong>69414 Create specific error codes in LS Central for Omni in web service StoreInvTransactionSendV2</strong><ul><li><b>StoreInvTransactionSendV2</b> request now returns specific error codes when error occures insted of the generic code 1000 and error text. These are the specific error codes:<ul><li>Error codes for StoreInvTransactionSendV2:<ul><li>2001  No lines to import.</li><li>2002  Transaction has already been received.</li><li>2003  Store Inventory Worksheet not found.</li><li>2004  WorksheetSeqNo must be unique in transaction.</li><li>2005  Transaction No. must be unique in transaction.</li><li>2006  Unexpected end of transaction.</li><li>2007  Too many lines in transaction.</li><li>2008  Area Code must have a value in Store Inventory Line : WorksheetSeqNo=%3, Line No.=%5. It cannot be empty.</li></ul></li></ul></li>
<li>Error codes for StoreInvTransactionSendV2:<ul><li>2001  No lines to import.</li><li>2002  Transaction has already been received.</li><li>2003  Store Inventory Worksheet not found.</li><li>2004  WorksheetSeqNo must be unique in transaction.</li><li>2005  Transaction No. must be unique in transaction.</li><li>2006  Unexpected end of transaction.</li><li>2007  Too many lines in transaction.</li><li>2008  Area Code must have a value in Store Inventory Line : WorksheetSeqNo=%3, Line No.=%5. It cannot be empty.</li></ul></li>
<li>2001  No lines to import.</li>
<li>2002  Transaction has already been received.</li>
<li>2003  Store Inventory Worksheet not found.</li>
<li>2004  WorksheetSeqNo must be unique in transaction.</li>
<li>2005  Transaction No. must be unique in transaction.</li>
<li>2006  Unexpected end of transaction.</li>
<li>2007  Too many lines in transaction.</li>
<li>2008  Area Code must have a value in Store Inventory Line : WorksheetSeqNo=%3, Line No.=%5. It cannot be empty.</li>
<li>Commerce 2025.10.</li></ul>
<strong>64526 LSC NA - EcomCalculateBasket to utilize NA tax calculations</strong><ul><li>Details not available.</li></ul>
<strong>62169 Customer Order Header page 10012030 "LSC CO Details" total amount doesnt include taxes</strong><ul><li>
<p>New events, <b>OnAfterCompressedCOLinesTotalIncreased</b> and <b>OnAfterCOLinesTotalIncreased</b> were added in LSC CO Utility Codeunit.</p>
</li></ul>
