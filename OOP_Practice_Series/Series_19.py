class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

times3 = Multiplier(3)

print(callable(times3)) 

result = times3(10)
print(result) 
