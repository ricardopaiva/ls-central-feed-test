---
title: "Autotests hotfixes - 29.0.2 Autotests, Release date November 3, 2026 - Hotfixes"
product: Autotests
version: "29.0.2"
subproduct: Autotests
minor_version: "29.0"
date: 2026-11-03 00:00:00+00:00
order: 7
guid: 988cad3b8101658e32a3b926a4bc6d744adcb54d
---

<strong>90853 Book captured web pre-auth as a Payment line on the collect transaction; fix mixed Payment + Pre-Auth double booking</strong>
<ul><li>Collecting a web order that was paid in advance now creates a payment line on the POS transaction. The statement posts that payment, so the transaction balances and has transaction payment entries. Orders that mix a payment and a pre-authorization no longer book the pre-authorized amount twice.</li><li><b>Action required by partners:</b></li><li>  ◦ Check that the collecting POS uses a local request. Open the POS functionality profile of the terminal and go to <b>Web Requests &gt; CustomerOrderUpdateV5</b>. On the highest-priority row, set <b>Local Request</b> to <b>Yes</b> and leave <b>Dist. Location</b><b>blank</b>. Remote setups keep posting to the general ledger.</li></ul>
