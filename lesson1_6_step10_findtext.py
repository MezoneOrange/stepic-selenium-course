import time

from selenium import webdriver


def fill_form(link):
    """fills s default form from Selenium course's tasks"""
    browser = webdriver.Chrome()
    try:
        browser.get(link)

        first_name = browser.find_element_by_css_selector('.first_block .first')
        first_name.send_keys('Imre')

        last_name = browser.find_element_by_css_selector('.first_block .second')
        last_name.send_keys('Kalman')

        email = browser.find_element_by_css_selector('.first_block .third')
        email.send_keys('imre_kalman@music.com')

        button = browser.find_element_by_css_selector('form button[type="submit"]')
        button.click()

        time.sleep(2)

        welcome_text_element = browser.find_element_by_tag_name('h1')
        welcome_text = welcome_text_element.text

        return welcome_text


    finally:
        time.sleep(3)
        browser.quit()


if __name__ == '__main__':
    link = "http://suninjuly.github.io/registration1.html"
    text = fill_form(link)
    assert "Congratulations! You have successfully registered!" == text


