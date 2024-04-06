#OOP-Property-method-overriding
class Animal():
	def __init__(self):
		self.species = 'general'
	def produce_sound(self):
		print('General animal sound')

class Dog(Animal):
	def __init__(self):
		self.species = 'Canis familiaris'
	def produce_sound(self):
		print('woof, woof!')
                
my_pet = Dog()
print(my_pet.species)
my_pet.produce_sound()	#override super class method
#----------------------------------------------------------------------------------------------------------------------------------

# OOP-isinstance-is
class Vehicle:
	def __init__(self, speed):
		self.speed = speed

class LandVehicle(Vehicle):
	def __init__(self, speed, wheel_count):
			super().__init__(speed)	# or we can use this: Vehicle.__init__(self, speed)		
			self.wheel_count = wheel_count

class Car(LandVehicle):
    pass

my_vehicle = Vehicle(50)
my_landV = LandVehicle(50, 4)
my_car = Car(60, 4)

print(isinstance(my_vehicle, Car))
print(isinstance(my_landV, Vehicle))
print(isinstance(my_car, LandVehicle))

print()
my_vehicle = Vehicle(60)
new_vehicle = my_vehicle
print(my_vehicle is new_vehicle)
my_vehicle = Vehicle(60)
new_vehicle = Vehicle(60)
print(my_vehicle is new_vehicle)

num = 5
num2 = 3
num2 += 2
print("is with int:", num is num2)
#--------------------------------------------------------------------------------------------------------------------

# OOP-multiple-inheritance
class Vehicle():
    def go(self):
        print('Goint!')
    def introduce(self):
        print('I am a Vehicle!')
class Flyable():
    def fly(self):
        print('Flying!')
    def introduce(self):
        print('I am a Flyable!')
class Airplane(Vehicle, Flyable):
    pass

my_plane = Airplane()
my_plane.go()
my_plane.fly()
my_plane.introduce()
str = 'Hello'
str2 = 'Hell'
str2 += 'o'
print("is with string: ", str is str2)
print("== with string", str == str2)
#----------------------------------------------------------------------------------------------------------------

# OOP-multiple-inheritance
# MRO: Method Resolution Order
class Vehicle():
    def go(self):
        print('Goint!')
    def introduce(self):
        print('I am a Vehicle!')
class Flyable():
    def fly(self):
        print('Flying!')
    def introduce(self):
        print('I am a Flyable!')
class Airplane(Vehicle, Flyable):
    pass

my_plane = Airplane()
my_plane.go()
my_plane.fly()
my_plane.introduce()
#----------------------------------------------------------------------------------------------------------------

#OOP: The __bases__ property

class Vehicle():
   pass
        
class Rideable():
   pass
      
class PetrolVehicle(Vehicle):
   pass
        
class Car(PetrolVehicle, Rideable):
   pass

print(Vehicle.__bases__)		# output: (<class 'object'>,)
print(Rideable.__bases__)		# output: (<class 'object'>,)
print(PetrolVehicle.__bases__)	# output: (<class '__main__.Vehicle'>,)
print(Car.__bases__)			# output: (<class '__main__.PetrolVehicle'>, <class '__main__.Rideable'>)

#----------------------------------------------------------------------------------------------------------------
