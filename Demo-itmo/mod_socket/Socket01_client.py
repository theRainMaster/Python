
'''
socket.connect(hosname, port ) открывает соединение TCP с Hostname и port.
Как только у вас открыт сокет, вы можете читать его, как любой объект ввода-вывода.
Когда это будет сделано, не забудьте закрыть его, так как вы закроете файл.

'''
import socket               # Импорт модуля socket

s = socket.socket()         # Создание объекта socket
host = socket.gethostname() # Получить имя компьютера 
port = 12345                # Зарезервируйте порт для обслуживания

s.connect((host, port))
# Receive no more than 1024 bytes
msg = s.recv(1024) 

s.close                     # Закройте сокет, когда закончите

print (msg.decode('ascii'))
