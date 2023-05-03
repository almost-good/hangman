import random
from words import words
import string


def get_word(words):
    word = random.choice(words)

    if '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_word(words)
    word_letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)
    
    life = 6

    while len(word_letters) > 0 and life > 0:
        print("You have ", life, "lifes and you have tried these letters: ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("\n", ' '.join(word_list), "\n")

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet and user_letter not in used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter) 

            else:
                life -= 1
                print("Letter is not in word.")

        elif user_letter in used_letters:
            print("You already tried that one! Try again!")

        else:
            print("Incorrect value! Try again!")

    if life == 0:
        print("You lost the game! The word was: ", word)

    else:
        print("You won a game! The word is: ", word)


hangman()