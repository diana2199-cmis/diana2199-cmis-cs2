import random

def rangeNumber(minimumNumber,maximumNumber):
    return random.radint(minimumNumber,maximumNumber)

def inputGuess():
    random = random.random
    if guess == str(random):
        yourGuess = True
    if guess > str(random):
        yourGuess = "That's over by " + abs(random - guess)
    if guess < str(random):
        yourGuess = "That's under by " + abs(random - guess)




def main():

    minimumNumber = raw_input("What is the minimum number? ")
    maximumNumber = raw_input("What is the maximum number? ")
    yourGuess = raw_input("What do you thik it is?: ")
