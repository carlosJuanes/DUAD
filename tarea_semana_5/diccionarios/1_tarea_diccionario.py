# 1- Create a dictionary that stores the following information about a hotel:

hotel = {
    "name": "hotel 5 star",
    "number_of_stars": "5",
    "rooms": [
        {
            "number": 10,
            "floor": "first",
            "price_per_night": 100.00,
        },
        {
            "number": 20,
            "floor": "second",
            "price_per_night": 200.00,
        },
        {
            "number": 30,
            "floor": "third",
            "price_per_night": 300.00,
        }
    ]
}
print(hotel)
# for precio in hotel.values():
#     print(precio)
# print(hotel["rooms"][1]["price_per_night"])

# deleted_item=hotel.pop("rooms")
# print(hotel)
# print(deleted_item)
# deleted_item=hotel.pop()