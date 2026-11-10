from db import PgManager

def validated_query():
    try:
        db_manager=PgManager(db_name="postgres", user="postgres", password="qwert12345", host="localhost",)
        table_query=db_manager.execute_query( "SELECT table_name FROM information_schema.tables WHERE table_name IN ('users', 'cars', 'rentals');",())
        table_list=[table[0] for table in table_query]
        table_required=['users','cars', 'rentals']
        for table in table_required:
            if not table in table_list:
                return(f"the table: {table} was not found.")
        availability_query=db_manager.execute_query(" SELECT COUNT(*) FROM lyfter_car_rental.cars WHERE car_status='available';",())
        available_cars=[cars[0] for cars in availability_query]
        if available_cars[0]>=1:
            print("DB OK. operating system functioning normally")
    except Exception as e:
        print(f"DB ERROR. No cars available. {e}")


if __name__ == '__main__':
    validated_query()