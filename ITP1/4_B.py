import math
def roundCircle(r):
	return 2 * math.pi * r

def volumeCircle(r):
	return math.pi * r * r

if __name__ == "__main__":
	r = float(raw_input())
	print "{0:15f}".format(volumeCircle(r)) + " " + "{0:15f}".format(roundCircle(r))

