#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"
with open("Input/Letters/starting_letter.txt", "r") as letter:
    data = letter.read()
    with open("Input/Names/invited_names.txt", "r") as invited_names:
        names = invited_names.readlines()
        formatted_names = []
        for name in names:
            name = name.strip()
            formatted_names.append(name)
            named_letter = data.replace(PLACEHOLDER, name)
            with open(f"Output/ReadyToSend/letter to {name}.txt", "w") as letter_to_send:
                letter_to_send.write(named_letter)

