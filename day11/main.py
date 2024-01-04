############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from replit import clear
import random
from art import logo


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if len(cards) == 2 and sum(cards) == 21:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score, computer_score):
  if user_score == 0:
    return "You got BlackJack, you win!"
  elif computer_score == 0:
    return "Computer got BlackJack, you lose."
  elif user_score >21:
    return "You've gone bust, Computer wins."
  elif computer_score >21:
    return "Computer busted, you win!"
  elif user_score < computer_score:
    return "You lose"
  elif user_score == computer_score:
    return "It's a draw."
  else:
    return "You win!"


def play_game():
  
  print(logo)
  
  game_on = True
  user_cards = []
  computer_cards = []

  for _ in range (2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while game_on:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
  
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_on = False
    else:
      play_on = input("Do you want to draw another card 'y' or 'n'? ").lower()
      if play_on == "y":
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
      else :
        game_on = False
          
      
  while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)
      
  print(f"Your final cards: {user_cards}, final score: {user_score}")
  print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play BlackJack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
  



