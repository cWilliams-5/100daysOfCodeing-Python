# Password Generator
# 100 Days Of Python Day 4

import random

print('Welcome to the PyPasswordGenerator')
letters = int(input('How many letters would you like in your password?'))
numbers = int(input('How many numbers would you like?'))
symbols = int(input('How many symbols would you like?'))
total = letters + numbers + symbols
count = 0
# countL = 0
# countN = 0
# countS = 0
password = ''
alpha = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G',
         'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'M', 'm', 'n', 'N',
         'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U',
         'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']
num = [1,2,3,4,5,6,7,8,9,0]
sym = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ';', ':', '?', '/']
while count <= total:
    if letters > 0 and numbers > 0 and symbols > 0:
        ran = random.randint(1,3)
        if ran == 1:
            password = password + (random.choice(alpha))
            letters += -1
        if ran == 2:
            password = password + (str(random.choice(num)))
            numbers += -1
        if ran == 3:
            password = password + (random.choice(sym))
            symbols += -1
    elif letters > 0 and numbers > 0:
        ran = random.randint(1,2)
        if ran == 1:
            password = password + (random.choice(alpha))
            letters += -1
        if ran == 2:
            password = password + (str(random.choice(num)))
            numbers += -1
    elif letters > 0 and symbols > 0:
        ran = random.randint(1, 2)
        if ran == 1:
            password = password + (random.choice(alpha))
            letters += -1
        if ran == 2:
            password = password + (random.choice(sym))
            symbols += -1
    elif numbers > 0 and symbols > 0:
        ran = random.randint(1,2)
        if ran == 1:
            password = password + (str(random.choice(num)))
            numbers += -1
        if ran == 2:
            password = password + (random.choice(sym))
            symbols += -1
    elif letters > 0:
        password = password + (random.choice(alpha))
        letters += -1
    elif numbers > 0:
        password = password + (random.choice(num))
        numbers += -1
    elif symbols > 0:
        password = password + (random.choice(sym))
        symbols += -1
    count += 1
print(password)