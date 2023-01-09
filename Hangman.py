
import random
import string
import words


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses the word from the list words
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)  ## get a vaid word
    word_letters = set(word)  ## getting the individual letter of the word
    alphabet = set(string.ascii_uppercase)  ## getting the complete set of alphabets
    used_letters = set()  # what letter user has guessed
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # letter used to be told to the user
        print('Hey you have', lives, 'life left you have used the these letters so far:', ' '.join(used_letters))
        ## what current word is
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("current word: ", ' '.join(word_list))
        ##getting user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:  # the input is not guessed before
            used_letters.add(user_letter)  # updated the used letter
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('you have lost a life')
        elif user_letter in used_letters:
            print("You have already used the word please use a different one")
        else:
            print("Please enter a valid word")
    if len(word_letters) == 0:
        print(" Hey you have won the word you guessed is correct", word)
    else:
        print("Sorry you lost the word was", word)


