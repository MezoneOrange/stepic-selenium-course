import time

from selenium import webdriver

from lesson2_1_step5_robotsRule import calculate_result as calc


browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    number = browser.find_element_by_id('input_value').text
    result = calc(int(number))

    browser.execute_script("window.scrollBy(0, 150);")

    field = browser.find_element_by_id('answer').send_keys(result)

    check = browser.find_element_by_id('robotCheckbox').click()

    radio = browser.find_element_by_id('robotsRule').click()

    button = browser.find_element_by_css_selector('form button[type="submit"]').click()
finally:
    time.sleep(10)
    browser.quit()