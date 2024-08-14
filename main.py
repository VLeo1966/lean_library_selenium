from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

# Функция для поиска и перехода на страницу по запросу пользователя
def search_wikipedia(query):
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(10)  # Ждем загрузки страницы
    # Находим и кликаем на ссылку
    a = browser.find_element(By.LINK_TEXT, query)
    a.click()

# Функция для вывода параграфов текущей статьи
def browse_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        if input("Нажмите Enter для получения следующего параграфа или введите 'q' для выхода: ").lower() == 'q':
            break

# Функция для перехода на связанную страницу
def go_to_related_page():
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable":
            hatnotes.append(element)

    if hatnotes:
        hatnote = random.choice(hatnotes)
        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
        browser.get(link)
        print(f"Переход по ссылке: {link}")
    else:
        print("Связанные статьи не найдены.")

# Функция для выполнения нового поиска
def perform_new_search():
    new_query = input("Введите новый запрос для поиска на Википедии: ")
    search_wikipedia(new_query)
    time.sleep(3)
# Основная программа
if __name__ == "__main__":
    browser = webdriver.Firefox()

    try:

        browser.get("https://ru.wikipedia.org")
        time.sleep(5)
        # Проверяем, что сайт открылся правильно
        assert "Википедия" in browser.title
        time.sleep(10)
        # Запрос у пользователя первоначального запроса
        initial_query = input("Введите запрос для поиска на Википедии: ")
        search_wikipedia(initial_query)
        time.sleep(3)
        while True:
            print("\nВыберите действие:")
            print("1. Листать параграфы текущей статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Сделать новый поиск")
            print("4. Выйти из программы")
            choice = input("Введите номер выбранного действия: ")

            if choice == '1':
                browse_paragraphs()
                time.sleep(3)  # Ждем загрузки страницы
            elif choice == '2':
                go_to_related_page()
                time.sleep(3)  # Ждем загрузки страницы
                sub_choice = input("\nВыберите действие:\n1. Листать параграфы новой статьи\n2. Перейти на связанную страницу\nВведите номер действия: ")
                if sub_choice == '1':
                    browse_paragraphs()
                    time.sleep(3)  # ��дем загрузки страницы
                elif sub_choice == '2':
                    go_to_related_page()
                    time.sleep(3)  # ��дем загрузки страницы
            elif choice == '3':
                perform_new_search()
                time.sleep(3)  # Ждем загрузки страницы
            elif choice == '4':
                print("Выход из программы...")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    finally:
        browser.quit()
