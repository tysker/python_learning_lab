import random


play_list = ["Rock", "Paper", "Scissors"]

player = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
)
computer = random.randint(0, len(play_list) - 1)

print(f"Computer chose: {play_list[computer]}")
print(f"You chose: {play_list[player]}")

if player == computer:
    print("Draw")
elif player == 0 and computer == 1:
    print("You Loose")
elif player == 0 and computer == 2:
    print("You Won")
elif player == 1 and computer == 0:
    print("You Won")
elif player == 1 and computer == 2:
    print("You Loose")
elif player == 2 and computer == 0:
    print("You Loose")
elif player == 2 and computer == 1:
    print("You Win")
