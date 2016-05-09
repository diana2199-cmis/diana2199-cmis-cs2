# This program makes a story based on your input about yourself
# It asks for...
# 1. First letter of your first and last name 
# 2. Age, grade, and number of family members
# 3. Birthday, month, and year
# 4. 

import random
import math

def one(firstLetter):
    if firstLetter == "a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m":
        return "She lived with her family in a city. "
    elif #continue this part:
        return "She lived alone in a forest. "

def output(name):
    return """*Hello {} :)""".format(name)

def main():
    name = raw_input("*What is your name? ")
    print output(name)
    print "*This program will make a story based on your input about yourself."
    print ""
    print "<Once upon a time, there was a girl named Iva.>"
    print ""
    firstLetter = raw_input("*What is the first letter of you name? ")
    print one(firstLetter)
    
main()
