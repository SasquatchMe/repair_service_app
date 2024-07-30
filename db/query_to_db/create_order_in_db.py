from db.models.tables import Order
from db.query_to_db.query_to_db import get_user_id_by_tg_id


def create_order(data: dict, tg_id):
    user_id = get_user_id_by_tg_id(tg_id)
    order_type_id = data['order_type_id']
    breaking_type_id = data['breaking_type_id']
    desc = data['desc']
    breaking_image_path = data['breaking_image_path']
    model_name = data['model_name']
    service_sticker_image_path = data['service_sticker_image_path']
    phone = data['phone']
    comment = data['comment']

    Order.create(
        user_id=user_id,
        order_type_id=order_type_id,
        breaking_type_id=breaking_type_id,
        desc=desc,
        breaking_image_path=breaking_image_path,
        model_name=model_name,
        service_sticker_image_path=service_sticker_image_path,
        phone=phone,
        comment=comment
    )
