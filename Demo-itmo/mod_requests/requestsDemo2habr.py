import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/hub/python/'
page = requests.get(url)
print(page)
print(page.text)

# Stepping Through a Page with Beautiful Soup

soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())
# prettify() method in order to turn the Beautiful Soup parse tree into a nicely formatted Unicode string. 
# Изменить дерево разбора Beautiful Soup в отформатированную строку Unicode.


news_list = soup.findAll('h2', class_='post__title')
print("-------new title------\n", news_list)

# use the get_text() method to extract all the text from inside that tag:
for i, it in enumerate(news_list, start = 1):
    print(i, it.get_text())

news_list2 = soup.findAll('li', class_='content-list__item content-list__item_news-topic')
print("-------news------\n", news_list2)

# use the get_text() method to extract all the text from inside that tag:
for i, it in enumerate(news_list2, start = 1):
    print(i, it.get_text())



# Finding Instances of a Tag

print("----find_all('p')------")
st = soup.find_all('p')
print(st)

# use the get_text() method to extract all the text from inside that tag:
print("----use the get_text()------")
print(st[2].get_text())

# Finding Tags by Class and ID

# In Beautiful Soup we will assign the string for the class to the keyword argument class_:
print("----use class_='inline-list__item-link hub-link'------")
print(soup.find_all(class_='inline-list__item-link hub-link')[2].get_text())

# We can also specify that we want to search for the class chorus only within <p> tags,
# in case it is used for more than one tag:
print("----use class_'a'='inline-list__item-link hub-link'------\n", soup.find_all('a', class_='inline-list__item-link hub-link'))

# We can also use Beautiful Soup to target IDs associated with HTML tags.
# In this case we will assign the string 'third' to the keyword argument id:
print("---------finr id='third'------\n", soup.find_all(id='third'))
