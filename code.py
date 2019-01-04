import time
import random

def show_rules():
  print("Guide to this rulebook: press enter whenever you see a '>' in order to continue reading.")
  input(">")
  print("You will be the player, and you will play against the computer, who will be the dealer.")
  input(">")
  print("Your goal is to collect a hand that is greater than the dealer's hand, but less than a maximum value of 21 points. If you exceed 21 points or are unable to to beat the dealer's hand,then you lose.")
  input(">")
  print("You will be dealt two cards face-up, and the dealer will also have two cards, but one will be face-up and the other will be face-down.")
  input(">")
  print("If the first two cards of a hand are worth 21 points, then the hand is called blackjack. The one with blackjack wins. If both player and dealer have blackjack, then it is a draw.")
  input(">")
  print("If the dealer's face-up card is worth 10 points, they can check if their face-down card is blackjack.")
  input(">")
  print("If neither the dealer nor the player gets blackjack, the player has several options.")
  input(">")
  print("Hit - you take another card. This can be repeated until your hand exceeds 21 points or you choose to stand.")
  input(">")
  print("Stand - you take no more cards and keep your hand.")
  input(">")
  print("Split - if your hand has two cards of the same value, you can split your hand in two and take two more cards. Your two new hands are played separately.")
  input(">")
  print("After you decide to stand, the dealer reveals their face-down card. They can then take additional cards. If they exceed 21 points, then you win.")
  input(">")
  print("The cards from 2 to 10 are worth the number of the card's face value. Face cards (jacks, queens, and kings) are worth 10 points. Aces can be worth 1 or 11 points depending on which prevents the hand from exceeding 21.")

def get_player_cards():
  deck_of_cards = {
    'heart': {
      'ace': 1,
      'one': 1,
      'two': 2,
      'three': 3,
      'four': 4,
      'five': 5,
      'six': 6,
      'seven': 7,
      'eight': 8,
      'nine': 10,
      'ten': 10,
      'jack': 10,
      'queen': 10,
      'king': 10
    },
    'spade': {
      'ace': 1,
      'one': 1,
      'two': 2,
      'three': 3,
      'four': 4,
      'five': 5,
      'six': 6,
      'seven': 7,
      'eight': 8,
      'nine': 10,
      'ten': 10,
      'jack': 10,
      'queen': 10,
      'king': 10
    },
    'club': {
      'ace': 1,
      'one': 1,
      'two': 2,
      'three': 3,
      'four': 4,
      'five': 5,
      'six': 6,
      'seven': 7,
      'eight': 8,
      'nine': 10,
      'ten': 10,
      'jack': 10,
      'queen': 10,
      'king': 10
    },
    'diamond': {
      'ace': 1,
      'one': 1,
      'two': 2,
      'three': 3,
      'four': 4,
      'five': 5,
      'six': 6,
      'seven': 7,
      'eight': 8,
      'nine': 10,
      'ten': 10,
      'jack': 10,
      'queen': 10,
      'king': 10
    }
  }
  suits = ("heart", "spade", "club", "diamond")
  suit_choice1 = random.choice(suits)
  face_value = ("ace", "one", "two", "three", "four", "five", "six", "seven", "eight","nine", "ten", "jack", "queen", "king")
  card_choice1 = random.choice(face_value)
  value1 = deck_of_cards[suit_choice1][card_choice1]
  print(f"{card_choice1} of {suit_choice1}")
  suit_choice2 = random.choice(suits)
  card_choice2 = random.choice(face_value)
  while suit_choice1 == suit_choice2 and card_choice1 == card_choice2:
    suit_choice2 = random.choice(suits)
    card_choice2 = random.choice(face_value)
  value2 = deck_of_cards[suit_choice2][card_choice2]
  print(f"{card_choice2} of {suit_choice2}")
  if card_choice1 == "ace":
    input1 = int(input("Do you want your ace to be worth 1 point or 11 points? "))
    while input1 != 1 and input1 != 11:
      input1 = int(input("Please input either 1 or 11. "))
    value1 = input1
  if card_choice2 == "ace":
    input2 = int(input("Do you want your ace to be worth 1 point or 11 points? "))
    while input2 != 1 and input2 != 11:
      input2 = int(input("Please input either 1 or 11. "))
    value2 = input2
  return [value1, value2]

def check_value(total_value):
  if total_value == 21
    print("Congrats, you got blackjack!")
  elif total_value > 21:
    print("You lost because the total value of your hand is bigger than 21!")
  else:
    print("What would you like to do now?")
 
print("Welcome to Blackjack!")
time.sleep(1)
print("Do you want me to explain the rules?")
time.sleep(1)
rules_decision = input("Enter Y for yes and N for no. ").title()
while rules_decision != "Y" and rules_decision != "N":
    print("Please input either Y or N.")
    rules_decision = input("Enter Y for yes and N for no. ").title()
if rules_decision == "Y":
 show_rules()
else:
  print("Alright, then let's start playing!")

current_hand = get_player_cards()
total_value = 0
for value in current_hand:
  total_value += value
print(f"The total value of your hand is {total_value}.")
check_value(total_value)