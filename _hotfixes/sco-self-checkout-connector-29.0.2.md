---
title: "SCO hotfixes - 29.0.2 Self-Checkout Connector, Release date November 10, 2026 - Hotfixes"
product: SCO
version: "29.0.2"
subproduct: Self-Checkout Connector
minor_version: "29.0"
date: 2026-11-10 00:00:00+00:00
order: 27
guid: 466ac5ae79aedcfc3d01d6d3ec622b0743d27041
---

<strong>90764 GS1 item actions (Block on POS / Ask) not enforced on SCO, Mobile POS Light and WebPOS add-to-transaction paths</strong>
<ul><li>Block a recalled lot at self-checkout. GS1 item actions now apply when you add an item with an extended barcode at self-checkout, Mobile POS Light, and WebPOS, not just on the interactive POS. Items set to <b>Block on POS</b> are rejected, and items set to <b>Ask if allowed</b> to sell are blocked too, because there is no cashier to ask. The customer sees the Text on POS message you have set.</li><li>  ◦ <b>Action required by partners:</b></li><li>    ▪ Ship the Core app and the SelfCheckOut app together. Backporting to 27.1 needs both.</li><li>    ▪ Check that your self-checkout and Mobile POS Light clients handle the new rejection codes (1008 and 1628).</li><li>    ▪ Set a <b>Text on POS</b> message on the item actions that should block a sale, so customers see a clear message.</li></ul>
