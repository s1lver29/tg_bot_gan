import asyncio
import sys

from aiogram.utils import executor
from loguru import logger

from lib.headlers import *
from lib.settings import bot, dp


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

    executor.start_polling(dp, skip_updates=True)