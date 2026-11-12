---
title: "Pharmacies hotfixes - 29.0.3 Norway, Release date November 10, 2026 - Hotfixes"
product: Pharmacies
version: "29.0.3"
subproduct: Norway
minor_version: "29.0"
date: 2026-11-10 00:00:00+00:00
order: 18
guid: 87549abbd0431a2bb960c9f4a52829e9b8270f0d
---

<strong>89100 New attribute "qs" in "Adding water" object in new PDDv2</strong>
<ul><li><b>Qs</b><b>option was added to Water Quantity UoM</b></li><li>  ◦ A <b>Qs</b> option was added to Water Quantity UoM on the prescription order line (and posted line), so pharmacists can record <b>filled to measuring line, unspecified amount</b> instead of forcing a 0 ml entry.</li><li>  ◦ Selecting Qs clears the quantity value automatically, and entering a real quantity clears Qs back out - the two are mutually exclusive.</li><li>  ◦ <b>Add Water Qty</b> dialog was fixed so a 0 ml quantity paired with Qs no longer triggers the <b>incomplete water data</b> prompt.</li><li>  ◦ The outbound eResept quality-check message and the PDD read-back mapping both use this same field now.</li></ul>
