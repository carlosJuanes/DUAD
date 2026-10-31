from db import PgManager

db_manager=PgManager(db_name="postgres", user="postgres", password="qwert12345", host="localhost",)

class UserRepository:
    def __init__(self, db_manager):
        self.db_manager=db_manager


    def _format_user(self, user_record):
        return{
            "id":user_record[0],
            "full_name":user_record[1],
            "email":user_record[2],
            "user_name":user_record[3],
            "password":user_record[4],
            "birthdate":user_record[5],
            "account_status":user_record[6],
        }


    def turn_delinquent(self, _id):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users SET account_status=%s WHERE ID=%s",
                ("delinquent", _id)
            )
            print("account status update successfully")
            return True
        except Exception as e:
            print(f"error updating account status: {e}")
            return False            


    def validated_existence(self, _id):
        try:
            result=self.db_manager.execute_query(
                "SELECT id FROM lyfter_car_rental.users WHERE id=%s",
                (_id,)
            )
            if result:
                print("user found!!!")
                return True
            return False
        except Exception as e:
            print(f"Error validating user: {e}")
            return False


    def validate_user(self, email, user_name):
        try:
            result=self.db_manager.execute_query(
                "SELECT email, user_name FROM lyfter_car_rental.users WHERE email=%s or user_name= %s",
                (email, user_name)
            )
            if result:
                print("Email or username already exists")
                return True
            return False
        except Exception as e:
            print(f"error validating the user: {e}")
            return False


    def create_user(self, full_name, email, user_name,  password, birthdate, account_status):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.users (full_name, email, user_name, password, birthdate, account_status) VALUES (%s, %s, %s, %s, %s, %s)",
                (full_name, email, user_name, password, birthdate, account_status),
            )
            print("user inserted successfully")
            return True
        except Exception as e:
            print(f"error inserting a user in to database: {e}")
            return False


    def update_account_status(self, _id, new_status):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.users SET account_status=%s WHERE ID=%s",
                (new_status, _id)
            )
            print("account status update successfully")
            return True
        except Exception as e:
            print(f"error updating account status: {e}")
            return False


class CarRepository:
    def __init__(self, db_manager):
        self.db_manager=db_manager


    def _format_car(self, car_record):
        return{
            "id":car_record[0],
            "vin_number":car_record[1],
            "make":car_record[2],
            "model":car_record[3],
            "year":car_record[4],
            "car_status":car_record[5],
        }

    
    def validated_existence(self, _id):
        try:
            result=self.db_manager.execute_query(
                "SELECT id FROM lyfter_car_rental.cars WHERE id=%s",
                (_id,)
            )
            if result:
                print("the car already exists")
                return True
            return False
        except Exception as e:
            print(f"Error validating car: {e}")
            return False


    def valid_car(self, vin_number):
        try:
            result=self.db_manager.execute_query(
                "SELECT vin_number FROM lyfter_car_rental.cars WHERE vin_number=%s",
                (vin_number)
            )
            if result:
                print("the vin number already exist")
                return True
            return False
        except Exception as e:
            print(f"error validating the car: {e}")
            return False



    def created_car(self, vin_number, make, model, year, car_status):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.cars (vin_number, make, model, year, car_status) VALUES (%s, %s, %s, %s, %s)",
                (vin_number, make, model, year, car_status)
            )
            print ("car insert successfully")
            return True
        except Exception as e:
            print(f"Error inserting a car into data base: {e}")
            return False


    def update_car_status(self, _id, new_status):
        try:
            self.db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET car_status=%s WHERE ID=%s",
                (new_status, _id)
            )
            print("Car status update successfully")
            return True
        except Exception as e:
            print(f"Error updating car status: {e}")
            return False


    def disabled_car(self, car_id):
        try:
            db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET car_status=%s WHERE id=%s",
                ('disabled', car_id) 
            )
            print("Car status successfully changed")
            return True
        except Exception as e:
            print(f"error updating status ")
            return False


    def get_by_status_(self, status):
        try:
            results =db_manager.execute_query(
                "SELECT *  FROM lyfter_car_rental.cars WHERE car_status=%s",
                (status)
            )
            formatted_result=[self._format_car(result) for result in results]
            return formatted_result
        except Exception as e:
            print(f"Error getting results from the database: {e}")
            return False


class RentalRepository:
    def __init__(self, db_manager):
        self.db_manager=db_manager


    def _format_rental(self, rental_record):
        return{
            "id":rental_record[0],
            "user_id":rental_record[1],
            "car_id":rental_record[2],
            "rental_date":rental_record[3],
            "rental_status":rental_record[4],
        }

    def get_rental_by_id(self, _id):
        try:
            result=self.db_manager.execute_query(
                "SELECT * FROM lyfter_car_rental.rentals WHERE id=%s",
                (_id,)
            )
            if not result:
                raise ValueError("No results were found in the database.")
            formatted_result=self._format_rental(result[0])
            return formatted_result
        except Exception as e:
            print(f"Error getting results from the database: {e}")
            return False


    def rental_car(self, user_id, car_id):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.rentals (user_id, car_id, rental_status) VALUES (%s, %s, %s)",
                (user_id, car_id, 'rented')
            )
            print("Car successfully rented")
            return True
        except Exception as e:
            print(f"error while trying to rent the car: {e}")
            return False


    def update_status(self, _id, new_status):
        try:
            db_manager.execute_query(
                "UPDATE lyfter_car_rental.rentals SET rental_status=%s WHERE id=%s",
                (new_status, _id)
            )
            print("status update successfully")
            return True
        except Exception as e:
            print (f"Error updating the status: {e}")
            return False


    def completed_rental(self, rental_id, car_id):
        try:
            db_manager.execute_query(
                "UPDATE lyfter_car_rental.rentals SET rental_status =%s WHERE id =%s",
                ('available', rental_id)
            )
            print("Rental status successfully changed")
            db_manager.execute_query(
                "UPDATE lyfter_car_rental.cars SET car_status=%s WHERE id=%s",
                ('available', car_id)
            )
            print("Car status successfully changed")
            return True
        except Exception as e:
            print(f"error while completing rental: {e}")
            return False            


class BaseRepository:
    def __init__(self, db_manager):
        self.db_manager=db_manager

    def get_by_filter(self, table_name, filter=None):
        query=f"SELECT * FROM lyfter_car_rental.{table_name}"
        conditions=[]
        values=[]
        if filter:
            for column, value in filter.items():
                conditions.append(f" {column} =%s")
                values.append(value)
                query+= " WHERE " + " AND ".join(conditions)
        try:
            return self.db_manager.execute_query(query, tuple(values))
        except Exception as e:
            print(f"Error fetching date from {table_name}: {e}")
            return False

