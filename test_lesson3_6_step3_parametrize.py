import time
import math

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def answer():
    return str(math.log(int(time.time())))


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser

    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize("link",
                         ["https://stepik.org/lesson/236895/step/1",
                          "https://stepik.org/lesson/236896/step/1",
                          "https://stepik.org/lesson/236897/step/1",
                          "https://stepik.org/lesson/236898/step/1",
                          "https://stepik.org/lesson/236899/step/1",
                          "https://stepik.org/lesson/236903/step/1",
                          "https://stepik.org/lesson/236904/step/1",
                          "https://stepik.org/lesson/236905/step/1"])
def test_correct_task(browser, link):
    browser.implicitly_wait(10)
    browser.get(link)
    browser.find_element_by_class_name("textarea").send_keys(answer())
    browser.find_element_by_class_name('submit-submission').click()
    result = browser.find_element_by_class_name('smart-hints__hint').text
    assert result == "Correct!", "Expected result was 'Correct!'"


if __name__ == "__main__":
    try:
        browser = webdriver.Chrome()
        test_correct_task(browser, "https://stepik.org/lesson/236895/step/1")
    finally:
        browser.quit()