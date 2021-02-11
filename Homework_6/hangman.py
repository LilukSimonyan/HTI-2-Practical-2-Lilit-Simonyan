import random
import os

def get_a_random_word():
    file_name = 'fruits.txt'
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, file_name)

    with open('fruits.txt') as f:
        fruits = [row.strip() for row in f.readlines()]
        return random.choice(fruits)

word = get_a_random_word()
print(word)

def game():
    l = len(word)
    step = 5
    guess = ['_ '] * l
    indefinite_letter = '_ '
    while step != 0:
        if indefinite_letter not in guess:
            return f'{"".join(guess)}\nYou won the game.'
        else:
            letter = input(f'Guess the word. {step} mistakes left.\n{"".join(guess)}\nGuess a letter: ').lower()
            if letter in word:
                for i in range(l):
                    if letter == word[i]:
                        guess[i] = (word[i]+" ").upper()

            else:
                step -= 1
    else:
        return "You lost the game."

print(game())
