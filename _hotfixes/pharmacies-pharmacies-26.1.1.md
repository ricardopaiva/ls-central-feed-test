---
title: "Pharmacies hotfixes - 26.1.1 Pharmacies, Release date July 15, 2025 - Hotfixes"
product: Pharmacies
version: "26.1.1"
subproduct: Pharmacies
minor_version: "26.1"
date: 2025-07-15 00:00:00+00:00
order: 94
guid: 8b200bbe10b09ed59752d50cbe7b3b63a46a4cbb
---

<strong>67397 LS Central for pharmacies: Make procedures global</strong>
<ul><li>Procedure <b>InsertDelegateEntry</b> is visible to extensions.</li></ul>
<strong>67398 Global access to functions in codeunit 10015311 "LSC PH Item Search Management"</strong>
<ul><li>Following functions were made visible to third party extensions:<ul><li>AutoFindSubstitutionItem</li><li>SetQtyFilter</li><li>CreateSubstitutionItem</li></ul></li>
<li>AutoFindSubstitutionItem</li>
<li>SetQtyFilter</li>
<li>CreateSubstitutionItem</li></ul>
<strong>67399 Expose functions and Clear Data Permission filters in "LSC PH Session"</strong>
<ul><li>Functions <b>InitializeProfile</b> and <b>Logout in PH Session</b> were exposed.</li></ul>
<strong>67400 Global access to functions in table 10015301 "LSC PH Item"</strong>
<ul><li>Functions in table <b>Pharmacy Item</b> were exposed:<ul><li>QtyInDispense</li><li>SetLocationFilterFromStore</li></ul></li>
<li>QtyInDispense</li>
<li>SetLocationFilterFromStore</li></ul>
<strong>67401 Global access to functions in codeunit 10015455 "LSC PH Omni Prescr. Service"</strong>
<ul><li>Functions were exposed in <b>CU 10015455</b>:<ul><li>CalcSelectedPrescriptions</li><li>GetActivePrescriptions</li></ul></li>
<li>CalcSelectedPrescriptions</li>
<li>GetActivePrescriptions</li></ul>
<strong>67402 Global access to function GetCurrText in table 10015370 "LSC PH Prescription"</strong>
<ul><li>Details not available.</li></ul>
<strong>67403 Global access to functions in codeunit 10015300 "LSC PH Utility"</strong>
<ul><li>Function <b>GetPrice</b> in Pharmacy Utility was exposed.</li></ul>
<strong>67405 Global access to functions in Omni PH-Document tables</strong>
<ul><li>Functions exposed:<ul><li>Procedure <b>CreatePHDocumentFromCO</b> in table 10015455 <b>LSC PH Omni PH-Document</b></li><li>Procedure <b>CreatePHDocumentLine</b> in  table 10015456 <b>LSC PH Omni PH-Document Line</b></li></ul></li>
<li>Procedure <b>CreatePHDocumentFromCO</b> in table 10015455 <b>LSC PH Omni PH-Document</b></li>
<li>Procedure <b>CreatePHDocumentLine</b> in  table 10015456 <b>LSC PH Omni PH-Document Line</b></li></ul>
<strong>67406 Global access to functions in codeunit 10037619 "LSC PH CO Utils"</strong>
<ul><li>Function <b>PharmacyCustomerOrderCreatePHDoc</b> was exposed.</li></ul>
