# Libraries needed for scraping operations
import time
from dataclasses import dataclass, asdict
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@dataclass
class Flight():
    operator: str
    flight_time: str
    stopover: str
    price: str
    bags: str

class KayakScraper():
    def __init__(self, url=None, driver=None) -> list[Flight]:
        self.url = url
        # Setup Browser
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920,1080')  # headless has no window size by default
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36')
        self.driver = webdriver.Chrome(options=options)


    def search_flight_oneway(self, origin: str="ZRH", destination: str="SAW"):
        departure_date = input("Please enter the departure date [YYYY-DD-MM]: ")

        # construct url for search request
        self.url = f"https://www.kayak.com/flights/{origin}-{destination}/{departure_date}?sort=bestflight_a"

        # scrape the flight
        self.driver.get(self.url)
        time.sleep(15)  # Increased wait time for full page load
        
        # remove unnecessary data like ads from the flights:
        flights = self.driver.find_elements('xpath', "//div[contains(@class, '-result-item-container')]")
        flights_cleaned = []

        for f in flights:
            is_ad = f.find_elements('xpath', './/div[text()="Ad"]')
            if not is_ad:
                flights_cleaned.append(f)

        kayak_flight: list[Flight] = []

        for flight in flights_cleaned:
            try:
                price = flight.find_element('xpath', ".//div[contains(@class, '-price-text')]").text
            except:
                price = ""
            try:
                stopover = flight.find_element('xpath', ".//div[contains(@class, '-mod-variant-default')]/span").text
            except:
                stopover = ""
            try:
                flight_time = flight.find_element('xpath', ".//div[contains(@class, '-mod-variant-large')]").text
            except:
                flight_time = ""
            try:
                operator = flight.find_element('xpath', ".//div[contains(@dir, 'ltr')]").text
            except:
                operator = ""
            try:
                bag = flight.find_element('xpath', ".//div[contains(@aria-label, 'carry-on')]").text
            except:
                bag = ""

            if price and flight_time:  # Only need core fields
                kayak_flight.append(Flight(operator, flight_time, stopover, price, bag))

        # return
        return kayak_flight


    def generate_payload(self, flights: list[Flight]=None):
        return {"fligths":[asdict(flight) for flight in flights]}