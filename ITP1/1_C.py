def square(a,b):
	return a*b
def circumferenc(a,b):
	return (a+b)*2

if __name__ == "__main__":
	s = raw_input().split(" ")
	a = int(s[0])
	b = int(s[1])
	sq = square(a,b)
	ci = circumferenc(a,b)
	print str(sq) + " " + str(ci)	
