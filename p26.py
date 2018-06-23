
def lengthOfCycle(n):
	numerator = 1
	pastNumerators = [1]
	while True:
		numerator = 10 * (numerator % n)
		if numerator == 0:
			return 0
		if numerator in pastNumerators:
			return len(pastNumerators) - pastNumerators.index(numerator)
		pastNumerators.append(numerator)

longestCycle = 0
bestD = 1
for i in range(1, 1000):
	cycleLen = lengthOfCycle(i)
	if cycleLen > longestCycle:
		longestCycle = cycleLen
		bestD = i

print(bestD)
	

