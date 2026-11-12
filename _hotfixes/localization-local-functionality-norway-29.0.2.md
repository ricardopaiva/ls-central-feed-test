---
title: "Localization hotfixes - 29.0.2 Local Functionality Norway, Release date November 3, 2026 - Hotfixes"
product: Localization
version: "29.0.2"
subproduct: Local Functionality Norway
minor_version: "29.0"
date: 2026-11-03 00:00:00+00:00
order: 12
guid: f490b3c41596cc98dd6c5b67dbd7f6e50c14b560
---

<strong>91346 Obsolete the country-specific session defaults codeunit in LS Central AL</strong>
<ul><li>The Norwegian and Swedish localization apps now set the one-copy receipt limit themselves when a session starts. The limit no longer depends on the Business Central base localization, so it applies on W1 Business Central too, and it works in every session, not only at POS login.</li><li><b>Action required by partners:</b></li><li>  ◦ Update the LS Central NO and SE apps together with LS Central 30.0 or later. With an older NO or SE app, the one-copy receipt limit is no longer enforced.</li></ul>
