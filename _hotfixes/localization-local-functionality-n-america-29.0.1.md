---
title: "Localization hotfixes - 29.0.1 Local Functionality N-America, Release date October 27, 2026 - Hotfixes"
product: Localization
version: "29.0.1"
subproduct: Local Functionality N-America
minor_version: "29.0"
date: 2026-10-27 00:00:00+00:00
order: 15
guid: 0febef69894ea474796d2a9202a1cc51a9056466
---

<strong>85690 Make Live Weight and Scale Validation, Banker’s Rounding, and NTEP Certification Configurable</strong>
<ul><li>Details not available.</li></ul>
<strong>87690 Click & Collect tax area not applied for Shopify orders</strong>
<ul><li>Choose whether customer orders and POS sales are taxed with the customer's tax area or the store's. Use the new <b>Use Store Tax Area</b> field on the <b>Retail Setup</b> page. If the ship-to address has a tax area, it's still used first; the setting decides what happens otherwise.</li><li>  ◦ <b>Off (default):</b> the customer's tax area is used when the customer is tax liable and has one. Otherwise, the store's tax area is used.</li><li>  ◦ <b>On:</b> the store's tax area is used. If the store does not have one, the customer's tax area is used.</li><li>With the setting on, click and collect orders from web channels, such as Shopify, are taxed with the pickup store's tax area. This applies when all items are collected at one store.</li><li>When web orders are created through the CustomerOrderCreateV6 web service, a tax area sent with the order is always kept. Click and collect orders without one now follow the setting, so with the default (off) they no longer get the pickup store's tax area automatically.</li><li><b>Action required by partners:</b></li><li>  ◦ If click and collect orders created through the CustomerOrderCreateV6 web service should keep using the pickup store's tax area, or if you want orders taxed by store rather than by customer, select Use Store Tax Area on the Retail Setup page. Otherwise, none.</li></ul>
<strong>88501 Deposit Reversal Uses Tax-Inclusive Amount as Base and Does Not Validate Deposit Balance During Collection</strong>
<ul><li>Collect customer orders created outside the POS, such as Shopify orders, without sales tax being added a second time. The POS now collects the amount the customer paid, so the deposit reversal matches the deposit.</li></ul>
