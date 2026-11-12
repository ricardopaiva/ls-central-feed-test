---
title: "LS Central hotfixes - 29.0.5, Release date November 10, 2026 - Hotfixes"
product: LS Central
version: "29.0.5"
subproduct: 
minor_version: "29.0"
date: 2026-11-10 00:00:00+00:00
order: 1
guid: 713403f868b29bbf76c45c848bc4ec80b6497760
---

<strong>91757 Fix permission error on Retail Purchase Order for users without extension rights</strong>
<ul><li>[Internal use only] Fix the <b>You do not have the required permissions to install the selected app</b> error that appeared for users without extension management permissions, such as users with the D365 BASIC and LSCentralPermissions permission sets.</li><li>Since version 29.0, the error appeared when opening pages like Retail Purchase Order, Retail Item Card, Retail Item List, and Retail Setup. These pages now open normally, because the check for the LS Central Labels extension no longer needs extension management permissions.</li><li><b>Action required by partners:</b></li><li>  ◦ None. You no longer need to assign the Exten. Mgt. - Admin permission set as a workaround. You can remove it from users who only had it for this reason.</li></ul>
<strong>91606 Table layout positions reset to zero – customer environment and Cronus BC28</strong>
<ul><li>Table layout now keeps its mode when you join tables, drag a table onto another one, or transfer a seating in Adjust mode, so <b>Save</b> no longer resets table sizes and positions.</li><li>Joining, disjoining and transferring by drag now save the layout straight away and refresh the view.</li><li><b>Action required by partners:</b></li><li>  ◦ None</li></ul>
<strong>91356 Self Service Kiosk: restore menu translations, session language, and speed lost since 29.0.0</strong>
<ul><li>[Internal use only] Fix Self Service Kiosk menus that showed the wrong language and loaded slowly. When a customer switches language, menu items, offers, and units now appear in the chosen language again, and the language also applies to checkout and cross-sell. Menus for a sales type open quickly however many hierarchies the store has, because the kiosk now loads them once when it starts.</li><li><b>Action required by partners:</b></li><li>  ◦ None. After you update a price, restart the kiosk or reload its page to show the new price.</li></ul>
<strong>91289 Store Inventory Worksheet issues with SN Sales Tracking</strong>
<ul><li>Two issues were fixed, in the Store Inventory worksheet for items whose serial numbers are only tracked when they are sold (SN Sales Tracking).</li><li><b>Insert Not Counted</b> now adds one line per item with the actual stock quantity, instead of a line for every serial number that was sold.</li><li>Posting a worksheet no longer leaves behind item reservation entries that stopped the next worksheet from posting.</li><li><b>Action required by partners:</b></li><li>  ◦ None for new postings. <b>Two things to know</b>:</li><li>    ▪ Serial or lot numbers entered on a worksheet line aren't carried to the item ledger entry when the item tracking code doesn't require them for that entry type.</li><li>    ▪ Reservation entries left behind by earlier postings aren't removed by this fix. If a worksheet still fails with 'Item No. must be equal to ... in Reservation Entry', contact LS Retail support to remove them.</li></ul>
<strong>91062 Fix retail pricing for activity product charges</strong>
<ul><li>Fix zero prices on additional charges. When you look up the additional charges for an activity product through the bookings web service, items set to use the retail price now return their retail price, even when no reservation exists yet.</li><li>The price is calculated for the store of the activity location you send in the request.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
<strong>90987 Click & Collect partial collection: wrong lines in the OrderPayment webhook and POS balance not zero on the second collection</strong>
<ul><li>Collect Click &amp; Collect orders item by item without errors. The payment notification that LS Central sends to the web shop now lists the items collected in that collection, instead of an empty list or the previous item. On the POS, paying in full for a later partial collection now leaves no balance.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
<strong>90839 Device dialog for printer uses Forecourt banner</strong>
<ul><li>Details not available.</li></ul>
<strong>90764 GS1 item actions (Block on POS / Ask) not enforced on SCO, Mobile POS Light and WebPOS add-to-transaction paths</strong>
<ul><li>Block a recalled lot at self-checkout. GS1 item actions now apply when you add an item with an extended barcode at self-checkout, Mobile POS Light, and WebPOS, not just on the interactive POS. Items set to <b>Block on POS</b> are rejected, and items set to <b>Ask if allowed</b> to sell are blocked too, because there is no cashier to ask. The customer sees the Text on POS message you have set.</li><li>  ◦ <b>Action required by partners:</b></li><li>    ▪ Ship the Core app and the SelfCheckOut app together. Backporting to 27.1 needs both.</li><li>    ▪ Check that your self-checkout and Mobile POS Light clients handle the new rejection codes (1008 and 1628).</li><li>    ▪ Set a <b>Text on POS</b> message on the item actions that should block a sale, so customers see a clear message.</li></ul>
<strong>90693 POS client: connect resets useCore on an existing legacy SignalR connection</strong>
<ul><li>Details not available.</li></ul>
<strong>90643 "Multiple Printer Handling" broke legacy printer routing</strong>
<ul><li>The <b>Multiple Printers Handling</b> on POS Terminal was fixed.  The default option of <b>Print to All</b> now prints to all printers as it used to in earlier versions where the Printing Role and SubRole would have to match on any additional Printer.</li><li>Additional Printers with empty Role/SubRole will not be printed to.</li><li>The new way of doing <b>Print to All</b> can be used by selecting a 3rd option in the Enum.  Where additional printers with empty Role/SubRole will also be printed to.</li></ul>
<strong>90398 Syncing Hardware Profile after running the POS is full screen</strong>
<ul><li>Details not available.</li></ul>
<strong>89886 Upcoming reservations - commands activation fix needed, seating fix</strong>
<ul><li>Details not available.</li></ul>
<strong>89507 Error thrown when running Dining Availability Search action from Bookings role center for the first time</strong>
<ul><li>[Internal use only] There was an error that appeared the first time you ran Dining Availability Search from the Bookings role center. The search now opens and shows results on the first run.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
<strong>89029 Investigate easier POS PageRunModal testing</strong>
<ul><li>Details not available.</li></ul>
<strong>88491 "LSC Customer Order Line" retain "PTE Json Carrier"</strong>
<ul><li>Attach your own data to each discount line when you create a customer order, the same way you can for the order header, lines, and payments. Your extension can read it in the <b>OnAfterCreateCustomerOrderCreateV6</b> event. The data is not saved on the created order.</li><li><b>Action required by partners:</b></li><li>  ◦ Optional. To read discount line data, add the new CustomerOrderDiscountLineTemp parameter to your OnAfterCreateCustomerOrderCreateV6 subscriber.</li></ul>
<strong>88398 Al - Changing priority for Discount Offer triggers total update for all Offers, leading to long COMMERCE_UPDATE processing times</strong>
<ul><li>Added fix for changing priority for Discount Offer triggers total update for all Offers, leading to long COMMERCE_UPDATE processing times.</li></ul>
<strong>87777 String request error - Maximum call stack size exceeded. - Dual display POS - cancel2/payment-state reset restores stale session data across transactions</strong>
<ul><li>Details not available.</li></ul>
<strong>84995 API: dataTranslations - replace GetDataTranslation</strong>
<ul><li>A new read-only API page 10014523 exposes LS Central data translations over OData v4 at GET /api/lsRetail/retailCore/v1.0/companies({id})/dataTranslations.</li><li>  ◦ It returns each entry's id, translationId, translationKey, languageCode, translation, and lastModifiedDateTime.</li><li>  ◦ Use it as the modern replacement for the legacy GetDataTranslation OData service, which keeps working unchanged.</li><li><b>Action required:</b></li><li>  ◦ None. To adopt, point clients at the new endpoint and make sure the consuming user holds the LS Central permission set.</li></ul>
<strong>82070 Lazy load SignalR libraries in POS client</strong>
<ul><li>Details not available.</li></ul>
