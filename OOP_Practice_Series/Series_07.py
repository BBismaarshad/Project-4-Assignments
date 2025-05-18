class Employee:
    def __init__ (self, name , _salary , __snn):
        
        self.name = name 
        self._salary = _salary
        self.__snn = __snn

emp = Employee("Bisma" , 12000 , "123-49-9976 ")

print(f"public : " ,emp.name)
print(f"Protected :", emp._salary)
print(f"private :", emp.__snn)

print("Private (__ssn) via name mangling:", emp._Employee__ssn)

