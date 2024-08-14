from selenium import webdriver
import time
browser = webdriver.Firefox()
# Создаём объект браузера, через который мы будем действовать.
# Если мы работаем с Firefox

browser = webdriver.Firefox()

# В кавычках указываем URL сайта, на который нам нужно зайти
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")

#Задержка в 10 секунд
time.sleep(10)

browser.quit()
#Закрываем браузер