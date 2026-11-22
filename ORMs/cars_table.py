from sqlalchemy import Table, Column, Integer, String, ForeignKey
from db import metadata_obj

create_cars_table=Table(
    'cars',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('vin_number', String(50)),
    Column('make', String(20)),
    Column('model', String(20)),
    Column('year', Integer),
    Column('user_id', ForeignKey('users.id')),
)
