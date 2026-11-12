---
title: "LS Central hotfixes - 29.0.4, Release date November 3, 2026 - Hotfixes"
product: LS Central
version: "29.0.4"
subproduct: 
minor_version: "29.0"
date: 2026-11-03 00:00:00+00:00
order: 2
guid: d95a32f66128355d51e821a0d24970d2f1950cbf
---

<strong>91243 Shopify Logging Hooks in LS Central -- Current job logs and Web Service Request Logs are insufficient when troubleshooting uploads to Shopify for 60K items over a period of a 3 months.</strong>
<ul><li>New integration events let partners log Shopify requests, errors and scheduler job runs without modifying standard code:</li><li>  ◦ <b>OnAfterShopifySendGQLReq</b> <b>(codeunit LSCShopifyWebServices):</b> Raised after every Shopify GraphQL request, with the store, query, input, response, whether the request failed and the full error message. It is also raised when the API key is blank, before the request is skipped. The same event is available in the Shopify BC Connector for LS Central (codeunit LSCShpfyUtils), with the shop code instead of the store number.</li><li>  ◦ <b>OnAfterShopifyOrderError</b> <b>(codeunit LSCShopifyWebServices):</b> Raised for each customer order result that returns an error, with the order ID, update time, result code and error text.</li><li>  ◦ <b>OnAfterRunScheduleJobWithResult</b> <b>(codeunit LSC Scheduler Util):</b> raised after a scheduler job finishes, with whether the job succeeded and the error text if it failed. The existing OnAfterRunScheduleJob event is unchanged.</li><li>  ◦ <b>OnBeforeWriteToLog</b> <b>(codeunit LSCMarketUtils):</b> Raised before a web request is written to the log. A subscriber can set IsHandled to write the log somewhere else. The event is shared by the market integrations, so subscribers should filter on the function name.</li><li>In the Shopify BC Connector for LS Central, when Shopify returns several errors for one request, all of them are now kept in the error message instead of only the last one.</li><li>Behavior is unchanged when there are no subscribers.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
<strong>91242 Shopify Price Sync in LS Central : Price calculation hooks with IsHandled in LSCShopifySchPrice (codeunit 10034383)</strong>
<ul><li><b>Two new integration events</b> are available in the Shopify price synchronization, so partners can replace the standard price calculation with their own logic without modifying standard code. Each event has an IsHandled parameter: when a subscriber sets it, the standard logic is skipped.</li><li>  ◦ <b>OnBeforeGetPrices (codeunit LSCShopifySchPrice):</b> Raised at the start of GetPrices. When handled, the subscriber's result and prices are used and the changed-since-last-run filter, discount lookup and standard price calculation are skipped.</li><li>  ◦ <b>OnPushPriceOnBeforeGetVariantPrice (codeunit LSCShopifySchPrice):</b> Raised for each variant before the variant price is looked up. When handled, the standard variant price lookup is skipped and the subscriber's UnitPrice, ComparePrice, NoTax and HaveNewPrice values are used.</li><li>Price synchronization to Shopify is unchanged when there are no subscribers.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
<strong>90901 Can not print multiple Kitchen slips after send to kitchen</strong>
<ul><li>Kitchen orders print every configured copy again. If you list the same printer several times in the hardware profile for a role and sub role, each kitchen order prints one slip per line, as it did in version 27. Since 28.1, only one slip printed. Different printers under the same sub role each print a slip too.</li><li><b>Action required by partners:</b></li><li>  ◦ None</li></ul>
<strong>90825 Overflow under conversion of Microsoft.Dynamics.Nav.Runtime.Decimal18 value 22.47 to System.Int32</strong>
<ul><li>Sell items in a special group without hitting an overflow error when the discount percentage has decimals. The POS now picks the best discount correctly when an item belongs to several special groups.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
<strong>90638 Add OnAfterCOPrintShipOrder event</strong>
<ul><li>New event <b>OnAfterCOPrintShipOrder</b> was added to <b>LSC POS Print Utility CO</b> codeunit.</li></ul>
<strong>90637 Add new POS Print events for CO elements on Sales Slip</strong>
<ul><li>New events <b>OnAfterPrintPaymentInfo</b> and <b>OnBeforePrintCustomerLine</b> were added.</li></ul>
<strong>90379 LS Central 28.1 – POS transaction cannot be posted after bottle voucher cash payout due to blank POS Data Entry Type</strong>
<ul><li>Post transactions that contain voucher entries without a voucher type.</li><li>Before, posting stopped with the error <b>POS Data Entry Type does not exist</b> when a voucher entry had no voucher type, for example after you suspended a transaction and retrieved it on another POS. The cash payout went through, but the transaction stayed open.</li><li>The Shopify gift card integration no longer blocks posting in this case, even if you do not use Shopify.</li></ul>
<strong>89318 Add OnAfterLoadMatrixCell event in LoadMatrix in page DimensionMatrix 10001420</strong>
<ul><li>Details not available.</li></ul>
<strong>87277 Coupon with Affects=Next Item Line not applied</strong>
<ul><li>Store Coupons configured with Affects set to Next Item Line now apply their discount correctly when scanned before the qualifying item.</li><li>Previously, the coupon was silently voided at Total instead of discounting the item.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
