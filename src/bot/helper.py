from telegram.ext import CallbackContext, Updater
from telegram import ReplyKeyboardMarkup

from bot import bot
from data import available_keyboards


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def send_message(message: str, new_keyboard_index: int, update: Updater, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=message,
                             reply_markup=ReplyKeyboardMarkup(available_keyboards.keyboards[new_keyboard_index]))
