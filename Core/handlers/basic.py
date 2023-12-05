from aiogram.types import Message
from Core.keyboard.create_post_keyboard import start_builder
from aiogram.fsm.context import FSMContext
from Core.routers.states import CreatePostState


async def start(message: Message, state: FSMContext):
    await message.answer(text=f"Hello, {message.from_user.first_name}",
                         reply_markup=start_builder.as_markup(resize_keyboard=True))
    await state.set_state(CreatePostState.start_state)
