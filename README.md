# Kayak Flight Scraper and Flight Lookup

This project was created for learning purposes in my BSc Data Science for the module: "Acquiring Data from the Web".

The goal was to scrape real flight data from Kayak for any route and date using Selenium for browser automation and BeautifulSoup for parsing. 
Along the way I also explored reverse engineering Kayak's internal API by analyzing network requests in the browser DevTools.

<hr>

Note: Currently this scraper only supports one-way flights on kayak.ch with CHF as currency. Support for kayak.com is being explored via API reverse engineering, as the site uses dynamically generated class names which make HTML scraping unreliable.

The scraped data can later be used to make interesting analyses such as:

- How does the price change the closer you get to the departure date?
- Which airlines are cheapest for a given route?
- What time of day has the cheapest flights?
- Is there a correlation between flight duration and price?

## Tech Stack

- Python
- Selenium
- BeautifulSoup

## Usage

**Example:**
```bash
uv run main.py ZRH SAW 2026-03-28
```

> Disclaimer
This project is for educational purposes only. Scraping Kayak may violate their Terms of Service. Do not use this for commercial purposes.