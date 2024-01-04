#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

EASY_LIVES = 10
HARD_LIVES = 5

def generate_random():
  """ Generates random number between 1- 100"""
  return random.randint(1, 100)

def check_answer(guess, game_no, lives):
  if guess == game_no:
    print(f"You Win! The answer was {game_no}.")
  elif guess < game_no:
    print("Too low.")
    return lives - 1
  elif guess > game_no:
    print("Too high.")
    return lives - 1

def set_difficulty():
  difficulty = input("Choose your difficulty, type 'easy' or 'hard': ")
  if difficulty == 'easy':
    return EASY_LIVES 
  else:
    return HARD_LIVES

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  game_no = generate_random()
  print(game_no)
  lives = set_difficulty()
  
  guess = 0
  while guess != game_no:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    lives = check_answer(guess, game_no, lives)
    if lives == 0:
      print("You lose, you've run out of guesses.")
      return
    elif lives != 0 and guess != game_no:
      print("Guess again.")
     
game()
