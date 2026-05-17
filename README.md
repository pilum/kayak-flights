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

You will be prompted for three inputs:

1. **Origin** airport code (e.g. `ZRH`)
2. **Destination** airport code (e.g. `SAW`)
3. **Departure date** in `YYYY-MM-DD` format (e.g. `2026-06-06`)

The scraper then opens a browser, accepts the Kayak cookie banner, scrolls to the
bottom of the page so all lazy-loaded results render, and collects every flight.

## Output

For each flight the scraper collects: operator, flight time, stopover, price and
baggage info. The results are:

- printed to the console as JSON, and
- exported to a CSV file in the directory you ran the command from, named
  `ORIGIN_DESTINATION_YYYY_MM_DD.csv` (e.g. `ZRH_SAW_2026_06_06.csv`).

> Disclaimer:
> This project is for educational purposes only. Scraping Kayak may violate their Terms of Service. Do not use this for commercial purposes.