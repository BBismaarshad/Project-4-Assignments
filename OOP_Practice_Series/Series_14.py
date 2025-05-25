class Employee:

    def __init__(self,name ):
        self.name = name 


class Department:
    def __init__(self,employee):
        self.employee = employee


emplo = Employee ("Bisma")

dept = Department (emplo)

print(dept.employee.name)
