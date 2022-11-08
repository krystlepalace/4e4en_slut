import time
import logging
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from datetime import datetime
from random import randint
import requests

TOKEN = ''
MSG1 = 'Доброе утречко, семпай <3'
MSG2 = 'Спокойной ночи, семпай! .3'

logging.basicConfig(level=logging.INFO, filename='bot_log.log', filemode='w')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
	user_name = message.from_user.first_name
	user_id = message.from_user.id
	logging.info(f'{user_id} {user_name} {time.asctime()}')
	await message.reply(f'Привет, {user_name}-кун! ^_^')

	for i in range(14):
		now = int(datetime.now().strftime('%H'))
		if 6 <= now <= 12:
			await bot.send_message(user_id, MSG1)
			await asyncio.sleep(60 * 60 * 16)
		elif now >= 22 or now <= 3:
			await bot.send_message(user_id, MSG2)
			await asyncio.sleep(60 * 60 * 8)


@dp.message_handler(commands=['magic'])
async def magic(message: types.Message, command: types.BotCommand):
	user_name = message.from_user.first_name
	user_id = message.from_user.id
	logging.info(f'{user_id} {user_name} {time.asctime()}')

	if command.args:
		probability = randint(0, 100)
		answer = f'Вероятность этой хуйни - {probability}%!'
		await bot.send_message(user_id, answer)
	else:
		await bot.send_message(user_id, 'Че? Напиши что надо предсказать.')


@dp.message_handler()
async def auto_reply(message: types.Message):
	user_name = message.from_user.first_name
	user_id = message.from_user.id
	logging.info(f'{user_id} {user_name} {time.asctime()}')

	await message.reply(['Да', 'Хз', 'Нет'][randint(0, 2)])

if __name__ == '__main__':
	executor.start_polling(dp)
