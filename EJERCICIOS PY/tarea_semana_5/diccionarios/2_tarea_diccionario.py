# Create a program that creates a dictionary using two lists of the same size,
#  using one for its keys and the other for its values.

keys = ["spain", "france", "italy", "germany"]
values = ["madrid", "paris", "rome", "berlin"]

countries_and_capitals = {}
length = len(keys) 

for index in range(length): 
    country = keys[index]
    capital = values[index]
    countries_and_capitals[country] = capital
print(countries_and_capitals)