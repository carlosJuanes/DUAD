from db import PgManager


try:
    db_manager=PgManager(db_name="postgres", user="postgres", password="qwert12345", host="localhost",)
    table_query=db_manager.execute_query( "SELECT table_name FROM information_schema.tables WHERE table_name IN ('users', 'cars', 'rentals');",())
    availability_query=db_manager.execute_query(" SELECT COUNT(*) FROM lyfter_car_rental.cars WHERE car_status='available';",())
    print("DB OK. operating system functioning normally")
except Exception as e:
    print(f"DB ERROR. No cars available. {e}")

