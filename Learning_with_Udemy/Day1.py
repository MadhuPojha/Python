#-------------------------------------------------------------------------------------------------------

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
