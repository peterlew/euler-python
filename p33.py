
# after some paper work, the only case where this can happen is when 
# 1 <= a, b, c <= 9
# we have the form BA/AC = B/C, as in the example (a = 9, b = 4, c = 8)
# and 9bc + ac = 10ab

from fractions import Fraction

prod = Fraction(1, 1)

for a in range(1, 10):
	for b in range(1, 10):
		for c in range(1, 10):
			if 9 * b * c + a * c == 10 * a * b:
				prod *= Fraction(10 * b + a, 10 * a + c)

print(prod.denominator)
			
