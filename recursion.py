#countdown
def countdown(n):
	#this is the base case
    #base case does not call itself
    if n<0:
        print "Blastoff!"
    #this is the recursive case
    #recursive case calls itself
    else:
        print n
        countdown(n-1)

#countup
def countup(n):
    if n>10:
        print "Blastoff!"
    else:
        print n
        countup(n+1)

#countdownfrom
def countdown_from_to(start,stop):
    if start<stop:
        print "Blastoff!"
    else:
        print start
        countdown_from_to(start-1,stop)

#countupfrom
def countup_from_to(start,stop):
    if start>stop:
        print "Blastoff!"
    else:
        print start
        countup_from_to(start+1,stop)

#adder
def adder(next,total):
    if next == "":
        print "The sum is: " + str(total)
    else:
        total += float(next)
        next = raw_input("Running total: " + str(total) + "\n" + "Next Number: ")
        return adder(next,total)

def main():
    countdown(23)
    countup(-300)
    countdown_from_to(156,99)
    countup_from_to(2,53)
    adder(0,0)

main()

