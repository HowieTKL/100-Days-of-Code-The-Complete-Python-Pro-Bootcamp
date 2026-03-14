import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key, value)
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     print(index, row)
#
# # Keyword Method with iterrows()
# print({row.student:row.score for (index, row) in student_data_frame.iterrows()})


#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter:row.code for (index, row) in nato.iterrows()}
print(nato)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        phonetic = [nato[letter] for letter in word] # if letter in nato.keys()
    except KeyError:
        print("Only letters accepted")
        generate_phonetic()
    else:
        print(phonetic)

generate_phonetic()