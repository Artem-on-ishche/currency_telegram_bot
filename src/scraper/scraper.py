import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

from data import constants, supported_currencies


def calculate_currency_amount(target_currency_code: str, money: float, conversion_type: int):
    data = get_data()

    for currency_info in data:
        currency_code, currency_amount, exchange_rate = currency_info
        if currency_code == target_currency_code:
            if conversion_type == 0:
                return money / exchange_rate * currency_amount
            else:
                return money * exchange_rate / currency_amount


def get_data():
    file = open("data/exchange_rates.txt", "r")

    latest_date = file.readline().replace('\n', '')
    current_date = datetime.now(pytz.timezone('Europe/Kiev')).strftime("%d.%m.%Y")

    data_to_return = []

    # the data is relevant
    if latest_date == current_date:
        lines = file.readlines()

        for line in lines:
            line = line.replace('\n', '')

            data = line.split(constants.SEPARATOR)
            data_to_return.append([data[0], int(data[1]), float(data[2])])

    # the data is outdated
    else:
        page = requests.get(constants.NATIONAL_BANK_URL)
        soup = BeautifulSoup(page.content, "html.parser")

        new_date = soup.select("span#exchangeDate")[0].string
        if new_date == latest_date:  # somehow the data turned out to be relevant
            lines = file.readlines()

            for line in lines:
                line = line.replace('\n', '')

                data = line.split(constants.SEPARATOR)
                data_to_return.append([data[0], int(data[1]), float(data[2])])

        else:  # the data is surely outdated
            # close the file and open it in writing mode
            file.close()
            file = open("data/exchange_rates.txt", "w")

            file.write(new_date + '\n')

            table_rows = soup.select("table#exchangeRates tbody tr")

            for table_row in table_rows:
                currency_code = table_row.contents[3].text

                if currency_code in supported_currencies.supported_currencies.values():
                    currency_amount = table_row.contents[5].text
                    exchange_rate = table_row.contents[9].text
                    exchange_rate = exchange_rate.replace(',', '.')

                    file.write(currency_code + constants.SEPARATOR
                               + currency_amount + constants.SEPARATOR
                               + exchange_rate + '\n')
                    data_to_return.append([currency_code, int(currency_amount), float(exchange_rate)])

    file.close()
    return data_to_return
