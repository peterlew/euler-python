
fib1 = 1
fib2 = 1
fib3 = 2
ind = 3

while fib3 < 10**999:
	fib1 = fib2
	fib2 = fib3
	fib3 = fib1 + fib2
	ind += 1

print(ind)
