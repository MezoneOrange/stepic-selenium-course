import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    a = browser.find_element_by_id('num1').text
    b = browser.find_element_by_id('num2').text
    result = str(int(a) + int(b))

    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_visible_text(result)

    button = browser.find_element_by_css_selector('form button[type="submit"]').click()
finally:
    time.sleep(10)
    browser.quit()