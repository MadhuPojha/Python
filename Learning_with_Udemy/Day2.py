# OOP: Instance, Class, Local Variables
class House():
    counter = 0     # class variable
    def __init__(self, address, area, price):
        self.address = address  #instance variable
        self.area = area        #instance variable
        self.price = price      #instance variable
        House.counter += 1  #increasing class variable

        House.quality = 'low'       # creating class var
        self.quality = 'medium'     # class var into instance var
        quality = 'high'            # local var
        print(House.quality, self.quality, quality)
    def present(self):
        print('The house at', self.address, 'has an area of', self.area, 'and cose', self.price)
    
house = House('Jungfru 9', 80, 600000)  #output: The house at Jungfru 9 has an area of 80 and cose 600000
house.present()
print('Class Var:', House.counter)  #Class Var
print(House.quality)        #printing class var
#print(self.quality, quality) we cannot access these two var, Not allowed outside the class
#-----------------------------------------------------------------------------------------------------------------------------------

# OOP-Method
class Doctor():
    def __init__(self, fName='John', lName='Smith'):
        self.fName = fName
        self.lName = lName
        self.__format_names()

    def __format_names(self):
        self.fName = self.fName.title()
        self.lName = self.lName.title()

    def introduce(self):
        print('Hi, I am', self.fName) #output: Hi, I am Alexander

    def compare_name(self, name_to_compare):
        if self.fName == self.compare_name:
            print('We have the same name!')
        else:
            print('Sorry, my name is different..')

    def get_first_last_name_together(self):
        return self.fName + ' ' + self.lName
doc = Doctor('Alexander', 'Smith')
doc.introduce()
doc.compare_name('John')
print(doc.__dict__)     #output: {'fName': 'Alexander', 'lName': 'Smith'}
#----------------------------------------------------------------------------------------------------------------------------------

#Can you have a default value for the self constructor parameter?
# ANS: you can do that, but the value will be simply ignored by Python.

class Car():
  def __init__(self='default value', speed=100):    # default value for self ignored
    self.speed = speed
 
my_toyota = Car()
print(my_toyota.__dict__)   #output: {'speed': 100}
#----------------------------------------------------------------------------------------------------------------------------------

#OOP-reflection-introspection
#TASK: Create a func that modifies all the string properties of any object by turning them into empty string
def empty_string(user_object):
    for prop_name in user_object.__dict__.keys():
        prop_value = getattr(user_object, prop_name)
        if isinstance(prop_value, str):
            setattr(user_object, prop_name, '')

class Doctor():
    def __init__(self, fName='John', lName='Smith'):
        self.fName = fName
        self.lName = lName
        self.__format_names()

    def __format_names(self):
        self.fName = self.fName.title()
        self.lName = self.lName.title()

    def introduce(self):
        print('Hi, I am', self.fName)

    def compare_name(self, name_to_compare):
        if self.fName == self.compare_name:
            print('We have the same name!')
        else:
            print('Sorry, my name is different..')

    def get_first_last_name_together(self):
        return self.fName + ' ' + self.lName
    
doc = Doctor('Alexander', 'Smith')
doc.introduce()    # output: Hi, I am Alexander
empty_string(doc)
doc.introduce()    # output: Hi, I am
#----------------------------------------------------------------------------------------------------------------------------------

#OOP-Inheritance-intro

class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class WaterVehicle(Vehicle):
    pass

class Car(LandVehicle):
    pass

class Boat(WaterVehicle):
    pass
print(issubclass(LandVehicle, Vehicle))		# True
print(issubclass(WaterVehicle, Vehicle))	# True

print(issubclass(Car, LandVehicle))			# True
print(issubclass(Car, WaterVehicle))		# False

print(issubclass(Boat, LandVehicle))		# False
print(issubclass(Boat, WaterVehicle))		# True
#----------------------------------------------------------------------------------------------------------------------------------

#OOP-Inheritance-properties:
class Vehicle:
	def __init__(self, speed):
		self.speed = speed

class LandVehicle(Vehicle):
	def __init__(self, speed, wheel_count):
			super().__init__(speed)	# or we can use this: Vehicle.__init__(self, speed)		
			self.wheel_count = wheel_count

class Car(LandVehicle):
    pass

car = Car(5, 10)
print(car.__dict__)	# output:{'speed': 5, 'wheel_count': 10}
print(car.speed)	# output: 5
#----------------------------------------------------------------------------------------------------------------------------------

#OOP-Inheritance-class-variables-methods

class Vehicle:
	class_msg = 'This is the message from the Vehicle class!'
	def __init__(self, speed):
		self.speed = speed

class LandVehicle(Vehicle):
	def __init__(self, speed, wheel_count):
			super().__init__(speed)	# or we can use this: Vehicle.__init__(self, speed)		
			self.wheel_count = wheel_count

	def speed_up(self):
		self.speed += 5

class Car(LandVehicle):
	def super_speed(self):
		print('Super speed activated!')
		super().speed_up()
		super().speed_up()
		super().speed_up()

car = Car(10, 4)
print(car.__dict__) 
car.super_speed()
print(car.__dict__) 
car.speed_up()
print(car.__dict__) 
#----------------------------------------------------------------------------------------------------------------------------------

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
str = 'Hello'
str2 = 'Hell'
str2 += 'o'
print("is with string: ", str is str2)
print("== with string", str == str2)



