# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

# print(nato_alphabet.keys())

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Using try and except to catch errors
running = True

while running:
    user_input = input("Enter Word: ").upper()
    try:
        code = [nato_alphabet[letter] for letter in user_input]
    except KeyError:
        print("Sorry only letters in hte alphabet please")
    else:
        print(code)




