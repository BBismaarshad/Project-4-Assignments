# Define the Car class
class Car:
    def __init__(self, brand):
        # Public variable
        self.brand = brand

    # Public method
    def start(self):
        print(f"{self.brand} started")

# Instantiate the Car class
my_car = Car("Toyota")

# Access public variable from outside the class
print(my_car.brand)

# Call public method from outside the class
my_car.start()
