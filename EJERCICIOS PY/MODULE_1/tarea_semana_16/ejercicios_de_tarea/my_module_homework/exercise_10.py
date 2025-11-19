# 10 Create a test class containing at least 3 methods that perform operations on numbers 
# (such as addition, average, or conversion), and write tests for the following scenarios:
# A case using positive numbers.
# A case using negative numbers.
# A case using zeros."

class MathOperations:
    def __init__(self):
        pass
    
    def sum(self, number_1, number_2):
        result=number_1 + number_2
        return result
    
    def rest(self, number_1, number_2):
        result=number_1- number_2
        return result
    
    def division(self, number_1, number_2):
        if number_2==0:
            raise ValueError("cannot be divided by zero")
        result= number_1/ number_2
        return result
    

