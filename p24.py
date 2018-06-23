
# there are 9! permutations beginning with 0, (362880 permutations)
# there are 9! permutations beginning with 1, (725760 )
# so the millionth permutation will begin with 2
# then there are 8! permutations beginning with 0 ...

# in general, we're going to have a_1 * 9! + a_2 * 8! + ... + a_10 = 1000 000

from functools import reduce

nthAvailable = []

target = 1000000 - 1  #what's considered the "first" permutation is actually 0, so...
for i in range(10):
	fact = reduce(lambda x, y: x * y, range(1, 10 - i), 1)
	d = 0
	while fact <= target:
		target -= fact
		d += 1
	nthAvailable.append(d)

total = 0
digits = list(range(10))
for n in nthAvailable:
	total *= 10
	newDig = digits[n]
	total += newDig
	digits.remove(newDig)

print(total)
	
