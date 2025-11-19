"""5- Input Validation before Sorting
        -Create a function that receives a list and validates:
        -That all elements are numbers
        -That it is not empty
        -Then apply bubble_sort if the validations pass
        -If there is an error, it must return an appropriate message"""


def bubble_sort(input_list):
    for outer_index in range(0, len(input_list)-1):
        has_made_change= False
        for index in range(0, len(input_list)-1-outer_index):
            current_element=input_list[index]
            next_element=input_list[index+1]
            print(f"iterating: {outer_index} - {index}, current element: {current_element}, next element: {next_element}")
            if current_element>next_element:
                print("the current number is greater than the next number, moving...")
                input_list[index+1]=current_element
                input_list[index]=next_element
                has_made_change=True
        if not has_made_change:
            return input_list
    return input_list

def validated_bubble_sort(input_list):
    if not input_list:
        return ("Error the list is empty")
    for element in input_list:
        if not isinstance(element,(int, float)):
            return "Error: List contains non-numeric elements"
    return bubble_sort(input_list)


print( validated_bubble_sort([5,4,10,51,1]))
print(validated_bubble_sort([5,4,"Hola",51,1]))