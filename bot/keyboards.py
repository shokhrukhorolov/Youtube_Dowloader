from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton



chBtn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="1080", callback_data="1080")],
    [InlineKeyboardButton(text="720", callback_data="720")],
    [InlineKeyboardButton(text="360", callback_data="360")],
    [InlineKeyboardButton(text="🎧", callback_data="mp3")],
    # [InlineKeyboardButton(text="🖼️", callback_data="jpg")],
])