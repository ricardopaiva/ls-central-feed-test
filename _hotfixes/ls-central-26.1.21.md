---
title: "LS Central hotfixes - 26.1.21, Release date August 28, 2025 - Hotfixes"
product: LS Central
version: "26.1.21"
subproduct: 
minor_version: "26.1"
date: 2025-08-28 00:00:00+00:00
order: 13
guid: 71f186dfd9b396f063b925ce0d0b8c8c32b60d36
---

<div><strong>70331 'tender Operation' and 'FLOAT_ENT' handling - event missing a parameter</strong>
<ul><li>A new parameter, <b>SafTenderDataTable</b> variable was added in existing event <b>OnBeforeInitMenuOnInitSafTenderPanel</b> in LSC Safe Denom. Panel Commands codeunit.</li></ul>
<strong>70115 SC-2688-Public Method Request - LSC TR: Store Credit voucher extra print slip required during returns</strong>
<ul><li><b>PrintExtraPayment</b> procedure made public in POS Print Utility.</li></ul>
<strong>70101 Refund issue in Offline POS_V2</strong>
<ul><li>Bugfix to not compress POS Sales Lines when returning items linked to parent lines.</li></ul>
<strong>70010 Suspend Transaction after marking lines as CO returns an Error</strong>
<ul><li>Now Customer Order transactions can be suspended. However, it is only possible <b>before</b> the Customer Order is created.</li></ul>
<strong>69925 Unable to change discount on discount offer products</strong>
<ul><li>Now it is possible to change discount on discount offer products.</li></ul>
<strong>69906 Insufficient Quantity on Receipt Item During Statement Posting - Recipe BOMs</strong>
<ul><li>Statement posting now works with excluded recipe/ingredients and Inventory Setup option <b>Prevent Negative Inventory</b>.</li></ul></div>
