from telegram import KeyboardButton

from data import supported_currencies

keyboards = [
    [[KeyboardButton("Доступні валюти")], [KeyboardButton("Конвертувати")]],
    [[KeyboardButton(name)] for name in supported_currencies.supported_currencies.keys()],
]
