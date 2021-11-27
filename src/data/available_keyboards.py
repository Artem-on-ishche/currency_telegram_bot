from telegram import KeyboardButton

from data import supported_currencies

keyboards = [
    [[KeyboardButton("Доступні валюти")], [KeyboardButton("Гривня -> Валюта")], [KeyboardButton("Валюта -> Гривня")]],
    [[KeyboardButton(name)] for name in supported_currencies.supported_currencies.keys()],
]
