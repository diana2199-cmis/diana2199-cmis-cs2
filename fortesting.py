#while True:
#	print ":)",

#while False:
#    print ":("

#x = 0
#while x <10:
#	print x
#        x += 1

#x = 100
#while x >= 0:
#    print x
#    x -= 1

#def countFrom1(x,y):
#    while x < y:
#        print x
#        x += 1
#    while x >= y:
#        print x
#        x -= 1
#countFrom1(2,5)

#def addOdds(n):
#    sum = 0
#    if n > 0:
#        while n > 0:
#            if n % 2 == 1:
#                sum += n
#            n -= 1
#    elif n < 0:
#        while n < 0:
#            if n % 2 == 1:
#                sum += n
#            n += 1
#    return sum
#print addOdds(9)

def grid(w,h):
    out = ""
    while w > 0:
        print ".",
        w -= 1
        while h > 0:
            print h * w
            h -= 1
print grid(4,5)

def grud(w,h):
    out = ""
    y = 0
    while y < h:
        x = 0
        while x < w:
            out += "."
            x += x
        y += 1
        out += "
