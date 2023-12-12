from art import logo, vs
from game_data import data
import random


def getChoice(choice2):
  if bool(choice2):
    rand1 = random.randint(0, len(data) - 1)
    while data[rand1]["name"] == choice2["name"]:
      rand1 = random.randint(0, len(data) - 1)
    choice1 = choice2
    choice2 = data[rand1]
  else:
    rand1 = random.randint(0, len(data) - 1)
    rand2 = random.randint(0, len(data) - 1)
    if rand1 == rand2:
      if rand2 < 24:
        rand2 += 5
      else:
        rand2 += -5
    choice1 = data[rand1]
    choice2 = data[rand2]
  return choice1, choice2

def getAnswer(choice1, choice2):
  if choice1['follower_count'] > choice2['follower_count']:
    answer = 'a'
    return answer
  else:
    answer = 'b'
    return answer

def comparison(answer, score):
  userAnswer = input(f"Who has more followers? ")
  if userAnswer.lower() == answer:
    score += 1
    print("You are right!")
    print(f"Current Score: {score}")
    c =  True
    return c
  else:
    print(f"You are wrong! Final Score: {score}")
    c = False
    return c

def main():
  # print logo and welcome message
  print(logo)
  commence = True
  score = 0
  choice1 = {}
  choice2 = {}
  # run a while statement
  while commence:
    # get  and display the comparisons
    choice1, choice2 = getChoice(choice2)
    print(f"Compare A: {choice1['name']}, a(n) {choice1['description']}, from {choice1['country']}")
    print(vs)
    print(f"With B: {choice2['name']}, a(n) {choice2['description']}, from {choice2['country']}")
    answer = getAnswer(choice1, choice2)
    # get user answer
    # check if answer is correct
    # if correct restart loop, if wrong exit loop
    commence= comparison(answer, score)
    if commence:
      score += 1
  quit()


if __name__ == "__main__":
  main()