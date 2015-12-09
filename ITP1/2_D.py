def isCircleInARectangle(W,H,x,y,r):
	if (x-r) < 0 or (x+r) > W or(y-r) < 0 or (y+r) > H:
		return False
	else:
		return True


if __name__ == "__main__":
	s = raw_input().split(" ")
	W = int(s[0])
	H = int(s[1])
	x = int(s[2])
	y = int(s[3])
	r = int(s[4])

	if isCircleInARectangle(W,H,x,y,r):
		print "Yes"
	else:
		print "No"
