import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print('You have used these letters: ', ' '.join(used_letters))


        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            user_letters.add(user_letter)
            if user_letter in word_letter:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('you have already used that character. please try again.')

        else:
            print('invalid character. Pls Try Again')




user_input = input('Type something')
print(user_input)

























