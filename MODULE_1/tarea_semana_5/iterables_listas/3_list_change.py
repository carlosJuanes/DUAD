# Create a program that swaps the first and last elements of a list. It must work with lists of any size.


numbers=[100,200,300,400,500]
first_number=numbers[0]
numbers[0]=numbers[len(numbers)-1]
numbers[len(numbers)-1]=first_number
print(numbers)
