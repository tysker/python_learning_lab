import random
from logo import stages
from words import word_list

random_word = random.choice(word_list)
print(random_word)

placeholder = ""
for pos in range(len(random_word)):
    placeholder += "_"
print(placeholder)


game_over = False
correct_letters = []
lives = 7
while not game_over:
    print(f"Lives: {lives}/7")
    guessed_letter = input("Guess a letter: ").upper()

    display = ""
    for letter in random_word:
        if letter == guessed_letter:
            display += letter
            correct_letters.append(guessed_letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guessed_letter not in random_word:
        lives -= 1

    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("You win")
    elif lives == 0:
        game_over = True
        print("You lost")
