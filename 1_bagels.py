import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''Bagels, một trò chơi suy đoán.

Tôi đang suy nghĩ về một số có {} chữ số không lặp lại.
Hãy cố gắng để đoán ra nó. Sau đây là những gợi ý tôi dành cho bạn:

Pico: Một chữ số đúng, sai vị trí.
Fermi: Một chữ số đúng, đúng vị trí.
Bagels: Không có chữ số đúng.

Ví dụ, nếu chữ số bí mật là 248 và bạn đoán 843
>> Bạn sẽ nhận được gợi ý: Fermi Pico.'''.format(NUM_DIGITS))

    while True:  # Main game loop.
        # This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print('Tôi đang nghĩ về 1 số.')
        print(' Bạn có {} lần đoán.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Lần #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # They're correct, so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print('Hết lượt.')
                print('Đáp án là {}.'.format(secretNum))

        # Ask player if they want to play again.
        print('Muốn chơi lại? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:4 Project #1
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ' '.join(clues)


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
