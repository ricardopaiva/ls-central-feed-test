---
title: "Localization hotfixes - 26.1.6 Local Functionality Germany, Release date September 18, 2025 - Hotfixes"
product: Localization
version: "26.1.6"
subproduct: Local Functionality Germany
minor_version: "26.1"
date: 2025-09-18 00:00:00+00:00
order: 63
guid: 2197c321503fbecefd17b807e3a83135da616322
---

<strong>69704 CashPointClosings do not work in Germany's Fiskaly implementation</strong>
<ul><li>Improved Cash Point Closing refresh processes.</li>
<li>Fixed Business date source.</li></ul>
<strong>70647 CashPointClosing - add non required objects</strong>
<ul><li>Included <b>non-required</b> fields, that are necessary to have a correct export.<ul><li>payment_types</li><li>amounts_per_vat_id</li><li>lines</li></ul></li>
<li>payment_types</li>
<li>amounts_per_vat_id</li>
<li>lines</li>
<li>New field on Tender Type Setup - Fiskaly Tender Type. Values:<ul><li>Bar</li><li>Unbar</li><li>ECKarte</li><li>Kreditkarte</li><li>ElZahlungsdienstleister</li><li>GuthabenKarte</li><li>Keine</li></ul></li>
<li>Bar</li>
<li>Unbar</li>
<li>ECKarte</li>
<li>Kreditkarte</li>
<li>ElZahlungsdienstleister</li>
<li>GuthabenKarte</li>
<li>Keine</li>
<li>Obsoleted: Store Card - <b>Update DSFinV-K VAT Definitions</b> action</li>
<li>Adjusted <b>LSCDE DSFinV-K Export ID</b> on <b>POS VAT Code</b> table<ul><li>Old Minimum value 1000, New minimum value 0<ul><li>This is for setting <b>default</b> Fiskaly defined IDs, custom IDs are from 1000-9999 as they were.</li></ul></li></ul></li>
<li>Old Minimum value 1000, New minimum value 0<ul><li>This is for setting <b>default</b> Fiskaly defined IDs, custom IDs are from 1000-9999 as they were.</li></ul></li>
<li>This is for setting <b>default</b> Fiskaly defined IDs, custom IDs are from 1000-9999 as they were.</li>
<li>
<p>On POS VAT Code page, the <b>Generate VAT Definitions</b> action updates every store with DSFINV-K enabled using the store's credentials.</p>
</li></ul>
<strong>70831 LSC DE - Error in Fiskaly Integration prevents statements from being posted</strong>
<ul><li>Details not available.</li></ul>
<strong>71488 LSC DE Localisation bring PopUp in POS</strong>
<ul><li>Details not available.</li></ul>
