from datetime import datetime, timedelta
import locale

# Set the locale to Uzbek
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import date_callback
from keyboards.inline.serviceKeyboard import back_button

locale.setlocale(locale.LC_TIME, 'uz_UZ')

# Get current date
today = datetime.today()

# Create a list of the next 6 dates
dates = [today + timedelta(days=i) for i in range(7)]

# Format the dates as "day-month name" in Uzbek (e.g. "15-aprel")
formatted_dates = [date.strftime('%d-%B') for date in dates]

print(formatted_dates)

days_in_dic = {}
ctr = 1
for date in formatted_dates:
    days_in_dic[date] = f"day-{ctr}"
    ctr += 1
print(days_in_dic)

datesMenu = InlineKeyboardMarkup(row_width=2)
for key, value in days_in_dic.items():
    datesMenu.insert(InlineKeyboardButton(text=key, callback_data=date_callback.new(day_with_name=value)))
datesMenu.insert(back_button)