---
title: "LS Central hotfixes - 26.1.16,  Release date August 14, 2025 - Hotfixes"
product: LS Central
version: "26.1.16"
subproduct: 
minor_version: "26.1"
date: 2025-08-14 00:00:00+00:00
order: 17
guid: 1989941852b1e3a8ebaa84dfa2d84d72ec993a4e
---

<strong>69994 Customer Order Edit - Refund Returns an Error</strong>
<ul><li>Multiple add and void lines on POS could result in an error: <b>Customer Order cannot be Updated. Changes will be rolled back</b>. This was fixed. </li></ul>
<strong>69982 Customer Order/Sales Order amount check</strong>
<ul><li>Customer Orders and Sales Orders created error in mismatch amounts. That was fixed. This was related to Customer orders in currency other than LCY.</li></ul>
<strong>69903 AL: Fix WS interfaces</strong>
<ul><li>Made SendRequest WS function public<ul><li>CustomerOrderCancel</li><li>CustomerOrderCreateV6</li><li>CustomerOrderEdit</li><li>MemberContactCreate</li><li>MemberContactUpdate.</li></ul></li>
<li>CustomerOrderCancel</li>
<li>CustomerOrderCreateV6</li>
<li>CustomerOrderEdit</li>
<li>MemberContactCreate</li>
<li>MemberContactUpdate.</li></ul>
