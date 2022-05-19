from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.markdown import hbold

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, <b>{message.from_user.full_name}</>!\n\n"
                         f"Для начала работы, отправь мне пожалуйста твой токен от сервиса kopeechka.store\n\n"
                         f"<b>P.S.</> Токен состоит из 32 симоволов, прошу не ошибаться\n\n"
                         f"<i>Пример</>: <b>05fa02c8710c2f60d617587ae69bf91a</>",
                         reply_markup=types.ReplyKeyboardRemove())
