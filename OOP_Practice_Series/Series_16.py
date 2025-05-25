
def log_function_call(fun):
    def wrapper():
        print("Function is beging called")
        return fun()
    return wrapper

@log_function_call
def say_hell():
    print("hello Bisma ")

say_hell()


