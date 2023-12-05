from aiogram import Router, F
from aiogram.filters import Command
from Core.handlers.basic import start
from Core.routers.create_post_routers import base_post_router

basic_router = Router()

basic_router.message.register(start, Command("start"))
basic_router.include_router(base_post_router)
