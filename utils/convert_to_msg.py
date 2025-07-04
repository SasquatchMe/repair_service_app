from loguru import logger

from db.models.tables import Order
from db.query_to_db.query_to_db import get_order_by_order_id


def get_message_from_order_db(order_id):
    order: Order = get_order_by_order_id(order_id)
    msg = (f"*Номер заявки:* {order.id}\n"
           f"*Дата создания:* {order.date_create}\n\n"
           f"*Тип заявки:* {order.order_type_id.order_type}\n"
           f"*Тип неисправности:* {order.breaking_type_id.breaking_type}\n"
           f"*Контактный номер:* {order.phone}\n"
           f"*Адрес:* {order.user_id.object_id.address}\n\n"
           f"*Статус заявки: {order.status_id.status}*")

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


def get_update_message_from_order_db(order_id):
    order: Order = get_order_by_order_id(order_id)
    msg = (f"❗*Уведомление о изменении статуса заявки*❗\n\n"
           f"*Номер заявки:* {order.id}\n"
           f"*Дата создания:* {order.date_create}\n"
           f"*Статус заявки: {order.status_id.status}*")
    return msg


def get_update_message_from_order_db_with_est_time(order_id):
    order: Order = get_order_by_order_id(order_id)
    msg = (f"❗*Уведомление о изменении статуса заявки*❗\n\n"
           f"*Номер заявки:* {order.id}\n"
           f"*Дата создания:* {order.date_create}\n"
           f"*Статус заявки: {order.status_id.status}*\n\n"
           f"*Ориентировочное время прибытия мастера: {order.est_date_complete}*\n"
           )
    return msg


def get_decline_message(order_id):
    order: Order = get_order_by_order_id(order_id)
    msg = (f"❗*Уведомление об отмене заявки*❗\n\n"
           f"*Номер заявки:* {order.id}\n"
           f"*Дата создания:* {order.date_create}\n"
           f"*Статус заявки: {order.status_id.status}*\n\n"
           f"*Причина отказа: {order.decline_desc}*")
    return msg
