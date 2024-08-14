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
