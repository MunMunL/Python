rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

game_images = [rock, paper, scissors]

my_choice = int(input("What do you choose? \nType 0 for Rock\nType 1 for Paper\nType 2 for Scissors\n"))
bot_choice = random.randint(0 , 2)

if my_choice >= 3:
  print("You chose an invalid number you lose")
else:
  print(game_images[my_choice])

  print("Computer choose:")
  print(game_images[bot_choice])
  
  if my_choice == 0 and bot_choice == 2:
    print("You win")
  elif bot_choice == 0 and my_choice == 2:
    print("You lose")
  elif my_choice > bot_choice:
    print("You win")
  elif bot_choice > my_choice:
    print("You lose")
  elif my_choice == bot_choice:
    print("It's a tie")
