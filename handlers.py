from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards import menu
from loader import dp


@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    await message.answer("Выберите интересующий вас пункт меню.", reply_markup=menu)


@dp.message_handler(Text(equals=["Расчитать работу", "Как пользоваться?", "Контакты"]))
async def get_(message: Message):
    await message.answer(f"Вы выбрали \"{message.text}\". Спасибо.", reply_markup=ReplyKeyboardRemove())
