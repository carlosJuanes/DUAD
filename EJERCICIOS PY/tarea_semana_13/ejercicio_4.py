"""Create a function that prints “Hello, [name]” two times:
Create a decorator @repeat_twice that makes the decorated function execute two times in a row,
with the same arguments."""


def repeat_twice(func):
    def wrapper(name, *args, **kwarg):
        func(name, *args, **kwarg)
        func(name, *args, **kwarg)
    return wrapper

@repeat_twice
def greet_person(name):
    print(f"Hello, {name}")
    


greet_person("Carlos Juanes")
