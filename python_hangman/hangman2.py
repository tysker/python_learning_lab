import random

words = ["HOME", "GARAGE", "COMPANY", "DOG", "ANIMAL"]
lives = 7
gameOver = False
planks = []


def appendPlanks():
    for w in word:
        planks.append("_")


def printInfo():
    print(f"Lives {lives}/7")
    print(" ".join(planks))


def searchForLetterInWord(letter):
    contains = 0
    for index, w in enumerate(word):
        if w == letter.upper():
            planks[index] = w
            contains += 1
    if contains > 0:
        return True
    else:
        return False


def checkIfWon():
    contains = 0
    for p in planks:
        if p == "_":
            contains += 1
    if contains == 0:
        return True
    else:
        return False


# 1. Generate a random word
word = random.choice(words)

# 2. Generate planks as letters in word
appendPlanks()

while not gameOver:
    printInfo()

    # 3. Ask user to guess a letter
    guessedLetter = input("Please guess a letter!\n")

    # 4. Is the guessed lettere in the word?
    isLetterFound = searchForLetterInWord(guessedLetter)

    if isLetterFound:
        print("You found a letter!\n")
    else:
        print("Wrong letter!. You missed one live!")
        lives -= 1

    isGameWon = checkIfWon()

    if lives == 0:
        print("You lost all lives! Game Over!")
        gameOver = True
    elif isGameWon:
        print("You found all letters. You won!")
        gameOver = True
    else:
        gameOver = False
