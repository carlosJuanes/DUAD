"""1- Create a bubble sort on your own without reviewing the lesson's code."""


def my_bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) -1):
        has_made_change= False
        for index in range(0, len(list_to_sort)-1 -outer_index):
            current_element=list_to_sort[index]
            next_element=list_to_sort[index+1]
            print(f"iterating: {outer_index} - {index}, current element: {current_element}, next element: {next_element}")
            if current_element>next_element:
                print(f"the current number is greater than the next number, moving...")
                list_to_sort[index]=next_element
                list_to_sort[index+1]=current_element
                has_made_change=True
        if not has_made_change:
            return list_to_sort
    return list_to_sort

my_list=[1, 2, 3, 4, 5]
my_bubble_sort(my_list)
print(my_list)

