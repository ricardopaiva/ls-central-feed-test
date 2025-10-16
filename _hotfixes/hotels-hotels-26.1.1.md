---
title: "Hotels hotfixes - 26.1.1 Hotels, Release date June 24, 2025 - Hotfixes"
product: Hotels
version: "26.1.1"
subproduct: Hotels
minor_version: "26.1"
date: 2025-06-24 00:00:00+00:00
order: 67
guid: 5ca8d01fb7dfe1a0effa64c78597e9005a2fce3e
---

<strong>68276 Refund process fails in some scenarios</strong>
<ul><li>Fixed an issue where a refund on the POS did not enable the PAY button. Applicable to <b>Accrual Accounting</b> only.</li>
<li>Fixed an issue where refunding payment, including deposit charge, reused the already refunded deposit.</li>
<li>Fixed an issue regarding <b>String too long</b> in the refund panel on POS</li>
<li>When refunding a transaction that has a deposit and a tip in same transaction, you could only refund the tip but not the deposit amount. This was fixed.</li>
<li>Fixed an issue where POS showed wrong balance after refunding deposit after finalizing all folios (on reservations with both guest and company folios) - (issue with deposit assignment not being removed).</li>
<li>Removed the popup on preypayment in accrual accounting when paying on POS.</li>
<li>The amount is now auto-filled for the prepayment, when doing prepayment on the POS from PAY button (reservation still in house).</li></ul>
