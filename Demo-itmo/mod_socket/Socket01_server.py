
'''
Работа с сокетами реализуется в Python низкоуровневым модулем socket, поддерживающим адреса IPv4 и адреса IPv6.
подробнее https://docs.python.org/3/library/socket.html
Для создания интернет-сервера:
- используем функцию socket, доступную в модуле socket для создания объекта socket (Сокет состоит из IP-адреса и порта)
- затем объект socket используется для вызова других функций для настройки сервера сокетов.
- далее вызовите функцию bind(hostname, port), чтобы указать порт для вашей службы на данном хосте.
- и затем вызовите метод accept возвращаемого объекта.
Этот метод ожидает, когда клиент подключится к указанному вами порту,
а затем вернет объект connection, который представляет соединение с этим клиентом.

'''
import socket               # Импорт модуля socket

s = socket.socket()         # Создание object socket
host = socket.gethostname() # Получить имя компьютера 
port = 12345                # Зарезервируйте порт для обслуживания
s.bind((host, port))        # Привязка к адресу ((инициализирует IP-адрес и порт)

s.listen(5)                 # Переводит сервер в режим приема соединений (5 - максимальное кол-во пользователей)

while True:
   c, addr = s.accept()     # Установить соединение с клиентом - Принимает соединение и блокирует приложение в ожидании сообщение от клиента
   print('Получил соединение от', addr)
   msg = 'Hello, Thank you for connecting'+ "\r\n"
   c.send(msg.encode('ascii'))  # Отправляет данные клиенту и возвращает количество отправленных байт
   c.close()                # Закрываем соединение