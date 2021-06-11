import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

CHROME_DRIVER_PATH = "/Users/Thomas/CODE/chromedriver"

GOOGLE_FORM = "########"

ZILLOW_SEARCH = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
                "%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A" \
                "-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C" \
                "%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22" \
                "%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22" \
                "%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C" \
                "%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B" \
                "%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D" \
                "%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D "

header = {
    "User-Agent": "########",
    "Accept-Language": "en-US,en;q=0.9",
}

zillow_data = requests.get(ZILLOW_SEARCH, headers=header).text

soup = BeautifulSoup(zillow_data, "html.parser")
# print(soup.prettify())

all_link_elements = soup.select(".list-card-top a")

all_links = []
for link in all_link_elements:
    href = link["href"]
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

all_addresses = []
all_address_elements = soup.select(".list-card-info address")
for adds in all_address_elements:
    adds_text = adds.get_text()
    all_addresses.append(adds_text)

all_prices = []
all_price_elements = soup.select(".list-card-price")
for price in all_price_elements:
    price_text = price.get_text()
    all_prices.append(price_text)

# print(all_links)
# print(all_addresses)
# print(all_prices)

# Create Google Form
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

for i in range(len(all_links)):
    driver.get(GOOGLE_FORM)
    time.sleep(2)

    form_address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    form_address.send_keys(all_addresses[i])
    form_price.send_keys(all_prices[i])
    form_link.send_keys(all_links[i])

    time.sleep(1)

    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit_button.click()
