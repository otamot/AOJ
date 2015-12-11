import sys

def cyzou(A,N):
	up = 0
	down = 0
	for i in range(0,N-1):
		down = max(down,A[i]-A[i+1])
		up = min(up,A[i]-A[i+1])
	print str(-up) + " " + str(down)


if __name__ == "__main__":
	kosuu = int(raw_input())
	for i in range(kosuu):
		N = int(raw_input())
		A = []
		S = raw_input().split(" ")
		for s in S:
			A.append(int(s))
		cyzou(A,N)

