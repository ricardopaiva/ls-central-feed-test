---
title: "LS Central hotfixes - 29.0.3, Release date November 3, 2026 - Hotfixes"
product: LS Central
version: "29.0.3"
subproduct: 
minor_version: "29.0"
date: 2026-11-03 00:00:00+00:00
order: 3
guid: cebbb4f6594ee1bb01b9f04445682cf66c98ede5
---

<strong>91060 Add event-publisher OnBeforeSendDataEntries</strong>
<ul><li>New event <b>OnBeforeSendDataEntries</b> was added to <b>POS Transaction Server Utility</b> codeunit.</li></ul>
<strong>90853 Book captured web pre-auth as a Payment line on the collect transaction; fix mixed Payment + Pre-Auth double booking</strong>
<ul><li>Collecting a web order that was paid in advance now creates a payment line on the POS transaction. The statement posts that payment, so the transaction balances and has transaction payment entries. Orders that mix a payment and a pre-authorization no longer book the pre-authorized amount twice.</li><li><b>Action required by partners:</b></li><li>  ◦ Check that the collecting POS uses a local request. Open the POS functionality profile of the terminal and go to <b>Web Requests &gt; CustomerOrderUpdateV5</b>. On the highest-priority row, set <b>Local Request</b> to <b>Yes</b> and leave <b>Dist. Location</b><b>blank</b>. Remote setups keep posting to the general ledger.</li></ul>
<strong>90059 OnBeforeRunRequest in codeunit 10033130 LSCRetailMessageReadUtils</strong>
<ul><li>New event <b>OnBeforeRunRequest</b> was added to <b>LSCRetailMessageReadUtils</b> codeunit.</li></ul>
