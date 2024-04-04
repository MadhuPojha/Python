# 1. Write a program that takes a list of integers and uses list comprehension to create a new list containing only the even numbers from the original list.

listOf_int = [10,11,12,13,14,15,16,17,18,19,20]
#First Way: 
listOf_EvenNo = [i for i in listOf_int if i % 2 == 0]
print("Original list is:", listOf_int)
print("Even number from the above list is: ", listOf_EvenNo)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Write a program that creates a new tuple containing only the even numbers from a given tuple of integers.

no_tuple = (1,2,3,4,5,6,7,8,9,10)
tupleOf_evenNo = ()
listOf_evenNo = []
for i in range(len(no_tuple)):
    if no_tuple[i] % 2 == 0:
        listOf_evenNo.append(no_tuple[i]) #cannot add directly in tupleOf_evenNo because tuples are immutable
tupleOf_evenNo = tuple(listOf_evenNo)
print("Original tuple: ", no_tuple)
print("Even numbers from a above tuple: ", tupleOf_evenNo)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Write a program that takes two integers as input, base and exponent, and calculates the power using loops.

base = int(input("Enter a base: "))
exponont = int(input("Enter a exponent: "))
result = 1
for num in range(exponont):
    result *= base 
print("Ques1. Here is result: ",result)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4. Write a program that merges two dictionaries into a single dictionary. If a key is common to both dictionaries, the value from the second dictionary should be used.
dict1 = {
    "Name" : "Suhana",
    "Age" : "30",
    "Country" : "India"
}
dict2 = {
    "DOB" : "5 July 2014",
    "Email" : "abc@gmail.com",
    "Country" : "Sweden"
}
print("First dictionary dict1 is: ", dict1)  #{'Name': 'Suhana', 'Age': '30', 'Country': 'India'}
print("Second dictionary dict2 is: ", dict2) #{'DOB': '5 July 2014', 'Email': 'abc@gmail.com', 'Country': 'Sweden'}
dict3 = {}
for key in dict1:
    if key in dict1:
        if key not in dict2:
            dict2[key] = dict1[key] 
        else:
            dict2[key] = dict2[key]
dict3.update(dict2)
print("After merges third dictionary dict3 is: ", dict3) #{'DOB': '5 July 2014', 'Email': 'abc@gmail.com', 'Country': 'Sweden', 'Name': 'Suhana', 'Age': '30'}
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5. Write a program that takes a string as input and prints its reverse. 

my_String = "Program"
#print("Reverse of {} is {}:".format(my_String, my_String[::-1])) #===> Simple way output is:margorP

lenOf_Str = len(my_String)    # reverse the defined string using loop
reverse_Str = ""
while lenOf_Str > 0:
    reverse_Str += my_String[lenOf_Str - 1]
    lenOf_Str -= 1
print("Reverse of {} is {}:".format(my_String, my_String[::-1]))  #output is:margorP
#-------------------------------------------------------------------------------------------------------------------------------------------------------------

# 6. Write a program that calculates the sum of all elements in a given tuple.

my_tuple = (1,2,3,4,5) 
print("Original tuple is: ", my_tuple)
print("sum of all elements in a above tuple is:", sum(my_tuple)
