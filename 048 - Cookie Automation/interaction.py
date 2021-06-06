from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/Thomas/CODE/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# # article_count = driver.find_element_by_css_selector("#articlecount a")
# # # print(article_count.text)
# # article_count.click()
#
# # all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()
#
# search_bar = driver.find_element_by_name("search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname_form = driver.find_element_by_name("fName")
fname_form.send_keys("John")

lname_form = driver.find_element_by_name("lName")
lname_form.send_keys("Smith")

email_form = driver.find_element_by_name("email")
email_form.send_keys("johnsmith@yahoo.com")

# email_form.send_keys(Keys.ENTER)
button = driver.find_element_by_css_selector("form button")
button.click()
# button.click()






# driver.quit()
