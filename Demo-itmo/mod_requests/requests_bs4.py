import requests
"""
BeautifulSoup является библиотекой Python для парсинга HTML и XML документов - используется для скрапинга веб-страниц.
BeautifulSoup позволяет трансформировать HTML-документ в древо объектов Python - теги, навигация или комментарии.
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
pip install beautifulsoup4
"""

from bs4 import BeautifulSoup 

page = requests.get('https://yandex.ru')
soup = BeautifulSoup(page.text, 'html.parser') # html.parser - встроенный пакет, поставляемый с Python



city = soup.find(class_='geolink__reg')
print (city.prettify())
"""
Скрипт спарсил главную страницу Яндекса
и получил содержимое тега с классом geolink__reg из HTML кода/
Метод prettify позволяет создавать отформатированное дерево тегов
с результатами поиска
:
<span class="geolink__reg">
 Санкт-Петербург
</span>
"""
print (city.contents[0])    # Санкт-Петербург
