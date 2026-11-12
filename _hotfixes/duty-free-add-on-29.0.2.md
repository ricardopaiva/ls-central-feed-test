---
title: "Duty Free Add-On hotfixes - 29.0.2, Release date November 10, 2026 - Hotfixes"
product: Duty Free Add-On
version: "29.0.2"
subproduct: 
minor_version: "29.0"
date: 2026-11-10 00:00:00+00:00
order: 9
guid: 833a6f8a811a4721cf143e81759271122517d59d
---

<strong>91196 Restore redirected-flight confirmation when the boarding pass does not match the store airport (Validate Sites ignored)</strong>
<ul><li>Restore the confirmation when you scan a boarding pass that does not match the store airport and Validate Sites is on. Validate Sites was being ignored, so the scan was accepted and Flight, Route, and Destination stayed empty.</li><li>Now POS asks whether the flight is redirected to the current location. If you answer No, the pass is not registered.</li><li>For a single-leg boarding pass, answering Yes now takes you straight to "Will the flight continue to the next location?", as in earlier versions. Before, POS opened the Route Leg Selection panel and ended with "Redirection of flight cancelled!", so nothing was saved.</li><li><b>Action required by partners:</b></li><li>  ◦ None. If you do not want this check, turn off Validate Sites in the Duty Free profile.</li></ul>
<strong>91859 Add integration events for boarding entry confirmation and flight redirection</strong>
<ul><li>Added integration events to change the <b>The Boarding Card is not linked to this location</b> prompt and to suppress or answer the <b>Will the flight continue to the next location?</b> prompt. The first prompt now ends with a question mark.</li><li><b>Action required by partners:</b></li><li>  ◦ None. Existing behavior is unchanged unless an extension subscribes to the new events.</li></ul>
