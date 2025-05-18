class Logger:
    def __init__ (self):
        print("Logger initialized: object create.")

    def __del__(self):
        print("Logger terminated: object destroyed.")    

log = Logger()
del log        
