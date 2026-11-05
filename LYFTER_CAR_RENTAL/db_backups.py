import csv
from db import PgManager
from datetime import datetime


db_manager=PgManager(db_name="postgres", user="postgres", password="qwert12345", host="localhost",)

users_path=f"db_backups/users_backups_{datetime.now().strftime('%Y-%m-%d')}.csv"
cars_path=f"db_backups/cars_backups_{datetime.now().strftime('%Y-%m-%d')}.csv"
rentals_path=f"db_backups/rentals_backups_{datetime.now().strftime('%Y-%m-%d')}.csv"

with open(users_path, 'w', encoding='utf-8', newline='') as file:
    users_db=db_manager.execute_query("SELECT * FROM lyfter_car_rental.users",())
    raw_header=db_manager.cursor.description
    headers=[column[0] for column in raw_header]
    writer=csv.writer(file)
    writer.writerow(headers)
    writer.writerows(users_db)
print("THE USER FILE HAS BEEN CREATED SUCCESSFULLY")


with open(cars_path, 'w', encoding='utf-8', newline='') as file:
    cars_db=db_manager.execute_query("SELECT * FROM lyfter_car_rental.cars",())
    raw_header=db_manager.cursor.description
    headers=[column[0] for column in raw_header]
    writer=csv.writer(file)
    writer.writerow(headers)
    writer.writerows(cars_db)
print("THE CARS FILE HAS BEEN CREATED SUCCESSFULLY")


with open(rentals_path, 'w', encoding='utf-8', newline='') as file:
    rentals_db=db_manager.execute_query("SELECT * FROM lyfter_car_rental.cars",())
    raw_header=db_manager.cursor.description
    headers=[column[0] for column in raw_header]
    writer=csv.writer(file)
    writer.writerow(headers)
    writer.writerows(rentals_db)
print("THE RENTALS FILE HAS BEEN CREATED SUCCESSFULLY")