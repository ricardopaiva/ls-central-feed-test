---
title: "Hotels hotfixes - 26.1.17 Hotels, Release date October 7, 2025 - Hotfixes"
product: Hotels
version: "26.1.17"
subproduct: Hotels
minor_version: "26.1"
date: 2025-10-07 00:00:00+00:00
order: 47
guid: 3a378a812e61b24c7660c6d4a20b7dfb3ce84c43
---

<strong>72466 Hotel refund Retail Charges in DRE line should not be not allowed from POS</strong>
<ul><li>An issue was fixed, with refunding a <b>Retail Charge</b> on POS, the charge cannot be refunded.</li></ul>
<strong>72433 Early checkout and night has been paid on POS throws an error</strong>
<ul><li>Fixed so the early checkout process works with paid lines, now a third option was added to the early checkout process, the options are:<ul><li>Apply the early checkout policy (Default).</li><li>Do NOT apply the early checkout policy (No penalty charged - charged only for nights stayed).</li><li>Ignore the early checkout policy (Full stay charged).</li></ul></li>
<li>Apply the early checkout policy (Default).</li>
<li>Do NOT apply the early checkout policy (No penalty charged - charged only for nights stayed).</li>
<li>Ignore the early checkout policy (Full stay charged).</li>
<li>Hotel Res Entry entries are changed to <b>checkedOut</b> so they should not be taking availability - should be able to sell the room.</li></ul>
<strong>63439 Keep same rate on reservation when changed</strong>
<ul><li><b>Keep current rates</b> option was added to the Rate Change page. When set, the current rates are used in the new dates.</li></ul>
