"""
Requests — это модуль Python, который можно использовать
для отправки всех видов HTTP-запросов

pip install requests
"""

import requests
# Создание запроса GET
req = requests.get('http://itcenter.itmo.ru/')

r1 = req.encoding     #  'utf-8' # кодировка страницы
r2 = req.status_code  #   200    # код состояния запроса
print(req, r1, r2)  # <Response [200]> utf-8 200 - ресурс работает и можно с ним взаимодействовать


# скачивание файла-изображения с сайта
image = requests.get('https://img-prod-cms-rt-microsoft-com.akamaized.net/cms/api/am/imageFileData/RE37Bcs?ver=e981&q=90&m=6&h=278&w=494&b=%23FFFFFFFF&l=f&o=t&aim=true')
with open('new_image.png', 'wb') as f:
    f.write(image.content)
