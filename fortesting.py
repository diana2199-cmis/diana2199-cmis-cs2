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
