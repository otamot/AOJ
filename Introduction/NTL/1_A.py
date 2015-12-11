import sys
import math
def primeFactorize(n):
	i = 2
	sys.stdout.write(str(n) + ":")
	while True:
		if n == 1:
			break
		elif i > math.sqrt(n):
			sys.stdout.write(" " + str(n))
			break
		elif n % i == 0:
			sys.stdout.write(" " + str(i))
			n = n / i
		else:
			i = i + 1
	sys.stdout.write("\n")

if __name__ == "__main__":
	n = input()
	primeFactorize(n)

