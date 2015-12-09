def printUntilInputZero():
	i = 1
	x = int(raw_input())
	while x != 0:
		print "case "+str(i)+": "+ str(x)
		i = i + 1
		x = int(raw_input())

if __name__ == "__main__":
	printUntilInputZero()
		
