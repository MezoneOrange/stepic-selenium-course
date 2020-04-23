import time

from selenium import webdriver

from lesson2_1_step5_robotsRule import calculate_result as calc


link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    button = browser.find_element_by_css_selector('button').click()
    alert = browser.switch_to.alert.accept()

    number = browser.find_element_by_id("input_value").text
    browser.find_element_by_id('answer').send_keys(calc(int(number)))
    browser.find_element_by_css_selector('.container button').click()
finally:
    time.sleep(5)
    browser.quit()