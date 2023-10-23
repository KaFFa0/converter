from bs4 import BeautifulSoup
import requests

url = 'https://www.cbr.ru/currency_base/daily/'

content = requests.get(url)
print(content.text)
soup =  BeautifulSoup(content.text,'html.parser')
currencies = soup.find_all('tr')

for cur in currencies[1:]:
    print(cur.text)