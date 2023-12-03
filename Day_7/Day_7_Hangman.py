#Step 1
import random
correctCount = 0
def guess(display, chosen_word, correctCount):
    guess = input('Choose a letter:  ').lower()
    print(guess)
    x = 0
    for i in chosen_word:
        if i == guess:
            print('right')
            display[x] = i
            correctCount+=1
            print(correctCount)
        else:
            print('wrong')
        x+=1
    return(correctCount)
def main():
    word_list = ["aardvark", "baboon", "camel"]
    chosen_word = random.choice(word_list)
    print(chosen_word)
    display = []
    for i in chosen_word:
        display.append('_')
    print(display)
    while len(chosen_word) != correctCount:
        guess(display, chosen_word, correctCount)
        dispStr = ''
        for ii in display:
            dispStr = dispStr + ii
        print(dispStr)
        print(correctCount)


if __name__ == "__main__":
    main()