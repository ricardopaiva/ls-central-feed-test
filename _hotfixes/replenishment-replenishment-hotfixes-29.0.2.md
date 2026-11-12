---
title: "Replenishment hotfixes - 29.0.2 Replenishment hotfixes, Release date October 30, 2026 - Hotfixes"
product: Replenishment
version: "29.0.2"
subproduct: Replenishment hotfixes
minor_version: "29.0"
date: 2026-10-30 00:00:00+00:00
order: 26
guid: e0236bd69767ceb2a13a572c4e2468bbb7e03b4f
---

<strong>89571 Integration Events for Replenishment Update Like-for-Like and Replenishment Calculation #715</strong>
<ul><li>The following integration events have been added to the Replenishment for LS Central extension:</li><li>  ◦ Codeunit <b>LSC REPL Update Like-for-Like</b></li><li>    ▪ OnUpdateLikeForLikeFromStmtOnBeforeInsertReplenPlannedStockDemand</li><li>  ◦ Codeunit <b>LSC REPL Calculation</b>:</li><li>    ▪ OnUpdQtyInDetailLinesTOOnBeforeDistributeReplenJrnlDetailsQuantity</li></ul>
<strong>89770 Expose GetStoreLocationFilter in Replenishment Stock Demand Worksheet</strong>
<ul><li>Global variable <b>StoreLocationFilter</b> is now protected in page <b>LSC REPL Stock Demand Wrksh</b>, so it can be accessed from page extensions.</li></ul>
<strong>90812 Planned Stock Demand Overflow Error in Replen. Journal</strong>
<ul><li><b>Delete Processed Planned Stock Demand Entries</b></li><li>  ◦ Processed Planned Stock Demand entries can now be deleted, either automatically with a scheduler job (using codeunit "LSC REPL Del. Pl.Stock Dem.") or manually with the <b>Replen. Delete Planned Stock Demand</b> report.</li><li>  ◦ A new field, <b>Days to Keep Planned Stock Demand Lines</b>, is added to the Replen. Setup page. It specifies how many days processed Planned Stock Demand entries are kept. Processed entries with a process date older than this are deleted. The remaining entries are renumbered, resetting the Entry No. sequence and freeing up available integer values.</li></ul>
