# Tip Calculator
# 100 Days Of Python Day 4

import random
rock = '''
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            '''
paper = '''
                _______
            ---'   ____)____
                      ______)
                      _______)
                     _______)
            ---.__________)
            '''
scissors = '''
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            '''

print('Welcome to Rock Paper Scissors')
throw = input('What would you like to throw?\n'
              '0 = Rock, 1 = Paper, 2 = Scissors\n')
if throw == '0':
    print("This is what you chose:")
    print(rock)
elif throw == '1':
    print("This is what you chose:")
    print(paper)
elif throw == '2':
    print("This is what you chose:")
    print(scissors)
else:
    print('incorrect entry')
cOptions = [0, 1, 2]
cThrow = random.randint(0, (len(cOptions)-1))
print(cThrow)
if cThrow == 0:
    print("This is what the Computer chose:")
    print(rock)
elif cThrow == 1:
    print("This is what the Computer chose:")
    print(paper)
elif cThrow == 2:
    print("This is what the Computer chose:")
    print(scissors)
if throw == cThrow:
    print('Tie')
elif throw == '0' and cThrow == 1:
    print("Computer Wins")
elif throw == '0' and cThrow == 2:
    print("You Win")
elif throw == '1' and cThrow == 2:
    print("Computer Wins")
elif throw == '1' and cThrow == 0:
    print("You Win")
elif throw == '2' and cThrow == 0:
    print("Computer Wins")
elif throw == '2' and cThrow == 1:
    print("You Win")