"""
Define a Student Class:
    Define a class named Student with the following attributes:
    name: Name of the student (string).
    age: Age of the student (int).
    grade: Grade level of the student (int).    
Add Methods:
    Add the following methods to the Student class:
    get_info( ): Method to display the student's information.
    promote ( ): Method to promote the student to the next grade level.
Test the Class:
    Create instances of the Student class and test its methods:
    Create a student named "Anna" with age 15 and grade 9. Use the get_info() method to display her information.
    Promote Anna to the next grade level using the promote() method, then use get_info() to display her updated information.
"""
class Student:
    def __init__(self, name, age, grade): 
        self.name = name
        self.age = age
        self.grade = grade

    def getInfo(self):
        return f'Student name is {self.name}, age is {self.age} and grade is {self.grade}'

    def promote(self):
        self.grade = self.grade + 1
        
testCase = Student("Anna", 15, 9)
print(testCase.getInfo())           #output: Student name is Anna, age is 15 and grade is 9
testCase.promote()
print("Updated record:", testCase.getInfo()) #output: Updated record: Student name is Anna, age is 15 and grade is 10
