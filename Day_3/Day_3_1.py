# Treasure Hunt
# 100 Days Of Python Day 3

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
firstStep = input('You are at a cross road where'
                  ' do want to go? Type "left" or "right"\n').lower()
if firstStep == 'left':
    secondStep = input('You\'ve come to a lake. There is an island '
                       'in the middle of the lake.\nType "wait" to wait'
                       ' for a boat. Type "swim" to swim across\n').lower()
    if secondStep == 'wait':
        thirdStep = input('You arrive at the island unharmed. There is a house'
                          ' with 3 doors.\nOne red, one yellow, and one blue.\n'
                          'Which color do you choose?\n').lower()
        if thirdStep == 'red':
            print('It\'s a room full of fire. Game Over, try again.')
        elif thirdStep == 'yellow':
            print('You found the treasure! You Win!')
        else:
            print('You enter a room of beasts. Game Over.')
    else:
        print('You get attacked by a giant, angry trout. Game Over, try again.')
else:
    print("You have fallen in a whole and died. Game Over, try again.")


