import kayak
import json
import csv
from dataclasses import asdict, fields

print("Scraper initialized...")
k = kayak.KayakScraper()
print("Done...")

origin = input("Please enter the origin airport code [e.g. ZRH]: ")
destination = input("Please enter the destination airport code [e.g. SAW]: ")
departure_date = input("Please enter the departure date [YYYY-MM-DD]: ")

print("Searching for flights...")
flights = k.search_flight_oneway(origin, destination, departure_date)

payload = k.generate_payload(flights)
print(f"Found {len(flights)} flights:")
print(json.dumps(payload, indent=2, ensure_ascii=False))

csv_filename = f"{origin}_{destination}_{departure_date.replace('-', '_')}.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=[field.name for field in fields(kayak.Flight)])
    writer.writeheader()
    for flight in flights:
        writer.writerow(asdict(flight))
print(f"Exported {len(flights)} flights to {csv_filename}")

