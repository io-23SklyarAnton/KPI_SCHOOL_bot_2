from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

start_builder = ReplyKeyboardBuilder()
start_builder.row(KeyboardButton(text="/create_post"))

cancel_builder = ReplyKeyboardBuilder()
cancel_builder.row(KeyboardButton(text="/cancel"))

skip_img_builder = ReplyKeyboardBuilder()
skip_img_builder.row(KeyboardButton(text="skip"), KeyboardButton(text="/cancel"))

time_builder = InlineKeyboardBuilder()
for hour in range(0, 24):
    time_builder.add(InlineKeyboardButton(text=f"{hour:02}", callback_data=f"set_time-{hour:02}:00"))
    time_builder.adjust(6)

confirm_post_builder = ReplyKeyboardBuilder()
confirm_post_builder.row(KeyboardButton(text="/save_post"), KeyboardButton(text="/decline_post"))