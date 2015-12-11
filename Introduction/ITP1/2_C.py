import sys
def sorting(lis):
	lis.sort()
	
	sys.stdout.write(str(lis[0]))
	for i in range(1,len(lis)):
		sys.stdout.write(" " + str(lis[i]))
	print ""

if __name__ == "__main__":
	s = raw_input().split(" ")
	lis = []
	for i in s:
		lis.append(int(i))
	sorting(lis)
