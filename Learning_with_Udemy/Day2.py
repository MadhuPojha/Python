#Instance, Class, Local Variables
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

#OOP-Method
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






