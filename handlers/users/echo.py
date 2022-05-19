from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from handlers.users.get_code import get_code_kopeechka
from keyboards.inline.menu import menu, menu_close, menu_again
from loader import dp

token = []
email = []


@dp.message_handler(Text(contains="Код отправлен"))
async def get_code(message: types.Message):
    code = get_code_kopeechka(email=email[0], token=token[0])
    if code == "Не приходит код на почту":
        await message.answer(f"Не приходит код на почту - {email[0]}",
                             reply_markup=types.ReplyKeyboardRemove())
        return
    if code == "Нe удалось получить КОД с почты":
        await message.answer(f"Нe удалось получить КОД с почты - {email[0]}, можешь попробовать повторить попытку\n\n"
                             f"Отправь мне снова свой email",
                             reply_markup=types.ReplyKeyboardRemove())
        return
    if code is None:
        await message.answer(f"Укажи верный email",
                             reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer(f"Ваш код - {code}",
                             reply_markup=menu_close)


@dp.message_handler(Text(contains="Завершить работу"))
async def close_app(message: types.Message):
    await message.answer(f"{message.from_user.first_name} Вы завершили работу\n"
                         f"До новых встреч!✋", reply_markup=types.ReplyKeyboardRemove())


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    text = message.text
    if "@" in text:
        email.clear()
        email.append(text)
        await message.reply(f'Спасибо я получил твой email - {text}\n\n'
                            f'Теперь:\n\n'
                            f'Открой свой Facebook аккаунт и нажми кнопку - <b>Отправить код</> или <b>Resend code</>\n\n'
                            f'👇После этого жми кнопку внизу - ✅ Код отправлен', reply_markup=menu)
    if " " in text.strip():
        await message.reply(f'{message.from_user.first_name}, я тут только за тем чтобы поработать!\n'
                            f'Отправляй мне пожалуйста то что я говорю! Спасибо 😂')

    if len(text) == 32:
        token.clear()
        token.append(text)
        await message.reply(f'Спасибо я получил твой токен - {text}\n\n'
                            f'Теперь отправь мне пожалуйста свой email')


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{message}</code>")
