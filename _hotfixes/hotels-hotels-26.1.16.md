---
title: "Hotels hotfixes - 26.1.16 Hotels, Release date September 30, 2025 - Hotfixes"
product: Hotels
version: "26.1.16"
subproduct: Hotels
minor_version: "26.1"
date: 2025-09-30 00:00:00+00:00
order: 46
guid: e4f4bdfb26b0823253ac245ddaeb07d4ad158ccc
---

<strong>72383 Cannot change property on a reservation (rate change page)</strong>
<ul><li>Now you are able to change property on a confirmed reservation without issues.</li></ul>
<strong>72380 Room allocation not reset when modifying bookings online</strong>
<ul><li>When changing the room type via web service, the room numbers were not cleared in Hotel Res Entry table. This was fixed. </li></ul>
<strong>72318 Shorten stay on an inhouse reservation throws an error on rate not found</strong>
<ul><li>There was an issue where shortening a stay on the Rate Change page gave  a <b>New Rate not found</b> error. This was fixed.</li></ul>
<strong>72084 LS Hotels 25.3.22 causing issue at the checkout steps when customer is performing Hotel Bookings on the Web</strong>
<ul><li>An issue was fixed, where changing a group status fails with error <b>Not allowed to change status from Confirmed to Confirmed</b>.</li></ul>
<strong>70170 Modify rate and discount for room types when creating a group reservation</strong>
<ul><li>In the price builder lines from the group reservation it is now possible to change the price directly by changing the new fields, either the discount % or Unit price. In the Total Amount field will then show the price based on these two fields.</li></ul>
