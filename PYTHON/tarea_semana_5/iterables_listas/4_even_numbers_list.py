# Create a program that removes all odd numbers from a list.


number_list=[7,50,19,30,21,10,40,60,13,19,47,80,3,7,100]
even_numbers=[]

for number in number_list:
    if number%2==0:
        even_numbers.append(number)
print(even_numbers)
