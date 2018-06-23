
from Useful import isPrime, primesUnder

def lenPrimeChain(a, b):
	n = 0
	while True:
		if not isPrime(n * n + a * n + b):
			return n
		n += 1

bestChainLen = 40
bestA, bestB = 1, 41
# we could restrict a, but probably won't have to
for a in range(-999, 1000):
	# b must be positive and prime for the n = 0 case
	for b in primesUnder(1000):
		thisLen = lenPrimeChain(a, b)
		if thisLen > bestChainLen:
			bestChainLen = thisLen
			bestA, bestB = a, b

print(bestA * bestB)
		


