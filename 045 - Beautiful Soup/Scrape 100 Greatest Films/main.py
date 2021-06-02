from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.empireonline.com/movies/features/best-movies-2'
chrome_driver_path = 'chromedriver'

chrome_options = Options()
chrome_options.add_argument('--headless')

webdriver = webdriver.Chrome(ChromeDriverManager().install())

with webdriver as driver:
    # Set timeout time
    wait = WebDriverWait(driver, 10)
    # Retrieve url in headless browser
    driver.get(url)
    page_contents = driver.page_source
    driver.close()

soup = BeautifulSoup(page_contents, "html.parser")
all_films = soup.find_all(name="h3", class_="jsx-4245974604")
all_films_titles = [title.text for title in all_films]
all_films_titles.reverse()

print(all_films_titles)

with open("100-Movies.txt", "w") as file:
    for film in all_films_titles:
        file.write(f"{film}\n")
