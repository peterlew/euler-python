
from Useful import divisors

upperLimit = 28123

abundants = []

for i in range(2, upperLimit):
	if sum(divisors(i)) > i:
		abundants.append(i)

hitSums = {}

for i in range(len(abundants)):
	for j in range(i, len(abundants)):
		hitSums[abundants[i] + abundants[j]] = True

total = 0
for i in range(1, upperLimit + 1):
	if i in hitSums:
		continue
	total += i 

print(total)
	
		
