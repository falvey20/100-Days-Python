from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "########"
FB_PASSWORD = "########"

# Set Driver and get page
chrome_driver_path = "/Users/Thomas/CODE/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://tinder.com/")

time.sleep(2)

log_in_btn = driver.find_element_by_xpath('//*[@id="o1286841894"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in_btn.click()

time.sleep(2)

log_in_with_fb_btn = driver.find_element_by_xpath('//*[@id="o-441539182"]/div/div/div[1]/div/div[3]/span/div[2]/button')
log_in_with_fb_btn.click()

time.sleep(4)

# Get handles for each window
all_windows = driver.window_handles
base_window = all_windows[0]
fb_login_window = all_windows[1]
time.sleep(2)

# Switch to fb login window once open
driver.switch_to.window(fb_login_window)

# Accept cookie pop-up
accept_cookie = driver.find_element_by_class_name("_9o-t")
accept_cookie.click()

print(driver.title)

email_input = driver.find_element_by_id("email")
email_input.send_keys(EMAIL)
password_input = driver.find_element_by_id("pass")
password_input.send_keys(FB_PASSWORD)
fb_login_btn = driver.find_element_by_id("loginbutton")
fb_login_btn.click()

time.sleep(2)
# Revert to initial window
driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)

# Allow location
allow_location_btn = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_btn.click()

# Disallow notifications
notifications_btn = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_btn.click()

# Allow cookies
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

# Tinder allows 100 likes per day.
for n in range(100):

    # 1 second between likes.
    time.sleep(1)

    try:
        like_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    # Catch "It's a match" pop-up and close.
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        # If like button hasn't loaded wait 2 seconds.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
