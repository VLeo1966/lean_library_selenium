# Wikipedia Navigation Bot

This Python script automates the process of browsing Wikipedia articles using Selenium. The bot allows the user to search for Wikipedia articles, read paragraphs from the articles, and navigate to related articles, all within a command-line interface.

## Features

- **Search Wikipedia**: Enter a query to search for a specific Wikipedia article.
- **Browse Paragraphs**: Read paragraphs of the current article, with text wrapped to fit the terminal width.
- **Navigate to Related Articles**: Choose to navigate to a related article from the current page.
- **Perform a New Search**: Start a new search within Wikipedia.
- **Exit**: Exit the program at any time.

## Prerequisites

- Python 3.x
- Selenium (`pip install selenium`)
- WebDriver for your browser (e.g., [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) or [GeckoDriver](https://github.com/mozilla/geckodriver/releases) for Firefox)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/wikipedia-navigation-bot.git
    cd wikipedia-navigation-bot
    ```

2. **Install the required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

    *(Note: Make sure `selenium` is listed in your `requirements.txt` file)*

3. **Download and set up WebDriver**:
   - For Chrome users: Download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it's in your system's PATH.
   - For Firefox users: Download [GeckoDriver](https://github.com/mozilla/geckodriver/releases) and ensure it's in your system's PATH.

## Usage

1. **Run the script**:
    ```bash
    python wikipedia_navigation_bot.py
    ```

2. **Follow the prompts**:
   - Enter your search query to start browsing Wikipedia.
   - Choose from the menu to browse paragraphs, navigate to related articles, perform a new search, or exit.

3. **Example**:
    ```
    Введите запрос для поиска на Википедии: Солнечная система
    Значение слова - [description of Solar System]
    Нажмите Enter для получения следующего параграфа или введите 'q' для выхода:
    ```

## Customization

- **Text Wrapping**: The text wrapping width can be customized by changing the `width` parameter in the `textwrap.fill()` method in the `browse_paragraphs` function.
- **Sleep Timers**: The sleep timers (`time.sleep()`) can be adjusted or removed based on your internet speed or preference.

## Contributing

Feel free to submit issues or pull requests if you find bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
Вот пример файла `README.md`, который можно использовать для этого проекта на GitHub:

```markdown
# Введение в работу с динамическим контентом с использованием Selenium

Этот проект предоставляет практическое руководство по работе с динамическим контентом на веб-страницах, используя инструмент автоматизации браузера Selenium. В рамках урока мы изучим основы работы с DOM и JavaScript (JS), а также научимся использовать Selenium для взаимодействия с веб-страницами.

## Теория на сегодня

### Что будет на уроке
- Введение в DOM и JavaScript.
- Работа с динамическим контентом.
- Использование Selenium для автоматизации взаимодействия с веб-страницами.

## План урока

1. **Понимание DOM и JS**
   - Что такое DOM и как он взаимодействует с JavaScript.
   - Как DOM представляет структуру веб-страниц.
   - Как JavaScript используется для манипуляции DOM.

2. **Практика с Selenium**
   - Установка и настройка Selenium.
   - Автоматизация работы с браузером.
   - Взаимодействие с элементами веб-страницы.

## Основные понятия

### DOM (Document Object Model)

🧠 **DOM** — это программный интерфейс, представляющий структуру веб-страниц в виде дерева объектов. Каждый элемент веб-страницы является узлом этого дерева, что позволяет программам (в том числе с помощью JavaScript) взаимодействовать с элементами страницы: добавлять, изменять или удалять их.

### JavaScript (JS)

🧠 **JavaScript** — язык программирования, используемый для создания интерактивных элементов на веб-страницах. JS позволяет манипулировать DOM, изменяя элементы страницы на лету.

### Selenium

🧠 **Selenium** — мощный инструмент для автоматизации веб-браузеров. Он позволяет имитировать действия пользователя, такие как клики, ввод текста и прокрутка страниц. Selenium широко используется для тестирования веб-приложений и автоматизации рутинных задач.

## Настройка и использование Selenium

### 1. Установка Selenium

- Откройте терминал и установите Selenium:
  ```bash
  pip install selenium
  ```

### 2. Создание простого скрипта для работы с браузером

- Импортируем необходимые библиотеки:
  ```python
  from selenium import webdriver
  import time
  ```

- Создаём объект браузера и открываем веб-страницу:
  ```python
  browser = webdriver.Chrome()  # Или webdriver.Firefox()
  browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
  time.sleep(10)
  browser.quit()
  ```

### 3. Автоматизация действий на сайте

- Открываем страницу и делаем скриншоты:
  ```python
  browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
  browser.save_screenshot("dom.png")
  time.sleep(10)
  browser.get("https://ru.wikipedia.org/wiki/Selenium")
  browser.save_screenshot("selenium.png")
  browser.refresh()
  ```

### 4. Взаимодействие с элементами на сайте

- Пример кода для взаимодействия с поисковой строкой на Википедии:
  ```python
  browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
  search_box = browser.find_element(By.ID, "searchInput")
  search_box.send_keys("Солнечная система")
  search_box.send_keys(Keys.RETURN)
  time.sleep(5)
  ```

### 5. Работа с контентом на странице

- Извлечение текста из параграфов:
  ```python
  paragraphs = browser.find_elements(By.TAG_NAME, "p")
  for paragraph in paragraphs:
      print(paragraph.text)
      input()
  ```

- Переход по ссылкам и взаимодействие с контентом:
  ```python
  hatnotes = []
  for element in browser.find_elements(By.TAG_NAME, "div"):
      cl = element.get_attribute("class")
      if cl == "hatnote navigation-not-searchable":
          hatnotes.append(element)

  hatnote = random.choice(hatnotes)
  link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
  browser.get(link)
  ```

## Результаты урока

Сегодня мы:
- Узнали, что такое DOM и JS.
- Научились работать с Selenium, используя его для автоматизации задач на веб-страницах.

## Дополнительные материалы

- [Скачать Firefox](https://www.mozilla.org/ru/firefox/new/)
- [Скачать Chrome](https://www.google.com/intl/ru_ru/chrome/)
- [Драйвер для Firefox (geckodriver)](https://github.com/mozilla/geckodriver/releases)
- [Драйвер для Chrome (chromedriver)](https://chromedriver.chromium.org/)
```

Этот файл `README.md` предлагает полное руководство по установке и использованию Selenium для взаимодействия с динамическим контентом на веб-страницах, а также объясняет ключевые концепции, такие как DOM и JavaScript.