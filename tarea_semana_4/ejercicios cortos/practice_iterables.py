# 1. Create a program that iterates and prints the values of two lists of the same size simultaneously

first_list=["MAY", "FORCE", "WITH"]
second_list=["THE", "BE", "YOU"]

for index in range(len(first_list)):
    first=first_list[index]
    second=second_list[index]
    print(f"{first} {second}")
    
