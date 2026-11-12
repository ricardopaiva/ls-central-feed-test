---
title: "SCO hotfixes - 29.0.1 Self-Checkout Connector, Release date October 30, 2026 - Hotfixes"
product: SCO
version: "29.0.1"
subproduct: Self-Checkout Connector
minor_version: "29.0"
date: 2026-10-30 00:00:00+00:00
order: 28
guid: bbb4fb2773de5a7ec2432b939c04726bb9b5b017
---

<strong>90110 Sco Connector - Calc & Post Transaction</strong>
<ul><li>Post self-checkout transactions without recalculating them. If a price changes after the customer has been charged, posting no longer fails with a balance mismatch. It uses the amounts the customer already paid.</li><li><b>Action required by partners:</b></li><li>  ◦ To skip the recalculation when posting, subscribe to the <b>OnBeforeCalculateOnPost</b> event in the SCO Connector and set <b>SkipCalculation to true</b>. Posting then requires a zero balance, within the store's allowed difference in transactions. Discount lines are not returned in the response on this path.</li><li>  ◦ Otherwise, none.</li></ul>
