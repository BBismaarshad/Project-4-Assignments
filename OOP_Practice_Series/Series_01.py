class Student:

    def __init__ (self, name ,marks):

        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")  
        print(f"Marks: {self.marks}")




s1 = Student ("Bisma", 70)

s1.display()
