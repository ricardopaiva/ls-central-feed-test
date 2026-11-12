---
title: "Web Kitchen Service hotfixes - 29.0.1 Web KDS, Release date October 27, 2026 - Hotfixes"
product: Web Kitchen Service
version: "29.0.1"
subproduct: Web KDS
minor_version: "29.0"
date: 2026-10-27 00:00:00+00:00
order: 37
guid: 413c4d54083f0867311cd8802e16791c593fb3f4
---

<strong>89798 Printer does not follow "Show only routed items"</strong>
<ul><li>Print Order on Expeditor stations now follows the <b>Show Only Routed Items setting</b>, so Bar items that are not routed to the Expeditor station are no longer printed.</li><li>  ◦ Previously, when Show Only Routed Items was enabled, Print Order on an Expeditor station ignored the setting and printed every item of the order, including items routed only to other stations such as the Bar printer. Print Order on an Expeditor station now prints only the items routed to that Expeditor station, which matches what the Expeditor screen displays. Printing from other station types is unchanged.</li><li>  ◦ Restaurants that have Show Only Routed Items enabled only see the routed items on Expeditor printed order slips, with Bar items removed. No configuration change is required, as the existing Show Only Routed Items store setting is used. When the setting is disabled, Expeditor printing behaves as before.</li></ul>
<strong>90687 Fix SonarCloud Reliability findings (C# and frontend)</strong>
<ul><li>Internal code-quality clean-up of the Kitchen Display System that resolves open SonarCloud reliability findings in the service and the Web KDS. There is no functional change to configuration or to how orders are processed.</li><li>  ◦ On the service side, shutdown and restart handling now honours cancellation more consistently, so a graceful shutdown skips its short grace period when a shutdown is already underway, and store database queries are now issued as split queries, which return the same data as before.</li><li>    ▪ On the Web KDS, order cards can now be selected with the keyboard (Tab to focus, Enter or Space to select), and the password field in the confirmation dialog has an accessible label, and a few other clickable elements and inputs were made keyboard- and screen-reader-friendly.</li><li>    ▪ Behaviour for mouse and touch users is unchanged.</li><li>  ◦ No user action is required and no settings need to be changed. Keyboard and screen-reader users of the Web KDS can now operate order cards and the password prompt more easily. Restaurants will not see any other difference in day-to-day operation.</li></ul>
