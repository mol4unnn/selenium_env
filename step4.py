from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
browser = webdriver.Chrome()

try:
    # Указываем ссылку на страницу, которую тестируем
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.ID,"treasure")
    x = x_element.get_attribute("valuex")
    print("x=", x)
    y = calc(x)
    # print("y=", y)

    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(y)

    option1 = browser.find_element(By.ID,"robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.ID,"robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn-default")
    button.click()

    print("Тест успешно завершен. 20 сек на закрытие браузера....")



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(12)
    # закрываем браузер после всех манипуляций
    browser.quit()