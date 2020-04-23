import os
import time

from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    name = browser.find_element_by_name('firstname').send_keys('Keisy')
    surname = browser.find_element_by_name('lastname').send_keys('Railey')
    email = browser.find_element_by_name('email').send_keys('key_ray@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element_by_id('file').send_keys(file_path)

    button = browser.find_element_by_css_selector('form button[type="submit"]').click()
finally:
    time.sleep(10)
    browser.quit()