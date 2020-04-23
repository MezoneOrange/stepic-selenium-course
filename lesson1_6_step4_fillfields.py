import time

from selenium import webdriver


def fill_form(browser):
    """fills s default form from Selenium course's tasks"""

    first_name = browser.find_element_by_name('first_name')
    first_name.send_keys('Dmitry')

    last_name = browser.find_element_by_name('last_name')
    last_name.send_keys('Shelukhin')

    city = browser.find_element_by_css_selector('.form-control.city')
    city.send_keys('Ekaterinburg')

    country = browser.find_element_by_css_selector('.form-group:nth-child(4) .form-control')
    country.send_keys('Russia')

    button = browser.find_element_by_xpath('//form/div[6]/button[@type="submit"]')
    button.click()


if __name__ == '__main__':
    link = "http://suninjuly.github.io/find_xpath_form"

    try:
        browser = webdriver.Chrome()
        browser.get(link)
        fill_form(browser)

    finally:
        time.sleep(30)
        browser.quit()