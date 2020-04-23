import math
import time

from selenium import webdriver


def calculate_result(x) -> str:
    """Returns result of the ln(abs(12*sin(x)))"""
    return str(math.log(abs(12*math.sin(x))))


if __name__ == '__main__':
    link = 'http://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    try:
        browser.get(link)
        number_from_page = browser.find_element_by_id('input_value')
        number = int(number_from_page.text)
        result = calculate_result(number)

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