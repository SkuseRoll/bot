from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Расчитать работу"),
        ],
        [
            KeyboardButton(text="Как пользоваться?"),
            KeyboardButton(text="Контакты"),
        ],
    ],
    resize_keyboard=True
)
