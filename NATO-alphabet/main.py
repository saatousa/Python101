
import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")



phonetic_dict = {row["letter"]: row["code"] for (index, row) in nato_alphabet.iterrows()}



def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
