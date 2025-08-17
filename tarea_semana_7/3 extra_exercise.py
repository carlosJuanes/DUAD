# Create a function sumar_valores(list) that:
# - Receives a list of mixed elements (strings, integers, floats)
# - Tries to convert each element to a float
# - If successful, adds the value to a total and displays: "<value> summed correctly"
# - If unsuccessful, displays: "Invalid element: <value>"
# - Finally, prints the total sum

def sum_values(input_list): 
    total_sum = 0
    for element in input_list:
        try:
            float_element = float(element)
            print(f"{float_element} summed correctly") 
            total_sum += float_element
        except ValueError:
            print(f"Invalid element: {element}") 
    print(f"Total sum: {total_sum}") 

my_list = ['10', 'manzana', '5.5', '3', 'n/a']
sum_values(my_list)