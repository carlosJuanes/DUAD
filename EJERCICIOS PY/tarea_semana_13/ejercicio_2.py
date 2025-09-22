"""Create a decorator that checks if all the parameters of the decorated function are numbers, and raises an exception if not."""


def check_numbers(func):
    def wrapper(*args, **kwarg):
        for arg in args:
            try:
                float(arg)
            except ValueError:
                raise TypeError("Error: Argument is not a number.")
        for value in kwarg.values():
            try:
                float(value)
            except ValueError:
                raise TypeError("Error: Argument is not a number.")        
        result=func(*args, **kwarg)
        return result
    return wrapper


@check_numbers
def sum(a, b):
    return(a+b)

try:
    sum_1=sum(1,"c")
    print(f"the result is: {sum_1}")
except TypeError as e:
    print(e)

try:
    sum_2=sum(10, 20)
    print(f"the result is: {sum_2}")
except TypeError as e:
    print(e)

try:
    sum_3=sum("hello", "world" )
    print(f"the result is: {sum_3}")
except TypeError as e:
    print(e)

try:
    sum_4=sum(1, 2)
    print(f"the result is: {sum_4}")
except TypeError as e:
    print(e)


