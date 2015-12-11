def abc(a,b,c):
	if a < b and b < c:
		return True
	else:
		return False

if __name__ == "__main__":
	s = raw_input().split(" ")
	a = int(s[0])
	b = int(s[1])
	c = int(s[2])
	if abc(a,b,c):
		print "Yes"
	else:
		print "No"
