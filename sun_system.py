from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Если работаем в Firefox
browser = webdriver.Firefox()
# Если работаем в Chrome
# browser = webdriver.Chrome()

# Открываем главную страницу Википедии
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

# Проверяем, что сайт открылся правильно
assert "Википедия" in browser.title
time.sleep(5)

# Находим окно поиска
search_box = browser.find_element(By.ID, "searchInput")

# Вводим текст "Солнечная система" в поисковую строку и отправляем запрос
search_box.send_keys("Солнечная система")
search_box.send_keys(Keys.RETURN)
time.sleep(5)

# Находим и кликаем на ссылку "Солнечная система"
a = browser.find_element(By.LINK_TEXT, "Солнечная система")
a.click()
