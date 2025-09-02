# Create a program that uses a list to delete keys from a dictionary.


vehicle_description= {
    "brand":"toyota",
    "model":"corolla",
    "year":"2016",
    "color":"rojo"
}
keys_to_delete=["year","color"]
value_deleted={}
print(f"original dictionary= {vehicle_description}")

for keys in keys_to_delete:
    delete=vehicle_description.pop(keys)
    value_deleted[keys]=delete
print(f"dictionary with deleted keys= {vehicle_description}")
print(f"deleted keys= {value_deleted}")