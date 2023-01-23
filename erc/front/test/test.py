class MyMeta(type):
    def __call__(self, *args, **kwds):
        return super().__call__(*args, **kwds)

class Example(metaclass=MyMeta):
    def __call__(self, *args, **kwds):
        return True
    
    def __new__(cls):
        return super().__new__(cls)
    
    def __init__(self) -> None:
        pass

a = Example()
b = Example.__new__(Example).__init__()
print(a)
print(b)


class SomeClass:
    def __init__(self):
        pass
