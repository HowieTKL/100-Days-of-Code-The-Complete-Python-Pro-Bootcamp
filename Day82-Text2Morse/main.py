import morse_code

phrase = input("Input phrase: ")
print(phrase)
phrase = phrase.upper()
for letter in phrase:
    if letter in morse_code.morse_code.keys():
        print(morse_code.morse_code[letter], end=" ")