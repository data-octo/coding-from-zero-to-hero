import random

def numbergame(upperlimit):
    '''Please a number guessing game.'''
    guesses = 1
    win = 0
    name = input("Hi, what's your name? ")
    print('Hi, ', name)
    print("Let's play a game")
    while True:
        print("I'm thinking of a number between 1 and ", upperlimit)
        guess = int(input("What's your first guess? "))
        number = random. randint(1, upperlimit)
        playing = True
        while playing:
            if guess == number:
                print("That's it!")
                print("You guessed it in ", guesses, "guesses!")
                win = 1
                break
            elif guess < number:
                guess = int(input("Nope. Higher. "))
            elif guess > number:
                guess = int(input("Nope. Lower. "))
            else:
                guess = int(input("Error"))
            guesses += 1

        replay = input("Play again? (y/n) ")
        while replay != "y" and replay != "n":
            replay = int(input("Error"))
        if replay == "n":
            break
        elif replay == "y":
            guesses = 1
            win = 0

numbergame(100)