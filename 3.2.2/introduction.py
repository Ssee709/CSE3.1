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