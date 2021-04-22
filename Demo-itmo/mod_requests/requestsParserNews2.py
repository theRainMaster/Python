# парсер новостей
import requests
from bs4 import BeautifulSoup

# сохраним наш URL в переменную:
url = 'http://mignews.com/mobile'

# отправим GET()-запрос на сайт и сохраним полученное в переменную 'page':
page = requests.get(url)

# Проверим подключение:
print(page.status_code)

# если код вернул статус код '200', значит это, что мы успешно подключены и все в полном порядке.

# создадим два списка
new_news = []
news = []

# воспользуемся BeautifulSoup4 и передадим ему page:
soup = BeautifulSoup(page.text, "html.parser")

# весь html-код нашей страницы:
print(soup)

# воспользуемся функцией поиска в BeautifulSoup4:
news = soup.findAll('a', class_='lenta')

print(news)
"""
вместе с текстом новостей вывелись теги
'a', 'span', классы 'lenta' и 'time2',
а также 'time2 time3'
"""

for i in range(len(news)):
    if news[i].find('span', class_='time2 time3') is not None:
        new_news.append(news[i].text)

print(new_news)

# Выведем данные:
for i in range(len(new_news)):
    print(new_news[i])

