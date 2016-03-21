import math
#this simple program calculates your lucky number using you birthmonth and birthdate

#this function does the calculation
def calculation(birthmonth, birthdate):
	return (birthmonth*5-5+birthdate)/6+2

def output(name,birthmonth, birthdate,result):
    return """{}, Your birthmonth is {}, your birthdate is {}, your lucky number is {}""".format(name,birthmonth,birthdate,result)

#this main function organizes functions above and calls them in correct order
def main():
    name = raw_input("Hello :) What's your name? ")
    birthmonth = raw_input("Type your birthmonth (in number) ")
    birthdate = raw_input("Type your birthdate (in number) ")
    result = calculation(int(birthmonth),int(birthdate))
    print output(name, birthmonth, birthdate, result)

main()
