from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

EMAIL = "########"
PASSWORD = "########"
PHONE_NO = "########"

# Set Driver and get page
chrome_driver_path = "/Users/Thomas/CODE/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=92000000&keywords=python%20developer&location=Worldwide&sortBy=R&position=1&pageNum=0")

# Open sign in page
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(5)

# Fill sign in form
email = driver.find_element_by_id("username")
email.send_keys(EMAIL)
password = driver.find_element_by_id("password")
password.send_keys(PASSWORD)
# Enter to send form
password.send_keys(Keys.ENTER)

time.sleep(5)

all_jobs = driver.find_elements_by_css_selector(".job-card-container--clickable")

for job in all_jobs:
    job.click()
    time.sleep(2)

    try:
        # Locate and click the apply button
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        # If form requires phone number and the field is empty, then fill in the number.
        time.sleep(5)
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE_NO)
        else:
            continue

        # Submit the application form
        submit_button = driver.find_element_by_css_selector("footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element_by_css_selector(".artdeco-modal__actionbar .artdeco-button--primary")
            discard_button.click()
            print("Complex application, Skipped.")
            continue
        else:
            submit_button.click()

        # One application is sent, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    # If job can not be applied to (already applied/not accepting applications), Skip.
    except NoSuchElementException:
        print("Not possible to apply to this job")
        continue

time.sleep(5)
driver.quit()
