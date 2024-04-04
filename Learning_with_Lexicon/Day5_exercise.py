# 1. Calsulate area and radius of circle

class Circle:
    pi = 3.14
    def __init__(self, radius = 1): #Circle get initialized with radius
        self.radius = radius
    def get_Area(self):                 # method for calculate the area of circle
        return self.radius * self.radius *self.pi
    def set_Radius(self, radius):   # method for reset the radius
        self.radius = radius
    def get_Radius(self):           # method for getting radius
        return self.radius

c = Circle()
c.set_Radius(2)
print("Radius of a circle is ", c.get_Radius()) # output: Radius of a circle is  2
print("Area of a circle is ", c.get_Area())     #output: Area of a circle is  12.56
#------------------------------------------------------------------------------------------------------------------------------------

# 2. Create Person class and display info

class Person:  # Define a class names as Person
  def __init__(self, name, age):  #_init__ method in Python is used to initialize objects of a class.
    self.name = name
    self.age = age

  def __str__(self):  #The string representation of an object WITH the __str__() function
    return f"Person name is {self.name} and age is {self.age}."

p1 = Person("John", 36)  # p1 is object of class Person
print(p1)  
#------------------------------------------------------------------------------------------------------------------------------------

# 3. Create strudent class & display info

class Student:  #Defined a class named Student 
    def __init__(self, name, age, grade): # Intializing attribute name, age, agrade
        self.name = name
        self.age = age
        self.grade = grade

    def getInfo(self):  # Method to display the student's information.
        return f'Student name is {self.name}, age is {self.age} and grade is {self.grade}'

    def promote(self):  # Method to promote the student to the next grade level
        self.grade = self.grade + 1
        
testCase = Student("Anna", 15, 9)
print(testCase.getInfo())           #output: Student name is Anna, age is 15 and grade is 9
testCase.promote()  #Calling this method to update the grade
print("Updated record:", testCase.getInfo()) #output: Updated record: Student name is Anna, age is 15 and grade is 10
#------------------------------------------------------------------------------------------------------------------------------------

# 4. Use data dictionary in class

class Person:
    def __init__(self, data:dict):
        self.__dict__ = data
    def __str__(self):
        return ', '.join([f'{key} = {value}' for key, value in self.__dict__.items()])    
    
data_dict1 = {
    'a': 10,
    'b':20
}
data_dict2 = {
    'a': 10,
    'b': 20
}
p1 = Person(data_dict1)
p2 = Person(data_dict2)
print(p1)
print(p2) 
#------------------------------------------------------------------------------------------------------------------------------------

# 5. Use **kwargs in class

class Person:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __str__(self):
        return ', '.join([f'{key} : {value}' for key, value in self.__dict__.items()])    

p1 = Person(name='Madhu', age=35)
p2 = Person(name='Madhu', age=35, email='mad@gmail.com')

print(p1)   # output=> name : Madhu, age : 35
print(p2)   # output=> name : Madhu, age : 35, email : mad@gmail.com
