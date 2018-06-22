
from Useful import isSquare, isqrt

for a in range(1, 334):
	for b in range(a + 1, (1000 - a) // 2 + 1):
		cSquared = a**2 + b**2 
		if isSquare(cSquared):
			c = isqrt(cSquared)
			if a + b + c == 1000:
				print(a * b * c)
				exit()
		 	
