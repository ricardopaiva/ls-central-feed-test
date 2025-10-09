---
title: "Hotels hotfixes - 26.1.4 Hotels, Release date July 15, 2025 - Hotfixes"
product: Hotels
version: "26.1.4"
subproduct: Hotels
minor_version: "26.1"
date: 2025-07-15 00:00:00+00:00
order: 61
guid: 2b76d4fda604c603be79bc8ac8b8588c2ba0139c
---

<strong>68562 Balance on POS not correct after doing refund on payment with deposits and charges</strong>
<ul><li>The balance is now correct after doing a refund on a payment, that included deposit and charge (charged item that was originally paid on POS with deposit collection) and the error <b>No Deposit available to consume</b> does not show when the refunded amount is paid.</li>
<li>An issue where the company deposit was not being inserted to the journal if the deposit collection was unassigned (folio no = 0) was fixed. Now it checks for it and inserts if available, then users can just void that line if they do not want to use the deposit.</li></ul>
