# This program makes a story based on your input about yourself
# It asks for...
# Your name and ...
# 1. First letter of your first name 
# 2. Age
# 3. Grade
# 4. Number of family members
# 5. Birthmonth

import random
import math

# First letter of your first name
def one(firstLetter):
    if firstLetter == "a" or firstLetter == "b" or firstLetter == "c" or firstLetter == "d" or firstLetter == "e" or firstLetter == "f" or firstLetter == "g" or firstLetter == "h" or firstLetter == "i" or firstLetter == "j" or firstLetter == "k" or firstLetter == "l" or firstLetter == "m":
        return "<She lived with her family in a city.> "
    elif firstLetter == "n" or firstLetter == "o" or firstLetter == "p" or firstLetter == "q" or firstLetter == "r" or firstLetter == "s" or firstLetter == "t" or firstLetter == "u" or firstLetter == "v" or firstLetter == "w" or firstLetter == "x" or firstLetter == "y" or firstLetter == "z":
        return "<She lived alone in a forest.> "

# Type in your age in number
def two(age):
    if int(age) < 20:
        return "<One day, she decided to run away.>"
    else:
        return "<One day, she decided to stay home all day.>"
    

#Type in your grade in number
def three(grade):
    if int(grade) > 7:
        return "<But her aunt called and asked to go visit her>"
    else: 
        return "<But her uncle called and asked to go visit him>"

def four(familyMem):
    if int(familyMem) < 100:
        randomOne = random.randint(10,100)
        return randomOne

def five(birthMonth):
    if int(birthMonth) < 13:
        randomTwo = random.random() * 10
        return randomTwo

def output(name):
    return """*Hello {} :)""".format(name)

def main():
    name = raw_input("*What is your name? ")
    print output(name)
    print "*This program will make a story based on your input about yourself."
    print "."
    print "<Once upon a time, there was a girl named Iva.>"
    print "."
    firstLetter = raw_input("*What is the first letter of you name? ")
    print "."
    print one(firstLetter)
    print "."
    age = raw_input("*Type your age in number. ")
    print "."
    print two(age)
    print "."
    grade = raw_input("*Type your current school grade in number. ")
    print "."
    print three(grade)
    print "."
    familyMem = raw_input("*Type number of people in your family. ")
    print "."
    randomOne = four(familyMem)
    print "<Iva had", four(familyMem), "baht in her bag.>"
    print "<To save money, she decided to walk.> "
    print "."
    birthMonth = raw_input("Type in your birth month in number " )
    print "."
    print "<She walked for about", int(five(birthMonth)), "km, then decided to take a rest.> "
    
main()
