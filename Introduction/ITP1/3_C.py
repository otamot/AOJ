if __name__ == "__main__":
	while True:
		s = raw_input().split(" ")
		x = int(s[0])
		y = int(s[1])
		if x == 0 and y == 0:
			break
		print str(min(x,y)) + " " + str(max(x,y))
