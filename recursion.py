#countdown
def countdown(n):
    if n<0:
        print "Blastoff!"
    else:
        print n
        countdown(n-1)

def main():
    countdown(23)

main()

#countup
def countup(n):
    if n>10:
        print "Blastoff!"
    else:
        print n
        countup(n+1)
 
def main():
    countup(-300)

main()

#countdownfrom
def countdown_from_to(start,stop):
    if start<stop:
        print "Blastoff!"
    else:
        print start
        countdown_from_to(start-1,stop)

def main():
    countdown_from_to(156,99)

main()

#countupfrom
def countup_from_to(start,stop):
    if start>stop:
        print "Blastoff!"
    else:
        print start
        countup_from_to(start+1,stop)

def main():
    countup_from_to(2,53)

main ()

#adder
def adder(next,total):
    if next == "":
        print "The sum is: " + str(total)
    else:
        total += float(next)
        next = raw_input("Running total: " + str(total) + "\n" + "Next Number: ")
        return adder(next,total)

def main():
    adder(0,0)

main()

