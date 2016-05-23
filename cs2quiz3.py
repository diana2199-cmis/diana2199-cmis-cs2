#Section 1: Terminology
# 1) What is a recursive function? correct
# A recursive function is a function that does one thing or another depending on the input
# 
#
# 2) What happens if there is no base case defined in a recursive function? correct
# If there is no base case defined in a recursive function, the function gets an error message.
#
#
# 3) What is the first thing to consider when designing a recursive function? correct
# First thing to consider when designing a recursive function is how the output changes depending on the input user type in
#
#
# 4) How do we put data into a function call? correct
# You can put data into a function call by using arguments.
#
# 
# 5) How do we get data out of a function call? correct
# You can get data out of a function call by using return.
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 = 2 
#a2 = 6 
#a3 = -1 correct

#b1 = 2 correct
#b2 = 2 correct 
#b3 = 4 correct

#c1 = -2 correct
#c2 = 4 correct
#c3 = 4

#d1 = 6 correct 
#d2 = 8 correct
#d3 = 4 correct

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

# HAVE: base case +2, recursion case +2, recursive returns 1, main function +1

def averageOdd(number,next):
    # this is a base case
    if next == "":
        print "The average of your odd numbers was " + float(number)
    # recursive case
    else:
        print next

def main():
    next = raw_input("Next: ")
    odd = number % 2
    number = odd / 2
    averageOdd(average,next)

main()
