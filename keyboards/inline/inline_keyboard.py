from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_cadastr_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("✅ Кадастр есть", callback_data="cadastr_yes"))
    keyboard.add(InlineKeyboardButton("❌ Кадастр нет", callback_data="cadastr_no"))
    return keyboard

# Transformator uchun inline tugmalar
def get_transformer_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("✅ Трансформатор есть", callback_data="transformer_yes"))
    keyboard.add(InlineKeyboardButton("❌ Трансформатор нет", callback_data="transformer_no"))
    return keyboard

# So‘rov boshlash tugmasi
def get_request_button():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("📝 Начать запрос", callback_data="start_request"))
    return keyboard

# Qayta boshlash tugmasi
def get_restart_button():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🔄 Начать заново", callback_data="restart_request"))
    return keyboard

def get_finish_button():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("✅ Завершить", callback_data="finish_upload"))
    return keyboard