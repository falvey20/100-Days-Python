import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/THERMOS-Stainless-Compact-Bottle-Ounce/dp/B08JWJND52/ref=sr_1_32_sspa?dchild=1&keywords=thermos&qid=1622908504&sr=8-32-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUFZaUkFHUEJVMjRUJmVuY3J5cHRlZElkPUEwNzcwMDMzUUREOEo1UVRZRVZGJmVuY3J5cHRlZEFkSWQ9QTAyNzY4NDgzRDVVV004UFA2MFFLJndpZGdldE5hbWU9c3BfbXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
title = soup.find(id="productTitle").get_text().strip()
# print(title)
# print(soup.prettify())

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

TARGET_PRICE = 26
MY_EMAIL = "########"
MY_PASSWORD = "########"

if price_as_float <= TARGET_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
                            )
