from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("⁉️Напишите в техподдержку - @SocroboticHelp_bot",
            "👇 Или воспользоваться списоком команд: ",
            "",
            "/start - Начать работу",
            "/help - Задать вопрос в техподдержку")
    
    await message.answer("\n".join(text),
                         reply_markup=types.ReplyKeyboardRemove())
