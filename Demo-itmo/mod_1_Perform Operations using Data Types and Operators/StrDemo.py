# Строка - это упорядоченная неизменяемая последовательность символов Юникода

# 1. Преобразование числа к строке
x = str("s1")   # x станет 's1'  
y = str(2)      # y станет '2'  
z = str(3.0)    # z станет '3.0'
print(x, type(x), id(x)) # <class 'str'>
a = "Привет, Мир!"  
print(a[1])             # р
# a[1] = 'л' # TypeError: 'str' object does not support item assignment


# 2. Арифметические операции
#    Тип результата операции определяется типом аргументов

# s1 + s2
# Соединяет строки s1 и s2
print("Py" + "thon")    # 'Python'
# или просто написать рядом
print("Py" "thon")      # 'Python'

# s1 * n
# Составляет строку из n повторений строки s1
print("па" * 2)         # 'папа'

# 3. Равенство и сравнение
#    Результат логического типа
#
#    Операции сравнения выполняются посимвольно слева направо с учетом кодировки.
#    Таблица символов Юникода на http://unicode-table.com/.

# s1 == s2, s1 != s2
# Проверка строк на равенство/неравенство
print("текст1" == "текст2") # False
print("текст1" != "текст2") # True

# x > y, x < y, x >= y, x <= y
# Больше, меньше, больше или равно, меньше или равно
print("текст1" > "текст2") # False
print("текст1" <= "текст2") # True

# Возможно составление цепочек сравнений
print("текст1" < "текст12" <= "текст2") # True

# s1 in s2
# Проверка вхождения строки s1 в s2
print("p" in "Python")      # False


# 4. Использование методов строк
""" Строки неизменяемый тип данных, поэтому все методы, которые преобразуют строку
возвращают новую строку, а исходная строка остается неизменной"""

s = "ЭТО просТо ТеКст"
print(ord(s[0])) # 1069 - Возвращает номер символа из таблицы Unicode
print(chr(1069)) # Э - Возвращает символ по номеру из таблицы Unicode

print(s.upper(), s.lower(), s.title(), s.capitalize(), s.swapcase())
      # capitalize()    Возвращает копию строки с первым символом в верхнем регистре
      # title()         Возвращает копию строки, в которой первые символы каждого слова преобразованы в верхний регистр, а все остальные - в нижний регистр.
      # swapcase()      Возвращает копию строки, в которой регистр меняется на обратный
      # ('ЭТО ПРОСТО ТЕКСТ', 'это просто текст', 'Это Просто Текст', 'Это просто текст', 'это ПРОСтО тЕкСТ')

print(s.find("Т"))          # 1 - на какой позиции находится первый символ подстроки (для первого совпадения)

print(s.replace("Т", "т"))  # 'ЭтО просто теКст'

lst1 = s.split()      # Возвращает список строк, разбитых по строке-параметру
print(lst1)          # ['ЭТО', 'просТо', 'ТеКст']

lst2 = s.split('Т')     
print(lst2)         # ['Э', 'О прос', 'о ', 'еКст']
print("-o-".join(lst1))    # 'ЭТО-o-просТо-o-ТеКст'



# Проверка на то, начинается или заканчивается ли строка на определенные символы
print(s.startswith('ЭТ'))   # True
print(s.endswith('ст'))     # True

b = """Напишем первую строку
Теперь вторую
48 больше трех"""
print("b:",type(b),"\n",b)
lst = b.split('\n')     
print(lst)

lst = b.strip()  # По умолчанию метод strip() убирает пробельные символы. В этот набор символов входят: \t\n\r\f\v
print(lst)

# Методу strip можно передать как аргумент любые символы - тогда в начале и в конце строки
# будут удалены все символы, которые были указаны в строке:
print("([123/456])".strip('[])('))       # 123/456


# 5. Форматирование строк с помощью метода str.format()

s1 = "The novel ’{0}' was published in {1} year".format("Hard Times", 1854)
print(s1)                       # The novel ’Hard Times' was published in 1854 year

s2 = "{{{0}}} {1} numeric".format("I'm text", "I'm not")
print(s2)                       # {I'm text} I'm not numeric

s3 = "{0}{1}".format("The amount due is $", 200)
print(s3)                       # The amount due is $200

# Использование имен полей (именованные аргументы)

s4 = "{who} turned {age} this year".format(who="She", age=88)
s5 = "The {who} was {0} last week".format(10, who="boy") # в списке аргументов именованные аргументы всегда следуют после позиционных
print(s4, "\n", s5)      # She turned 88 this year 
                         # The boy was 10 last week


# Имена полей могут ссылаться на коллекции, такие как списки

stock = ["paper", "envelopes", "notepads", "pens", "paper clips"]
s6 = "We have {0[1]} and {0[2]} in stock".format(stock)
print(s6)               # We have envelopes and notepads in stock

# Словари в качестве аргументов

d = dict(animal="elephant", weight=12000)
s7 = "The {0[animal]} weighs {0[weight]}kg".format(d)
print(s7)               # The elephant weighs 12000kg

# Форматирование строк с помощью f-строк
"""
F-строки — это литерал строки с буквой f перед ним.
Внутри f-строки в паре фигурных скобок
указываются имена переменных, которые надо подставить
f-строки — это выражение, которое выполняется
"""
who = "Holly"
age = 99
s4 = f"{who.upper()} turned {age} this year"
print("f:", s4)         # HOLLY turned 99 this year







