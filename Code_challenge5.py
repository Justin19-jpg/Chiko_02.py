num = eval(input("give a number, "))
factorial = 1

for x in range(num,0,-1):
	factorial *= x
print("The factorial of ",num,"is",factorial)
