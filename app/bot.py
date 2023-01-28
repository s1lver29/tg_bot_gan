import sys

from aiogram.utils import executor
from aiogram.types import BotCommand
from loguru import logger

from bot.headlers import *
from bot.settings import dp

async def set_commands(dp):

    commands = [
        BotCommand(command="/start",  description="Начать взаимодействие с ботом"),
        BotCommand(command="/set_style",  description="Стиль для фотографии"),
        BotCommand(command="/set_source",   description="Фотография для наложения стиля"),
        BotCommand(command="/generate",    description="Генерация новой фотографии")
    ]

    await dp.bot.set_my_commands(commands)


if __name__ == '__main__':
    logger.remove()
    logger.add(
        'logs/debug.log',
        format='[{time:YYYY-MM-DD HH:mm:ss}] {level} | {message}',
        level='TRACE'
    )
    logger.add(
        sys.__stdout__,
        format='[{time:YYYY-MM-DD HH:mm:ss}] {level} | {message}',
        level='TRACE',
        colorize=True
    )

    executor.start_polling(dp, skip_updates=True, on_startup=set_commands)