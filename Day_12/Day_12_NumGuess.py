from art import logo
import random

def number_pick():
    #this will get the number from the user
    pick = int(input("Please select a number between 1 and 100:\n"))
    return pick
def num_check(num, count, pick):
    #this will check the number and reduce the chances difference will be 1 if num is higher than pick,
    # 2 if less than
    #difference = ""
    if num == pick:
        inCorrect = False
    elif num > pick:
        inCorrect = True
        count += -1
        if count > 0:
            print("Too Low\nGuess Again")
        else:
            print("Too Low")
    else:
        inCorrect = True
        count += -1
        if count > 0:
            print("Too High\nGuess Again")
        else:
            print("Too High")
    return count, inCorrect


def main():
    print("WELCOME\nTO......")
    print(logo)
    num = random.randint(1, 100)
    inCorrect = True
    difficulty = int(input('Please select a difficulty:\nEasy (1)\nHard (2)\n'))
    count = 0
    if difficulty == 1:
        count = 10
    elif difficulty == 2:
        count = 5
    else:
        print('Incorrect entry')
    while inCorrect:
        if count <= 0:
            print(f"Out of chances. The correct number was {num}. You Lose")
            quit()
        else:
            print(f"You have {count} attempts remaining.")
            selection = number_pick()
            count, inCorrect = num_check(num, count, selection)
    print(f"Congradulations the number was {num}, You Win!!!")


if __name__ == "__main__":
    main()