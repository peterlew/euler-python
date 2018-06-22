
from Useful import toDigits

def isPalindrome(n):
	digits = toDigits(n)
	return(digits == digits[::-1])

upperLimit = 1000
largestFound = 0

for i in range(100, upperLimit):
	for j in range(100, upperLimit):
		cand = i*j
		if isPalindrome(cand):
			if cand > largestFound:
				largestFound = cand

print(largestFound)
