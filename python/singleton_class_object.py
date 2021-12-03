class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta,cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    pass

class Constants(SingletonClass):

    def __init__(self):
        self.name = 'name'

c = Constants()
c2 = Constants()

print(c, c2)
print(id(c), id(c2))

print(c.name, c2.name)

c.name = 'changed'
print(c.name, c2.name)

c2.name = 'changed again'
print(c.name, c2.name)
