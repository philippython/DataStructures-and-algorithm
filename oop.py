# Creating a Base class
class Base:
    #  class attribute
    attr1 = 80
    def __init__(self, city):
        self.a = "GeeksforGeeks"
        self.__c = city
 
# Creating a derived class
class Derived(Base):
    def __init__(self, city):
 
        # Calling constructor of
        # Base class
        super().__init__(self, city)
        print("Calling private member of base class: ")
 
 
# Driver code
obj1 = Base("New York")
print(obj1.a)
 
print(obj1.attr1)
# Uncommenting print(obj1.c) will
# raise an AttributeError
 
obj2 = Derived("Toronto")
print(obj2.__c)
# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class