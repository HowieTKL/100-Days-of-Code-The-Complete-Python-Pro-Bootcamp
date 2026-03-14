rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
selection = int(input("rock, paper, or scissors (0,1,2)): "))
computer_selection = random.randint(0, 2)
images = [rock, paper, scissors]

print("you")
if selection < 0 or selection > 2:
    print("unknown")
    exit()

print(images[selection])
print()
print("computer")
print(images[computer_selection])

if selection == computer_selection:
    print("draw")
elif selection == 0 and computer_selection == 2:
    print("You win")
elif selection == 2 and computer_selection == 1:
    print("You win")
elif selection == 1 and computer_selection == 0:
    print("You win")
else:
    print("You lose")
