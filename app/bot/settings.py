from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


load_dotenv()

main_text = 'Данный бот умеет переносить стиль фотографии на другую фотографию'
photo_style_text = 'Отправь мне фото, которое будет отражать стиль исходной фотографии'
photo_source_text = 'Отправь мне фото, которое будет изменяться под стиль другой фотографии'
error_generate = 'Нужны две фотографии для генерации новой'

API_TOKEN=getenv('API_TOKEN', default='')

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
