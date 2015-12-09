from decimal import *
def printDevided(a,b):
	
	d = a/b
	r = a%b
	b = Decimal(a)/Decimal(b)
	print str(d)+" "+str(r)+" "+"{0:.15f}".format(b)

if __name__ == "__main__":
	s = raw_input().split(" ")
	a = int(s[0])
	b = int(s[1])
	printDevided(a,b)
