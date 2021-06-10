from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

CHROME_DRIVER_PATH = "/Users/Thomas/CODE/chromedriver"
IG_EMAIL = "########"
IG_PASSWORD = "########"
SIMILAR_ACC = "designboom"

class InstaFollower:
    def __init__(self, chrome_driver):
        self.driver = webdriver.Chrome(executable_path=chrome_driver)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        accept_cookies = self.driver.find_element_by_xpath("/html/body/div[3]/div/div/button[1]")
        accept_cookies.click()
        time.sleep(1)

        email_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_input.send_keys(IG_EMAIL)
        password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(IG_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(2)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACC}")
        time.sleep(2)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        follower_modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal element by the height of the modal"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
        

follow_bot = InstaFollower(CHROME_DRIVER_PATH)
follow_bot.login()
follow_bot.find_followers()
follow_bot.follow()
