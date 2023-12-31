from bs4 import BeautifulSoup
import requests

url = 'https://www.cbr.ru/currency_base/daily/'

content = requests.get(url)
print(content.text)
soup =  BeautifulSoup(content.text,'html.parser')
currencies = soup.find_all('tr')

for cur in currencies[1:]:
    n = len(cur.text)
    print(f'{cur.text[4:8]}\n{cur.text[9]} {cur.text[11:n-1]} rubles')