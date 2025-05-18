
class Counter:
    count = 0


    def __init__(self):

        Counter.count += 1


    @classmethod
    def show_count(cls):
        print(f"Total object created : {cls.count}")

cls1 = Counter()
cls2 = Counter()
Counter.show_count()        

