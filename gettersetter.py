class A:
    def __init__(self):
        # __slots__ = ()
        
        self.__name = ""

    # @property
    # def name(self):
    #     return self.__name

    # @name.setter
    # def name(self, name):
    #     self.__name = name

a = A()
a.name = "test"

b = a.name

print(b.__dict__)