import asyncio
from settings import bot

from aiogram import Bot


async def main(bot: Bot):
    print(await bot.get_session())
    await (await bot.get_session()).close()

if __name__ == "__main__":
    asyncio.run(main(bot))
