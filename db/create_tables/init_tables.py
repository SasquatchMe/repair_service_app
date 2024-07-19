# from db.create_tables.company import create_table_company
from db.create_tables.entity import create_table_entity
from db.create_tables.masters import create_table_master
from db.create_tables.orders import create_table_order
from db.create_tables.services import create_table_services
from db.create_tables.status import create_table_status
from db.create_tables.users import create_table_user


def init_tables():
    create_table_status()
    create_table_user()
    create_table_services()
    create_table_master()
    create_table_order()
    create_table_entity()
    # create_table_company()