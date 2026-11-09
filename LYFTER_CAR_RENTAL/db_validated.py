from db import PgManager

def validated_query():
    try:
        db_manager=PgManager(db_name="postgres", user="postgres", password="qwert12345", host="localhost",)
        table_query=db_manager.execute_query( "SELECT table_name FROM information_schema.tables WHERE table_name IN ('users', 'cars', 'rentals');",())
        table_list=[table[0] for table in table_query]
        for table in table_list:
            if not table in ('users','cars', 'rentals'):
                return("Some of the required tables were not found.")
        availability_query=db_manager.execute_query(" SELECT COUNT(*) FROM lyfter_car_rental.cars WHERE car_status='available';",())
        available_cars=[cars[0] for cars in availability_query]
        if len(available_cars)>=1:
            print("DB OK. operating system functioning normally")
    except Exception as e:
        print(f"DB ERROR. No cars available. {e}")


if __name__ == '__main__':
    validated_query()