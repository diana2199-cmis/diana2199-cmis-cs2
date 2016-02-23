import math
#add two numbers together
def add (a, b):
	return a + b
#subtract one number from another number
def sub (d, e):
	return d - e
#multiple two numbers
def mul (g, h):
	return g * h
#divide one number by another number
def div (j, k):
	return (j / k)
#calculate number of seconds using number of hours
def hours_from_seconds (a):
	return a / 3600
print hours_from_seconds (86400)
#calculate area of circle using radius of the circle
def circle_area (a):
	return math.pi * (a**2)
print circle_area (5)
#find volume of sphere using radius of the sphere
def sphere_volume (a):
	return 1.33333333333 * math.pi * (a**3)
print sphere_volume (5)
#takes two diameters of sphere and return average volumes
def avg_volume (a, b):
	 return ((1.0/6 * math.pi * a**3) + (1.0/6 * math.pi * b**3)) /2
print avg_volume(10, 20)
#find area of triangle using three side lengths
def area (a, b, c):
	return math.sqrt (2.75*(2.75-a)*(2.75-b)*(2.75-c))
print area (1.0, 2.0, 2.5)

def right_align (word):
	return (80-len(word))*(" ")+word
print right_align ("Hello")

def center (word):
	return (40-len(word))*(" ")+word
print center ("Hello")

def msg_box (word):
    return "+" + ((len(word)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word) +4)*"-") + "+"
print msg_box ("Hello")

def msg_box (word):
    return "+" + ((len(word)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word) +4)*"-") + "+"
print msg_box ("I eat cats!")

a= add (3, 4)
b= sub (5, 3)
c= mul (4, 4)
d= div (2.0, 3.0)
e= hours_from_seconds (86400)
f= circle_area (5)
g= sphere_volume (5)
h= avg_volume (10, 20)
i= area (1.0, 2.0, 2.5)
j= right_align ("Hello")
k= center ("Hello")
l= msg_box ("Hello")
m= msg_box ("I eat cats!")
print msg_box(str(a))
print msg_box(str(b))
print msg_box(str(c))
print msg_box(str(d))
print msg_box(str(e))
print msg_box(str(f))
print msg_box(str(g))
print msg_box(str(h))
print msg_box(str(i))
print msg_box(j)
print msg_box(k)
print l
print m
