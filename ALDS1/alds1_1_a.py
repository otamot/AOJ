import sys
def insertionSort(A,N):
	for i in range(1,N):
		sys.stdout.write(str(A[0]))
		for k in range(1,N):
			sys.stdout.write(" " + str(A[k]))
		print ""
		v = A[i]
		j = i - 1
		while(j >= 0 and A[j] > v):
			A[j+1] = A[j]
			j = j - 1
		A[j+1] = v
		

if __name__ == "__main__":
#	sys.stdout.write("N:")

	N=int(raw_input())
#	print N
	st = raw_input().split(" ")
	A = []
	for s in st:
		A.append(int(s))
#	print A
	if len(A) != N:
		print "error"
		sys.exit()
	insertionSort(A,N)
#	print Ai
	sys.stdout.write(str(A[0]))
	for k in range(1,N):
		sys.stdout.write(" " + str(A[k]))
	print ""
