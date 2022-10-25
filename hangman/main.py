
import re
import random

# Getting the answer.
pool_file = open("hangman-sample-answer-pool.txt")

pool_answers = []

pool_answer_line =  pool_file.readline()

while pool_answer_line:
    pool_answers.append(pool_answer_line)
    
    pool_answer_line = pool_file.readline()

pool_file.close()

answer = random.choice(pool_answers)

answer = answer.upper() #.upper() means upppercase

# Game Setup.
num_of_inc_guesses = 5 # variable names must be lowercase

answer_guessed = [] # arrays are lists, use []

for current_answer_character in answer: # answer is a string, goes through each character
    # inside has to be indented
    if re.search("^[A-Z]$", current_answer_character): # first needs reject pattern; searching for whats inside; ^ = starts $ = ends
        answer_guessed.append(False) #T/F first letter capitalized; append adds to list
    else:
        answer_guessed.append(True)

# Game  logic.
current_incorrect_guesses = 0

letters_guessed = []

while current_incorrect_guesses < num_of_inc_guesses and False in answer_guessed:
    # Game Summary
    print (f"Number of incorrect guesses left: {num_of_inc_guesses - current_incorrect_guesses}")

    print("Guessed letters: ", end =  "")
    
    for current_guessed_letter in letters_guessed:
        print(current_guessed_letter, end = " ")

    print()

    # Display puzzle board.
    for current_answer_index in range(len(answer)): #val od answer, getting the length, going through index
        if answer_guessed[current_answer_index]:
            print(answer[current_answer_index], end = "")
        else:
            print("_", end = "")

    print()

    # Let user guess a letter.
    letter = input("Enter a letter: ")

    letter = letter.upper()

    print()

    # Check if user entered a valid letter.
    if re.search("^[A-Z]$", letter) and len(letter) == 1 and letter not in letters_guessed:
        current_letter_index = 0

        # Insert the letter in list of letter guesses (insertion sort)
        for current_letter_guessed in letters_guessed:
            if letter < current_letter_guessed:
                break
            
            current_letter_index += 1
        
        letters_guessed.insert(current_letter_index, letter)

        # See if letter is in the answer.
        if letter in answer:
            for current_answer_index in range(len(answer)):
                if letter == answer[current_answer_index]:
                    answer_guessed[current_answer_index] = True
        else:
            current_incorrect_guesses += 1

# Post-game summary.
if current_incorrect_guesses < num_of_inc_guesses:
    print("Congratulations, you won!")
else:
    print(f"Sorry, you lost. The answer was {answer}")
            
        