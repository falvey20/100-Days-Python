from selenium import webdriver

chrome_driver_path = "/Users/Thomas/CODE/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.python.org/")
#
# # price = driver.find_element_by_id("priceblock_ourprice")
# # print(price.text)
#
# event_dates = driver.find_elements_by_css_selector(".event-widget time")
# # for date in event_dates:
# #     print(date.text)
# event_titles = driver.find_elements_by_css_selector(".event-widget li a")
#
# event_dict = {}
#
# for n in range(len(event_dates)):
#     event_dict[n] = {
#         "time": event_dates[n].text,
#         "name": event_titles[n].text
#     }
#
# print(event_dict)
#
# # driver.quit()
# driver.quit()
