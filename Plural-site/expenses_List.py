#LIST & LOOP in Python

expenses = [10.50, 8, 5, 15, 20, 5, 3]

#total = sum(expenses)
#print('You spent $', total, sep='')

sum = 0
for x in expenses:
    sum = sum + x
print('You spent $', sum, sep='')

# Sencond way 

total = 0
expenses = []
num_expenses = int(input("Enter # of expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expenses:")))

total = sum(expenses)
print('You spent $', total, sep='')

