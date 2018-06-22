
from math import sqrt, floor 

def factor(n):
	lim = floor(sqrt(float(n)))
	ind = 2
	while ind <= lim:
		if n % ind == 0:
			return([ind] + factor(n // ind))
		ind += 1
	return [n]
