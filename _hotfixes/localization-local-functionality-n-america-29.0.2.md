---
title: "Localization hotfixes - 29.0.2 Local Functionality N-America, Release date November 3, 2026 - Hotfixes"
product: Localization
version: "29.0.2"
subproduct: Local Functionality N-America
minor_version: "29.0"
date: 2026-11-03 00:00:00+00:00
order: 11
guid: 91c34f6e40eb867b27512b4ab693378c440e176d
---

<strong>91198 Max, Min and Live weight should use formatted qty amounts</strong>
<ul><li>See the Max, Min, and Live weight values on the POS screen in the same 2:2 format as other weights when NTEP Certification is turned on. The POS client produces these values, so they follow the format only where the client uses the quantity formatting. The text on the <b>Capacity By Division Size</b> button comes from setup and does not  change.</li><li><b>Action required by partners:</b></li><li>  ◦ To show two decimal places in the <b>Capacity By Division Size</b> button text, update the text in setup.</li></ul>
<strong>91197 Formatting for quantity values to have 2:2 decimal precision</strong>
<ul><li>See weights with two decimal places everywhere they appear when NTEP Certification is turned on in the POS functionality profile. The 2:2 format now applies to the Qty column in the POS journal and to the net and tare weights on receipts, including reprints and receipts printed after payment.</li><li>Before, it applied only while the selected line was a scale item. Quantities in other units do not change, and nothing changes when NTEP Certification is off.</li></ul>
<strong>89751 Discount Posting in Statement loses Item Dimensions due to LSCNA</strong>
<ul><li>Keep item dimensions on discount entries when you post POS statements. Discount G/L entries now keep the item, customer, and sales type dimensions of the sales line. Before, the first taxed line of a transaction lost these dimensions on its discount entries.</li></ul>
<strong>89750 Check EBT Balance</strong>
<ul><li>Check the balance of an EBT card at the POS before you take payment. Use the EBT_BALANCE_DIALOG command to run the balance inquiry and show the balance in a message once the terminal approves it.</li><li>The EBT_BALANCE command runs the same inquiry without showing the balance, so the EBT amount check can use it when you tender. Both commands take the EBT tender type code as the parameter and work on a sale with no lines yet.</li><li>The inquiry does notcharge the card. A declined, canceled, or failed inquiry is no longer recorded as approved, and it no longer triggers the failed card payment recovery on the next card tender.</li><li><b>Action required by partners:</b></li><li>  ◦ To show the balance on screen, add the EBT_BALANCE_DIALOG command to a POS button and enter the EBT tender type code as the parameter.</li></ul>
<strong>89702 POS tender fails with 'No POS Functionality Profile found with Code'</strong>
<ul><li>Tender a sale on a POS terminal that has no functionality profile assigned without getting the error <b>No POS Functionality Profile found with Code</b>. The payment amount calculation now uses the functionality profile the POS has already resolved for the session.</li></ul>
