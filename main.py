from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
bot = Bot('')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Open web page', web_app=WebAppInfo(url='https://github.com/DarkdragonicuS/NixiTestBot/web/index.html')))
    await message.answer('Hello World!', reply_markup=markup)

executor.start_polling(dp)
