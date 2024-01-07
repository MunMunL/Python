import pandas

nato_alpha = pandas.read_csv("nato_phonetic_alphabet.csv")
print(nato_alpha)
nato_dict = {row.letter: row.code for (index, row) in nato_alpha.iterrows()}
print(nato_dict)

is_on = True

def generate_phoenetic():
    guess = input("Enter a word: ").upper()
    try:
        nato_code = [nato_dict[letter] for letter in guess]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phoenetic()
    else:
        print(nato_code)

generate_phoenetic()