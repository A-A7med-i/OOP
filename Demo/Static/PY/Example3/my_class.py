class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @staticmethod
    def static_method():
        print("Static Method")

    @staticmethod
    def get_count():
        return MyClass.count
