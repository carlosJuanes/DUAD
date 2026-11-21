from sqlalchemy import insert, select, and_, or_, update, bindparam, delete
from addresses_table import created_addresses_table
from cars_table import created_cars_table
from users_table import created_user_table
from db import engine, metadata_obj


class UserRepository():
    def __init__(self, engine):
        self.engine=engine

    def created_user(self, full_name, email):
        try:
            stmt=insert(created_user_table).values(full_name=full_name, email=email)
            with self.engine.connect() as conn:
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print(f"Error creating user:{e}")

    def update_user(self, id, **kwargs):
        try:
            int_id=int(id)
            result=select(created_user_table).where(created_user_table.c.id==int_id)
            stmt=(
                update(created_user_table)
                .where(created_user_table.c.id==int_id)
                .values(kwargs)
                )
            with self.engine.connect() as conn:
                select_result=conn.execute(result)
                if not select_result.first():
                    print("User not found")
                    return False
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print(f"Error updating the user: {e}")

    def delete_user(self, id):
        try:
            int_id=int(id)
            result=select(created_user_table).where(created_user_table.c.id==int_id)
            stmt=delete(created_user_table).where(created_user_table.c.id==int_id)
            with self.engine.connect() as conn:
                select_result=conn.execute(result)
                if not select_result.first():
                    print("User not found")
                    return False
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print(f"Error Deleting the user: {e}")

    def get_all_users(self):
        try:
            stmt=select(created_user_table)
            with self.engine.connect() as conn:
                result=conn.execute(stmt)
                return result.mappings().all()
        except Exception as e:
            print(f"Error getting the users: {e}")


class CarRepository():
    def __init__(self, engine):
        self.engine=engine

    def created_car(self, vin_number, make, model, year, user_id):
        try:
            int_year=int(year)
            int_user_id=int(user_id)
            stmt=insert(created_cars_table).values(vin_number=vin_number, make=make, model=model, year=int_year, user_id=int_user_id)
            with self.engine.connect() as conn:
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print(f"Error creating the car: {e}")

    def associate_car_with_user(self, car_id, user_id):
        try:
            int_user_id=int(user_id)
            int_car_id=int(car_id)
            result=select(created_user_table).where(created_user_table.c.id==int_user_id)
            stmt=(
                update(created_cars_table)
                .where(created_cars_table.c.id==int_car_id)
                .values(user_id=int_user_id)
            )
            with self.engine.connect() as conn:
                select_result=conn.execute(result)
                if not select_result.first():
                    print("User was not found")
                    return False
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print(f"Error updating the user id in the cars table: {e}")

    def update_cars(self, id, **kwargs):
        try:
            int_id=int(id)
            result=select(created_cars_table).where(created_cars_table.c.id==int_id)
            stmt=(
                update(created_cars_table)
                .where(created_cars_table.c.id==int_id)
                .values(kwargs)
            )
            with self.engine.connect() as conn:
                select_result=conn.execute(result)
                if not select_result.first():
                    print("Car was not found")
                    return False
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print(f"Error updating the car: {e}")

    def delete_car(self, id):
        try:
            int_id=int(id)
            result=select(created_cars_table).where(created_cars_table.c.id==int_id)
            stmt=delete(created_cars_table).where(created_cars_table.c.id==int_id)
            with self.engine.connect() as conn:
                select_result=conn.execute(result)
                if not select_result.first():
                    print("Car was not found")
                    return False
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print(f"Error deleting the car: {e}")

    def get_all_cars(self):
        try:
            stmt=select(created_cars_table)
            with self.engine.connect() as conn:
                result=conn.execute(stmt)
                return result.mappings().all()
        except Exception as e:
            print(f"Error getting the cars:{e}")
        

class AddressRepository():
    def __init__(self, engine):
        self.engine=engine

    def created_address(self, address, user_id):
        try:
            stmt=insert(created_addresses_table).values(address=address, user_id=user_id)
            with self.engine.connect() as conn:
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print(f"Error creating address table:{e}")

    def update_address(self, id, **kwargs):
        try:
            int_id=int(id)
            result=select(created_addresses_table).where(created_addresses_table.c.id==int_id)
            stmt=(
                update(created_addresses_table)
                .where(created_addresses_table.c.id==int_id)
                .values(kwargs)
                )
            with self.engine.connect() as conn:
                select_result=conn.execute(result)
                if not select_result.first():
                    print("Address was not found")
                    return False
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print(f"Error updating the address: {e}")

    def delete_address(self, id):
        try:
            int_id=int(id)
            result=select(created_addresses_table).where(created_addresses_table.c.id==int_id)
            stmt=delete(created_addresses_table).where(created_addresses_table.c.id==int_id)
            with self.engine.connect() as conn:
                select_result=conn.execute(result)
                if not select_result.first():
                    print("Address was not found")
                    return False
                conn.execute(stmt)
                conn.commit()
        except Exception as e:
            print(f"Error deleting the address:{e}")

    def get_all_address(self):
        try:
            stmt=select(created_addresses_table)
            with self.engine.connect() as conn:
                result=conn.execute(stmt)
                return result.mappings().all()
        except Exception as e:
            print(f"Error getting the address:{e}")
        