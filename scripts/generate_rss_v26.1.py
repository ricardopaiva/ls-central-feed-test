import requests
from bs4 import BeautifulSoup
import os
from slugify import slugify
import hashlib

URL = "https://help.lscentral.lsretail.com/Content/Hotfixes/Hotfixes-26-1.htm"


def parse_items(item_details_tags):
    items = []

    current_item = None

    for item_details_tag in item_details_tags:
        if item_details_tag.name == 'h4':
            current_item_title = item_details_tag.get_text(strip=True)
            current_item_details = []

            current_item = (current_item_title, current_item_details)
            items.append(current_item)

        elif item_details_tag.name == 'ul':
            details = item_details_tag.select("li")
            for detail in details:
                current_item_details.append(detail)

    return items


def scrape_release_notes(content_div):
    if content_div:
        # Parses the main content container and extracts the products (LS Central, Hotels, Localization, etc)
        products = {}
        current_product = None

        versions = {}
        current_version = None

        items  = {}
        for content_tag in content_div.find_all(['h3', 'div'], recursive=False):
            if content_tag.name == 'h3':
                current_product = clean_text(content_tag.get_text(strip=False))
                products[current_product] = {}
                versions = products[current_product]
                current_version = None

            elif content_tag.name == 'div' and current_product:
                for products_subtag in content_tag.find_all(['a', 'div'], recursive=True):
                    if products_subtag.name == 'a':
                        # current_version = extract_version(products_subtag.get_text(strip=True))
                        current_version = products_subtag.get_text(strip=True)
                        versions[current_version] = []
                    elif products_subtag.name == 'div' and current_product and current_version:
                        item_details_tags = products_subtag.find_all(['h4', 'ul'], recursive=False)
                        items = parse_items(item_details_tags)
                        versions[current_version].append(items)

        return products
    else:
        print("No article content found.")


def extract_release_date(version_str):
    """
    Extracts the release date from a version string like:
    '26.1.0, Release date July 8, 2025'
    Returns a timezone-aware datetime object. If not found, returns current UTC time.
    """
    import re
    from datetime import datetime, timezone
    match = re.search(r"Release date ([A-Za-z]+ \d{1,2}, \d{4})", version_str)
    if match:
        date_str = match.group(1)
        try:
            return datetime.strptime(date_str, "%B %d, %Y").replace(tzinfo=timezone.utc)
        except Exception:
            pass
    return datetime.now(timezone.utc)


def extract_version(version_str: str) -> str:
    """
    Extracts the version number from a version string like:
    '26.1.0, Release date July 8, 2025'
    Returns the version as a string (e.g., '26.1.0').
    If not found, returns an empty string.
    """
    import re
    match = re.match(r"^([\d\.]+)", version_str.strip())
    if match:
        return match.group(1)
    return ""


def extract_sub_product_from_version(version_str: str) -> str:
    """
    Extracts the sub product from a version string like:
    '26.1.0 Local Functionality Germany, Release date July 8, 2025'
    Returns the sub product as a string (e.g., 'Local Functionality Germany').
    If not found, returns an empty string.
    """
    import re
    match = re.match(r"^[\d\.]+\s+(.*?)\s*,\s*Release date", version_str.strip())
    if match:
        return match.group(1).strip()
    return ""


