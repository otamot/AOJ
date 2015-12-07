def s2hms(s):
	h = s / 3600
	s = s % 3600
	m = s / 60
	s = s % 60
	print str(h) + ":" + str(m) + ":" + str(s)

if __name__ == "__main__":
	s = int(raw_input())
	s2hms(s)


