#Create an algorithm that asks the user for the gender of 6 people, where 1 represents female and 2 represents male.
#  Finally, display the percentage of women and men.

num_people=6
counter=1
num_females=0
num_males=0
percentage_female=0
percentage_male=0

while counter<=num_people:
    gender_input=int(input(f"please enter the gender for the person number {counter} (1 for female 2 for male)= "))
    if gender_input==1:
        num_females=num_females + 1
    elif gender_input==2:
        num_males=num_males+1
    counter=counter+1

percentage_female=num_females*100/num_people
percentage_male=num_males*100/num_people

print(f"the percentage of female is {percentage_female}%")
print(f"the percentage of male is {percentage_male}%")
