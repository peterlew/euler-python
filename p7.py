
from math import sqrt, floor

primes = [2]
cur = 3 

while len(primes) < 10001:
	top = floor(sqrt(cur))
	for p in primes:
		if p > top:
			primes.append(cur)
			break
		elif cur % p == 0:
			break
	cur += 1

print(primes[-1])
			
