import requests
from bs4 import BeautifulSoup


def calculate_currency_amount(currency_name: str, money: float):
    page = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
    soup = BeautifulSoup(page.content, "html.parser")

    table_rows = soup.select("table#exchangeRates tbody tr")
    for table_row in table_rows:
        if table_row.contents[3].text == currency_name:
            currency_amount = int(table_row.contents[5].text)
            exchange_rate = table_row.contents[9].text
            exchange_rate = float(exchange_rate.replace(',', '.'))

            return money / exchange_rate * currency_amount
