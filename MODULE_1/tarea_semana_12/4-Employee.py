class Employee:
    def __init__(self, name, salary):
        self._name=name
        self._salary=salary

    @property
    def name(self):
        print(f"Name:")
        return self._name
    
    @property
    def salary(self):
        print("Salary: ")
        return self._salary
    

    @name.setter
    def name(self, new_name):
        self._name=new_name

    @salary.setter
    def salary(self, new_salary):
        if new_salary > 0:
            self._salary=new_salary
        else:
            raise ValueError("error the salary should not be a negative number")
        
    def promote(self, percentage):
        new_salary=self._salary+(self._salary*percentage)
        self.salary=new_salary

try:
    employee_1=Employee("Ana", 1000)
    employee_1.promote(0.1)
    print(employee_1.salary)
    print(employee_1.name)
    
except ValueError as e:
    print(e)