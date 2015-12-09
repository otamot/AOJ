def nDivisors(a,b,c):
	count = 0
	for i in range(a,b+1):
		if c % i == 0:
			count = count + 1
	return count

if __name__ == "__main__":
	s = raw_input().split(" ")
	a = int(s[0])
	b = int(s[1])
	c = int(s[2])
	print str(nDivisors(a,b,c))
