---
title: "Autotests hotfixes - 26.1.3 Autotests, Release date July 8, 2025 - Hotfixes"
product: Autotests
version: "26.1.3"
subproduct: Autotests
minor_version: "26.1"
date: 2025-07-08 00:00:00+00:00
order: 49
guid: 158700bb1bfca674f8540eb7f4a58bef183063a8
---

<strong>68248 Valid Offer not triggered in Hospitality POS</strong>
<ul><li>Resolved discount was not  applied when the Member Club did not have attributes.</li></ul>
<strong>68160 Member card number missing error when editing a CO with member points payment</strong>
<ul><li>Updated record on the POS Transactions <b>singleinstance</b> codeunit.</li><li>Fixed an issue on backoffice when opening the Member Card from a Customer order.</li></ul>
<strong>68071 Payment difference G/L line in Sales Order linked to CO</strong>
<ul><li>Rounding issue was solved when a second Sales Order was created from Customer Order. CO was created for Warehouse delivery. The SO was partly delivered. Then the Customer Order was edited on POS and additional Item was added. That resulted in an abnormal rounding line, created in the second Sales Order.</li></ul>
