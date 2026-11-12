---
title: "Shopify BC Connector hotfixes - 29.0.3 Shopify BC Connector, Release date November 10, 2026 - Hotfixes"
product: Shopify BC Connector
version: "29.0.3"
subproduct: Shopify BC Connector
minor_version: "29.0"
date: 2026-11-10 00:00:00+00:00
order: 29
guid: 33874433fa9364f4322b68fb28928a353e667cab
---

<strong>91901 Missing transaction when order captured web pre-auth as a Payment line on the collect transaction with discounts</strong>
<ul><li>Orders with a line discount now come into LS Central with the same discount percent as in Shopify.</li><li>Previously, when prices included VAT, the percent was calculated on the net amount and came out too high (for example, 23.81 instead of 20).</li><li>Because the POS recalculates the line from that percent, the line amount no longer matched the captured payment, and finishing the sale with the web tender didn't create a payment entry.</li><li>The line amount now matches the Shopify payment, so the payment is registered.</li><li>The percent is now stored with five decimals, so non-round discounts also reproduce the Shopify line amount. A discount that is given on the whole order rather than on the lines is now calculated from the gross line total, and an order that is free after the discount no longer fails at that step of the import.</li><li><b>Action required by partners:</b></li><li>  ◦ None</li></ul>
<strong>91170 Extension of LS/Shopify connector for new brand field in Item</strong>
<ul><li>You can now send an item's brand to Shopify as the product vendor. Turn on Use Brand as Vendor on the Shopify Shop card, and products whose item has a brand show the brand name as the vendor in Shopify. Items without a brand keep their vendor name. If you use Item HTML with vendor information, the product description also gets a Brand row, and the vendor stays in the description.</li><li>  ◦ <b>Action required by partners:</b></li><li>    ▪ None. The new option is off by default.</li></ul>
