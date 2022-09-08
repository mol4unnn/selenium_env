import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

@pytest.mark.parametrize('test_input', ["https://stepik.org/lesson/236895/step/1",
            "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1",
            "https://stepik.org/lesson/236898/step/1",
            "https://stepik.org/lesson/236899/step/1",
            "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1",
            "https://stepik.org/lesson/236905/step/1"
            ])
def test_stepik(browser, test_input):
    browser.get(test_input)
    browser.implicitly_wait(5)
    ans = browser.find_element(By.CLASS_NAME, "ember-text-area").send_keys(math.log(int(time.time())))
    button = browser.find_element(By.CLASS_NAME,"submit-submission")
    button.click()
    answer = WebDriverWait(browser,5).until(EC.visibility_of_element_located((By.CLASS_NAME,"smart-hints__hint"))).text
    assert answer == "Correct!", "Answer должен быть Correct!"



