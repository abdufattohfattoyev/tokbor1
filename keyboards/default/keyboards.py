from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_location_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton("📍 Отправить местоположение", request_location=True))
    return keyboard


