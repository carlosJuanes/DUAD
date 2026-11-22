from sqlalchemy import Table, Column, Integer, String, ForeignKey
from db import metadata_obj

create_addresses_table= Table(
    'addresses',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('address', String(200), nullable=False),
    Column('user_id', ForeignKey('users.id'), nullable=False),
)
