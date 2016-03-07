# Part 1 Terminology : 12/15 points total 
# Part 2 Programming : 15/25 points total 
# Total 27/40 

#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# The symbol "=" is called assignment operator. It is used to assign the value on its right to its left. That means it assigns the value on the right to the left.
# 1 point 
#
#2 3pts) Write a technical definition for 'function'
# A function is a named sequence of statement that perform a special task, or a computation. Defining a function means to specify name and sequence of statements. When you have a function, you can use its name to call a function.
# 3 points
#
#3 1pt) What does the keyword "return" do?
# The keyword "return" takes in argument from a function and return, or spit out, a result. The result is called return value.
# 3 points 
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1: interger ex) 1, 26, -43
#	2: floating point ex) 0.3, 0.0, -234.123
#	3: string ex) "Hey"
#	4: tuple ex) "Diana", "Oh", "Grade", 9, "CMIS"
#	5: boolean ex) True, False
#5 points 
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
# A function definition is defining, or giving a function value. It specifies name of a new function and the sequence of statements that execute when the function is called. Function call is when you spit out the function by using the function's name. You first used function definition to define a function, then you use function call to call a function.
#
#2 points 
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:
#	2:
#	3:
#0 points 
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi
#Justification: 
#Have: header line, return value, parameter name, function name,parameter name, return value, header line, second headerline, getting input, calling output function, correcnt diameter formula, variable name, calling main
#Missing: incorrect formula, incorrect output format, incorrect use of format function, converting input, explanatory comments, code format
# points (15/25)
import math

def main():
    area1 = raw_input("Area of C1: ")
    area2 = raw_input("Area of C2: ")
    area3 = raw_input("Area of C3: ")
    
    dia1 = div(int(area1), math.pi)
    dia2 = div(int(area2), math.pi)
    dia3 = div(int(area3), math.pi)

def left_align (word):
    return (80-len(word))*(" ")+word
print left_align ("c1")

def right_align (dia1):
    return div(int(area1), math.pi)
print right_align 
  
    return (80-len(word))*(" ")+word
print left_align ("c2")

    print right_align dia2

    return (80-len(word))*(" ")+word
print left_align ("c3")

    print right_align dia3
