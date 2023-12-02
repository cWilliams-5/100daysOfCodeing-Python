from replit import clear
# HINT: You can call clear() to clear the output in the console.

from art import logo


def get_info():
    name = input("What is the name?\n")
    bid = int(input("What is the bid?\n"))
    return (name, bid)


def whoWins(allBids):
    maxBid = 0
    for key in allBids:
        if allBids[key] > maxBid:
            maxBid = allBids[key]
            winner = key
    print(f"{winner} is the winner with a bid of ${maxBid}")
    quit()


def main():
    print(logo)
    print("Welcome to the Aution House")
    allBids = {}
    again = True
    while again:
        name, bid = get_info()
        allBids[name] = bid
        cont = input("Is there another bidder?\n")
        if cont.lower() == 'no':
            again = False
        else:
            clear()
    whoWins(allBids)


if __name__ == "__main__":
    main()