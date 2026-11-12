---
title: "Pharmacies hotfixes - 29.0.1 Pharmacies, Release date November 3, 2026 - Hotfixes"
product: Pharmacies
version: "29.0.1"
subproduct: Pharmacies
minor_version: "29.0"
date: 2026-11-03 00:00:00+00:00
order: 24
guid: 73b20b4b3b02f0e5d1120816275530c4a992fdde
---

<strong>86180 Database lockings in pharma</strong>
<ul><li>Database locks on prescription order lines during dispensing were improved.</li><li>Approving a prescription line no longer holds locks on prescription order lines while the Final Control panel is being rebuilt.</li><li>The panel's inventory and reservation figures are now specific to the current store and can be read without waiting for other sessions.</li><li>  ◦ This means that users dispensing the same item in a different store will no longer be blocked by an ongoing approval process.</li></ul>
<strong>89481 Fix translation</strong>
<ul><li>There was a wrong Icelandic translation that was fixed. Navigate on Dispense Order is now set to Valmynd.</li></ul>
<strong>90233 Bag labels can now be printed after insurance is confirmed</strong>
<ul><li>Bag labels could show an insurance/customer amount split that differed from the confirmed prescription order, because labels were printed before the insurance confirmation ran.</li><li>A new flow profile step option, <b>Print Labels After Processing</b>, now prints the labels after the step has been processed, so they show the confirmed amounts.</li><li>The option is off by default, so existing behavior is unchanged.</li><li>  ◦ To use it, enable it on the flow profile step that has both Ask for No. of Bags and Confirm Insurance.</li></ul>
