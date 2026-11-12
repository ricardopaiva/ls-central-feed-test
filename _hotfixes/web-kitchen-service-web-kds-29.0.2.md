---
title: "Web Kitchen Service hotfixes - 29.0.2 Web KDS, Release date November 3, 2026 - Hotfixes"
product: Web Kitchen Service
version: "29.0.2"
subproduct: Web KDS
minor_version: "29.0"
date: 2026-11-03 00:00:00+00:00
order: 36
guid: 1618372a3019df4330a0ee7dc4a87b2e9600c20c
---

<strong>75730 WKS Package Vulnerability Solve (Bringing back FrontEnd Unit tests)</strong>
<ul><li>Details not available.</li></ul>
<strong>89715 KDS Performance and Label Printer Issue</strong>
<ul><li>There was an issue where an offline label printer could slow down the Kitchen Display System for all stations, including order intake, recall and bump.</li><li>  ◦ Print requests sent to a printer that could not be reached kept the KDS waiting for minutes, which delayed other work. Each print request to the Hardware Station now stops waiting after a set time, and a printer that cannot be reached is paused for a growing period before the KDS tries it again. These timings are configurable under Printer Resilience on the Time Intervals screen, with Print Timeout In Seconds (default 15), First Retry Wait In Seconds (default 30) and Maximum Retry Wait In Seconds (default 300).</li><li>  ◦ Orders, recalls and bumps should stay responsive while a label printer is offline. Items for a paused printer are not printed during the pause and are printed again once the printer responds, so check the label printer if labels appear to be missing.</li><li>  ◦ No action is required unless you want to change the timing values.</li></ul>
<strong>89798 Printer does not follow "Show only routed items"</strong>
<ul><li>Print Order on Expeditor stations now follows the <b>Show Only Routed Items setting</b>, so Bar items that are not routed to the Expeditor station are no longer printed.</li><li>  ◦ Previously, when Show Only Routed Items was enabled, Print Order on an Expeditor station ignored the setting and printed every item of the order, including items routed only to other stations such as the Bar printer. Print Order on an Expeditor station now prints only the items routed to that Expeditor station, which matches what the Expeditor screen displays. Printing from other station types is unchanged.</li><li>  ◦ Restaurants that have Show Only Routed Items enabled only see the routed items on Expeditor printed order slips, with Bar items removed. No configuration change is required, as the existing Show Only Routed Items store setting is used. When the setting is disabled, Expeditor printing behaves as before.</li></ul>
<strong>90687 Fix SonarCloud Reliability findings (C# and frontend)</strong>
<ul><li>Internal code-quality clean-up of the Kitchen Display System that resolves open SonarCloud reliability findings in the service and the Web KDS. There is no functional change to configuration or to how orders are processed.</li><li>  ◦ On the service side, shutdown and restart handling now honours cancellation more consistently, so a graceful shutdown skips its short grace period when a shutdown is already underway, and store database queries are now issued as split queries, which return the same data as before.</li><li>    ▪ On the Web KDS, order cards can now be selected with the keyboard (Tab to focus, Enter or Space to select), and the password field in the confirmation dialog has an accessible label, and a few other clickable elements and inputs were made keyboard- and screen-reader-friendly.</li><li>    ▪ Behaviour for mouse and touch users is unchanged.</li><li>  ◦ No user action is required and no settings need to be changed. Keyboard and screen-reader users of the Web KDS can now operate order cards and the password prompt more easily. Restaurants will not see any other difference in day-to-day operation.</li></ul>
<strong>91008 Vulnerabilities on npm packages</strong>
<ul><li>Details not available.</li></ul>
