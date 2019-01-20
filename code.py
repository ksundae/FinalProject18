import time
import random

class Player:
  """class keeping track of traits of the player"""

  def __init__(self, name):
    self.hand = []
    self.values = []
    self.name = name
    self.total_value = 0
  
  def get_cards(self, cards_to_pick):
    """randomly draws one card from the deck, adds it to the player's hand"""
    time.sleep(1)
    while cards_to_pick > 0:
      suit_choice = random.choice(list(deck_of_cards.keys()))
      card_choice = random.choice(list(deck_of_cards[suit_choice].keys()))
      self.hand.append(card_choice)
      value = deck_of_cards[suit_choice][card_choice]
      if card_choice == "ace":
        if self.name == "player":
          print(self.hand)
          ace_choice = int(input("Do you want your ace to be worth 1 point or 11 points? "))
          while ace_choice != 1 and ace_choice != 11:
            ace_choice = int(input("Please input either 1 or 11. "))
          value = ace_choice
        elif self.name == "dealer":
          value = 11
      del deck_of_cards[suit_choice][card_choice]
      cards_to_pick -= 1
      self.values.append(value)
    return card_choice

  def check_value(self):
    """finds the total value of the hand and checks the winner and loser"""
    self.total_value = 0
    for value in self.values:
      self.total_value += value
    if self.name == "player":
      print(f"The total value of your hand is {player.total_value}.")
    elif self.name == "dealer":
      print(f"The dealer's hand is worth a total of {dealer.total_value} points.")
    input(">")

class Dealer(Player):
  """class keeping track of traits of the dealer"""
  def __init__(self, name):
    self.hand = []
    self.values = []
    self.name = name
    self.total_value = 0

def introduction():
  """show intro, ask player if they want to see rules or not"""
  print("Welcome to Blackjack!")
  time.sleep(1)
  print("Press enter whenever you see a '>' in order to continue reading.")
  time.sleep(1)
  print("Do you want me to explain the rules?")
  rules_decision = input("Enter Y for yes and N for no. ").title()
  while rules_decision != "Y" and rules_decision != "N":
    print("Please input either Y or N.")
    rules_decision = input("Enter Y for yes and N for no. ").title()
  if rules_decision == "Y":
    show_rules()
  else:
    print("Alright, then let's start playing!")
    input(">")

def show_rules():
  """print the rules for the player"""
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

def first_round():
  """in the first round, draw two cards for the player and one card for the dealer"""
  print("These are your cards:")
  card_choice = player.get_cards(2)
  if card_choice != "ace":
    print(player.hand)
  time.sleep(1)
  player.check_value()
  if player.total_value < 21:
    print("This is the dealer's first card.")
    dealer.get_cards(1)
    print(dealer.hand)
    time.sleep(1)
    dealer.check_value()
  elif player.total_value == 21:
    print("Congrats, you got blackjack!")
    print("This is the dealer's first card.")
    card_choice = dealer.get_cards(1)
    print(dealer.hand)
    time.sleep(1)
    if card_choice == "jack" or card_choice == "queen" or card_choice == "king":
      print("The dealer has a face card! Let's check if they have blackjack.")
      dealer.get_cards(1)
      print(dealer.hand)
      dealer.check_value()
      if dealer.total_value == 21:
        print("You and the dealer both got blackjack! You tied!")
      else:
        print("The dealer does not have blackjack! You won!")

def player_move_choice():
  """lets the player choose a move between hit, stand, and split"""
  global player_move
  player_move = ""
  time.sleep(1)
  if player.hand[0] == player.hand[1] and player.value[0] == player.value[1]:
    player_move = input("Split, hit, or stand? ").lower()
    while player_move != "split" and player_move != "hit" and player_move != "stand":
      player_move = input("Please choose split, hit, or stand. ")
    if player_move == "split":
      player_split()
    elif player_move == "hit":
      player_hit()
    elif player_move == "stand":
      player_stand()
    else:
      print("You fell into the void!")
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
  return player_move

def player_hit():
  """allows the player to hit and add one card to their hand"""
  player.get_cards(1)
  time.sleep(1)
  print(player.hand)
  time.sleep(1)
  player.check_value()

def player_stand():
  """allows the player to stand and stop drawing cards, switches to dealer's turn"""
  print("Let's check the dealer's other card.")
  dealer.get_cards(1)
  time.sleep(1)
  print(dealer.hand)
  time.sleep(1)
  dealer.check_value()
  if dealer.total_value < 15:
    print("The dealer decided to take more cards.")
    while dealer.total_value < 15:
      dealer.get_cards(1)
      print(dealer.hand)
      time.sleep(1)
      dealer.check_value()
  determine_win_lose()
  time.sleep(1)

def player_split():
  """global hand1
  global hand2
  print("These are your cards:")
  hand1.append(player_hand[0])
  hand2.append(player_hand[1])
  get_player_cards(1)
  hand1.append(this_card)
  print(hand1)
  get_player_cards(1)
  hand2.append(this_card)
  print(hand2)"""

def determine_win_lose():
  """compares the totals of the player's hand and the dealer's hand"""
  if player.total_value > 21:
    print("You lost because the total value of your hand is bigger than 21! You lost!")
  elif dealer.total_value > 21:
    print("The dealer lost because the total value of their hand is bigger than 21! You win!")
  elif dealer.total_value > player.total_value:
    print("The dealer's hand beat yours! You lost!")
  elif dealer.total_value < player.total_value:
    print("You beat the dealer's hand! You won!")
  elif dealer.total_value == player.total_value:
    print("You tied with the dealer!")

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
    'nine': 9,
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
    'nine': 9,
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
    'nine': 9,
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
    'nine': 9,
    'ten': 10,
    'jack': 10,
    'queen': 10,
    'king': 10
  }
}
player_move = ""
introduction()
player = Player("player")
dealer = Dealer("dealer")
first_round()
while player_move != "stand" and player.total_value < 21 and dealer.total_value < 21:
  player_move = player_move_choice()
if player.total_value > 21:
    print("You lost because the total value of your hand is bigger than 21!")