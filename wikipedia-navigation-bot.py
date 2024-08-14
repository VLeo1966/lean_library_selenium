from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import textwrap

# Функция для поиска и перехода на страницу по запросу пользователя
def search_wikipedia(query):
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)  # Ждем загрузки страницы
    # Находим и кликаем на ссылку
    a = browser.find_element(By.LINK_TEXT, query)
    a.click()

# Функция для вывода параграфов текущей статьи
def browse_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        wrapped_text = textwrap.fill(paragraph.text, width=80)  # Разбиваем текст на строки по ширине экрана
        print(wrapped_text)
        if input("Нажмите Enter для получения следующего параграфа или введите 'q' для выхода: \n").lower() == 'q':
            print("\n")
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

# Основная программа
if __name__ == "__main__":
    browser = webdriver.Firefox()

    try:

        browser.get("https://ru.wikipedia.org")
        # Проверяем, что сайт открылся правильно
        assert "Википедия" in browser.title
        time.sleep(5)
        # Запрос у пользователя первоначального запроса
        initial_query = input("Введите запрос для поиска на Википедии: ")
        search_wikipedia(initial_query)

        while True:
            print("\nВыберите действие:")
            print("1. Листать параграфы текущей статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Сделать новый поиск")
            print("4. Выйти из программы")
            choice = input("Введите номер выбранного действия: ")

            if choice == '1':
                browse_paragraphs()
            elif choice == '2':
                go_to_related_page()
                sub_choice = input("\nВыберите действие:\n1. Листать параграфы новой статьи\n2. Перейти на связанную страницу\nВведите номер действия: ")
                if sub_choice == '1':
                    browse_paragraphs()
                elif sub_choice == '2':
                    go_to_related_page()
            elif choice == '3':
                perform_new_search()
            elif choice == '4':
                print("Выход из программы...")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    finally:
        browser.quit()
