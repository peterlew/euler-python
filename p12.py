
from Useful import numDivisors

counter = 0 
triangle = 0

while True:
	counter += 1
	triangle += counter
	if numDivisors(triangle) > 500:
		print(triangle)
		exit()
