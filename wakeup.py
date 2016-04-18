import math

def calculation(firstNumber,secondNumber,thirdNumber,fourthNumber,fifthNumber):
    return (firstNumber + secondNumber + thirdNumber + fourthNumber + fifthNumber)/5

def output(average,integer,evenOdd)
    print """
The average is {}
The integer part of the average is {}
The integer is {}
""".format(average,integer,evenOdd)

def main():
    print "This program will ask you for 5 integer or float values."
    print "It will calculate the average of all values from 0 inclusive to 10 exclusive."
    print "It will print out whether the resulting average is even or odd."
    firstNumber = float(raw_input ("n1: "))
    secondNumber = float(raw_input ("n2: "))
    thirdNumber = float(raw_input ("n3: "))
    fourthNumber = float(raw_input ("n4: "))
    fifthNumber = float(raw_input ("n5: "))
    average = calculation(float(firstNumber), float(secondNumber), float(thirdNumber), float(fourthNumber), float(fifthNumber))
    print output()

main()
