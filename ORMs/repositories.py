from sqlalchemy import insert, select, and_, or_, update, bindparam, delete
from addresses_table import create_addresses_table
from cars_table import create_cars_table
from users_table import create_user_table
from db import engine, metadata_obj


class UserRepository():
    def __init__(self, engine):
        self.engine=engine

    def create_user(self, full_name, email):
        try:
            stmt=insert(create_user_table).values(full_name=full_name, email=email)
            with self.engine.connect() as conn:
                conn.execute(stmt)
                conn.commit()
                return True
        except Exception as e:
            print(f"Error creating user:{e}")
            return False

    def update_user(self, id, **kwargs):
        try:
            int_id=int(id)
            result=select(create_user_table).where(create_user_table.c.id==int_id)
            stmt=(
                update(create_user_table)
                .where(create_user_table.c.id==int_id)
                .values(kwargs)
                )
            with self.engine.connect() as conn:
                select_result=conn.execute(result)
                if not select_result.first():
                    print("User not found")
                    return False
                conn.execute(stmt)
                conn.commit()
                return True
        except Exception as e:
            print(f"Error updating the user: {e}")
            return False

    def delete_user(self, id):
        try:
            int_id=int(id)
            result=select(create_user_table).where(create_user_table.c.id==int_id)
            update_cars=(
                update(create_cars_table)
                .where(create_cars_table.c.user_id==int_id)
                .values(user_id=None)
            )
            update_address=(
                update(create_addresses_table)
                .where(create_addresses_table.c.user_id==int_id)
                .values(user_id=None)
            )
            stmt= delete(create_user_table).where(create_user_table.c.id==int_id)
            with self.engine.connect() as conn:
                select_result=conn.execute(result)
                if not select_result.first():
                    print("User not found")
                    return False
                conn.execute(update_cars)
                conn.execute(update_address)
                print(stmt.compile(engine))
                conn.execute(stmt)
                conn.commit()
                return True
        except Exception as e:
            print(f"Error Deleting the user: {e}")
            return False

    def get_all_users(self):
        try:
            stmt=select(create_user_table)
            with self.engine.connect() as conn:
                result=conn.execute(stmt)
                return result.mappings().all()
        except Exception as e:
            print(f"Error getting the users: {e}")


class CarRepository():
    def __init__(self, engine):
        self.engine=engine

    def create_car(self, vin_number, make, model, year, user_id):
        try:
            int_year=int(year)
            if not user_id:
                user_id=None
            else:
                user_id=int(user_id)
            stmt=insert(create_cars_table).values(vin_number=vin_number, make=make, model=model, year=int_year, user_id=user_id)
            with self.engine.connect() as conn:
                conn.execute(stmt)
                conn.commit()
                return True
        except Exception as e:
            print(f"Error creating the car: {e}")
            return False

    def associate_car_with_user(self, car_id, user_id):
        try:
            int_user_id=int(user_id)
            int_car_id=int(car_id)
            result_user=select(create_user_table).where(create_user_table.c.id==int_user_id)
            result_car=select(create_cars_table).where(create_cars_table.c.id==int_car_id)
            stmt=(
                update(create_cars_table)
                .where(create_cars_table.c.id==int_car_id)
                .values(user_id=int_user_id)
            )
            with self.engine.connect() as conn:
                select_user=conn.execute(result_user)
                if not select_user.first():
                    print("User was not found")
                    return False
                select_car=conn.execute(result_car)
                if not select_car.first():
                    print("car was not found")
                    return False
                conn.execute(stmt)
                conn.commit()
                return True
        except Exception as e:
            print(f"Error updating the user id in the cars table: {e}")
            return False

    def update_cars(self, id, **kwargs):
        try:
            int_id=int(id)
            result=select(create_cars_table).where(create_cars_table.c.id==int_id)
            stmt=(
                update(create_cars_table)
                .where(create_cars_table.c.id==int_id)
                .values(kwargs)
            )
            with self.engine.connect() as conn:
                select_result=conn.execute(result)
                if not select_result.first():
                    print("Car was not found")
                    return False
                conn.execute(stmt)
                conn.commit()
                return True
        except Exception as e:
            print(f"Error updating the car: {e}")
            return False

    def delete_car(self, id):
        try:
            int_id=int(id)
            result=select(create_cars_table).where(create_cars_table.c.id==int_id)
            stmt=delete(create_cars_table).where(create_cars_table.c.id==int_id)
            with self.engine.connect() as conn:
                select_result=conn.execute(result)
                if not select_result.first():
                    print("Car was not found")
                    return False
                conn.execute(stmt)
                conn.commit()
                return True
        except Exception as e:
            print(f"Error deleting the car: {e}")
            return False

    def get_all_cars(self):
        try:
            stmt=select(create_cars_table)
            with self.engine.connect() as conn:
                result=conn.execute(stmt)
                return result.mappings().all()
        except Exception as e:
            print(f"Error getting the cars:{e}")
        

class AddressRepository():
    def __init__(self, engine):
        self.engine=engine

    def create_address(self, address, user_id):
        try:
            stmt=insert(create_addresses_table).values(address=address, user_id=user_id)
            with self.engine.connect() as conn:
                conn.execute(stmt)
                conn.commit()
                return True
        except Exception as e:
            print(f"Error creating address table:{e}")
            return False

    def update_address(self, id, **kwargs):
        try:
            int_id=int(id)
            result=select(create_addresses_table).where(create_addresses_table.c.id==int_id)
            stmt=(
                update(create_addresses_table)
                .where(create_addresses_table.c.id==int_id)
                .values(kwargs)
                )
            with self.engine.connect() as conn:
                select_result=conn.execute(result)
                if not select_result.first():
                    print("Address was not found")
                    return False
                conn.execute(stmt)
                conn.commit()
                return True
        except Exception as e:
            print(f"Error updating the address: {e}")
            return False

    def delete_address(self, id):
        try:
            int_id=int(id)
            result=select(create_addresses_table).where(create_addresses_table.c.id==int_id)
            stmt=delete(create_addresses_table).where(create_addresses_table.c.id==int_id)
            with self.engine.connect() as conn:
                select_result=conn.execute(result)
                if not select_result.first():
                    print("Address was not found")
                    return False
                conn.execute(stmt)
                conn.commit()
                return True
        except Exception as e:
            print(f"Error deleting the address:{e}")
            return False

    def get_all_address(self):
        try:
            stmt=select(create_addresses_table)
            with self.engine.connect() as conn:
                result=conn.execute(stmt)
                return result.mappings().all()
        except Exception as e:
            print(f"Error getting the address:{e}")
        