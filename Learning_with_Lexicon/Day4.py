# 1. Given a list of integers, return True if the sequence of numbers 1, 2, 3 appears in the list somewhere.
def arrayCheck(numList): 
    for i in range(len(numList) - 2):
        # Check if the current element and the next two elements form the sequence 1, 2, 3
        if numList[i] == 1 and numList[i + 1] == 2 and numList[i + 2] == 3:
            return True
    return False
  
test_List = [[1, 1, 2, 4, 1,3], [1, 1, 2, 4, 1], [1, 1, 2, 1, 2, 3] ]
result = [arrayCheck(case) for case in test_List]
print(result) # output => [False, False, True]
#-------------------------------------------------------------------------------------------------------------------

# 2. Given a string, return a new string made of every other character starting with the first, so "Hello" yields "Hlo".
def stringBits(str):
    return str[::2]

test_Str = ['Hello', 'Hi', 'Heeololeo']
result = [stringBits(str) for str in test_Str]
print(result) # output is: ['Hlo', 'H', 'Hello']
#-------------------------------------------------------------------------------------------------------------------

# 3. Return the number of even integers in the given array/list. 
def count_evens(no_List):
    return sum(1 for num in no_List if num%2 == 0)
    
test_List = [[2, 1, 2, 3, 4], [1, 3, 5], [2, 2, 0]]
result = [count_evens(n) for n in test_List]
print(result) #output is: [3, 0, 3]
#-------------------------------------------------------------------------------------------------------------------

# 4. Given a string, return a string where for every char in the original, # there are two chars.
def doubleChar(str):
    return ''.join(char * 2 for char in str)
    
test_Str = ['The', 'AAbb', 'Hi-There']
result = [doubleChar(s) for s in test_Str]
print(result) #output is: ['TThhee', 'AAAAbbbb', 'HHii--TThheerree']
