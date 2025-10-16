---
title: "Autotests hotfixes - 26.1.12 Autotests, Release date September 8, 2025 - Hotfixes"
product: Autotests
version: "26.1.12"
subproduct: Autotests
minor_version: "26.1"
date: 2025-09-08 00:00:00+00:00
order: 37
guid: eaf325e854815d5747f28e9bc9bcae09f66895d0
---

<strong>70835 Member Point Offer Not Triggering by Item Category After Upgrade to Version 26.1</strong><ul><li>The list of offers were only filtered by Item. This was fixed and  now finds an offer based on all types.</li></ul>
<strong>70601 Member Scheme Upgrade Skips a Level</strong><ul><li>Details not available.</li></ul>
<strong>70216 Referenced refund - Partial amount refund</strong><ul><li>When doing a referenced refund on a card payment in the POS, the POS now is able to do a partial amount refund. that is not fully refund the entire original amount of the card payment. The refunded amount for the card payment is stored on the original Card Entry for the payment and can be viewed in the <b>Transaction Registry</b> -&gt; <b>Card Entries</b> view for the original transaction.</li>
<li>When doing a second refund on the same payment the amount that is presented to the cashier has to be the remaining amount available for refund on the card payment not the original amount.</li>
<li>To activate this functionality configurations <b>Use Reference Refund</b> and <b>Use Refund Selection</b> must both be active.</li></ul>
