from aiogram import Router, F
from aiogram.filters import Command
from Core.handlers import сreate_post as c_p
from Core.routers.states import CreatePostState

base_post_router = Router()
write_title_router = Router()
write_description_router = Router()
setup_time_router = Router()
setup_date_router = Router()
setup_picture_router = Router()
confirm_post_router = Router()

# add routers to base router
create_post_routers = (write_title_router, write_description_router, setup_time_router,
                       setup_date_router, setup_picture_router, confirm_post_router)
base_post_router.include_routers(*create_post_routers)

# register handlers
base_post_router.message.register(c_p.create_post_start, CreatePostState.start_state, Command("create_post"))
base_post_router.message.register(c_p.cancel_post, Command("cancel"))

write_title_router.message.register(c_p.write_title, CreatePostState.title_state, F.text)
write_title_router.message.register(c_p.failed_title, CreatePostState.title_state)

write_description_router.message.register(c_p.write_description, CreatePostState.description_state, F.text)
write_description_router.message.register(c_p.failed_description, CreatePostState.description_state)

setup_time_router.callback_query.register(c_p.time_callback, CreatePostState.time_state, F.data.startswith("set_time"))
setup_time_router.message.register(c_p.failed_setup_date, CreatePostState.time_state)

setup_date_router.message.register(c_p.setup_date, CreatePostState.date_state, F.text)
setup_date_router.message.register(c_p.failed_setup_date, CreatePostState.date_state)

setup_picture_router.message.register(c_p.setup_picture, CreatePostState.picture_state, F.photo)
setup_picture_router.message.register(c_p.skipped_picture, CreatePostState.picture_state, F.text == "skip")
setup_picture_router.message.register(c_p.failed_setup_picture, CreatePostState.picture_state)

confirm_post_router.message.register(c_p.post_confirmed, CreatePostState.confirm_post_state, Command("save_post"))
confirm_post_router.message.register(c_p.post_declined, CreatePostState.confirm_post_state, Command("decline_post"))
