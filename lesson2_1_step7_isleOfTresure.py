import time

from selenium import webdriver

from lesson2_1_step5_robotsRule import calculate_result as calc


link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    chest_attribute = browser.find_element_by_id('treasure')
    number = chest_attribute.get_attribute('valuex')
    result = calc(int(number))

    field = browser.find_element_by_id('answer')
    field.send_keys(result)

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radio = browser.find_element_by_id('robotsRule')
    radio.click()

    button = browser.find_element_by_css_selector('form button[type="submit"]')
    button.click()
finally:
    time.sleep(10)
    browser.quit()