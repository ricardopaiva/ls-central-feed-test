---
title: "Hotels hotfixes - 26.1.7 Hotels, Release date August 19, 2025 - Hotfixes"
product: Hotels
version: "26.1.7"
subproduct: Hotels
minor_version: "26.1"
date: 2025-08-19 00:00:00+00:00
order: 61
guid: 692c618af6e1c489caaa96ac8a6fd94d9ce09188
---

<div><strong>70118 Tape Chart: fuzzy search doesn't work for room name</strong>
<ul><li>Fixed an issue where searching for Room on Tape Chart was case sensitive.</li></ul>
<strong>69952 Reconciliation Tool Fix for application of Cust Ledger Entry</strong>
<ul><li>Added new functionality to fix the previous Cust Ledger Entries applied to wrong reservations:<ul><li>New button in Hotel Reconciliation page <b>Fix Cust. Ledger Entries Applied</b></li><li>New page, <b>Fix Cust. Ledger Entries Applied</b>, to handle (Deposit) Customer Ledger Entries wrong applied. First, set the correct filters and then run the <b>Populate</b> action. Once you got the entries to fix, select them and do <b>Fix selected</b> action.</li></ul></li>
<li>New button in Hotel Reconciliation page <b>Fix Cust. Ledger Entries Applied</b></li>
<li>New page, <b>Fix Cust. Ledger Entries Applied</b>, to handle (Deposit) Customer Ledger Entries wrong applied. First, set the correct filters and then run the <b>Populate</b> action. Once you got the entries to fix, select them and do <b>Fix selected</b> action.</li></ul>
<strong>69829 Hotel POS refund payment lookup does not display all payments</strong>
<ul><li>Details not available.</li></ul>
<strong>69819 Using Folio Pay button to refund negative Folio balance creates extra lines in POS Sales Journal (checked out reservation)</strong>
<ul><li>Fixed an issue where refunding reservation extra items, creates extra lines in POS Trans Line.</li></ul>
<strong>69647 LS Hotels: Tape Chart not searchable by Reservation No.</strong>
<ul><li>Added ability to search by hotel reservation no. on the Tape chart.</li></ul>
<strong>69636 Application in the Night Audit Pay batch is not specific the reservation</strong>
<ul><li>Fixed an issue on applying customer ledger entries to corresponding reservations in the <b>Night Audit</b> process. Additionally, fixed an issue on, not creating deposit line for Accommodation Tax.</li></ul>
<strong>68856 Rate Code activities are not visible on Hotel Reservation web template</strong>
<ul><li>Fixed the issue about missing activities on Hotel Reservation POS template: The activities from rate code were not visible. It was because the DRE lines were not updated correctly with the Activity No. on the confirmation of reservation.</li></ul></div>
