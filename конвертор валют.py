from bs4 import BeautifulSoup
import requests

list_of_currencies = ['USD','CNY', 'RUB','EUR','CHF','GBP','JPY','UAH', 'KZT', 'BYN', 'TRY', 'PLN']

print("\t\t\t\t\t\t\t Welcome to Currency Converter!\n")
print('available currencies : \n')
print(*list_of_currencies, '\n')


init_currency = input('Enter an initial currency: ')
target_currency = input('Enter a target currency: ')
amount = int(input('Enter the amount: '))


url = 'https://www.cbr.ru/currency_base/daily/'

content = requests.get(url)
soup =  BeautifulSoup(content.text,'html.parser')
currencies = soup.find_all('tr')

if (init_currency != 'RUB' and target_currency != 'RUB'):
    for cur in currencies[1:]:#переводим первую валюту, введённую пользователем в рубли
        n = len(cur.text)
        val = cur.text[5:8]
        rub = float(cur.text[n-8:n-1].replace(',','.',1))
        if (val == init_currency):
            valuta_1 = round(amount*rub,5)

    for cur in currencies[1:]:#переводим вторую валюту, введённую пользователем в рубли
        n = len(cur.text)
        val = cur.text[5:8]
        rub = float(cur.text[n-8:n-1].replace(',','.',1))
        if (val == target_currency):
            valuta_2 = round(amount*rub,5)
            
    print(str(amount)+ ' ' + init_currency + ' = ' + str(amount*(valuta_2/valuta_1)) + target_currency)

#считаем отдельные случаи с рублём
elif (target_currency == 'RUB'):
    for cur in currencies[1:]:
        n = len(cur.text)
        val = cur.text[5:8]
        rub = float(cur.text[n-8:n-1].replace(',','.',1))
        if (val == init_currency):
            print(str(amount)+ ' ' + init_currency + ' = ' + str(amount*rub) + target_currency)

elif (init_currency == 'RUB'):
    for cur in currencies[1:]:
        n = len(cur.text)
        val = cur.text[5:8]
        rub = float(cur.text[n-8:n-1].replace(',','.',1))
        if (val == target_currency):
            print(str(amount)+ ' ' + init_currency + ' = ' + str(amount*(1/rub)) + target_currency)


