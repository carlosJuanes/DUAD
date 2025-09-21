"""Create a decorator that prints the parameters and return value of the function it decorates.."""


def display(func):
    def wrapper(*args):
        print("Parameters")
        print(*args)
        result=func(*args)
        print("return value:", result)
        return result

    return wrapper


@display
def create_user(name, last_name):
    return name, last_name


create_user("Carlos", "Juanes")