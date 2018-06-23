
from Useful import toDigits
from functools import reduce

def arePandigital(ns):
	digits = reduce(lambda x, y: x + y, map(toDigits, ns))
	digits.sort()
	return(digits == list(range(1, 10)))


# require a <= b (and of course b <= c)
# so a can be max 2 digits (3 would imply 3 for it, 3 for b, and 5 for c)
# and b can be at most 4 digits (5 would imply 1 for a, 5 for b, and 5 for c)

results = set() 
for a in range(1, 100):
	for b in range(a, 10000):
		if(arePandigital([a, b, a * b])):
			results.add(a * b)

print(sum(results))
			
	
