from asyncio.windows_events import NULL
import random

# Sets the guess value as NULL to prevent the game from ending immediately
guess = NULL

# Calls the 'random' class in python with the function randint and specifies the range
#  of 1 to 100, sets this value to the variable 'answer' prior to any function calls
answer = random.randint(1, 100)

# Initializes a counter for guesses to let the user know how well they've done
guessCount = 0

print("Guess the number. Random integer 1-100\n")

# Calls a while loop to run as long as the user's guess does not equal the answer
#  - If the guess is higher than the answer, output "Lower"
#  - If the guess is lower than the answer, output "Higher"
#  As soon as the guess is equal to the answer, the while loop exits and the guessCount is finalized
while (guess != answer):
    guess = int(input("Enter a number: "))
    if (guess > answer):
        print("Lower.\n")
    elif (guess < answer):
        print("Higher.\n")

    guessCount += 1

# Let the user know they've won and let them know how many guesses it took them (parsed as str var)
print("You guessed the correct number in " + str(guessCount) + " tries!")