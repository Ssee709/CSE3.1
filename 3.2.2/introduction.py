'''
import random

def random_number():
    n1 = random.randint(30, 50)
    print(n1)

for x in range(12):
    random_number()

x = 0
while x != 100:
    random_number()
    x += 1
'''

def larger_val(num1, num2):
    if num1 > num2:
        return num1
    elif num1 == num2:
        return num2
    else:
        return num2

biggest_number = larger_val(14, 22)

print(biggest_number)

'''
return, void, functions, parameters
classes'''

