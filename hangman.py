import random as r

wordlist = ['word', "scrabble", "computer", "hangman", "skyscraper", "telephone", "xylophone", "address", "microwave", "laptop", "smartphone", "mirror", "eggplant", "rocket", "mug", "coffee", "croissant"]
number_wrong_guesses = 0
rand_int = r.randint(0,len(wordlist)-1)
secret_word = wordlist[rand_int]
guessed_word = "_"*len(secret_word)
guessed_letters = []
for single_letter in guessed_word:
    guessed_letters.append(single_letter)


hangman_status = [''' 

""""""""
|
|
|
|
|
-----''',''' 
""""""""
|      |
|      O
|
|
|
-----''',''' 
""""""""
|      |
|      O
|     /
|
|
-----''',''' 
""""""""
|      |
|      O
|     /|
|
|
-----''','''
""""""""
|      |
|      O
|     /|\\
|
|
-----''','''
""""""""
|      |
|      O
|     /|\\
|     /
|
-----''','''
""""""""
|      |
|      O
|     /|\\
|     / \\
|
-----''',
]
wrong_guesses = []

print("")
print("                       Welcome to Hangman!")
print("")
print("")
while True:
    print(guessed_word)
    # print(f"(the secret word is: {secret_word})")
    print("")
    print("")

    guessed_letter = input(f"The word has {len(secret_word)} letters. Guess a letter: ")
    # if made a wrong guess with the single guessed letter
    if guessed_letter not in secret_word:
        wrong_guesses.append(guessed_letter)
        number_wrong_guesses +=1
        print(f"ZONK! You guessed a wrong letter!")
    # the guessed letter is within the word    
    else:
        index = 0
        for letter in secret_word:
            if letter == guessed_letter:
                guessed_letters[index] = letter
                guessed_word = "".join(guessed_letters)
            index += 1
        # checking for the win condition, all letters guessed right
        if guessed_word == secret_word:
            print("")
            print("CONGRATS! You guessed the word!")
            print("")
            print(guessed_word)
            break
    print("")
    print("")
    # print out no. of mistakes and wrong guesses, once 1 mistake was made
    if len(wrong_guesses) > 0:
        print("")
        print(f"You made {number_wrong_guesses} of {len(hangman_status)-1} mistakes.")
        print("wrong guesses: ", wrong_guesses)
        print("")
    print("")
    # if at least 1 mistake was made, print out the hangman
    if len(wrong_guesses) > 0:
        print(hangman_status[len(wrong_guesses)])
    print("")
    print("")
    # print "loose message" if no. of wrong guesses == allowed mistakes
    if len(wrong_guesses) == len(hangman_status)-1:
        print("YOU LOOSE! NOW YOU'RE DEAD!")
        break
    