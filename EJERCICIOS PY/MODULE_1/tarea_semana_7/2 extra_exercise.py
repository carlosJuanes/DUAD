# Create a function convert_to_integer(input_list) that:
# - Receives a list of strings
# - Tries to convert each element to an integer using int()
# - Uses try-except to catch ValueError errors
# - If an element cannot be converted, display "Could not convert element: <value>" and continue with the others.

def convert_to_integer(input_list): 
    for item in input_list: 
        try:
            item_int = int(item)
            print(f"{item} converted to {item_int}")
        except ValueError:
            print(f"Could not convert element: {item}") 

my_list = ['4', 'hola', '10', '5.2']
print("Result:")
convert_to_integer(my_list)
