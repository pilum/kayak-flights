import re, time, sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

args = sys.argv[1:]
origin = args[0]
destination = args[1]
date = args[2]

def search_flight_chf():
    # Setup undetected headless Browser
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--window-size=1920,1080')  # headless has no window size by default
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36')
    driver = webdriver.Chrome(options=options)

    # Date must be in the following format: YYYY/MM/DD 
    driver.get(f"https://www.kayak.ch/flights/{origin}-{destination}/{date}?sort=bestflight_a")

    # Seconds sleep to fully load the page. Tested it with mulitple times, 5 is sufficent.s
    time.sleep(5)

    # Get the source code and parse it
    source = driver.page_source
    soup = BeautifulSoup(source, "html.parser")

    # Extraction of all needed informations.
    # This will only work on kayak.ch.
    prices = soup.find_all('div', {'class': re.compile(r'price-text')})
    operators = soup.find_all('div', {'class': re.compile(r'operator-text')})
    times = soup.find_all('div', {'class': re.compile(r'mod-variant-large')})
    flight_time = soup.find_all('div', {'class': re.compile(r'mod-full-airport')})
    stopovers = soup.find_all('div', {'class': re.compile(r'mod-variant-default')})

    # Prices are loaded twice (Desktop/Mobile)
    prices = prices[::2]

    # Zip them all together
    all_flights = zip(operators, flight_time, times, stopovers, prices)

    # Print every flight available.
    print(f"Flights on {date} from {origin} to {destination}\n")
    for operator, ftime, duration_times, stopover, price in all_flights:
        print(f"Airline: {operator.text}\nFlight Duration: {ftime.text.replace("Std.", "Hrs.")}\nDeparture/Arrival: {duration_times.text}\nStopover: {stopover.text.replace("Std.", "Hrs.")}\nPrice: {price.text}\n")

search_flight_chf()