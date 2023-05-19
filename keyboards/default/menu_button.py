from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Buyurtma berish'),
            KeyboardButton(text='Navbatlar'),
        ],
        [
            KeyboardButton(text='Mening buyurtmalarim'),
            KeyboardButton(text='Yordam'),
        ],
    ],
    resize_keyboard=True
)
