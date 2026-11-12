---
title: "Shopify BC Connector hotfixes - 29.0.1 Shopify BC Connector, Release date October 30, 2026 - Hotfixes"
product: Shopify BC Connector
version: "29.0.1"
subproduct: Shopify BC Connector
minor_version: "29.0"
date: 2026-10-30 00:00:00+00:00
order: 31
guid: 8ab72de72703a8dee925265c9deeafa85428289e
---

<strong>90327 Shopify BC Connector – Customer metafields ("LS MetaData") fail: wrong table ID for LSC Member Contact</strong>
<ul><li>Fix the Shopify customer metafields (<b>LS MetaData</b>) sync, which failed because the connector read the wrong table. Customer metafields now come from the member contact, so they reach Shopify as expected.</li><li>A B2B MetaData setting was also added to the Shopify shop card, in a new Meta Data group.</li><li>  ◦ Turn it on to send customer metadata for B2B customers instead of member contact metadata.</li><li>  ◦ The metadata actions for customers and products now do nothing when Use MetaData is off.</li><li>  ◦ When you export a member contact to Shopify, its metafields now go to the new Shopify customer.</li><li><b>Action required by partners:</b></li><li>  ◦ If you use customer metafields and send them from the customer record, turn on B2B MetaData on the Shopify shop card. Without it, metadata is sent from the member contact. Re-map any customer metafield mappings that use the member point register table to the member contact table.</li></ul>
<strong>90145 Posting fulfilled Shopify order does not close CO / SO</strong>
<ul><li>Posting of Sales Order when pulling fulfilled order from Shopify was fixed.</li></ul>
