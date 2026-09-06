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
game_images = [rock, paper, scissors]
user_choice = int(input("Welcome to the Rock Paper Scissors game! Press 0, 1, 2 for Rock, Paper, Scissors. \n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
else:
    print("You typed wrong number ! YOU LOSE")
    exit()
computer_choice = random.randint(0,2)
print(game_images[computer_choice])

print(f"computer choose {computer_choice}")

if user_choice >= 3 or user_choice < 0 :
    print("You typed wrong number ! YOU LOSE")
elif user_choice == 0 and computer_choice == 1:
    print("You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
 print("You win!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif user_choice == computer_choice :
    print("its a tie")

# a differnet verion below ____


# import random
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# game_images = [rock, paper, scissors]
#
# user_choice = int(input("Welcome to the Rock Paper Scissors game! Press 0, 1, 2 for Rock, Paper, Scissors.\n"))
#
# # 1. First check if the input is valid
# if user_choice < 0 or user_choice > 2:
#     print("You typed an invalid number! YOU LOSE")
# else:
#     # 2. Display the choices visually
#     print(f"You chose:\n{game_images[user_choice]}")
#
#     computer_choice = random.randint(0, 2)
#     print(f"Computer chose:\n{game_images[computer_choice]}")
#
#     # 3. Determine the winner
#     if user_choice == computer_choice:
#         print("It's a tie!")
#     elif (user_choice == 0 and computer_choice == 2) or \
#             (user_choice == 1 and computer_choice == 0) or \
#             (user_choice == 2 and computer_choice == 1):
#         print("You win!")
#     else:
#         print("You lose!")