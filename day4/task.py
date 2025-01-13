import random

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

a = [rock, paper, scissors]

choices = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if choices not in [0, 1, 2]:
    print("Invalid choice! Please select 0, 1, or 2.")
    exit()

print(f"You chose:\n{a[choices]}")

computer_choice = random.randint(0, 2)
print(f"Computer chose:\n{a[computer_choice]}")

if choices == computer_choice:
    print("It's a draw!")
elif ((choices == 0 and computer_choice == 2) or (choices == 1 and computer_choice == 0)
      or (choices == 2 and computer_choice == 1)):
    print("You win!")
else:
    print("You lose. Better luck next time!")
