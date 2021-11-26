from telegram import *
from telegram.ext import *

from data import constants, supported_currencies, available_keyboards
from scraper import scraper
from bot import helper

chosen_currency = None


def start_command(update: Updater, context: CallbackContext):
    text = 'Привіт, ' + update.effective_chat.username + '!\n\n'
    text += '''     Цей бот може конвертувати гривні в іноземні валюти.
    Для цього він викоритсовує дані з сайту НБУ: https://bank.gov.ua/ua/markets/exchangerates

    Доступні команди:
        /start - запуск бота
        /help - коротка інформація

    Решта взаємодії відбувається через кнопки.

    Приємного користування!'''
    helper.send_message(text, 0, update, context)


def help_command(update: Updater, context: CallbackContext):
    text = '''Цей бот може конвертувати гривні в іноземні валюти.
    Для цього він викоритсовує дані з сайту НБУ: https://bank.gov.ua/ua/markets/exchangerates

    Доступні команди:
        /start - запуск бота
        /help - коротка інформація

    Решта взаємодії відбувається через кнопки:
        -> "Доступні валюти" - показує список валют, в які бот вміє переводити гроші
        -> "Конвертувати" - конвертує введене значення у гривнях у вказану валюту
        
    Ці самі команди можна вводити як текст замість того, щоб натискати на кнопки.
    
    Коли бот просить ввести суму грошей, потрібно ввести лише число
    
    На решту тексту бот реагує виведенням повідомлення про те, що він не знає такої команди.

    Приємного користування!'''
    helper.send_message(text, 0, update, context)


def currencies_command(update: Updater, context: CallbackContext):
    text = "Цей бот працює з такими валютами:\n\n"
    for currency_name in supported_currencies.supported_currencies.keys():
        text += supported_currencies.supported_currencies[currency_name] + ' - ' + currency_name + '\n'

    helper.send_message(text, 0, update, context)


def convert_command(update: Updater, context: CallbackContext):
    text = 'Виберіть в яку валюту Ви хочете конвертувати:'
    helper.send_message(text, 1, update, context)


def message_handler(update: Updater, context: CallbackContext):
    global chosen_currency
    message_text = update.message.text

    if message_text == "Доступні валюти":
        currencies_command(update, context)
        return

    if message_text == "Конвертувати":
        convert_command(update, context)
        return

    if message_text in supported_currencies.supported_currencies.keys():
        chosen_currency = message_text

        text = "Введіть скільки гривень Ви хочете конвертувати:"
        helper.send_message(text, 1, update, context)
        return

    message_text = message_text.replace(',', '.')
    message_text = message_text.strip()

    if helper.is_float(message_text) and chosen_currency is not None:
        currency_code = supported_currencies.supported_currencies[chosen_currency]

        money_in_hryvnia = float(message_text)
        money_in_currency = round(scraper.calculate_currency_amount(currency_code, money_in_hryvnia), 2)

        text = "{:.2f} гривень - це {:.2f} {}".format(money_in_hryvnia, money_in_currency, currency_code)
        helper.send_message(text, 0, update, context)

        chosen_currency = None
        return

    text = "Введений текст не є командою. Будь ласка, повторіть спробу."
    helper.send_message(text, 0, update, context)


def main():
    updater = Updater(constants.UNIQUE_TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, message_handler))

    updater.start_polling()

    updater.idle()
