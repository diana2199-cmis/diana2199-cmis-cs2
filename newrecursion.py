import random
def guessing(targetNum, tryNum):
	guess= int(raw_input ("What do you think it is?:"))
	if tryNum == 0:
		print "You're bad at this game"
		return 0
	elif int(guess) > int(targetNum):
		print "Too high"
		guessing(targetNum, tryNum-1)
		return 0
	elif int(guess) < int(targetNum):
		print "Too low"
		guessing(targetNum, tryNum-1)
		return 0
	elif targetNum == guess:
		print "Correct"
		return 1

def rounds(rounddd, right, tryAgain):
	targetNum = random.randint (0,100)
	if rounddd == 0:
		print right
	elif rounddd != 0:
		between = ("I am thinking of a number between 0 and 100")
		print between
		games=guessing(targetNum, tryAgain)
		adding= right + games
		print "You have {} rounds left".format(rounddd-1)
		rounds(rounddd-1, right, tryAgain)

def main (): 
    right = 0
    tryAgain =4
    rounddd=3
    rounds(rounddd, right, tryAgain)
main ()
