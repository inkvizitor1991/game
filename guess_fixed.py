import os

from random import choice
from string import ascii_lowercase

FILENAME = 'sowpods.txt'
os.chdir(os.path.dirname(__file__))


def get_rand_word(filename):
    with open(filename, 'r') as f:
        return choice([x.strip() for x in f]).lower()


def get_letter(attempt, guess):
    while True:
        user_input = input(f'> Guess a letter ({attempt} attempts left): ').lower()
        if len(user_input) != 1 or user_input not in ascii_lowercase:
            print("> Please input a letter!")
        elif user_input in guess:
            print(f"> You have guessed '{user_input}' before")
        else:
            break
    return user_input


def play(word):
    code_letters, wrong = [], []
    attempts = 6
    for letter in word:
        if letter.isalpha():
            code_letters.append('-')
        else:
            code_letters.append('   ')
    while attempts > 0:
        print('\nWrong guess:', ', '.join(wrong))
        print(' '.join(code_letters))
        entered_letter = get_letter(attempts, code_letters)
        for index, letter in enumerate(word):
            if letter == entered_letter:
                code_letters[index] = entered_letter
        if entered_letter not in word:
            attempts -= 1
            if entered_letter not in wrong:
                wrong.append(entered_letter)
        if '-' not in code_letters:
            print('> You win!')
            break
    else:
        print('> You lose...')
        print(f'> Answer: {word.capitalize()}')


if __name__ == "__main__":
    word = get_rand_word(os.path.join('data', FILENAME))
    play(word)
