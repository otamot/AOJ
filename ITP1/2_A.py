def lsCorrelation(a,b):
	if(a > b):
		print "a > b"
	elif(a < b):
		print "a < b"
	else:
		print "a == b"

if __name__ == "__main__":
	s = raw_input().split(" ")
	a = int(s[0])
	b = int(s[1])
	lsCorrelation(a,b)
