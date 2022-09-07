import random

object = input('Rock ~ Paper ~ Scissors: ')
objects = ['rock', 'paper', 'scissors']
choice = random.choice(objects)

# Game conditions
def game():
    if object == choice:
        print('Draw!')
    elif object == 'paper' and choice == 'rock':
        print('You won!')
    elif object == 'rock' and choice == 'scissors':
        print('You won!')
    elif object == 'scissors' and choice == 'paper':
        print('You won!')
    else:
        print('Computer won.')

game()