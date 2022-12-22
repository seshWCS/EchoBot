import random

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5912786406:AAEjsBmpQiSdCmi-OAYEJZfbpH3Z87HpCbw'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ echo bot by sesh\n")


@dp.message_handler(commands=['echo'])
async def echo(message: types.Message):
    await message.reply(message.text.removeprefix("/echo "))


@dp.message_handler(commands=['tolower'])
async def tolower(message: types.Message):
    await message.reply(message.text.removeprefix("/tolower ").lower())


@dp.message_handler(commands=['toupper'])
async def toupper(message: types.Message):
    await message.reply(message.text.removeprefix("/toupper ").upper())


@dp.message_handler(commands=['reverse'])
async def echo(message: types.Message):
    await message.reply(message.text.removeprefix("/reverse ")[::-1])


@dp.message_handler(commands=['shuffle'])
async def echo(message: types.Message):
    a = list(message.text.removeprefix("/shuffle "))
    random.shuffle(a)
    await message.reply(''.join(a))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

