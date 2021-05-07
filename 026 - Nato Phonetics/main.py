import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in file.iterrows()}

user_input = (input("Enter a word to have it converted to nato phonetic alphabet: ")).upper()

nato_converted = [nato_dict[letter] for letter in user_input]
print(nato_converted)
