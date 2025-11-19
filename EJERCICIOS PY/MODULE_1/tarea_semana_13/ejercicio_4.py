
"""Create a function that prints “Hello, [name]” two times:
Create a decorator @repeat_twice that makes the decorated function execute two times in a row,
with the same arguments."""


def repeat_twice(func):
    def wrapper(*args, **kwarg):
        result=(
        func(*args, **kwarg),
        func(*args, **kwarg))
        return result
    return wrapper

@repeat_twice
def greet_person(name):
    print(f"Hello, {name}")
    
greet_person(name="Carlos juanes")
greet_person("Carlos Juanes")
