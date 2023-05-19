from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# 1-usul.
from keyboards.inline.callback_data import time_callback

serviceMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💇‍♂️ Soch olish", callback_data="hair"),
            InlineKeyboardButton(text="🪒️ Soqol olish", callback_data="beard"),
        ],
        [
            InlineKeyboardButton(text="💇‍♂️Soch + 🪒soqol olish", callback_data="hair+beard"),
            InlineKeyboardButton(text="👨‍🦰 Soch bo'yatish", callback_data="hair_color"),
        ],
    ])

# coursesMenu = InlineKeyboardMarkup(row_width=1)
#
# python = InlineKeyboardButton(text="Python asoslari", callback_data=course_callback.new(item_name='python'))
# coursesMenu.insert(python)
#
# django = InlineKeyboardButton(text="Django", callback_data=course_callback.new(item_name='django'))
# coursesMenu.insert(django)
#
# telegram = InlineKeyboardButton(text="Telegram bot", callback_data=course_callback.new(item_name='telegram'))
# coursesMenu.insert(telegram)
#
# algorithm = InlineKeyboardButton(text="Algoritm", callback_data=course_callback.new(item_name='algorithm'))
# coursesMenu.insert(algorithm)
#
# back_button = InlineKeyboardButton(text="Ortga", callback_data='cancel')
# coursesMenu.insert(back_button)
#

back_button = InlineKeyboardButton(text="Ortga", callback_data='cancel')
free_times = {
    "09:00": "9am",
    "10:00": "10am",
    "11:00": "11am",
    "12:00": "12pm",
    "13:00": "13pm",
    "14:00": "14pm",
    "15:00": "15pm",
    "16:00": "16pm",
    "17:00": "17pm",
    "18:00": "18pm",
    "19:00": "19pm",
    "20:00": "20pm",
    "21:00": "21pm",
    "22:00": "22pm",
    "23:00": "23pm",
    }

timesMenu = InlineKeyboardMarkup(row_width=3)
for key, value in free_times.items():
    timesMenu.insert(InlineKeyboardButton(text=key, callback_data=time_callback.new(time=value)))
timesMenu.insert(back_button)



# telegram_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(text="Xarid qilish", url="https://mohirdev.uz/courses/telegram/")
#     ]
# ])
#
# algoritm_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(text="Ko'rish", url="https://mohirdev.uz/courses/algoritmlar/")
#     ]
# ])
