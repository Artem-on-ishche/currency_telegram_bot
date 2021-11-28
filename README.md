# currency_telegram_bot
A simple currency exchange telegram bot made as a test task for admission to one of the university's student organizations.

## What does this bot do?
It has 3 main commands:
1. Display the list of supported currencies
2. Convert UAH to selected currency
3. Convert selected currency to UAH

## Where does the bot get the data?
The data for the bot is scraped from the [National Bank Of Ukraine official website](https://bank.gov.ua/ua/markets/exchangerates).
As the data on the website is renewed only once a day, the bot writes the queried data along with the date when that data was aquired to the file <code>data/exchange_rates.txt</code>. Each time the user wants to convert the currency, the bot first checks if the data in the file is relevant, and only if it's not, it requests renewed data from the website.

## How to run and access the bot?
You need to run the bot locally on your machine. Locate file <code>src/main.py</code> and run it. To access the bot, find **@AdmissionSimpleCurrencyBot** in Telegram or follow this link: [t.me/AdmissionSimpleCurrencyBot](https://t.me/AdmissionSimpleCurrencyBot).
