import random

def output(target,guess,difference):
    if guess == target:
        print """
The target was {}.
Your guess was {}.
That is correct! You must be a phychic!
""".format(target,guess)
    if guess > target:
        print """
The target was {}.
Your guess was {}.
That's over by {}.
""".format(target,guess,difference)
    if guess < target:
        print """
The target was {}.
Your guess was {}.
That's under by {}.
""".format(target,guess,difference)

def main():
    minimumNumber = int(raw_input ("What is the minimum number? "))
    maximumNumber = int(raw_input ("What is the maximum number? "))
    print "I'm thinking of a number from", minimumNumber, "and", maximumNumber,"."
    guess = int(raw_input ("What do you think it is?: "))
    target = random.randint(int(minimumNumber),int(maximumNumber))
    difference = abs(guess-target)
    out= output(target,guess,difference)

main()
