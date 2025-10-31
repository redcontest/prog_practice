# задание 3
import random
import string
import itertools


letters = string.ascii_uppercase
digits = string.digits
special = '!@#$%^&*'
password = ''

for i in range(3):
    randnum = random.randint(0, len(letters) - 1)
    password += letters[randnum]
for i in range(3):
    randnum = random.randint(0, len(digits) - 1)
    password += digits[randnum]
for i in range(2):
    randnum = random.randint(0, len(special) - 1)
    password += special[randnum]

vars = [''.join(i) for i in itertools.permutations(password)]
print(vars[random.randint(0, len(vars) - 1)])
