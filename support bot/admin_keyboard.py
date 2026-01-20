from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def admin_keyboard():
    buttons = [
        [KeyboardButton(text="Kurs qo‘shish")],
        [KeyboardButton(text="Kursni pullik/bepul belgilash")],
        [KeyboardButton(text="Kurslar ro‘yxati")],
        [KeyboardButton(text="User progress")]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=True
    )
    return keyboard
