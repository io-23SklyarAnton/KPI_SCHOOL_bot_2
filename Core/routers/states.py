from aiogram.fsm.state import StatesGroup, State


class CreatePostState(StatesGroup):
    start_state = State()
    title_state = State()
    description_state = State()
    time_state = State()
    date_state = State()
    picture_state = State()
