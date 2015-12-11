def printTop3Mountain(mountains):
	mountains.sort()
	mountains.reverse()
	for i in range(0,3):
		print mountains[i]

if __name__ == "__main__":
	mountains = []
	for i in range(0,10):
		mountains.append(int(raw_input()))
	
	printTop3Mountain(mountains)

