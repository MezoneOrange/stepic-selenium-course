import time

from selenium import webdriver

from lesson2_1_step5_robotsRule import calculate_result as calc


link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    browser.find_element_by_css_selector('.trollface.btn').click()
    tabs = browser.window_handles
    tab2 = browser.switch_to.window(tabs[1])

    number = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(calc(int(number)))
    browser.find_element_by_css_selector('.container button').click()
finally:
    time.sleep(20)
    browser.quit()