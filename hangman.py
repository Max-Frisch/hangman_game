import random as r

wordlist = ['word', "scrabble", "computer", "hangman", "skyscraper", "telephone", "xylophone", "address", "microwave"]

rand_int = r.randint(0,len(wordlist)-1)
secret_word = wordlist[rand_int]
guessed_word = "_ "*len(secret_word)

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
|     /|\\
|
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
    print(f"(the secret word is: {secret_word})")
    print("")
    print("")

    guessed_letter = input(f"The word has {len(secret_word)} letters. Guess a letter: ")
    if guessed_letter not in secret_word:
        wrong_guesses.append(guessed_letter)
    print("")
    print("wrong guesses: ", wrong_guesses)
    print("")
    print("")
    print(hangman_status[len(wrong_guesses)])
    print("")
    print("")
    if len(wrong_guesses) == len(hangman_status)-1:
        print("YOU LOOSE, SUCKER! NOW YOU'RE DEAD!")
        break
    
    
    
    