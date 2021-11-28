from telegram import KeyboardButton

from data import supported_currencies, supported_commands

keyboards = [
    [[KeyboardButton(command)] for command in supported_commands.supported_commands],
    [[KeyboardButton(name)] for name in supported_currencies.supported_currencies.keys()],
]
