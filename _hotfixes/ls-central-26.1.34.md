---
title: "LS Central hotfixes - 26.1.34, Release date October 18, 2025 - Hotfixes"
product: LS Central
version: "26.1.34"
subproduct: 
minor_version: "26.1"
date: 2025-10-18 00:00:00+00:00
order: 2
guid: 74fc12202e6b4591d186267f5a05cda4cb6c53d2
---

<strong>73333 Issue with Retail Sales Order Currency Code for Customer Order with Sourcing Location</strong>
<ul><li>The logic was fixed, so the Sales Header currency code is now set based on the Customer Order’s Created Store currency instead of the Sourcing Store’s currency.</li></ul>
<strong>72762 Fix UpdateLock</strong>
<ul><li>Ref. to internal variable was changed, when getting last register number.</li></ul>
<strong>69530 LSC NA CA - Split the bill in 2, and the amount with taxes is not equally split</strong>
<ul><li>Details not available.</li></ul>
<strong>69137 Basis for calculating administrative costs - retail charge</strong>
<ul><li>When calculating retail charge with variable %, the net amount or gross amount is used as bases for the retail charge, not the net price or price * quantity as before.</li></ul>
