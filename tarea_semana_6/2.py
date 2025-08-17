# 2. "Experiment with the concept of scope:"
# "Try to access a variable defined inside a function from outside."

def name():
    my_name="Carlos Juanes"
    print(my_name)


# print(my_name)
print()
print()
# "Try to access a global variable from inside a function and change its value."
total_points = 0

def increase(points):
    global total_points
    print(f"Total points before increase: {total_points}")
    total_points += points
    print(f"Total points after increase: {total_points}")


def decrease(points):
    global total_points
    print(f"Total points before decrease: {total_points}")
    total_points -= points
    print(f"Total points after decrease: {total_points}")


print(f"Initial global score: {total_points}")

increase(10)

decrease(5)