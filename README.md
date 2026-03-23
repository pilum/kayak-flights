# Kayak Flight Scraper

This project was created for learning purposes in my BSc Data Science for the module: "Acquiring Data from the Web".

The goal was to scrape real flight data from Kayak for any route and date using Selenium for browser automation.
I also tried reverse engineering Kayak's internal API by analyzing network requests in DevTools, but that turned out to be way harder than expected so I went with scraping instead.

<hr>

Note: Currently this scraper only supports one-way flights on kayak.com. Two-way flight support is coming soon.

The scraped data can later be used to make interesting analyses such as:

- How does the price change the closer you get to the departure date?
- Which airlines are cheapest for a given route?
- What time of day has the cheapest flights?
- Is there a correlation between flight duration and price?

## Tech Stack

- Python
- Selenium

## Usage

```bash
python src/main.py
```

You will be prompted to enter a departure date. The scraper will then open a browser, search Kayak and return the flight results.

> Disclaimer:
> This project is for educational purposes only. Scraping Kayak may violate their Terms of Service. Do not use this for commercial purposes.