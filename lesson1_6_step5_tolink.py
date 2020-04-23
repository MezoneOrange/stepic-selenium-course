import math
import time

from selenium import webdriver

import lesson1_6_step4_fillfields as fill


link = 'http://suninjuly.github.io/find_link_text'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    site = browser.find_element_by_link_text(text)
    site.click()

    fill.fill_form(browser)  # I used my module for fill a form
finally:
    time.sleep(10)
    browser.quit()

