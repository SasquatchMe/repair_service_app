from db.models.tables import Object, User


def tg_user_exist(tg_id):
    user = User.get_or_none(User.tg_id == tg_id)
    if user:
        return True
    return False


def check_object_exist(login: str):
    check = Object.select().where(Object.login == login.lower())

    return True if check else False


def register_user_exist(tg_id, login, phone):
    user = User.get_or_none(User.tg_id == tg_id)
    object_id = Object.select(Object.id).where(Object.login == login.lower())
    if not user:
        User.create(tg_id=tg_id, object_id=object_id, phone=phone)
        return 'Register user'
    return 'User already registered'
