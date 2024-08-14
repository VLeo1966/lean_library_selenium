#     Этот код:
#
#     Открывает страницу Википедии о Солнечной системе.
#     Извлекает и выводит все параграфы (абзацы) текста по одному, ожидая нажатия клавиши Enter перед переходом к следующему параграфу.
#     Находит все элементы на странице с классом hatnote navigation-not-searchable, выбирает случайный элемент из них, находит в нем ссылку и переходит по ней.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

# Если работаем в Firefox
# browser = webdriver.Firefox()

# Если работаем в Chrome
browser = webdriver.Chrome()

# Заходим на страницу Солнечной системы
#browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

# Находим все параграфы на странице
paragraphs = browser.find_elements(By.TAG_NAME, "p")

# Перебираем параграфы и выводим текст каждого из них
for paragraph in paragraphs:
    print(paragraph.text)
    input("Нажмите Enter для получения следующего параграфа...")

# Находим элементы с классом "hatnote navigation-not-searchable"
hatnotes = []
for element in browser.find_elements(By.TAG_NAME, "div"):
    cl = element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable":
        hatnotes.append(element)

# Выбираем случайный элемент и переходим по ссылке
if hatnotes:
    hatnote = random.choice(hatnotes)
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
    browser.get(link)
else:
    print("Hatnote не найдены.")
