if __name__ == "__main__":
	size = input()
	l = map(int,raw_input().split(" "))
	if size == len(l):
		print str(min(l)) + " " + str(max(l)) + " " + str(sum(l))
	else:
		print "error"
