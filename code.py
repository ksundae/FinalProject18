import time
import random

def show_rules():
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
  print("Got it? Alright, let's begin! Good luck!")
  input(">")

def get_player_cards(cards_to_pick):
  suits = ("heart", "spade", "club", "diamond")
  face_value = ("ace", "one", "two", "three", "four", "five", "six", "seven", "eight","nine", "ten", "jack", "queen", "king")
  print("These are your cards:")
  time.sleep(1)
  while cards_to_pick > 0:
    suit_choice = random.choice(suits)
    card_choice = random.choice(face_value)
    #if card in dictionary does not exist??
    print(f"{card_choice} of {suit_choice}")
    value = deck_of_cards[suit_choice][card_choice]
    if card_choice == "ace":
      ace_choice = int(input("Do you want your ace to be worth 1 point or 11 points? "))
      while ace_choice != 1 and ace_choice != 11:
        ace_choice = int(input("Please input either 1 or 11. "))
      value = ace_choice
    del deck_of_cards[suit_choice][card_choice]
    cards_to_pick -= 1
    current_hand.append(value)
  return current_hand

def check_value():
  total_value = 0
  for value in current_hand:
    total_value += value
  print(f"The total value of your hand is {total_value}.")
  input(">")
  if total_value == 21:
    print("Congrats, you got blackjack!")
  elif total_value > 21:
    print("You lost because the total value of your hand is bigger than 21!")
  else:
    print("What would you like to do now?")

def player_move_choice():
  input(">")
  if current_hand[0] == current_hand[1]:
    player_split_choice = input("Split, hit, or stand? ").lower()
    while player_split_choice != "split" and player_split_choice != "hit" and player_split_choice != "stand":
      player_split_choice = input("Please choose split, hit, or stand. ")
    if player_split_choice == "split":
      player_split()
    elif player_split_choice == "hit":
      player_hit()
    elif player_split_choice == "stand":
      player_stand()
    else:
      print("You fell into the void.")
  else:
    player_move = input("Would you like to hit or stand? ").lower()
    while player_move != "hit" and player_move != "stand":
      player_move = input("Please choose either hit or stand. ").lower()
    if player_move == "hit":
      player_hit()
    elif player_move == "stand":
      player_stand()
    else:
      print("How did you get here?")

def player_hit():
  print("hit")

def player_stand():
  print("stand")

def player_split():
  print("split")

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
print("Welcome to Blackjack!")
time.sleep(1)
print("Press enter whenever you see a '>' in order to continue reading.")
print("Do you want me to explain the rules?")
rules_decision = input("Enter Y for yes and N for no. ").title()
while rules_decision != "Y" and rules_decision != "N":
    print("Please input either Y or N.")
    rules_decision = input("Enter Y for yes and N for no. ").title()
if rules_decision == "Y":
 show_rules()
else:
  print("Alright, then let's start playing!")
cards_to_pick = 2
current_hand = []
current_hand = get_player_cards(cards_to_pick)
input(">")
check_value()
player_move_choice()