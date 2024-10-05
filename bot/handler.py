
from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def command_start_handler(message:Message):
    await message.reply(f"Hi, {html.bold(message.from_user.full_name)}!")
    await message.answer("Send a link to the YouTube video you want to download")