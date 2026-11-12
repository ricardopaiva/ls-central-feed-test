---
title: "Pharmacies hotfixes - 29.0.2 Norway, Release date November 3, 2026 - Hotfixes"
product: Pharmacies
version: "29.0.2"
subproduct: Norway
minor_version: "29.0"
date: 2026-11-03 00:00:00+00:00
order: 22
guid: ec52e07a326cb487d1b55dab4fab68761dcd6a05
---

<strong>86428 Error when registering C-vitamin on refusjonskode §5-25 (yrkesskade)</strong>
<ul><li>There was an error when registering C-vitamin on refusjonskode §5-25 (yrkesskade). This was fixed.</li></ul>
<strong>87819 Get Lines in Credit Orders deletes order when ePrescription is inactive - Missing Credit type</strong>
<ul><li>Credit orders no longer get deleted when you select Finish Credit after adding lines with Get Lines. Get Lines now sets the credit type, so you can complete the credit.</li></ul>
<strong>89100 New attribute "qs" in "Adding water" object in new PDDv2</strong>
<ul><li><b>Qs</b> <b>option was added to Water Quantity UoM</b></li><li>  ◦ A <b>Qs</b> option was added to Water Quantity UoM on the prescription order line (and posted line), so pharmacists can record <b>filled to measuring line, unspecified amount</b> instead of forcing a 0 ml entry.</li><li>  ◦ Selecting Qs clears the quantity value automatically, and entering a real quantity clears Qs back out - the two are mutually exclusive.</li><li>  ◦ <b>Add Water Qty</b> dialog was fixed so a 0 ml quantity paired with Qs no longer triggers the <b>incomplete water data</b> prompt.</li><li>  ◦ The outbound eResept quality-check message and the PDD read-back mapping both use this same field now.</li></ul>
<strong>90646 Close Multiple Item Selection Behavior Change</strong>
<ul><li>On a product group prescription, closing the Multiple Items Selection page with Close, X, or Esc now keeps your selection. You get a prescription order line for each item you selected.</li><li>The page has a single Close button instead of OK and Cancel. To close it without keeping your changes, choose Discard Selection.</li></ul>
<strong>91357 76787 - Prescription dispatch request: Warning needed when prescription is downloaded before dispatch request is received</strong>
<ul><li>Reverted issue 76787, removing the warning that appeared when prescription is downloaded before dispatch request is received.</li></ul>
