from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

start_builder = ReplyKeyboardBuilder()
start_builder.row(KeyboardButton(text="/create_post"))

cancel_builder = ReplyKeyboardBuilder()
cancel_builder.row(KeyboardButton(text="/cancel"))

skip_img_builder = ReplyKeyboardBuilder()
skip_img_builder.row(KeyboardButton(text="skip"), KeyboardButton(text="/cancel"))
