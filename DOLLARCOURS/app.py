import logging
from button import button
from aiogram import Bot, Dispatcher, executor, types
import requests

API_TOKEN = '6635666492:AAFK_e2i932PeNFPPMy0KguQEEgqeK2fL7A'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN, parse_mode='html')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def cour(message: types.Message):
    API_KEY = '23bea55e684c697990caf28a'
    qiymat = message.text
    url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/USD/UZS'
    response = requests.get(url)
    r = response.json()
    await message.answer(f"<b>Vaqt: {r['time_last_update_unix']}\n"
                         f"USD -> UZS\n"
                         f"1AQSH dollari {r['conversion_rate']} sum</b>")


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
