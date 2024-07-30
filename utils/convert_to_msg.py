from db.models.tables import Order
from db.query_to_db.query_to_db import get_user_id_by_tg_id
from loguru import logger


def get_message_from_order_db(tg_id):
    user_id = get_user_id_by_tg_id(tg_id)
    order: Order = Order.get(Order.user_id == user_id)
    msg = (f"Тип заявки: {order.order_type_id.order_type}\n"
           f"Тип поломки: {order.breaking_type_id.breaking_type}\n"
           f"Дата создания: {order.date_create}\n"
           f"Контактный номер: {order.phone}\n"
           f"Адрес: {order.user_id.object_id.address}\n\n\n"
           f"Статус заявки: {order.status_id.status}")

    try:
        if order.breaking_image_path is not None:
            breaking_photo = order.breaking_image_path
        else:
            breaking_photo = None
        if order.service_sticker_image_path is not None:
            service_sticker_photo = order.service_sticker_image_path
        else:
            service_sticker_photo = None
    except Exception as ex:
        logger.debug(ex)
    finally:
        return breaking_photo, service_sticker_photo, msg
