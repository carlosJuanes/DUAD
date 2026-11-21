import db_backups
import db_validated
import seed_faker

def main():
    db_backups.connect()
    db_backups.create_users_backups()
    db_backups.create_cars_backups()
    db_backups.create_rentals_backups()
    db_validated.validated_query()
    seed_faker.connect_data()
    seed_faker.create_table_users()
    seed_faker.create_table_cars()
    seed_faker.create_rentals()

if __name__ == '__main__':
    main()