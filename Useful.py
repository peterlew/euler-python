
from math import sqrt, floor 

def factor(n):
	lim = floor(sqrt(float(n)))
	ind = 2
	while ind <= lim:
		if n % ind == 0:
			return([ind] + factor(n // ind))
		ind += 1
	return [n]

def toDigits(n):
	if n < 10:
		return([n])
	return(toDigits(n // 10) + [n % 10])

def nPrimes(n):

	primes = [2]
	cur = 3

	while len(primes) < n:
        	top = floor(sqrt(cur))
        	for p in primes:
                	if p > top:
                        	primes.append(cur)
                        	break
                	elif cur % p == 0:
                        	break
        	cur += 1
	
	return(primes)

def primesUnder(n):

	primes = [2]
	cur = 3

	while cur < n:
        	top = floor(sqrt(cur))
        	for p in primes:
                	if p > top:
                        	primes.append(cur)
                        	break
                	elif cur % p == 0:
                        	break
        	cur += 1
	
	return(primes)

def isqrt(n):
	x = n
	y = (x + 1) // 2
	while y < x:
		x = y
		y = (x + n // x) // 2
	return x

def isSquare(n):
	rt = isqrt(n)
	return(rt**2 == n)
	
def numDivisors(n):
	lim = floor(sqrt(float(n)))
	ind = 2
	expProd = 1 
	while ind <= lim:
		expCount = 1
		while n % ind == 0:
			expCount += 1	
			n //= ind
		expProd *= expCount
		ind += 1
		if expCount > 1:
			lim = floor(sqrt(float(n)))
	if n == 1:
		return(expProd)
	else:
		return(2 * expProd)

def divisors(n):
	lim = floor(sqrt(float(n)))
	ind = 2
	divs = [1]
	while ind <= lim:
		if n % ind == 0:
			if ind * ind == n:
				divs += [ind]
			else:
				divs += [ind, n // ind]
		ind += 1
	divs.sort()
	return divs
		























