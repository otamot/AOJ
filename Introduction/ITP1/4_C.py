def simpleCalculator(a,op,b):
	if op == "?":
		return "END"
	elif op == "+":
		return a+b
	elif op == "-":
		return a-b
	elif op == "*":
		return a*b
	elif op == "/":
		return a/b
	else:
		return "error"

if __name__ == "__main__":
	while True:
		s = raw_input().split(" ")
		a = int(s[0])
		op = s[1]
		b = int(s[2])
		ans = simpleCalculator(a,op,b)
		if(ans == "END"):
			break
		elif(ans == "error"):
			print ans
			break
		else:
			print str(ans)


