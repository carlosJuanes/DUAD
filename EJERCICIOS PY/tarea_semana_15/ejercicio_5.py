"Analyze the bubble_sort algorithm using Big O Notation"


"""=========================================================
            -1) BUBBLE SORT----→ O(N²)
========================================================="""
def my_bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) -1):                                       #O(N)
        has_made_change= False                                                               #O(1)
        for index in range(0, len(list_to_sort)-1 -outer_index):                             #O(N)
            current_element=list_to_sort[index]                                              #O(1)
            next_element=list_to_sort[index+1]                                               #O(1)
            print(f"iterating: {outer_index} - {index}, current element: {current_element}, next element: {next_element}") #O(1)
            if current_element>next_element:                                                       #O(1)
                print(f"the current number is greater than the next number, moving...")      #O(1)
                list_to_sort[index]=next_element                                             #O(1)
                list_to_sort[index+1]=current_element                                        #O(1)
                has_made_change=True                                                         #O(1)
        if not has_made_change:                                                              #O(1)
            return list_to_sort                                                              #O(1)
    return list_to_sort                                                                      #O(1)

my_list=[1, 2, 3, 4, 5]                                                                      #O(1)
my_bubble_sort(my_list)                                                                      #O(1)
print(my_list)                                                                               #O(1)


"""=========================================================
            -2) PRINT NUMBERS TIMES 2----→ O(N)
========================================================="""
def print_numbers_times_2(numbers_list):
	for number in numbers_list:                                                              #O(N)
		print(number * 2)                                                                    #O(1)



"""=========================================================
            -3) CHECK IF THE LIST HAVE AN EQUAL ----→ O(N²)
========================================================="""
def check_if_lists_have_an_equal(list_a, list_b):                                           
	for element_a in list_a:                                                                #O(N)
		for element_b in list_b:                                                            #O(N²)
			if element_a == element_b:                                                      #O(1)
				return True                                                                 #O(1)
				
	return False                                                                            #O(1)



"""=========================================================
            -4) PRINT TEN OR LESS ELEMENTS ----→ O(1)
========================================================="""
def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print)                                                           #O(1)
	for index in range(min(list_len, 10)):                                                  #O(1)
		print(list_to_print[index])                                                         #O(1)
		

"""=========================================================
            -5) GENERATE LIST TRIOS  ----→ O(N³)
========================================================="""
def generate_list_trios(list_a, list_b, list_c):                                            
	result_list = []                                                                        #O(1)
	for element_a in list_a:                                                                #O(N)
		for element_b in list_b:                                                            #O(N²)
			for element_c in list_c:                                                        #O(N³)
				result_list.append(f'{element_a} {element_b} {element_c}')                  #O(1)
				
	return result_list                                                                      #O(1)


"""=========================================================
            -6) EXTRA EXERCISE  
========================================================="""
"1)- The following two algorithms do the same thing: calculate the sum of the first n natural numbers"
"VERSION 1"
def manual_add(n):
    result = 0                                                                              #O(1)
    for i in range(1, n + 1):                                                               #O(N)
        result += i                                                                         #O(1)
    return result                                                                           #O(1)

"VERSION 2"
def add_formula(n):
    return n * (n + 1) // 2                                                                 #O(1)

"""Questions:
What is the complexity of each version?
R/ = Version 1 → O(N)
     Version 2 → O(1)

Which version would you use if the number were 1,000,000,000? Why?
R/ = I would use version two because it is the most efficient since it is based on a mathematical operation, 
regardless of the value of N, it would be easier to do, and in the first version, since N is 1,000,000,000, 
I would have to go through that same number of times to add."""

"-------------------------------------------------------------------------------------------------------------------"
"2)- Consider the following two algorithms:"
def linear_search(my_list, target):
    for item in my_list:                                                                    #O(N)
        if item == target:                                                                  #O(1)
            return True                                                                     #O(1)
    return False                                                                            #O(1)


def binary_search(my_list, target):
    low = 0                                                                                 #O(1)
    high = len(lst) - 1                                                                     #O(1)
    while low <= high:                                                                      #O(log N)
        mid = (low + high) // 2                                                             #O(1)
        if my_list[mid] == target:                                                          #O(1)
            return True                                                                     #O(1)
        elif my_list[mid] < target:                                                         #O(1)
            low = mid + 1                                                                   #O(1)
        else:
            high = mid - 1                                                                  #O(1)
    return False                                                                            #O(1)

""" Questions:
- What is the complexity of each algorithm?
    R/ Linear search = O(N)
       Binary search = O(log N)
- Under what conditions is each one appropriate to use?
    R/ Linear search = in small lists
       Binary search = in ordered lists
- What happens if the list is not sorted?
    R/ Linear search = It doesn't matter if it's not sorted
       Binary search = In this case it wouldn't work because the code assumes it is a list of sorted numbers
         since it discards each half, and by not being sorted it wouldn't work as expected."""

"------------------------------------------------------------------------------------------------------"
"Analyze the following function"
def print_all_pairs(my_dict):
    for key1 in my_dict:                                                                    #O(N)
        for key2 in my_dict:                                                                #O(N²)
            print(f"{key1}-{key2}")                                                         #O(1)
"""Questions
- What is the time complexity?
    R/ O(N²)
- How long does it take if there are 1 million keys?    
    R/ 1 000 000 X 1 000 000 = 1 trillion"""