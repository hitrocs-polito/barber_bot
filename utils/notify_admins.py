from data.config import ADMINS
import logging

from aiogram import Dispatcher


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(ADMINS[0], "Bot started!")

    except Exception as err:
        logging.exception(err)
