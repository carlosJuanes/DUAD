from faker import Faker
from db import PgManager
import random
from repositories import UserRepository, CarRepository, RentalRepository
from datetime import datetime, timedelta


def connect_data():
    db_manager=PgManager(db_name="postgres", user="postgres", password="qwert12345", host="localhost",)
    return db_manager


fake=Faker()


def create_table_users():
    db_manager=connect_data()
    repo_user=UserRepository(db_manager)
    for i in range(200):
        try:
            name=fake.name()
            email=fake.email()
            user_name=fake.user_name()
            password=fake.password()
            birthdate=fake.date_of_birth()
            account_status=random.choice(['regular', 'suspended', 'delinquent'])
            repo_user.create_user(name, email, user_name, password, birthdate, account_status)
        except Exception as e:
            print(f"error inserting users: {e}")
    print("The users were added successfully!!!")


def create_table_cars():
    db_manager=connect_data()
    repo_cars=CarRepository(db_manager)
    car_data={
        "Toyota":["Camry", "Avalon", ],
        "Pontiac":["Gemini", "GTO", "Torrent", ],
        "Ford":["Explorer Sport", "F-Series Super Duty"],
        "Saab":["9-3"],
        "BMW":["Z4"],
        "Infiniti":["I"],
        "Hyundai":["Accent"],
        "Mazda":["626"],
        "Kia":["Soul"],
        "Jeep":["Liberty"],
        "Audi":["RS 4"],
        "Jaguar":["XK Series"],
        "Suzuki":["SJ 410"],
        "Lincoln":["LS"]
    }

    for i in range(100):
        try:
            vin_number=fake.vin()
            make=random.choice(list(car_data.keys()))
            model=random.choice(car_data[make])
            year=random.randint(1950, 2020)
            car_status=random.choice(['rented', 'available', 'disabled'])
            repo_cars.created_car(vin_number, make, model, year, car_status)
        except Exception as e:
            print(f"error inserting cars: {e}")
    print("The cars were added successfully!!!")


def create_rentals():
    db_manager=connect_data()
    repo_rental=RentalRepository(db_manager)
    list_user_ids=db_manager.execute_query("SELECT id FROM lyfter_car_rental.users WHERE account_status='regular'", ())
    user_ids=[row[0] for row in list_user_ids]

    list_cars_ids=db_manager.execute_query("SELECT id FROM lyfter_car_rental.cars WHERE car_status='available'", ())
    cars_ids=[row[0] for row in list_cars_ids]
    for i in range(50):
        try:
            user_id=random.choice(user_ids)
            car_id=random.choice(cars_ids)
            rental_date=(datetime.now()-timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d')
            rental__status=random.choice(['available', 'rented', 'canceled'])
            repo_rental.rental_car(user_id, car_id, rental_date,rental__status)
        except Exception as e:
            print(f"error inserting vehicle rentals: {e}")
    print("Vehicle rentals were successfully created!!!")