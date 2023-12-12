from data import MENU, resources

def getAction():
    action = input(f"What would you like? (espresso (a)/latte (b)/cappuccino (c)): ")
    if action == 'a':
        action = 'espresso'
    elif action == 'b':
        action = 'latte'
    elif action == 'c':
        action = 'cappuccino'
    return action

def getPaid(cost):
    print(f"Please insert {cost}.")
    total = float(0)
    while total < cost:
        quarters = int(input("How Many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))
        total = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + pennies
        if total < cost:
            difference = float(cost - total)
            print(f"Insufficient funds, please insert {difference} more.")
        elif total > cost:
            difference = float(total - cost)
            print(f"Thank you. Your change is ${difference}.")
    resources['money'] += cost

def runCoffee(action):
    ingredients = MENU[action]['ingredients']
    cost = float(MENU[action]['cost'])
    bad = True
    for key in ingredients:
        if resources[key] >= ingredients[key]:
            bad = False
        else:
            print(f"Sorry there is not enough {key}.")
            return
    if not bad:
        getPaid(cost)
        for key in ingredients:
            resources[key] += (-1 * int(ingredients[key]))
        print(f"Here is your {action} ☕. Enjoy")

def main():
    print("hello")
    #get action
    action = "go"
    while action.lower() != "off":
        action = getAction()
        #if statements for each action option
        if action == '1':
            #report
            for key in resources:
                print(f"{key} : {resources[key]}")
        elif action.lower() in ('espresso', 'latte', 'cappuccino'):
            #espresso - reduce the resources
            runCoffee(action)
            #latte - reduce the resources
            #cappuccino - reduce the resources
        elif action.lower() == 'off':
            return
        else:
            print("Incorrect entry please try again")
    quit()


if __name__ == "__main__":
    main()