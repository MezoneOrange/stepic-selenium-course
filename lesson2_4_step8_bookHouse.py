import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from lesson2_1_step5_robotsRule import calculate_result as calc


link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    browser.find_element(By.ID, 'book').click()

    number = browser.find_element_by_id('input_value').text
    browser.find_element_by_id('answer').send_keys(calc(int(number)))
    browser.find_element_by_id('solve').click()
finally:
    time.sleep(20)
    browser.quit()