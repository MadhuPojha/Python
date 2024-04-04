# 1. String Formatting: (Use print formatting to print the following string: "Hello my dog's name is Sammy and he is 4 years old")

name = "Sammy" #assigning a value to the variable of string data type.
age = 4        #assigning a value to the variable of int data type.

print("Hello my dog's name is {] and he is {} years old".format(name, age)) # Printing output to the screen.
#----------------------------------------------------------------------------------------------------------------------------------

#2. Dictionary: (Using keys and indexing, grab the 'hello' from the dictionaries.

d1 = {'simple_key':'hello'}      # difine simple dictionary d1.
print("d1: ", d1['simple_key'])  # output: hello

d2 = {'k1':{'k2':'hello'}}       #difine nested dictionary.
print("d2: ", d2['k1']['k2'])    #output: hello

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]} #difine nested dictionary and nested list in one variable.
print("d3: ", d3['k1'][0]['nest_key'][1][0]) #output: hello
#----------------------------------------------------------------------------------------------------------------------------------

# 3. Reassign "hello" to be "goodbye"

l = [3,7,[1,4,'hello']] # List inside a list is called nested list.

l[2][2] = "goodbye"
print(l)
#----------------------------------------------------------------------------------------------------------------------------------

# 4. Use indexning to print:

str = "s = 'Python' # Assign a string types varialbe.
print(s[-2])   #output: 'o' 
print(s[:4])   #output: 'Pyth'
print(s[1:4])  #output: 'yth'
print(s[::-1]) #output: 'nohtyP'

#----------------------------------------------------------------------------------------------------------------------------------

# 5. Use a set to find the unique values from list 

myList = [1,1,1,1,1,2,2,2,2,3,3,3,3] # creating a variable myList of List daya type
print(set(mylist)) # Output is: [1,2,3]
