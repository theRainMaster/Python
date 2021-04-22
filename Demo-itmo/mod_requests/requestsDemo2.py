import requests
"""
BeautifulSoup является библиотекой Python для парсинга HTML и XML документов - используется для скрапинга веб-страниц.
BeautifulSoup позволяет трансформировать HTML-документ в древо объектов Python - теги, навигация или комментарии.
https://www.crummy.com/software/BeautifulSoup/bs4/doc/
pip install beautifulsoup4
"""

from bs4 import BeautifulSoup 

url = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'
page = requests.get(url)
print(page)
print(page.text)

# Stepping Through a Page with Beautiful Soup

soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())
# prettify() method in order to turn the Beautiful Soup parse tree into a nicely formatted Unicode string. 
# Изменить дерево разбора Beautiful Soup в отформатированную строку Unicode.

# Finding Instances of a Tag

print("----find_all('p')------")
st = soup.find_all('p')
print(st)

# use the get_text() method to extract all the text from inside that tag:
print("----use the get_text()------")
print(st[2].get_text())

# Finding Tags by Class and ID

# In Beautiful Soup we will assign the string for the class to the keyword argument class_:
print("----use class_='chorus'------")
print(soup.find_all(class_='chorus'))

# We can also specify that we want to search for the class chorus only within <p> tags,
# in case it is used for more than one tag:
print("----use class_'p'='chorus'------\n", soup.find_all('p', class_='chorus'))

# We can also use Beautiful Soup to target IDs associated with HTML tags.
# In this case we will assign the string 'third' to the keyword argument id:
print("---------finr id='third'------\n", soup.find_all(id='third'))
