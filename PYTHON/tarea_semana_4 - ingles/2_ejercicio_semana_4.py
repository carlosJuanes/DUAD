#2 create a program that ask the user for their , first name, last name, and age then displays whether they are a baby, child, 
#preteen, teenager, young adult, adult, or senior adult 
name=input("enter your name= ")
last_name=input("enter your last name= ")
age=int(input("enter your age= "))

if age<=2:
    print(f"{name} {last_name}, age {age} baby")
elif age<=6:
    print(f"{name} {last_name}, age {age} child")
elif age<=12:
    print(f"{name} {last_name}, age {age} preteen")
elif age<=20:
    print(f"{name} {last_name}, age {age} teenager")
elif age<=40:
    print(f"{name} {last_name}, age {age} young adult")
elif age<=65:
    print(f"{name} {last_name}, age {age} adult")
elif age>65:
    print(f"{name} {last_name}, age {age} senior adult")