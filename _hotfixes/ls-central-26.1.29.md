---
title: "LS Central hotfixes - 26.1.29, Release date September 30, 2025 - Hotfixes"
product: LS Central
version: "26.1.29"
subproduct: 
minor_version: "26.1"
date: 2025-09-30 00:00:00+00:00
order: 3
guid: a9cbcc985bc9b4e9076e3362a702a81fdf2281f7
---

<strong>72348 New-Event-EFT-InsertLogEntry</strong>
<ul><li>Details not available.</li></ul>
<strong>72335 Cannot change quantity of deals</strong>
<ul><li>There was an inability to change quantity on a deal line. This was fixed. </li></ul>
<strong>72327 Serial Number (SN) on Gift Receipt</strong>
<ul><li>New events were added, <b>AddItemSerialNoOnGiftReceipt</b> and  <b>OnBeforeGiftBufferInsert</b> in Codeunit <b>Gift Receipt POS Commands.</b></li></ul>
<strong>72283 Split bill error</strong>
<ul><li>Routing for WEB KDS was fixed. Had effect when splitting the bill.</li></ul>
<strong>72277 Commerce_Inventory stops due to special characters in item codes</strong>
<ul><li>Filter was adjusted to allow special characters.</li></ul>
<strong>72260 New event publishers: OnSendAfterStatusUpdateCompressed and OnSendAfterStatusUpdate</strong>
<ul><li>Two New events <b>OnSendAfterStatusUpdate</b> and <b>OnSendAfterStatusUpdateCompressed</b> in Codeunit <b>CO Omni Mgt.</b></li></ul>
<strong>72256 ASN Add Box Barcode No. fileld to GetASNDocumentLines web request</strong>
<ul><li>Details not available.</li></ul>
<strong>72209 SC-2059-EM - ZA AddPay Cross terminal return not very correctly for card transx.</strong>
<ul><li>Details not available.</li></ul>
<strong>72142 Duplicate ReceiptNo after suspending a transaction v25</strong>
<ul><li>There was an issue where suspending a transaction after a LogOut-LogIn on POS with WS enabled resulted in duplicate receipt numbers. This was fixed. </li></ul>
<strong>72140 Shopify item upload</strong>
<ul><li>String length error was fixed, when sending item to shopify where item no + variant code exceeded length of 20 characters.</li></ul>
<strong>71925 The G/L Account does not exist. Identification fields and values: No.=''</strong>
<ul><li>There was an error <b>G/L Account does not exist</b> in Statement Post when Transaction is using Tender Type where Account Type is <b>Bank Account.</b> This was fixed. </li></ul>
<strong>70590 AL: Shopify X Yue Hwa Issue</strong>
<ul><li>Details not available.</li></ul>
<strong>70374 AL: Public access to Event</strong>
<ul><li><b>OnBeforeSendShippingMessage</b> made public as <b>OnBeforeSendShippingMessagePub</b>.</li></ul>
<strong>70158 Upgrade failed from LS 25.3 to 26.1</strong>
<ul><li>When upgrading WKS tables: Check put in on new tables being empty - upgrade was only done if they are. Duplicate check was added for visual profile lines.</li></ul>
<strong>69549 Trans. Date and time missing in POS Voided Trans. Line</strong>
<ul><li><b>Trans. Date</b> and <b>Trans. Time</b> was filled on <b>POS Voided Trans. Line</b>.</li></ul>
<strong>66912 Matrix Drag and Drop is not working when using Windows AppShell</strong>
<ul><li>Details not available.</li></ul>
