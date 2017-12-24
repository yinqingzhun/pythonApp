import types

class Animal(object):
    def __init__(self):
        self.name = 'Animal'
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def __init__(self):
        self.name = 'Dog'
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    def __init__(self):
        self.name = 'Cat'
    def run(self):
        print('Cat is running...')
def fn():
    pass;


print(type(fn)==types.FunctionType)
print(type((x for x in range(10)))==types.GeneratorType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type(123)==int)
print(type('')==str)

dog=Dog();
print(isinstance(dog,Animal))
print(isinstance([1, 2, 3], (list)))
print(isinstance((1, 2, 3), (tuple)))
#print object methods and properties
#print(dir(Dog))
if(hasattr(dog,'name')):
    print(dog.name)
setattr(dog,'age',3);
print(getattr(dog,'x','x is absent'))
print(dog.age)
getattr(dog,'run')()


