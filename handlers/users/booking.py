import datetime
import logging
import re

from aiogram import types
from aiogram.types import CallbackQuery

from data.config import ADMINS
from handlers.users.google_api import create_event
from keyboards.inline.callback_data import time_callback, date_callback
from keyboards.inline.serviceKeyboard import serviceMenu, timesMenu
from keyboards.inline.serviceTime import datesMenu
from loader import dp, db, bot
from datetime import datetime, timedelta


@dp.message_handler(text='Buyurtma berish')
async def booking(message: types.Message):
    await message.answer("Quyidagi xizmatlardan bir yoki bir nechtasini tanlang.", reply_markup=serviceMenu)


@dp.callback_query_handler(text='hair')
async def buy_courses(call: CallbackQuery):
    await call.message.answer("Kunni tanlang", reply_markup=datesMenu)
    await call.message.delete()
    await call.answer(cache_time=60)


days = ("day-1", "day-2", "day-3", "day-4", "day-5", "day-6", "day-7")


@dp.callback_query_handler(date_callback.filter(day_with_name=days))
async def buy_course(call: CallbackQuery, callback_data: dict):
    call_data = callback_data.get("day_with_name")
    global chosen_day, chosen_date_name
    today = datetime.today()
    chosen_day = today + timedelta(days=int(call_data[-1])-1)
    chosen_day = chosen_day.strftime('%d-%m')
    await call.message.delete()
    await call.message.answer("Vaqtni tanlang!", reply_markup=timesMenu)


times = ('9am', '10am', '11am',
         '12pm', '13pm', '14pm',
         '15pm', '16pm', '17pm',
         '18pm', '19pm', '20pm',
         '21pm', '22pm', '23pm',)


@dp.callback_query_handler(time_callback.filter(time=times))
async def buy_course(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    time_pattern = re.compile(r"\b(\d{1,2})[ap]m\b", re.IGNORECASE)
    hour = int(time_pattern.findall(callback_data["time"])[0])

    first_name = db.get_firstname(call.from_user.id)
    last_name = db.get_lastname(call.from_user.id)
    number = db.get_number(call.from_user.id)
    date = f"{chosen_day}-2023"
    start_time = datetime.strptime(date, "%d-%m-%Y")
    start_time = start_time.replace(hour=hour, minute=0)
    end_time = start_time + timedelta(minutes=40)
    summary = "Soch oldirish"
    description = f"Ismi: {first_name[0]}\nFamiliya: {last_name[0]}\nRaqami: {number[0]}"
    create_event(start_time=start_time, end_time=end_time, summary=summary, description=description)
    day = ""
    if date == datetime.today().strftime("%d-%m-%Y"):
        day = "Bugun"
    await call.answer(f"✅ Buyurtmangiz qabul qilindi.\n"
                      f"😊 Sizni {day} soat {start_time.strftime('%H:%M')} da kutamiz!\n"
                      f"🤝 Albatta keling",
                      cache_time=60, show_alert=True)
    await bot.send_message(chat_id=ADMINS[0], text="#yangi_buyurtma\n\n"
                                                   f"Ismi: {first_name[0]}\n"
                                                   f"Familiya: {last_name[0]}\n"
                                                   f"Raqami: <a href='tel:{number[0]}'>{number[0]}</a>\n"
                                                   f"Kuni: {date}\n"
                                                   f"Boshlanish vaqti: {start_time.strftime('%H:%M')}\n"
                                                   f"Tugash vaqti: {end_time.strftime('%H:%M')}")


@dp.callback_query_handler(text='cancel')
async def cancel(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=serviceMenu)
    await call.answer()
