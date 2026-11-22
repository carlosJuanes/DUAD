from db import engine, metadata_obj
from sqlalchemy import insert, select, and_, or_, update, bindparam, delete
from repositories import UserRepository, CarRepository, AddressRepository
from db import metadata_obj

def prueba():
    metadata_obj
    users_rp=UserRepository(engine)

    cars_rp=CarRepository(engine)

    address_rp=AddressRepository(engine)

#    cars_rp.create_car(vin_number="fdnkfnlsd632", make="carlos", model="juanes", year=1992, user_id=3)
    print("antes")
    users_rp.delete_user(3)
    print("despues")

prueba()
