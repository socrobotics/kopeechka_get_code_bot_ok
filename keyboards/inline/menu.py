from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Код отправлен"),
        ],
        [
            KeyboardButton(text="⛔️Завершить работу"),
        ]
    ],
    resize_keyboard=True
)
menu_close = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⛔️Завершить работу"),
        ]
    ],
    resize_keyboard=True
)
menu_again = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚧 Повторить"),
        ],
        [
            KeyboardButton(text="⛔️Завершить работу"),
        ]
    ],
    resize_keyboard=True
)
