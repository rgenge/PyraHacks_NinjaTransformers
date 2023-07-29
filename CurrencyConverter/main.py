import requests
from bs4 import BeautifulSoup
from dateutil.parser import parse

def converter(from_currency, target_currency, amount):
    flag = 0
    content = requests.get(f"https://www.x-rates.com/table/?from={from_currency}&amount={amount}").content
    soup = BeautifulSoup(content,"html.parser")
    exchanges = soup.find_all("table")
    exchange_rates = {}
    for exchange in exchanges:
        for tr in exchange.find_all("tr"):
            tds = tr.find_all("td")
            if tds:
                currency=tds[0].text
                exchange_rate = float(tds[1].text)
                exchange_rates[currency] = exchange_rate
                if((currency == target_currency) & (flag == 0)):
                    flag = 1
                    print(currency)
                    print(exchange_rates[currency])

if __name__ == "__main__":
    import sys
    from_currency = input("Type the source currency like 'USD'")
    amount = input("Type the amount to be converted")
    float(amount)
    target_currency = input("Type the target currency like currencys.txt examples like 'Euro'")
    with open('currencys.txt') as myfile:
        if target_currency in myfile.read():
            print("Target Currency Found")
        else:
            sys.exit('Type a valid currency according to currencys.txt')
    converter(from_currency, target_currency, amount)



