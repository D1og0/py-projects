import random

number_to_guess = random.randint(0, 10)
guessed = False
tries = 0

while guessed == False:
    inp = int(input('Guess the number: '))
    tries += 1

    if inp < number_to_guess:
        print('Your guess is too low')
    elif inp > number_to_guess:
        print('Your guess is too high')
    else:
        print('You guessed the number. The number was ' + str(number_to_guess) + ', You guessed in ' + str(tries) + ' tries')
        tries = 0
        break