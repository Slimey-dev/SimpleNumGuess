import random


num_digits = 3
max_guesses = 10


def main():
    print('''Bagels is a deductive logic game.

          I am thinking of a {}-digit number with no repeated digits.
          Try guessing what it is.
          When I say:  That means:
            Pico         One digit is correct but in the wrong position.
            Fermi        One digit is correct but in the right position.
            Bagels       No digit is correct.

          For example, if you the secret number was 248 and your guess was 843 cluess would be Fermi Pico.'''.format(num_digits))

    while True:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(f'You gave {max_guesses}-guesses to get it.')

        numGuesses = 1
        while numGuesses <= max_guesses:
            guess = ' '
            while len(guess) != num_digits or not guess.isdecimal():
                print(f'Guess #{numGuesses}: ')
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > max_guesses:
                print('You ran out of guesses')
                print(f'The answer was {secretNum}.')

        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
        print('Thanks for playing!')


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    return ''.join(str(numbers[i]) for i in range(num_digits))


def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if not clues:
        return 'Bagels'
    clues.sort()
    return ' '.join(clues)


if __name__ == '__main__':
    main()
