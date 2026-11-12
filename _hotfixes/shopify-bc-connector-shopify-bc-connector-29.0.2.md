---
title: "Shopify BC Connector hotfixes - 29.0.2 Shopify BC Connector, Release date November 3, 2026 - Hotfixes"
product: Shopify BC Connector
version: "29.0.2"
subproduct: Shopify BC Connector
minor_version: "29.0"
date: 2026-11-03 00:00:00+00:00
order: 30
guid: c4ec7b79919e50f571043778a3f6ea92b0c69710
---

<strong>91243 Shopify Logging Hooks in LS Central -- Current job logs and Web Service Request Logs are insufficient when troubleshooting uploads to Shopify for 60K items over a period of a 3 months.</strong>
<ul><li>New integration events let partners log Shopify requests, errors and scheduler job runs without modifying standard code:</li><li>  ◦ <b>OnAfterShopifySendGQLReq</b> <b>(codeunit LSCShopifyWebServices):</b> Raised after every Shopify GraphQL request, with the store, query, input, response, whether the request failed and the full error message. It is also raised when the API key is blank, before the request is skipped. The same event is available in the Shopify BC Connector for LS Central (codeunit LSCShpfyUtils), with the shop code instead of the store number.</li><li>  ◦ <b>OnAfterShopifyOrderError</b> <b>(codeunit LSCShopifyWebServices):</b> Raised for each customer order result that returns an error, with the order ID, update time, result code and error text.</li><li>  ◦ <b>OnAfterRunScheduleJobWithResult</b> <b>(codeunit LSC Scheduler Util):</b> raised after a scheduler job finishes, with whether the job succeeded and the error text if it failed. The existing OnAfterRunScheduleJob event is unchanged.</li><li>  ◦ <b>OnBeforeWriteToLog</b> <b>(codeunit LSCMarketUtils):</b> Raised before a web request is written to the log. A subscriber can set IsHandled to write the log somewhere else. The event is shared by the market integrations, so subscribers should filter on the function name.</li><li>In the Shopify BC Connector for LS Central, when Shopify returns several errors for one request, all of them are now kept in the error message instead of only the last one.</li><li>Behavior is unchanged when there are no subscribers.</li><li><b>Action required by partners:</b></li><li>  ◦ None.</li></ul>
<strong>90379 LS Central 28.1 – POS transaction cannot be posted after bottle voucher cash payout due to blank POS Data Entry Type</strong>
<ul><li>Post transactions that contain voucher entries without a voucher type.</li><li>Before, posting stopped with the error <b>POS Data Entry Type does not exist</b> when a voucher entry had no voucher type, for example after you suspended a transaction and retrieved it on another POS. The cash payout went through, but the transaction stayed open.</li><li>The Shopify gift card integration no longer blocks posting in this case, even if you do not use Shopify.</li></ul>
