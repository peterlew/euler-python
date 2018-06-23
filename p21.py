
from Useful import divisors

results = {}

def sumOfDivisors(n):
	if n in results:
		return results[n]
	result = sum(divisors(n))
	results[n] = result
	return result

total = 0
for i in range(1, 10000):
	partner = sumOfDivisors(i)
	if sumOfDivisors(partner) == i and partner != i:
		total += i

print(total)

	
