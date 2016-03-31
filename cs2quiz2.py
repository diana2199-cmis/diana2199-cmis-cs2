#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) True, False
#b) and, or
#c) ==, >, <
#
#2) What does 'return' do?
# The word return takes in an argument from a function and returns a result. The result is called the return value.
#
#3) What are 2 ways indentation is important in python code?
#a) Indentation tells where function definition ends
#b) It tells when to call a function and return a value
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) 36
#problem1_b) sqrt of 3
#problem1_c) 0
#problem1_d) 5
#
#problem2_a) True
#problem2_b) False
#problem2_c) False
#problem2_d) False
#
#problem3_a) 0.3
#problem3_b) 0.5
#problem3_c) 1
#problem3_d) 0.5
#
#problem4_a) 7
#problem4_b) 5
#problem4_c) 0.125
#problem4_d) 5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

import math

def compare(a,b,c):
    return a,b,c

def output(firstNumber,secondNumber,thirdNumber):
    if firstNumber > secondNumber and firstNumber > thirdNumber:
        print """
A: {}
B: {}
C: {}
The largest number was {}
""".format(firstNumber,secondNumber,thirdNumber,firstNumber)
    if secondNumber > firstNumber and secondNumber > thirdNumber:
        print """
A: {}
B: {}
C: {}
The largest number was {}
""".format(firstNumber,secondNumber,thirdNumber,secondNumber)
    if thirdNumber > firstNumber and thirdNumber > secondNumber:
        print """
A: {}
B: {}
C: {}
The largest number was {}
""".format(firstNumber,secondNumber,thirdNumber,thirdNumber)
    if firstNumber == secondNumber == thirdNumber:
        print "You didn't follow directions"

def main():
    print "Type in 3 different numbers (decimals are OK!)"
    firstNumber = float(raw_input("A: "))
    secondNumber = float(raw_input("B: "))
    thirdNumber = float(raw_input("C: "))
    out = output(firstNumber,secondNumber,thirdNumber)

main()

