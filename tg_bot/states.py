from telebot.handler_backends import State, StatesGroup


class LoginStates(StatesGroup):
    login = State()
    get_phone = State()


class CRMStates(StatesGroup):
    lookup = State()
    order_type = State()
    breaking_type = State()
    desc = State()
    breaking_image = State()
    model_name = State()
    service_sticker_photo = State()
    contact = State()
    worktime = State()
    comment = State()
    confirm_order = State()
