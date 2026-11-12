---
title: "Autotests hotfixes - 29.0.1 Autotests, Release date October 30, 2026 - Hotfixes"
product: Autotests
version: "29.0.1"
subproduct: Autotests
minor_version: "29.0"
date: 2026-10-30 00:00:00+00:00
order: 8
guid: 5e5af3f51311ee973533d74a2714fc5bc50b1d5f
---

<strong>90853 Book captured web pre-auth as a Payment line on the collect transaction; fix mixed Payment + Pre-Auth double booking</strong>
<ul><li>Collecting a web order that was paid in advance now creates a payment line on the POS transaction. The statement posts that payment, so the transaction balances and has transaction payment entries. Orders that mix a payment and a pre-authorization no longer book the pre-authorized amount twice.</li><li><b>Action required by partners:</b></li><li>  ◦ Check that the collecting POS uses a local request. Open the POS functionality profile of the terminal and go to <b>Web Requests &gt; CustomerOrderUpdateV5</b>. On the highest-priority row, set <b>Local Request</b> to <b>Yes</b> and leave <b>Dist. Location</b> <b>blank</b>. Remote setups keep posting to the general ledger.</li></ul>
<strong>90230 Reactivate Insert Job Queue Default Entries action on Kitchen Service Configuration</strong>
<ul><li>The <b>Insert Job Queue Default Entries</b> action on the Kitchen Service Configuration page works again. It creates the Web KDS job queue category and the <b>Update routing information for Kitchen Display Stations</b> job. If the job already exists, the action resets it to the default settings.</li><li><b>Action required by partners:</b></li><li>  ◦ After you run the action, the new job queue entry is On Hold. Set its status to Ready so the routing update starts running.</li></ul>
<strong>89446 Issue with coupon and items with barcode pricing</strong>
<ul><li>A tender coupon can now be used on an item scanned with a price in the barcode, when that price is lower than the item's standard price.</li></ul>
<strong>89432 OneListCalculate results in coupon reservation</strong>
<ul><li>Calculate a web basket with a serial-number coupon, and the coupon is now validated and priced without being reserved.</li><li>  ◦ Previously, the calculation reserved the coupon for the web store POS terminal. If the shopper left without completing the order, the coupon stayed locked for the rest of the day, and a store POS showed the message that the coupon is reserved by another terminal.</li><li>  ◦ Now the coupon stays available in stores until an order is actually placed. A coupon that another terminal has reserved is still rejected, and placing the web order, the POS and Self-Checkout reserve coupons as before.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
<strong>89291 Mix & Match offer with Coupon condition is not removed when the coupon is voided from the transaction</strong>
<ul><li>Voiding a coupon line in the POS now removes the Mix &amp; Match offer discount from all lines when the coupon condition is no longer met.</li></ul>
<strong>89177 CO Prepayment - post to account</strong>
<ul><li>Customer orders paid with Post to Account now create the right customer claim and output VAT when you post the sales order. Before, the amount was closed against a prepayment invoice, so no claim was created and no VAT was posted.</li><li>When you use prepayment invoices, only the paid share of an order is now prepayment-invoiced. A mixed order, partly paid by cash or card and partly posted to the customer's account, is invoiced for just the paid amount.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
