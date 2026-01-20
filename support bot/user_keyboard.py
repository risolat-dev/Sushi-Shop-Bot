from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def next_lesson_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Keyingi dars ➡️", callback_data="next_lesson")]
        ]
    )
    return keyboard
