# Introduction to oop
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height
a = int(input('What is the width? '))
b = int(input('What is the height? '))
rectangle = Rectangle(a, b)
print('The area is ', rectangle.get_area())
#---------------------------------------------------------------------------------------------------------------------

# Classes and objects
class User:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def introduce(self):
        print(f'Hello, I am {self.name} and I live in {self.city}')
        
first_user = User('DarkKnight', 'Hell')
second_user = User('Ruler_of_darkness', 'Darkness')
third_user = User('Martin', 'Boston')

first_user.introduce()
second_user.introduce()
third_user.introduce()
#-----------------------------------------------------------------------------------------------------------------------------------

# Encapsulation and abstraction (Ecapsulation says that object should keep their state private only expose public function)

class Car():
    def __init__(self, model, colour, initial_speed = 0):
        self.model = model
        self.colour = colour
        if initial_speed < 0:
            self.__speed = 0    # __speed make the attribute private
        else:
            self.__speed = initial_speed
    
    def speed_up(self):
        self.__speed += 5

    def slow_down(self):
        if self.__speed < 5:
            self.__speed = 0
        else:
            self.__speed -= 5

    def show_speed(self):
        print(f'Current speed is {self.__speed}')

my_car = Car('T-Roc', 'red', 80)
my_car.show_speed()
#-----------------------------------------------------------------------------------------------------------------------------------

# Instance Variable
class Dog():
    def __init__(self, name, age):
        self.__name = name
        self.age = age

my_pet = Dog('Teddy', 2)
print(my_pet.__dict__)      #output: {'_Dog__name': 'Teddy', 'age': 2}
print(my_pet._Dog__name)    #output: Teddy
#-----------------------------------------------------------------------------------------------------------------------------------

# Introducing class variable

class Dog():
    counter = 0     # defining class variable name as counter
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.counter += 1    #assigning class variable
my_pet = Dog('Teddy', 2)
kates_pet = Dog('Foxt', 5)
adams_pet = Dog('Luna', 1)
print(my_pet.counter)
print(kates_pet.counter)
print(adams_pet.counter)
print(my_pet.__dict__)
print(Dog.counter)  # accessing class variable
