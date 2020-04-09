from bs4 import BeautifulSoup
import requests
import pprint

source = requests.get('http://quotes.toscrape.com/').text
soup = BeautifulSoup(source, 'lxml')

# d = soup.find('div', class_='quote')
# q = d.span.text
# print(q.encode('utf-8'))

# a = soup.find('small', class_='author')
# print(a.text.encode('utf-8'))

for quotes in soup.find_all('div', class_='quote', 'small', class_='author'):
    quote = quotes.span.text.encode('utf-8')
    print(quote)
# for authors in soup.find_all('small', class_='author'):
    author = authors.text.encode('utf-8')
    print(author)
    print('')


