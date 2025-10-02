# LS Central Hotfixes RSS Feed

This repository provides an automatically generated RSS feed for LS Central hotfixes, based on the official [LS Central Hotfixes documentation](https://help.lscentral.lsretail.com/Content/Hotfixes/Hotfixes-26-1.htm). The goal is to help partners and users stay up to date with the latest hotfix releases for each LS Central product.

## 📢 How to Subscribe to the RSS Feeds

All available RSS feeds can be found and subscribed to on the following page:

👉 [https://ricardopaiva.github.io/ls-central-feed/](https://ricardopaiva.github.io/ls-central-feed/)

Visit this page to browse and subscribe to product-specific or all-in-one RSS feeds. Simply click the RSS link or copy the feed URL into your preferred RSS reader.

## Features

- **Latest Major Version:** Currently, only the latest Business Central major version is included in the feeds.
- **Easy Subscription:** Partners can subscribe to product-specific or all-in-one RSS feeds to receive notifications about new hotfixes.

## How It Works

1. The Python script [`scripts/generate_rss_v26.1.py`](scripts/generate_rss_v26.1.py) fetches and parses the official LS Central Hotfixes page.
2. It generates Markdown files for each hotfix in the [`_hotfixes`](./_hotfixes) collection.
3. It creates RSS feed templates in the [`feeds`](./feeds) directory.
4. The static site is built using Jekyll, which processes the hotfix data and generates the RSS feeds.
5. GitHub Pages is used for hosting and deploying the site, making the RSS feeds publicly accessible for partners to subscribe.
6. The deployment workflow is scheduled to run automatically once a day, ensuring the site and feeds are always up to date with the latest hotfixes.

## Contributing & Feedback

Partners and users are welcome to open issues in this repository to make suggestions or request additional features.

---

**Disclaimer:**  

It is **not** an official tool from LS Retail.  

This is a personal repository created by me, based on a request from a partner.  
Built for fun, curiosity, and a bit of RSS magic. If it breaks, you know exactly who to blame!

Note that the script generates the feeds based on data from the LS Central release notes in the official documentation. This means the RSS feed will only be updated with a new hotfix after it has been added to the release notes pages.