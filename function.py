import math
#addition operation
def add(a,b):
	return a+b
w= add(3,4)
print w
#subtraction operation
def sub(a,b):
	return a-b
x= sub(5,3)
print x
#multiplication operation
def mul(a,b):
	return a*b
y= mul(4,4)
print y
#division operation
def div(a,b):
	return a/b
z= div(2.0,3)
print z
#takes number of seconds and turn into number of hours
def hours(a,b,c):
	return a/b/c
h=hours(86400,60,60)
print h
#using area of circle to find radius of the circle
def area(a):
	return math.pi* a**2
print area(5)
#find volume using radius of a sphere
def volume(r):
	return math.pi* 4/3* r**3
print volume(5)
