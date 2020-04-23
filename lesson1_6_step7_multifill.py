import time

from selenium import webdriver


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/huge_form.html')
    fields = browser.find_elements_by_css_selector('input[type="text"]')
    for field in fields:
        field.send_keys('name')

    button = browser.find_element_by_class_name('btn')
    button.click()
finally:
    time.sleep(30)
    browser.quit()