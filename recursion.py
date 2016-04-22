#countdown
def countdown_from_to(start,stop):
    if start<stop:
        print "Blastoff!"
    else:
        print start
        countdown_from_to(start-1,stop)

def main():
    countdown_from_to(156,99)

main()

#countup
def countup_from_to(start,stop):
    if start>stop:
        print "Blastoff!"
    else:
        print start
        countup_from_to(start+1,stop)

def main():
    countup_from_to(2,53)

main()

#adder
def adder(total,next):
    print "Running total: ", float(total)
    next = float(raw_input("Next number: "))
    total = total+next

def main():

    return
main()




