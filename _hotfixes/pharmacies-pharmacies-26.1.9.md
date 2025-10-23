---
title: "Pharmacies hotfixes - 26.1.9 Pharmacies, Release date October 21, 2025 - Hotfixes"
product: Pharmacies
version: "26.1.9"
subproduct: Pharmacies
minor_version: "26.1"
date: 2025-10-21 00:00:00+00:00
order: 95
guid: 8c2eb33ad05dc836182806acb238e87fcca290e0
---

<strong>71975 NO Upgrade: WT Not possible to download more than 2 prescriptions</strong>
<ul><li>Changed from POS Menu Line Parameter to POS Control Event (same as field changed).</li></ul>
<strong>72045 Pharmacy Dispense - Posting invoice</strong>
<ul><li>VAT calculation in Dispense Invoicing was fixed.</li></ul>
<strong>72647 Event OnBeforeSetDispensePostedOrderReservedAtPOS in function GetProductionOnClose in codeunit 10015658 "LSC PH Dispense POS Cmd"</strong>
<ul><li>Previous event <b>OnBeforeReserveDispensePostedOrderAtPOS</b> is obsoleted and was replaced with <b>OnBeforeReserveDispensePostedOrderAtPOSV2</b> with added parameters and Handled pattern.</li></ul>
<strong>73220 Function Exposures Swipe</strong>
<ul><li>Details not available.</li></ul>
