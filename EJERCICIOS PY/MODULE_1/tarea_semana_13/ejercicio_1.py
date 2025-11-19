"""Create a decorator that prints the parameters and return value of the function it decorates.."""


def display(func):
    def wrapper(*args,  **kwargs):
        print("Parameters")
        print(*args)
        for clave, valor in kwargs.items():
            print(f"{clave}: {valor}")
        result=func(*args, **kwargs)
        print("return value:", result)
        return result

    return wrapper


@display
def create_user(name, last_name, age=None):
    return name, last_name, age


create_user("Alfredo", "Medina", age=53)
create_user("Carlos", "Juanez", age=33)