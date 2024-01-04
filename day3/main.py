print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


print("You're in a forest.\nUp ahead is fork in the road.\nThere is a dense forest on the right and a windy path along the river with choppy rapids on the left.\nDo you want to go left or right?")
direction1 = input("Type 'left' or 'right'\n").lower()
print('''

''')
if direction1 == "left":
  print("You chose left along the river.\nThe path is windy and it eventually stops and leads you to the river.\nDo you jump in and swim across to the other side or try to build a boat?")
  direction2 = input("Type 'swim' or 'boat'\n").lower()
  print('''

''')
  if direction2 == 'boat':
    print("You chose to build a boat.\nYou'll need to find the materials to build the boat.\nIt's 3pm and the sun is slowly starting to set.")
    print("Do you:\n1. Call it a day and start building the boat tomorrow. Find some wood for fire to keep warm overnight.\n2. Try to find what you can to make a temporary boat just to get you over.\n3. Wait till the sun sets to use your flare to get help.\n4. Attempt to find anything we can to help us decide to build the boat or a fire to stay overnight.")
    direction3 = input("Type '1', '2', '3' or '4'\n")
    print('''

''')
    if direction3 == '1':
      print("You chose to find wood for fire, the wood is too damp to light a fire and you froze!  GAME OVER!")
    elif direction3 == '2':
      print("You chose to make a temporary boat.\nYou found a piece from a broken plane and you managed to get it to sail and eventually sailed to the island.\nYou found the treasure!! YOU WIN!")
    elif direction3 == '3':
      print("You chose to use your flare after sun set.\nThe leaves in the forest are very dry and caught the sparks from the flare and the forest caught fire! GAME OVER!")
    elif direction3 == '4':
      print("You chose to just start searching for any materials.\nYou stumbled into a wild boar and was eaten by the beast! GAME OVER")
      
  else:
    print("You chose to swim across the river.\nYou swam halfway through the river when you felt something brush against your leg.\nIt was a crocodile!\nYou were bitten by the crocodile. AHHHH!! GAME OVER!")

else:
  print("You chose right through the dense forest.\n  It was filled with poisonous snakes and you were bitten.  GAME OVER!")
