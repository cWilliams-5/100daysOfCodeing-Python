#Blackjack app

from art import logo
import random


def draw_card():
    # draws a single card
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    # calculates the user score and changes aces to 1 if necessary
    score = sum(cards)
    if 11 in cards:
        if score > 21:
            cards.remove(11)
            cards.append(1)
    return cards, score


def draw_dealer():
    # runs the entire dealer round and returns their cards and score
    draw = True
    dealer = []
    dealer.append(draw_card())
    dealer.append(draw_card())
    while draw:
        if 11 in dealer:
            if sum(dealer) > 21:
                dealer.remove(11)
                dealer.append(1)
        if sum(dealer) == 21:
            draw = False
            return dealer, 21
        elif sum(dealer) < 16:
            dealer.append(draw_card())
        else:
            draw = False
            return dealer, sum(dealer)


def main():
    repeat = True
    while repeat:
        print(logo)
        # start new game, draw cards
        user_cards = []
        dealer_cards = []
        dealer_cards, dealer_score = draw_dealer()
        user_cards.append(draw_card())
        user_cards.append(draw_card())
        user_cards, user_score = calculate_score(user_cards)
        dealer_cards, dealer_score = calculate_score(dealer_cards)
        dealer_show = []
        dealer_show.append(dealer_cards[1])
        print(f"Your cards are {user_cards}, current score {user_score}")
        print(f"Dealer's card showing is {dealer_show}")
        # easy win or lose tests
        draw = 'n'
        if len(dealer_cards) == 2 and dealer_score == 21:
            print(f"Dealer shows {dealer_cards}, they have 21. You lose :(")
        elif user_score == 21:
            print("You win!!!")
        elif user_score > 21:
            print("BUST! You lose :(")
            restart = input("Do you want to play again? (y/n)")
        else:
            draw = input("Do you want to draw another card? (y/n)\n")

        num_cards = 3
        while draw == 'y':
            # draw more cards and reveal more dealer cards
            user_cards.append(draw_card())
            user_cards, user_score = calculate_score(user_cards)
            if num_cards < len(dealer_cards):
                dealer_show.append(dealer_cards[num_cards - 1])
            print(f"Your cards are {user_cards}, current score {user_score}")
            print(f"Dealer's card showing is {dealer_show}")
            if num_cards == len(dealer_cards) and dealer_score == 21:
                print(f"Dealer shows {dealer_cards}, they have 21. You lose :(")
                draw = 'n'
            elif user_score == 21:
                print("You win!!!")
                draw = 'n'
            elif user_score > 21:
                print("BUST! You lose :(")
                draw = 'n'
            else:
                draw = input("Do you want to draw another card? (y/n)\n")
            num_cards += 1

        # once they dont draw another card
        print(f"FINAL SCORE:\n Your Cards: {user_cards} - Your Score: {user_score}\n Dealer Cards: {dealer_cards} - Dealer Score: {dealer_score}")
        if dealer_score > 21:
            print("Dedaler BUSTS! You win!!!")
        elif dealer_score > user_score:
            print(f"You lose :(")
        elif dealer_score < user_score and user_score < 21:
            print(f"You Win!!!")
        elif dealer_score == user_score and user_score < 21:
            print(f"Its a Draw.")
        restart = input("Do you want to play again? (y/n)")
        if restart == "n":
            repeat = False
            break
    print("Goodbye")
    quit()


if __name__ == "__main__":
    main()
