#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
num = number % 10
if num > 5:
    msg = 'and is greater than 5'
elif num == 0:
    msg = 'and is 0'
else:
    msg = 'and is less than 6 and not 0'
print(f'Last digit of {number} is {num} {msg}')
