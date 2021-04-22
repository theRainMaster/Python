import getpass                   # для определения информации о пользователе
import os
import socket                    # для работы с сокетами и получения IP-адре­сов
from datetime import datetime
from uuid import getnode as get_mac  # получает MAC-адрес машины
import speedtest        # замеряет характеристики интернет соединения pip install speedtest-cli
import psutil                    # работает с некоторыми низкоуровневыми системными функциями
import platform                  # информацию об ОС
#from PIL import Image            # для снятия скриншота

# Требуется узнать основные стабильные характеристики системы: IP- и MAC-адре­са, имя поль­зовате­ля и ОС:
name = getpass.getuser()                           # Имя пользователя
ip = socket.gethostbyname(socket.getfqdn())        # IP-адрес системы
mac = get_mac()                                    # MAC адрес
ost = platform.uname()                             # Название операционной системы

# Скорость интернет-соединения

inet = speedtest.Speedtest()
download = float(str(inet.download())[0:2] + "."                     # Входящая скорость
                + str(round(inet.download(), 2))[1]) * 0.125
uploads = float(str(inet.upload())[0:2] + "."                        # Исходящая скорость
                + str(round(inet.download(), 2))[1]) * 0.125

#Скорость замеряется библиотекой сервиса Speedtest.net и, соответственно, выдает результат в мегабитах, а не мегабайтах.
#Чтобы это исправить, разделим результат на 8 или умножим на 0,125 — это одно и то же. Манипуляцию проделываем дважды — для входящей и исходящей скорости.

zone = psutil.boot_time()
time = datetime.frontimestamp(zone)
