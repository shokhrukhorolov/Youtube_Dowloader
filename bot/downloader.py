import bot.keyboards as kb
import matlab

from aiogram import Router, F, types
from aiogram.types import Message, CallbackQuery, FSInputFile
# from aiogram.methods import SendVideo, SendAudio, SendPhoto

import yt_dlp as ytd
import wget
import os


rt = Router()

@rt.message(F.text)
async def getlink(message: Message):
    global link
    link = message.text

    await message.answer(message.text, reply_markup=kb.chBtn)
    await message.delete()


@rt.callback_query(F.data == "1080")
async def dw_1080(callback: CallbackQuery):
    await callback.message.answer("...")

    options = {
        'skip-download': True,
        'format_sort': ['res:1080', 'ext:mp4:m4a'],
        'outtmpl': 'output/video/%(title)s.%(ext)s'
    }

    with ytd.YoutubeDL(options) as ytdl:
        ytdl.download([link])
        result = ytdl.extract_info("{}".format(link))
        title = ytdl.prepare_filename(result)
        video = open(f'{title}', 'rb')

        await callback.message.answer_video(FSInputFile(path=video.name))

@rt.callback_query(F.data == "720")
async def dw_720(callback: CallbackQuery):
    await callback.message.answer("...")

    options = {
        'skip-download': True,
        'format_sort': ['res:720', 'ext:mp4:m4a'],
        'outtmpl': 'output/video/%(title)s.%(ext)s'
    }

    with ytd.YoutubeDL(options) as ytdl:
        ytdl.download([link])
        result = ytdl.extract_info("{}".format(link))
        title = ytdl.prepare_filename(result)
        video = open(f'{title}', 'rb')

        await callback.message.answer_video(FSInputFile(path=video.name))

@rt.callback_query(F.data == "360")
async def dw_360(callback: CallbackQuery):
    await callback.message.answer("...")

    options = {
        'skip-download': True,
        'format_sort': ['res:360', 'ext:mp4:m4a'],
        'outtmpl': 'output/video/%(title)s.%(ext)s'
    }

    with ytd.YoutubeDL(options) as ytdl:
        ytdl.download([link])
        result = ytdl.extract_info("{}".format(link))
        title = ytdl.prepare_filename(result)
        video = open(f'{title}', 'rb')

        await callback.message.answer_video(FSInputFile(path=video.name))


@rt.callback_query(F.data == "mp3")
async def dw_mp3(callback: CallbackQuery):
    await callback.message.answer("...")

    options = {
        'skip-download': True,
        'format': 'bestaudio/best',
        'outtmpl': 'output/mp3/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with ytd.YoutubeDL(options) as ytdl:
        ytdl.download([link])
        result = ytdl.extract_info("{}".format(link))
        title = ytdl.prepare_filename(result)[:-5]
        audio = open(f'{title}.mp3', 'rb')

        await callback.message.answer_audio(FSInputFile(path=audio.name))