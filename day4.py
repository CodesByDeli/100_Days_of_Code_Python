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



##########################################################
import random

list = ([rock, paper, scissors])
choice = int(input("What you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

player1 = (list[choice]) # actual player
player2 = random.choice([rock, paper, scissors]) # bot player

print(player1) # player
print(player2)


# combination with rock
if player1 == rock and player2 == scissors:
    print("You win!")
elif player1 == rock and player2 == paper:
    print("You lose!")
elif player1 == rock and player2 == rock:
    print("It's a daw.")
# combination with paper
elif player1 == paper and player2 == rock:
    print("You win!")
elif player1 == paper and player2 == paper:
    print("It's a daw.")
elif player1 == paper and player2 == scissors:
    print("You lose!")
# combinations scissoers
elif player1 == scissors and player2 == paper:
    print("You win!")
elif player1 == scissors and player2 == scissors:
    print("It's a daw.")
elif player1 == scissors and player2 == rock:
    print("You lose!")