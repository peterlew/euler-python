
# clearly, no single digit solutions exist
# two digit solutions are also out, as 2 -> 32 is the only real candidate
# and it just doesn't pan out

# three is worth testing, as is four digits

# as max digits to test, we have 9**5 = 59049
# that means even at all 9s, we have no chance of making it to 7 digits

# so we need to check 3, 4, 5, and 6 digit numbers

from Useful import toDigits

def test(n):
	return(n == sum(map(lambda x: x**5, toDigits(n))))

total = 0
for i in range(100, 1000000):
	if test(i):
		total += i

print(total)
