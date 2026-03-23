import kayak
import json

print("Scraper initialized...")
k = kayak.KayakScraper()
print("Done...")

print("Searching for flights...")
flights = k.search_flight_oneway("ZRH", "SAW")

payload = k.generate_payload(flights)

