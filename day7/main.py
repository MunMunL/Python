from replit import clear
import random

from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo, stages
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")

level = input("What level do you want. Type 'Easy', 'Medium' or 'Hard'\n").lower()
if level == "easy":
  print(f"The word begins with the letter '{chosen_word[0]}' and ends with the letter '{chosen_word[-1]}'")
elif level == "medium":
  print(f"Your clue is the letter '{chosen_word[random.randint(0 , len(chosen_word) - 1)]}'")
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()
    print(logo)

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"You've already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(chosen_word)

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
    
