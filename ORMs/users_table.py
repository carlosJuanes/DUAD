from sqlalchemy import Table, Column, Integer, String
from db import metadata_obj

create_user_table=Table(
    'users',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('full_name', String(50)),
    Column('email', String(50)),
)

