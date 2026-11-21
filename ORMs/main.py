from db import engine, metadata_obj
from repositories import UserRepository, CarRepository, AddressRepository

def main():
        users=[
        {
            "full_name":"carlos juanes",
            "email":"carlosjuanes@hotmail.com"
        },
            {
            "full_name":"alfredo medina",
            "email":"alfredomedina@hotmail.com"
        },
            {
            "full_name":"carlos medina",
            "email":"carlosmedina@hotmail.com"
        }
    ]

        cars=[
            {
                "vin_number":"5sd4f23sd1f231s",
                "make":"toyota",
                "model":"corolla",
                "year":2016,
                "user_id":1,
            },
            {
                "vin_number":"sdf456sd4fgd23",
                "make":"ford",
                "model":"runner",
                "year":2015,
                "user_id":2,
            },
            {
                "vin_number":"dsf5sd4f25",
                "make":"Honda",
                "model":"Pilot",
                "year":2019,
                "user_id":3,
            },
        ]

        addresses=[
            {
                "address":"14130 castle blvd",
                "user_id":1
            },
            {
                "address":"5409 riverdale",
                "user_id":2
            },
            {
                "address":"5406 kenilworth",
                "user_id":3
            },
        ]

        metadata_obj.create_all(engine)

        users_rp=UserRepository(engine)

        cars_rp=CarRepository(engine)

        address_rp=AddressRepository(engine)

        for user in users:
            users_rp.created_user(**user)

        for car in cars:
            cars_rp.created_car(**car)

        for address in addresses:
            address_rp.created_address(**address)
        
        users_rp.update_user(1, email="pedro_pablo@gmail.com")

        cars_rp.delete_car(2)

        address_rp.delete_address(3)

        users_rp.delete_user(3)

        print(users_rp.get_all_users())

        cars_rp.associate_car_with_user(3, 1)

        cars_rp.update_cars(1, year=2026)

        print(cars_rp.get_all_cars())

        address_rp.update_address(3 , address="xxxxxxxxxxxxxx")

        print(address_rp.get_all_address())

if __name__=="__main__":
    main()