def clean_text(text):
    """Clean text by replacing encoded characters with their readable equivalents"""
    replacements = {
        '\xa0': ' ',  # non-breaking space
        '\u200b': '',  # zero-width space
        '\u2019': "'", # smart quote
        '\u2018': "'", # smart quote
        '\u201c': '"', # smart quote
        '\u201d': '"', # smart quote
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def generate_hotfixes(content):
    hotfixes = []
    sort_id = 0
    for product, versions in content.items():
        for version, items_list in versions.items():
            title = f"{product} - {version} - Hotfixes"
            pub_date = extract_release_date(version)
            guid = hashlib.sha1(title.encode("utf-8")).hexdigest()

            content_items = []
            for items in items_list:
                for item_title, details in items:
                    item_text = f"<strong>{item_title}</strong>"
                    content_items.append(f"{item_text}")
                    items_array = [f"{detail}" for detail in details]
                    content_items.append(f"<ul>" + "\n".join(items_array) + "</ul>")
            content = "\n".join(content_items)

            sort_id += 1
            hotfixes.append({
                "sort_id": sort_id,
                "title": title,
                "product": product.replace(" hotfixes", ""),
                # "version": version.split(",")[0].strip(),
                "version": extract_version(version),
                "subproduct": extract_sub_product_from_version(version),
                "date": pub_date,
                "guid": guid,
                "content": content
            })
    return hotfixes


def generate_rss_feed(hotfix):  #save_hotfix_md
    """Save a hotfix entry as a markdown file."""
    os.makedirs("_hotfixes", exist_ok=True)

    filename = f"_hotfixes/{slugify(hotfix['product'])}-" \
           f"{slugify(hotfix['subproduct']) + '-' if hotfix.get('subproduct') else ''}" \
           f"{hotfix['version']}.md"

    front_matter = f"""---
title: "{hotfix['title']}"
product: {hotfix['product']}
version: "{hotfix['version']}"
subproduct: {hotfix['subproduct']}
minor_version: "{hotfix['version'].split('.')[0] + '.' + hotfix['version'].split('.')[1] if '.' in hotfix['version'] else '0'}"
date: {hotfix['date']}
order: {hotfix['sort_id']}
guid: {hotfix['guid']}
---

{hotfix['content']}
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(front_matter)


def save_feed_template(product=None, version=None):
    os.makedirs("feeds", exist_ok=True)

    # Construct feed name and filter
    if product and version:
        name = f"{product}-v{version}"
        filter_clause = f'| where: "product", "{product}" | where: "version", "{version}"'
    elif product:
        name = product
        filter_clause = f'| where: "product", "{product}"'
    elif version:
        name = f"v{version}"
        filter_clause = f'| where: "version", "{version}"'
    else:
        name = "all"
        filter_clause = ""

    filename = name.replace(" ", "-").lower()

    template = f"""---
layout: none
permalink: /feed/{filename}.xml
---
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>Hotfixes - {name}</title>
  <link>{{{{ site.url }}}}{{{{ site.baseurl }}}}{{{{ fix.url }}}}</link>
  <description>RSS feed for {name} hotfixes</description>
  {{% assign fixes = site.hotfixes {filter_clause} %}}
  {{% for fix in fixes %}}
  <item>
    <title>{{{{ fix.title }}}}</title>
    <link>{{{{ site.url }}}}{{{{ site.baseurl }}}}{{{{ fix.url }}}}</link>
    {{% if fix.title == "LS Central hotfixes - 26.1.33, Release date October 14, 2025 - Hotfixes" or fix.title == "LS Central hotfixes - 26.1.28, Release date September 23, 2025 - Hotfixes" %}}
      <pubDate>{{{{ "now" | date_to_rfc822 }}}}</pubDate>
    {{% else %}}
      <pubDate>{{{{ fix.date | date_to_rfc822 }}}}</pubDate>
    {{% endif %}}
    <guid>{{{{ fix.guid }}}}</guid>
    <description><![CDATA[{{{{ fix.content | markdownify | remove: '<p>' | remove: '</p>' }}}}]]></description>
  </item>
  {{% endfor %}}
</channel>
</rss>
"""
    with open(f"feeds/feed-{filename}.xml", "w", encoding="utf-8") as f:
        f.write(template)


# Step 1: Fetch the HTML (like wget)
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

# Step 2: Find the main content container and fetch the release notes
content_div = soup.find('div', role='main', id='mc-main-content')
content = scrape_release_notes(content_div)

# 3. Initialize RSS feed
hotfixes = generate_hotfixes(content)
for hotfix in hotfixes:
    generate_rss_feed(hotfix)  # Uses jekyll-feed plugin and liquid templates

# Save all hotfixes feed (feed-all.xml)
save_feed_template(product=None)

# Save hotfixes feed for each product (feed-<product>.xml)
unique_products = {product['product'] for product in hotfixes}
for unique_product in unique_products:
    save_feed_template(product=unique_product)
