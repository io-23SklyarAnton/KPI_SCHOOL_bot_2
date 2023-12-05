from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from Core.routers.states import CreatePostState
from Core.keyboard.create_post_keyboard import start_builder, cancel_builder, skip_img_builder


async def cancel_post(message: Message, state: FSMContext):
    await message.answer(text="post canceled",
                         reply_markup=start_builder.as_markup(resize_keyboard=True))
    await state.set_state(CreatePostState.start_state)


async def create_post_start(message: Message, state: FSMContext):
    await message.answer(text="let's create your post!\nWrite down the post title:",
                         reply_markup=cancel_builder.as_markup(resize_keyboard=True))
    await state.set_state(CreatePostState.title_state)


async def write_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await message.answer(text="The title created successfully!\nWrite down the post description:")
    await state.set_state(CreatePostState.description_state)


async def failed_title(message: Message):
    await message.answer(text="Write a simple text to create the title!")


async def write_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer(text="The description created successfully!\nSelect the post time:")
    await state.set_state(CreatePostState.time_state)


async def failed_description(message: Message):
    await message.answer(text="Write a simple text to create the description!")


async def setup_time(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    await message.answer(text="The time is set successfully!\nWrite down the post date ('YYYY:MM:DD')")
    await state.set_state(CreatePostState.date_state)


async def failed_setup_time(message: Message):
    await message.answer(text="Write the time in correct format ('HH:MI:SS')!\nFor instance: '21:23:01'")


async def setup_date(message: Message, state: FSMContext):
    await state.update_data(date=message.text)
    await message.answer(text="The date is set successfully!\nSend the post picture",
                         reply_markup=skip_img_builder.as_markup())
    await state.set_state(CreatePostState.picture_state)


async def failed_setup_date(message: Message):
    await message.answer(text="Write the time in correct format ('YYYY:MM:DD')!\nFor instance: '2023:12:31'")


async def setup_picture(message: Message, state: FSMContext):
    await state.update_data(picture=message.photo[-1])
    await message.answer(text="The picture is set successfully!\nYour post is ready to send!",
                         reply_markup=start_builder.as_markup())
    await state.set_state(CreatePostState.start_state)


async def skipped_picture(message: Message, state: FSMContext):
    await message.answer(text="Your post is ready to send!",
                         reply_markup=start_builder.as_markup())
    await state.set_state(CreatePostState.start_state)


async def failed_setup_picture(message: Message):
    await message.answer(text="Send the picture!")
