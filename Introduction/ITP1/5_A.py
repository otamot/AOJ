import sys
def printRectangle(H,W):
	for i in range(H):
		for j in range(W):
			sys.stdout.write("#")
		print ""

if __name__ == "__main__":
	H,W = [-1,-1]
	while(H != 0 and W != 0):
		if(H != -1 and W != -1):
			print ""
		H,W = map(int,raw_input().split(" "))
		printRectangle(H,W)
