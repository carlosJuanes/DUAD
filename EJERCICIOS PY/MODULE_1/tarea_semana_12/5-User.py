
from abc import ABC,abstractmethod

class User(ABC):
    @abstractmethod
    def get_role(self):
        pass


    @abstractmethod
    def has_permission(self, permission):
        pass


class AdminUser(User):
    def __init__(self, name):
        self.name=name

    def get_role(self):
        return "admin"
    
    def has_permission(self, permission):
        return True


class RegularUser(User):
    def __init__(self, name):
        self.name=name
    
    def get_role(self):
        return "user"
    
    def has_permission(self, permission):
        permission_list=["read","view"]
        return permission in permission_list


user_1=AdminUser("Carlos")
user_2=RegularUser("Andrea")
print(user_1.name)
print(user_1.get_role())
print(user_1.has_permission("delete"))
print(user_2.name)
print(user_2.get_role())
print(user_2.has_permission("delete"))
