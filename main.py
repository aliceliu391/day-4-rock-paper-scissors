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

#Write your code below this line 👇
import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

computer_choice = random.randint(0,2)

game_images = [rock, paper, scissors]
print(game_images[choice])

print(game_images[computer_choice])

if choice == computer_choice:
    print("You tie!")
elif choice == 2 and computer_choice == 0:
    print("You win")
elif choice > computer_choice:
    print("You win")
else:
    print("You lose.")
