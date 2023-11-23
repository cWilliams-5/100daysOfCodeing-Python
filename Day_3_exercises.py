# These are the interactive coding exercises for day 3

def do_Code():
    height = float(input('Enter your height (m): '))
    weight = int(input('Enter your weight (kg): '))

    bmi = weight / (height * height)
    if bmi < 18.5:
        print(f"your BMI is {bmi}, you are underweight.")
    elif bmi < 25:
        print(f"your BMI is {bmi}, you are a normal weight.")
    elif bmi < 30:
        print(f"your BMI is {bmi}, you are slightly overweight.")
    elif bmi < 35:
        print(f"your BMI is {bmi}, you are obese.")
    else:
        print(f"Your BMI is {bmi}, you are clinically obese.")

def do_Leap():
    year = int(input('What year do you want to check?\n'))
    criteria1 = year % 4
    criteria2 = year % 100
    criteria3 = year % 400
    if criteria1 == 0:
        if criteria2 != 0:
            print('Leap Year.')
        else:
            if criteria3 == 0:
                print('Leap Year')
            else:
                print("Not a Leap Year")
    else:
        print("Not a Leap Year")
def do_odd():
    oddCheck = int(input("Enter an integer: "))
    if (oddCheck % 2) == 0:
        print('The number is even.')
    else:
        print("The number is odd.")

def do_pizza():
    print('Thank you for choosing Python Pizza Deliveries!')
    size = input('What size do you want? S, M, or L\n').lower()
    add_pepperoni = input('Do you want to add pepperoni? Y or N\n').lower()
    extra_cheese = input('Do you want extra cheese? Y or N\n').lower()
    cost = 0
    if size == 'm':
        cost += 20
        if add_pepperoni == 'y':
            cost += 3
        if extra_cheese == 'y':
            cost += 1
    elif size == 'l':
        cost += 25
        if add_pepperoni == 'y':
            cost += 3
        if extra_cheese == 'y':
            cost += 1
    else:
        cost += 15
        if add_pepperoni == 'y':
            cost += 2
        if extra_cheese == 'y':
            cost += 1
    print(f"Your pizza will cost {cost}.")


def do_Love():
    print("The Love Calculator is calculating you score...")
    name1 = input('Enter your name.\n').lower()
    name2 = input('Enter their name.\n').lower()
    combined_names = name1 + name2
    t = combined_names.count('t')
    r = combined_names.count('r')
    u = combined_names.count('u')
    e = combined_names.count('e')
    trueTotal = t + r + u + e
    l = combined_names.count('l')
    o = combined_names.count('o')
    v = combined_names.count('v')
    loveTotal = l + o + v + e
    score = int(str(trueTotal) + str(loveTotal))
    if score < 10 or score > 90:
        print(f'Your score is {score}, you go together like coke and mentos')
    elif score >=40 and score <= 50:
        print(f"Your score is {score}, you are alright together")
    else:
        print(f'Your score is {score}')



def main():
    choice = input("What would you like to do? OPTIONS: "
                   "BMI, leap, odd, pizza, love\n").lower()
    if choice == 'bmi':
        do_Code()
    elif choice == 'leap':
        do_Leap()
    elif choice == 'odd':
        do_odd()
    elif choice == 'pizza':
        do_pizza()
    elif choice == 'love':
        do_Love()

main()