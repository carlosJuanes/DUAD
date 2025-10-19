"""1- Create the following unit tests for the bubble_sort algorithm:
    1. Works with a small list.
    2. Works with a large list (more than 100 elements).
    3. Works with an empty list.
    4. Does not work with non-list parameters."""


def my_bubble_sort(list_to_sort):
    if not isinstance(list_to_sort, list):
        raise TypeError("the input must be a list to be sorted")
    for outer_index in range(0, len(list_to_sort) -1):
        has_made_change= False
        for index in range(0, len(list_to_sort)-1 -outer_index):
            current_element=list_to_sort[index]
            next_element=list_to_sort[index+1]
            # print(f"iterating: {outer_index} - {index}, current element: {current_element}, next element: {next_element}")
            if current_element>next_element:
                # print(f"the current number is greater than the next number, moving...")
                list_to_sort[index]=next_element
                list_to_sort[index+1]=current_element
                has_made_change=True
        if not has_made_change:
            return list_to_sort
    return list_to_sort
