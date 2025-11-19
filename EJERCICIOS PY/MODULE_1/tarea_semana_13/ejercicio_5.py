"""Create a decorator @requires_login that:
Checks if the global variable user_logged_in is True.
If it's not, it should raise an exception "Unauthenticated user".
If it is, the decorated function executes normally."""

user_logged_in =True

def requires_login(func):
    def wrapper(*args, **kwarg):
        global user_logged_in
        if user_logged_in is False:
            raise ValueError("Unauthenticated user")
        result= func(*args, **kwarg)
        return result
    return wrapper


@requires_login
def view_profile():
    print("showing the profile...")


try:
    view_profile()
except ValueError as e:
    print(e)