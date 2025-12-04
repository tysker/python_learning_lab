import random 

words = ["HOME", "GARAGE", "COMPANY", "DOG", "ANIMAL"] 
word = random.choice(words) 
planks = [] 
game_over = False 
wrong_guesses = 0

hangman_stages = [
    """
    -|----------------
     |
     |
     |
     |
     |
     |
    / \\
    ----------
    """,
    """
    -|----------------
     |            |
     |
     |
     |
     |
     |
    / \\
    ----------
    """,
    """
    -|----------------
     |            |
     |            O
     |
     |
     |
     |
    / \\
    ----------
    """,
    """
    -|----------------
     |            |
     |            O
     |            |
     |
     |
     |
    / \\
    ----------
    """,
    """
    -|----------------
     |            |
     |            O
     |           /|
     |
     |
     |
    / \\
    ----------
    """,
    """
    -|----------------
     |            |
     |            O
     |           /|\\
     |
     |
     |
    / \\
    ----------
    """,
    """
    -|----------------
     |            |
     |            O
     |           /|\\
     |           /
     |
     |
    / \\
    ----------
    """,
    """
    -|----------------
     |            |
     |            O
     |           /|\\
     |           / \\
     |
     |
    / \\
    ----------
    """
]


for w in word: 
    planks.append("_") 

def findLetter(letter): 
    contains = 0 
    for index, c in enumerate(word): 
        if c == letter.upper(): 
            planks[index] = c 
            contains += 1 
        if contains > 0: 
            return True 
        else: return False 

def checkIfWon(): 
    contains = 0 
    for w in planks: 
        if w == "_": 
            contains += 1 
        if contains == 0: 
            return True 
        else: return False 

while not game_over: 
    # 1. Create a random word 

    # 2. Write planks to console print(planks) 

    # 3. User guess 
    user_guess = input("Please guess a letter!\n") 

    # 4. Check if guess is true or false 
    found_letter = findLetter(user_guess) 

    # 5. Check if game is won or lost 
    isWon = checkIfWon() 

    if isWon: 
        print("You won!") 
        game_over = True 

    if found_letter: print("Right Guess!") 
    else: print("Wrong Guess!") 
          wrong_guesses += 1 
    
    print(hangman_stages[wrong_guesses]) 

    if wrong_guesses == len(hangman_stages) - 1: 
        print("You Lost") game_over = True

