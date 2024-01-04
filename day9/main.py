from replit import clear
from art import logo
print(logo)

auction_dictionary = {}    
more_bids = False

def highest_bid(record):    
  max_value = int()
  winner = ""

  for value in auction_dictionary:
    if auction_dictionary[value] > max_value:
      max_value = auction_dictionary[value]
      winner = value

  print(f"The winner of the auction is {winner} with the bid of £{max_value}")


while not more_bids:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: £"))
  auction_dictionary[name] = bid
  other_bids = input("Are there any other bids? 'Yes' or 'No'\n").lower()
  if other_bids == "yes":
    clear()
  elif other_bids == "no":
    more_bids = True
    highest_bid(auction_dictionary)
    
