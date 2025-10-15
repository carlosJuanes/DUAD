"""2- Modify the bubble_sort to work from right to left, 
sorting the smaller numbers first"""


def my_bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort)-1):
        has_made_change=False
        for index in range(len(list_to_sort)-1, outer_index -1, -1):
            current_element=list_to_sort[index]
            before_element=list_to_sort[index-1]
            if current_element>before_element:
                list_to_sort[index]=before_element
                list_to_sort[index-1]=current_element
                has_made_change=True
        if not has_made_change:
            return list_to_sort
    return list_to_sort

my_list = [5, 2, 8, 1, 9]
my_bubble_sort(my_list)
print(f"Sorted list (R->L): {my_list}")