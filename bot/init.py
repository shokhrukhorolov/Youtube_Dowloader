from bot.downloader import rt
from bot.handler import router
from bot.config import TOKEN


from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode



async def main() -> None:
    dp = Dispatcher()

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_routers(router, rt)

    await dp.start_polling(bot)