---
title: "Hotels hotfixes - 26.1.5 Hotels, Release date July 22, 2025 - Hotfixes"
product: Hotels
version: "26.1.5"
subproduct: Hotels
minor_version: "26.1"
date: 2025-07-22 00:00:00+00:00
order: 63
guid: fc47fd284a4351d6d02d29a5dc74f5fad3518af4
---

<div><strong>69255 LS Hotel > Tape Chart cuts the display of hotel reservations that runs through dates with more than 7 nights stay</strong>
<ul><li>Fixed an issue where reservations that were booked over new year disappeared when moving dates on the tape chart.</li></ul>
<strong>69196 Open Hotel Reservation Deposit page from the POS</strong>
<ul><li>Now able to open the reservation deposit page from the folio deposit on the POS hotel template.</li></ul>
<strong>69155 Changing the Folio for a DRE posted to Finance results returns an error</strong>
<ul><li>Fixed update issue on changing <b>Folio No.</b> for posted revenue line <b>Detailed Revenue Entry</b>.</li></ul>
<strong>67503 Reconciliation tool - Fix duplicated room charge issues</strong>
<ul><li>New changes added to <b>Reconciliation Tool</b> to solve deposit issues related to duplicated charges to room created.</li>
<li>Added a new field next to filters to <b>Skip Deposit Checks</b>, so the process  runs faster by enabling it. Disabled by default.</li>
<li>New action, <b>Fix Duplicated Charges to Room</b>, added to fix the records with code 'C2R:DUPLICATED' found previously in the fixing process:<ul><li>If duplicated DRE line is not posted to finance, it deactivates the line and creates a reversal line with negative original amount.</li><li>If duplicated DRE line is posted to finance, it reverses the line as usual and needs to run the Night Audit to post it again.</li></ul></li>
<li>If duplicated DRE line is not posted to finance, it deactivates the line and creates a reversal line with negative original amount.</li>
<li>If duplicated DRE line is posted to finance, it reverses the line as usual and needs to run the Night Audit to post it again.</li>
<li>Additionally, <b>Fix tips</b> action was changed to include also searching of duplicated tips. So in the searching process, it also looks for tips from duplicated room charges, it adds DUPLICATED label for them in Description field. The fixing process works also for it. New field <b>Res. Balance</b> added because some cases were found, that were fixed manually by using a negative res. extra, and balance is correct and does not need to be fixed. The user has the information to decide whether to fix it or not.</li></ul></div>
